"""Bandregister (hdl/qband.sv) gegen ein Python-Modell pruefen; dazu die Zaehlung der Aufteilungen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.band_check --steps 6000 --seed 11

Zufaellige Befehlsfolgen mit gueltigen Buddy-Aufteilungen (rekursiv geteilt), absichtlich ungueltigen
(falsch ausgerichtet, ueberlappend, zu lang), Zellzugriffen innerhalb und ausserhalb der Baender, Wortzugriffen
ueber den Bus und Profilen (eingebrannt, ueberschrieben, zurueckgesetzt). Jede Antwort und die Flags layout_ok
und full muessen bitgenau gleich dem Modell sein.
"""

import argparse
import random
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path
from tempfile import TemporaryDirectory

HDL = Path(__file__).resolve().parent / "hdl"
SET_PART, WR_CELL, RD_CELL, WR_WORD, RD_WORD, SET_PROF, CLR_PROF, RD_PROF = range(1, 9)


class Band:
    def __init__(self, cells=128, parts=16, cw=1, busw=128):
        self.n, self.parts, self.cw, self.busw = cells, parts, cw, busw
        self.L = cells.bit_length() - 1
        self.cells = [0] * cells
        self.pv, self.pb, self.po = [0] * parts, [0] * parts, [0] * parts
        self.ov = [0] * (self.L + 1)
        self.ovw, self.ovp, self.ovc = [0] * (self.L + 1), [0] * (self.L + 1), [0] * (self.L + 1)

    def layout(self):
        ok, cover = True, [False] * self.n
        for i in range(self.parts):
            if not self.pv[i]:
                continue
            ln = 1 << self.po[i]
            if self.po[i] > self.L or self.pb[i] % ln or self.pb[i] + ln > self.n:
                ok = False
            for j in range(i + 1, self.parts):
                if self.pv[j]:
                    lj = 1 << self.po[j]
                    if self.pb[i] < self.pb[j] + lj and self.pb[j] < self.pb[i] + ln:
                        ok = False
            for c in range(self.pb[i], min(self.pb[i] + ln, self.n)):
                cover[c] = True
        return ok, ok and all(cover)

    def burned(self, n, field):
        return {0: (0x40000000 >> self.L) << n, 1: (n & 7) << 29, 2: n & 7, 3: n, 4: 1 << n,
                5: self.n >> n}.get(field, 0) & 0xFFFFFFFF

    def step(self, cmd, a, b, d):
        ok, data = 0, 0
        lay, _ = self.layout()
        if a < self.parts:
            n_a, base, ln = self.po[a], self.pb[a], 1 << self.po[a]
        L = self.L
        if cmd == SET_PART and a < self.parts:
            self.pv[a], self.po[a], self.pb[a] = (b >> (L + 4)) & 1, (b >> L) & 15, b & (self.n - 1)
            ok = 1
        elif cmd in (WR_CELL, RD_CELL) and a < self.parts and lay and self.pv[a] and b < ln:
            if cmd == WR_CELL:
                self.cells[base + b] = d & ((1 << self.cw) - 1)
            else:
                data = self.cells[base + b]
            ok = 1
        elif cmd in (WR_WORD, RD_WORD) and a < (self.n * self.cw + self.busw - 1) // self.busw:
            for c in range(self.busw):
                idx = a * self.busw + c
                if idx < self.n:  # CW = 1
                    if cmd == WR_WORD:
                        self.cells[idx] = (d >> c) & 1
                    else:
                        data |= self.cells[idx] << c
            ok = 1
        elif cmd == SET_PROF and a <= L and b < 3:
            self.ov[a] |= 1 << b
            if b == 0:
                self.ovw[a] = d & 0xFFFFFFFF
            elif b == 1:
                self.ovp[a] = d & 0xFFFFFFFF
            else:
                self.ovc[a] = d & 7
            ok = 1
        elif cmd == CLR_PROF and a <= L:
            self.ov[a] = 0
            ok = 1
        elif cmd == RD_PROF and a < self.parts and lay and self.pv[a] and b < 7:
            if b == 6:
                data = base
            elif b < 3 and self.ov[n_a] >> b & 1:
                data = (self.ovw, self.ovp, self.ovc)[b][n_a]
            else:
                data = self.burned(n_a, b)
            ok = 1
        lay2, full = self.layout()
        return ok, data, int(lay2), int(full)


def buddy_layout(rng, L, max_parts):
    """Zufaellige gueltige Aufteilung von 2^L Zellen in Buddy-Bloecke: Liste (base, order)."""
    blocks = [(0, L)]
    while len(blocks) < max_parts and rng.random() < 0.8:
        k = rng.randrange(len(blocks))
        base, order = blocks[k]
        if order == 0:
            continue
        blocks[k:k + 1] = [(base, order - 1), (base + (1 << (order - 1)), order - 1)]
    return blocks


def make_steps(rng, steps, cells=128, parts=16):
    L = cells.bit_length() - 1
    out = []
    while len(out) < steps:
        # neue Aufteilung, gelegentlich mit Fehler und mit Luecken
        blocks = buddy_layout(rng, L, parts)
        if rng.random() < 0.3 and len(blocks) > 1:
            blocks.pop(rng.randrange(len(blocks)))                  # Luecke: gueltig, nicht voll
        idx = rng.sample(range(parts), len(blocks))
        for p in range(parts):
            out.append((SET_PART, p, 0, 0))                          # alle Abschnitte loeschen
        for p, (base, order) in zip(idx, blocks):
            out.append((SET_PART, p, (1 << (L + 4)) | (order << L) | base, 0))
        if rng.random() < 0.25:                                      # absichtlicher Fehler
            p = rng.randrange(parts)
            kind = rng.randrange(3)
            if kind == 0:
                base, order = rng.randrange(1, cells) | 1, rng.randint(1, L)   # falsch ausgerichtet
            elif kind == 1:
                base, order = 0, L                                   # ueberlappt alles
            else:
                base, order = 0, rng.randint(L + 1, 15)              # zu lang
            out.append((SET_PART, p, (1 << (L + 4)) | (order << L) | base, 0))
        if rng.random() < 0.1:                                       # nur falsch ausgerichtet, ohne Ueberlappung
            for p in range(parts):
                out.append((SET_PART, p, 0, 0))
            order = rng.randint(1, L - 1)
            base = rng.randrange(0, cells - (1 << order)) | 1
            out.append((SET_PART, rng.randrange(parts), (1 << (L + 4)) | (order << L) | base, 0))
        for _ in range(rng.randint(5, 40)):
            cmd = rng.choice([WR_CELL, WR_CELL, RD_CELL, RD_CELL, WR_WORD, RD_WORD, SET_PROF, CLR_PROF,
                              RD_PROF, RD_PROF])
            a = rng.randrange(parts + 2) if cmd in (WR_CELL, RD_CELL, RD_PROF) else rng.randrange(L + 3)
            if cmd in (WR_WORD, RD_WORD):
                a = rng.randrange(3)
            b = rng.randrange(cells + 4) if cmd in (WR_CELL, RD_CELL) else rng.randrange(8)
            d = rng.getrandbits(128)
            out.append((cmd, a, b, d))
    return out


def count_layouts(L=7):
    """Zahl der Groessenmischungen (Partitionen von 2^L in Zweierpotenzen) und der Buddy-Belegungen."""
    @lru_cache(None)
    def mixes(n, m):
        if n == 0:
            return 1
        if m == 0:
            return 0
        return sum(mixes(n - k * m, m // 2) for k in range(n // m + 1)) if m > 1 else 1
    lay = 1
    for _ in range(L):
        lay = lay * lay + 1
    return mixes(1 << L, 1 << L), lay


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--steps", type=int, default=6000)
    ap.add_argument("--seed", type=int, default=11)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    steps = make_steps(rng, args.steps)
    with TemporaryDirectory() as tmp:
        stim = Path(tmp) / "band.txt"
        stim.write_text("\n".join(f"X {c} {a} {b} {d:x}" for c, a, b, d in steps) + "\n", encoding="ascii")
        sim = Path(tmp) / "band.vvp"
        subprocess.run([shutil.which("iverilog") or "iverilog", "-g2012", "-o", str(sim), str(HDL / "qband.sv"),
                        str(HDL / "qband_tb.sv")], check=True)
        out = subprocess.run([shutil.which("vvp") or "vvp", "-n", str(sim), f"+stim={stim}"], check=True,
                             capture_output=True, text=True).stdout
    rows = [line.split() for line in out.splitlines() if line.startswith("R ")]
    if len(rows) != len(steps):
        raise SystemExit(f"{len(rows)} Antworten fuer {len(steps)} Befehle")
    model = Band()
    stats = {"ok": 0, "guard": 0, "layout_bad": 0, "full": 0}
    for n, ((c, a, b, d), r) in enumerate(zip(steps, rows)):
        want = model.step(c, a, b, d)
        got = (int(r[1]), int(r[2], 16), int(r[3]), int(r[4]))
        if got != want:
            raise SystemExit(f"Befehl {n} ({c}, {a}, {b}, {d:x}): HDL {got} != Modell {want}")
        stats["ok" if got[0] else "guard"] += 1
        stats["layout_bad"] += got[2] == 0
        stats["full"] += got[3]
    mixes, layouts = count_layouts()
    print(f"Bandregister 128 Zellen, 16 Abschnitte, Bus 128 Bit: {len(steps)} Befehle = Modell "
          f"(ok {stats['ok']}, guard {stats['guard']}; Befehle bei ungueltiger Aufteilung {stats['layout_bad']}, "
          f"bei voller Belegung {stats['full']})")
    print("Baender je Stufe in 128 Zellen: " + ", ".join(f"HS({n}) {1 << n}er x{128 >> n}" for n in range(7, -1, -1)))
    print(f"Groessenmischungen: {mixes}; Buddy-Belegungen mit Lage: {layouts} (~{layouts:.2e})")


if __name__ == "__main__":
    main()
