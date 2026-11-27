"""Programmabbild QIMG fuer den Boot-Monitor (hdl/qboot.sv): Assembler, Disassembler, Pruefung gegen die Referenz.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.qimage --cases 600 --seed 3        # Pruefung (braucht iverilog)
    python -m qam.examples.coprocessor.qimage asm band.txt > prog.hex     # Befehlsband -> Abbild
    python -m qam.examples.coprocessor.qimage dis prog.hex                # Abbild lesbar ausgeben

Format (32-Bit-Worte, Hexdatei mit einem Wort je Zeile):
    0  0x51494D47 ("QIMG")
    1  Version 1 in [31:16], Zahl N der Programmworte in [15:0]
    2  Summe der N Programmworte mod 2^32
    3. Programm: HALT 0x0..., CFG 0x1 adr<<16 + Wert im naechsten Wort, LOAD 0x2..., GATE 0x3 op<<4 | ziel,
       EMIT 0x4...
Ein Abbild ist portabel: dasselbe Abbild laeuft auf der Simulation, spaeter auf dem FPGA und auf der
Python-Referenz (run_reference). Das Befehlsband der Testbench (C/B/G/E) laesst sich verlustfrei uebersetzen.
"""

import argparse
import random
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from .check import CFG, NAMES, OPS, default_cfg, make_cases, reference

HDL = Path(__file__).resolve().parent / "hdl"
SOURCES = ("qcfg.sv", "qgate2.sv", "qnorm2.sv", "qstep2.sv", "qcop2_top.sv", "qboot.sv", "qcop2_sys.sv", "qboot_tb.sv")
MAGIC, VERSION = 0x51494D47, 1
HALT, CFG_I, LOAD, GATE, EMIT = 0, 1, 2, 3, 4
BOOT = ("idle", "running", "done", "reject")


def program_words(runs):
    """runs: Liste (gates, cfg). Je Lauf: CFG-Zeilen, LOAD, GATE..., EMIT. Am Ende HALT."""
    words = []
    for gates, cfg in runs:
        for key, value in (cfg or {}).items():
            words += [(CFG_I << 28) | (CFG[key] << 16), value & 0xFFFFFFFF]
        words.append(LOAD << 28)
        words += [(GATE << 28) | (op << 4) | tgt for op, tgt in gates]
        words.append(EMIT << 28)
    words.append(HALT << 28)
    return words


def image(words, version=VERSION, magic=MAGIC, checksum=None):
    total = sum(words) & 0xFFFFFFFF if checksum is None else checksum
    return [magic, (version << 16) | len(words), total] + list(words)


def to_hex(img):
    return "\n".join(f"{w:08x}" for w in img) + "\n"


def from_hex(text):
    return [int(t, 16) for t in text.split()]


def disassemble(img):
    names = {v: k for k, v in CFG.items()}
    out = [f"MAGIC {img[0]:#010x}  VERSION {img[1] >> 16}  N {img[1] & 0xFFFF}  SUM {img[2]:#010x}"]
    prog, i = img[3:3 + (img[1] & 0xFFFF)], 0
    while i < len(prog):
        w, op = prog[i], prog[i] >> 28
        if op == CFG_I:
            adr = (w >> 16) & 31
            value = prog[i + 1] if i + 1 < len(prog) else None
            out.append(f"CFG {names.get(adr, adr)} {value}")
            i += 1
        elif op == GATE:
            out.append(f"GATE {NAMES.get((w >> 4) & 15, (w >> 4) & 15)} {w & 1}")
        else:
            out.append({HALT: "HALT", LOAD: "LOAD", EMIT: "EMIT"}.get(op, f"? {w:#010x}"))
        i += 1
    return "\n".join(out)


def tape_to_runs(text):
    """Befehlsband (C/B/G/E, mehrere Faelle) -> Liste (gates, cfg)."""
    names = {v: k for k, v in CFG.items()}
    runs, cfg, gates = [], {}, None
    for raw in text.splitlines():
        cell = raw.split("#", 1)[0].split()
        if not cell:
            continue
        if cell[0] == "C":
            cfg[names[int(cell[1])]] = int(cell[2])
        elif cell[0] == "B":
            gates = []
        elif cell[0] == "G":
            gates.append((int(cell[1]), int(cell[2])))
        elif cell[0] == "E":
            runs.append((gates or [], cfg))
            cfg = {}
    return runs


def run_reference(img, width=16):
    """Fuehrt ein Abbild auf der Python-Referenz aus: (boot_status, Liste der EMIT-Ergebnisse)."""
    if len(img) < 3 or img[0] != MAGIC or img[1] >> 16 != VERSION:
        return "reject", []
    n = img[1] & 0xFFFF
    prog = img[3:3 + n]
    if len(prog) != n or sum(prog) & 0xFFFFFFFF != img[2]:
        return "reject", []
    live, active, gates, emits, i = default_cfg(width), default_cfg(width), [], [], 0
    names = {v: k for k, v in CFG.items()}
    while i < n:
        w, op = prog[i], prog[i] >> 28
        i += 1
        if op == HALT:
            return "done", emits
        if op == CFG_I:
            if i == n:
                return "reject", emits
            adr = (w >> 16) & 31
            if adr in names:
                live[names[adr]] = prog[i]
            i += 1
        elif op == LOAD:
            active, gates = dict(live), []
        elif op == GATE:
            gates.append(((w >> 4) & 15, w & 1))
        elif op == EMIT:
            emits.append(reference(gates, width, active))
        else:
            return "reject", emits
    return "done", emits


def run_hdl(images, tmp, width=16, aw=10, iverilog=None, vvp=None):
    iverilog = iverilog or shutil.which("iverilog") or "iverilog"
    vvp = vvp or shutil.which("vvp") or "vvp"
    paths = []
    for n, img in enumerate(images):
        p = Path(tmp) / f"img{n}.hex"
        p.write_text(to_hex(img), encoding="ascii")
        paths.append(str(p))
    lst = Path(tmp) / "imgs.txt"
    lst.write_text("\n".join(paths) + "\n", encoding="ascii")
    sim = Path(tmp) / "boot.vvp"
    subprocess.run([iverilog, "-g2012", f"-Pqboot_tb.W={width}", f"-Pqboot_tb.AW={aw}", "-o", str(sim),
                    *[str(HDL / f) for f in SOURCES]], check=True)
    out = subprocess.run([vvp, "-n", str(sim), f"+imgs={lst}"], check=True, capture_output=True, text=True).stdout
    results, emits = [], []
    for line in out.splitlines():
        f = line.split()
        if line.startswith("case "):
            emits.append((int(f[3]), int(f[5]), int(f[7]), [int(x) for x in f[11:27]]))
        elif line.startswith("image "):
            results.append((BOOT[int(f[3])], emits, int(f[7])))
            emits = []
    return results


def check(cases, seed, width=16, aw=10):
    rng = random.Random(seed)
    runs = []
    for gates in make_cases(rng, cases):
        cfg = default_cfg(width)
        if rng.random() < 0.5:
            cfg.update(allow=rng.choice([0x1FF, rng.getrandbits(16)]), w_eff=rng.randint(2, 18),
                       k_max=rng.choice([255, rng.randint(0, 10)]), budget=rng.choice([0, rng.randint(0, 30)]),
                       flags=rng.choice([0, 1]))
        runs.append((gates, cfg))
    # In Abbilder zu hoechstens 2^aw Worten aufteilen.
    images, chunk = [], []
    for run in runs:
        if chunk and len(program_words(chunk + [run])) + 3 > (1 << aw):
            images.append(image(program_words(chunk)))
            chunk = []
        chunk.append(run)
    images.append(image(program_words(chunk)))
    good = len(images)
    # Fehlerhafte Abbilder: der Monitor muss ablehnen, ohne etwas auszugeben.
    w = program_words(runs[:3])
    images += [
        image(w, magic=0x12345678),
        image(w, version=2),
        image(w, checksum=(sum(w) + 1) & 0xFFFFFFFF),
        image([LOAD << 28, 0x7 << 28, EMIT << 28]),           # unbekannter Befehl, EMIT danach nie erreicht
        image([LOAD << 28, CFG_I << 28 | (2 << 16)]),         # CFG ohne Wert am Ende
        [MAGIC, (VERSION << 16) | 0xFFFF, 0],                   # laenger als der Speicher
        # ohne HALT: Ende nach N Worten (schreibt alle Laufzeitwerte, weil Register ueber Abbilder hinweg bleiben)
        image(program_words([([(OPS["h"], 0)], default_cfg(width))])[:-1]),
    ]
    with TemporaryDirectory() as tmp:
        got = run_hdl(images, tmp, width, aw)
    if len(got) != len(images):
        raise SystemExit(f"{len(got)} Ergebnisse fuer {len(images)} Abbilder")
    emitted, cycles = 0, 0
    for n, (img, (boot, emits, cyc)) in enumerate(zip(images, got)):
        want_boot, want = run_reference(img, width)
        if boot != want_boot or emits != want:
            first = next((j for j, (a, b) in enumerate(zip(emits, want)) if a != b), None)
            raise SystemExit(f"Abbild {n}: HDL {boot}, {len(emits)} Ausgaben; Referenz {want_boot}, {len(want)}; "
                             f"erste Abweichung bei Ausgabe {first}")
        if n < good:
            emitted += len(emits)
            cycles += cyc
    print(f"Boot-Monitor: {good} gueltige Abbilder mit {emitted} Laeufen (davon {sum(1 for _, c in runs if c != default_cfg(width))} "
          f"mit eigener Konfiguration) = exakte Referenz; {len(images) - good} fehlerhafte bzw. Grenz-Abbilder "
          f"richtig behandelt (reject ohne Ausgabe, done ohne HALT); {cycles} Takte fuer die gueltigen Abbilder")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("cmd", nargs="?", choices=["check", "asm", "dis"], default="check")
    ap.add_argument("datei", nargs="?")
    ap.add_argument("--cases", type=int, default=600)
    ap.add_argument("--seed", type=int, default=3)
    args = ap.parse_args()
    if args.cmd == "check":
        check(args.cases, args.seed)
    elif args.cmd == "asm":
        sys.stdout.write(to_hex(image(program_words(tape_to_runs(Path(args.datei).read_text())))))
    else:
        print(disassemble(from_hex(Path(args.datei).read_text())))


if __name__ == "__main__":
    main()
