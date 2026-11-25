"""Baustufe 0: exakte Zwei-Qubit-Einheit in SystemVerilog gegen Referenz und Qiskit pruefen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.check --cases 500 --seed 1

Braucht iverilog/vvp im Suchpfad und Qiskit 2.x. Drei Pruefungen je Fall:
1. HDL-Ausgabe gleich der exakten Python-Referenz (bitgenau, inklusive Status);
2. dekodierte HDL-Amplituden gleich dem Qiskit-Statevector (Toleranz 1e-9);
3. bei W=4 und W=3 dieselben guard-Faelle in HDL und Referenz.
"""

import argparse
import cmath
import random
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

HDL = Path(__file__).resolve().parent / "hdl"
OPS = {"nop": 0, "x": 1, "z": 2, "s": 3, "sdg": 4, "t": 5, "tdg": 6, "h": 7, "cx": 8}
NAMES = {v: k for k, v in OPS.items()}
ROT = {"z": 4, "s": 2, "sdg": 6, "t": 1, "tdg": 7}
STATUS = ("continue", "guard", "reject")
W8 = cmath.exp(1j * cmath.pi / 4)


def reference(gates, width):
    """Exakte Referenz mit denselben Regeln wie qstep2.sv."""
    c = [[0] * 4 for _ in range(4)]
    c[0][0] = 1
    k, status, done = 0, 0, 0
    lo, hi = -(1 << (width - 1)), (1 << (width - 1)) - 1
    for op, tgt in gates:
        if status:
            break
        t = [row[:] for row in c]
        kn, bad = k, False
        b = 2 if tgt else 1
        name = NAMES.get(op)
        if name is None:
            bad = True
        elif name == "x":
            for i in range(4):
                if not i & b:
                    t[i], t[i | b] = t[i | b], t[i]
        elif name == "cx":
            for i in range(4):
                if not i & b and i & (3 ^ b):
                    t[i], t[i | b] = t[i | b], t[i]
        elif name in ROT:
            for i in range(4):
                if i & b:
                    for _ in range(ROT[name]):
                        a = t[i]
                        t[i] = [-a[3], a[0], a[1], a[2]]
        elif name == "h":
            for i in range(4):
                if not i & b:
                    p = i | b
                    t[i], t[p] = ([x + y for x, y in zip(t[i], t[p])],
                                  [x - y for x, y in zip(t[i], t[p])])
            kn += 1
        flat = [x for row in t for x in row]
        if all(x % 2 == 0 for x in flat) and kn >= 2:
            t = [[x // 2 for x in row] for row in t]
            kn -= 2
        flat = [x for row in t for x in row]
        if bad:
            status = 2
        elif any(x < lo or x > hi for x in flat) or kn > 255:
            status = 1
        else:
            c, k, done = t, kn, done + 1
    return status, k, done, [x for row in c for x in row]


def decode(k, flat):
    return [sum(flat[4 * i + j] * W8 ** j for j in range(4)) / (2 ** 0.5) ** k for i in range(4)]


def qiskit_state(gates):
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector

    qc = QuantumCircuit(2)
    for op, tgt in gates:
        name = NAMES[op]
        if name == "cx":
            qc.cx(1 - tgt, tgt)
        elif name != "nop":
            getattr(qc, name)(tgt)
    return list(Statevector.from_instruction(qc).data)


def make_cases(rng, count):
    cases = [[], [(OPS["h"], 0), (OPS["cx"], 1)], [(OPS["h"], 0), (OPS["t"], 0), (OPS["h"], 0)]]
    # Lange H-T-Ketten lassen Nenner und Koeffizienten wachsen (guard bei kleinem W).
    cases += [[(OPS["h"], 0), (OPS["t"], 0)] * n for n in (5, 10, 20, 30, 40, 60)]
    while len(cases) < count:
        n = rng.randint(1, 40)
        cases.append([(rng.choice(list(NAMES)), rng.randint(0, 1)) for _ in range(n)])
    return cases


def run_hdl(cases, width, tmp, iverilog, vvp):
    stim = Path(tmp) / f"stim_{width}.txt"
    lines = []
    for gates in cases:
        lines.append("B")
        lines += [f"G {op} {tgt}" for op, tgt in gates]
        lines.append("E")
    stim.write_text("\n".join(lines) + "\n", encoding="ascii")
    sim = Path(tmp) / f"sim_{width}.vvp"
    subprocess.run([iverilog, "-g2012", f"-Pqstep2_tb.W={width}", "-o", str(sim),
                    str(HDL / "qstep2.sv"), str(HDL / "qstep2_tb.sv")], check=True)
    out = subprocess.run([vvp, "-n", str(sim), f"+stim={stim}"], check=True,
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        if not line.startswith("case "):
            continue
        f = line.split()
        rows.append((int(f[3]), int(f[5]), int(f[7]), [int(x) for x in f[11:27]], int(f[9])))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cases", type=int, default=500)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--iverilog", default=shutil.which("iverilog") or "iverilog")
    ap.add_argument("--vvp", default=shutil.which("vvp") or "vvp")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    cases = make_cases(rng, args.cases)
    # Unbekannte Opcodes fuer reject-Faelle anhaengen.
    cases += [[(OPS["h"], 0), (rng.randint(9, 15), 0), (OPS["x"], 1)] for _ in range(5)]

    with TemporaryDirectory() as tmp:
        for width in (16, 4, 3):
            rows = run_hdl(cases, width, tmp, args.iverilog, args.vvp)
            assert len(rows) == len(cases), (len(rows), len(cases))
            counts = {s: 0 for s in STATUS}
            max_dev, cycles = 0.0, 0
            for n, (gates, row) in enumerate(zip(cases, rows)):
                ref = reference(gates, width)
                hdl = row[:4]
                if hdl != ref:
                    raise SystemExit(f"W={width} Fall {n}: HDL {hdl} != Referenz {ref}; Gatter {gates}")
                counts[STATUS[ref[0]]] += 1
                cycles += row[4]
                if ref[0] == 0:
                    got = decode(ref[1], ref[3])
                    want = qiskit_state(gates)
                    dev = max(abs(a - b) for a, b in zip(got, want))
                    max_dev = max(max_dev, dev)
                    if dev > 1e-9:
                        raise SystemExit(f"W={width} Fall {n}: Qiskit-Abweichung {dev}; Gatter {gates}")
            print(f"W={width}: {len(cases)} Faelle, HDL = exakte Referenz in allen Faellen; "
                  f"Status {counts}; Gatter-Takte {cycles}; "
                  f"max |HDL - Qiskit| bei continue = {max_dev:.2e}")


if __name__ == "__main__":
    main()
