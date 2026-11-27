"""Zustandsspeicher nach ZFS-Vorbild (hdl/qstore.sv) gegen ein Python-Modell pruefen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.store_check --steps 3000 --seed 19

Die Datensaetze sind exakte Endzustaende (16 Koeffizienten zu 16 Bit und k) zufaelliger Schaltungen, einmal in
kanonischer sqrt(2)-Form und einmal ohne Kuerzen. Befehlsfolgen aus PUT, GET, SNAP, CLONE, DEL und FLIP (gekippte Bits
in einem oder beiden Spiegeln) muessen bitgenau gleich dem Modell antworten: Platz, Pruefsumme, Dedup, Reparatur,
laufender Pruefhash, belegte Plaetze, gelesener Inhalt. Dazu wird gezaehlt, wie viele gleiche Zustaende die Dedup in
kanonischer Form erkennt und wie viele ohne Kuerzen (gleicher Zustand, andere Darstellung).
"""

import argparse
import random
import shutil
import subprocess
import zlib
from pathlib import Path
from tempfile import TemporaryDirectory

from .check import decode, default_cfg, make_cases, reference

HDL = Path(__file__).resolve().parent / "hdl"
RW, SLOTS, NAMES = 264, 8, 8
PUT, GET, SNAP, CLONE, DEL, FLIP = range(1, 7)


def record(state):
    status, k, done, flat = state
    v = 0
    for i, c in enumerate(flat):
        v |= (c & 0xFFFF) << (16 * i)
    return v | (k & 0xFF) << 256


def crc(v, nbytes):
    return zlib.crc32(v.to_bytes(nbytes, "little")) & 0xFFFFFFFF


class Store:
    def __init__(self):
        self.a, self.b = [0] * SLOTS, [0] * SLOTS
        self.h, self.refc = [0] * SLOTS, [0] * SLOTS
        self.nv, self.nro, self.ns = [0] * NAMES, [0] * NAMES, [0] * NAMES
        self.audit, self.slot, self.hash, self.out = 0, 0, 0, 0

    def step(self, cmd, x, y, rec):
        ok = dedup = rep = bad = 0
        sa = self.ns[x] if x < NAMES else 0
        if cmd == PUT and x < NAMES and not (self.nv[x] and self.nro[x]):
            h = crc(rec, RW // 8)
            hit = next((s for s in range(SLOTS) if self.refc[s] and self.h[s] == h and self.a[s] == rec), None)
            free = next((s for s in range(SLOTS) if not self.refc[s]), None)
            if hit is not None or free is not None or (self.nv[x] and self.refc[sa] == 1):
                tgt = hit if hit is not None else free if free is not None else sa
                if hit is None:
                    self.a[tgt] = self.b[tgt] = rec
                    self.h[tgt] = h
                if not (self.nv[x] and sa == tgt):
                    self.refc[tgt] = (self.refc[tgt] if hit is not None else 0) + 1
                    if self.nv[x]:
                        self.refc[sa] -= 1
                self.nv[x], self.ns[x] = 1, tgt
                self.audit = crc(self.audit | h << 32, 8)
                ok, self.slot, self.hash, dedup = 1, tgt, h, int(hit is not None)
        elif cmd == GET and x < NAMES and self.nv[x]:
            self.slot, self.hash = sa, self.h[sa]
            ha, hb = crc(self.a[sa], RW // 8), crc(self.b[sa], RW // 8)
            if ha == self.h[sa]:
                self.out, ok = self.a[sa], 1
                if hb != self.h[sa]:
                    self.b[sa], rep = self.a[sa], 1
            elif hb == self.h[sa]:
                self.out, ok, rep = self.b[sa], 1, 1
                self.a[sa] = self.b[sa]
            else:
                bad = 1
        elif cmd in (SNAP, CLONE) and x < NAMES and y < NAMES and self.nv[x] and not self.nv[y]:
            self.nv[y], self.nro[y], self.ns[y] = 1, int(cmd == SNAP), sa
            self.refc[sa] += 1
            ok, self.slot = 1, sa
        elif cmd == DEL and x < NAMES and self.nv[x]:
            self.nv[x] = self.nro[x] = 0
            self.refc[sa] -= 1
            ok = 1
        elif cmd == FLIP and x < SLOTS and (y & 0x7FFF) < RW:
            bit = 1 << (y & 0x7FFF)
            if y >> 15:
                self.b[x] ^= bit
            else:
                self.a[x] ^= bit
            ok = 1
        used = sum(1 for r in self.refc if r)
        return ok, self.slot, self.hash, dedup, rep, bad, self.audit, used, self.out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--steps", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=19)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    # Kleiner Vorrat an Schaltungen, damit gleiche Zustaende vorkommen (auch aus verschiedenen Schaltungen).
    cases = [g for g in make_cases(rng, 400) if len(g) <= 6][:60]
    canon = [record(reference(g, 16, dict(default_cfg(16), flags=2))) for g in cases]
    plain = [record(reference(g, 16, dict(default_cfg(16), flags=0))) for g in cases]
    distinct_c, distinct_p = len(set(canon)), len(set(plain))
    # Physikalisch verschiedene Zustaende (Amplituden gerundet) ueber einen groesseren Vorrat
    big = make_cases(random.Random(args.seed + 1), 600)
    phys, rc, rp, rh = set(), set(), set(), set()
    for g in big:
        sc = reference(g, 16, dict(default_cfg(16), flags=2))
        sp = reference(g, 16, dict(default_cfg(16), flags=0))
        if sc[0] or sp[0]:
            continue
        phys.add(tuple(round(z.real, 9) + 1j * round(z.imag, 9) for z in decode(sc[1], sc[3])))
        rc.add(record(sc))
        rp.add(record(sp))
        rh.add(record(reference(g, 16, default_cfg(16))))
    steps = []
    for _ in range(args.steps):
        cmd = rng.choice([PUT, PUT, PUT, GET, GET, SNAP, CLONE, DEL, FLIP])
        x = rng.randrange(NAMES + 1) if cmd != FLIP else rng.randrange(SLOTS + 1)
        y = rng.randrange(NAMES + 1)
        rec = 0
        if cmd == PUT:
            rec = rng.choice(canon if rng.random() < 0.7 else plain)
        if cmd == FLIP:
            y = rng.randrange(RW + 2) | (rng.randrange(2) << 15)
        steps.append((cmd, x, y, rec))
    with TemporaryDirectory() as tmp:
        stim = Path(tmp) / "store.txt"
        stim.write_text("\n".join(f"X {c} {x} {y} {r:x}" for c, x, y, r in steps) + "\n", encoding="ascii")
        sim = Path(tmp) / "store.vvp"
        subprocess.run([shutil.which("iverilog") or "iverilog", "-g2012", "-o", str(sim), str(HDL / "qstore.sv"),
                        str(HDL / "qstore_tb.sv")], check=True)
        out = subprocess.run([shutil.which("vvp") or "vvp", "-n", str(sim), f"+stim={stim}"], check=True,
                             capture_output=True, text=True).stdout
    rows = [line.split() for line in out.splitlines() if line.startswith("R ")]
    if len(rows) != len(steps):
        raise SystemExit(f"{len(rows)} Antworten fuer {len(steps)} Befehle")
    model = Store()
    stats = {"dedup": 0, "repaired": 0, "bad": 0, "guard": 0}
    for n, ((c, x, y, r), row) in enumerate(zip(steps, rows)):
        want = model.step(c, x, y, r)
        got = (int(row[1]), int(row[2]), int(row[3], 16), int(row[4]), int(row[5]), int(row[6]), int(row[7], 16),
               int(row[8]), int(row[9], 16))
        if got != want:
            raise SystemExit(f"Befehl {n} ({c}, {x}, {y}): HDL {got} != Modell {want}")
        stats["dedup"] += got[3]
        stats["repaired"] += got[4]
        stats["bad"] += got[5]
        stats["guard"] += not got[0]
    print(f"Zustandsspeicher {SLOTS} Plaetze, {NAMES} Namen, Spiegel A/B: {len(steps)} Befehle = Modell "
          f"(Dedup {stats['dedup']}, repariert {stats['repaired']}, beide Spiegel falsch {stats['bad']}, "
          f"guard {stats['guard']}); Pruefhash am Ende {model.audit:08x}")
    print(f"Vorrat {len(cases)} Schaltungen: {distinct_c} verschiedene Zustaende in kanonischer Form, "
          f"{distinct_p} verschiedene Datensaetze ohne Kuerzen (gleicher Zustand, andere Darstellung)")
    print(f"Groesserer Vorrat (600 Schaltungen, nur continue): {len(phys)} verschiedene Zustandsvektoren; "
          f"als Datensaetze kanonisch {len(rc)}, gekuerzt durch 2 {len(rh)}, ohne Kuerzen {len(rp)}; "
          f"nur die kanonische Form macht die Dedup exakt")


if __name__ == "__main__":
    main()
