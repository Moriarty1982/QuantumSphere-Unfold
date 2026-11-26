#!/usr/bin/env python3
"""k382 (Erkundung, nicht blind): Nachrechnung der Skripte, die mu = beta_sym^2 als Amplitudenverhaeltnis b/a einsetzen.

Konvention F fuehrt x = beta_sym^2 als Verhaeltnis der Portgewichte (Energien), p_-/p_+ = x.  Liest man die Ports als die
zwei gegenlaeufigen Anteile (k253, k292), dann ist b^2/a^2 = x und das Amplitudenverhaeltnis b/a = beta_sym.
Dieses Skript laesst jedes betroffene Skript unveraendert und noch einmal mit b/a = beta_sym laufen (die Zeile, die mu
setzt, wird im Speicher ersetzt; die Dateien bleiben wie sie sind) und gibt die Zeilen aus, die sich aendern.

Aufruf:  python k382_nachrechnung.py [--beta 0.5494056410] > k382_out.txt
"""
import argparse
import difflib
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent / "hilbert_shift_felder_2026_11_24"

# (Datei, alte Zeile(nteil), neue Zeile(nteil));  {B} = beta_sym
PATCH = [
    ("feldgleichung/k292_hc_feste_norm.py", "g = 1.8644; m = (g - 1) / (g + 1)", "g = 1.8644; m = {B}"),
    ("feldgleichung/k297_hc_tauschsymmetrie.py", 'gL = sp.Float("1.8644"); muv = (gL - 1) / (gL + 1)',
     'gL = sp.Float("1.8644"); muv = sp.Float("{B}")'),
    ("feldgleichung/k298_test_h132.py", 'gLv = sp.Float("1.8644"); muv = (gLv - 1) / (gLv + 1)',
     'gLv = sp.Float("1.8644"); muv = sp.Float("{B}")'),
    ("feldgleichung/k299_hc_su2_vertraeglich.py", "gLv = 1.8644; muv = (gLv - 1) / (gLv + 1)", "gLv = 1.8644; muv = {B}"),
    ("feldgleichung/k301_fassung_F_am_igel.py", "gL = 1.8644; mu = (gL - 1) / (gL + 1)", "gL = 1.8644; mu = {B}"),
    ("feldgleichung/k302_test_h133.py", "mu = 0.3018", "mu = {B}"),
    ("feldgleichung/k303_rueckwaerts_kappa.py", "mu = 0.3018", "mu = {B}"),
    ("feldgleichung/k305_test_h136.py", "mu = 0.3018", "mu = {B}"),
    ("lambda_photon_h159/k350_test_h159.py", "muM = (GL - 1) / (GL + 1)", "muM = sp.sqrt((GL - 1) / (GL + 1))"),
]


def run(code, cwd):
    r = subprocess.run([sys.executable, "-c", code], cwd=cwd, capture_output=True, text=True, timeout=1500)
    return r.stdout.splitlines(), r.stderr.strip().splitlines()[-1:] if r.returncode else []


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--beta", default="0.5494056410"); a = ap.parse_args()
    print(f"k382: Nachrechnung mit b/a = beta_sym = {a.beta} statt b/a = beta_sym^2 (Zeilen '-' alt, '+' neu)")
    for rel, old, new in PATCH:
        src = (BASE / rel).read_text(encoding="utf-8")
        n = src.count(old)
        print(f"\n=== {rel}  (Ersetzung: '{old}' -> '{new.format(B=a.beta)}', {n} Stelle) ===")
        if n != 1:
            print("  NICHT GEPRUEFT: Ersetzungsstelle nicht eindeutig"); continue
        with tempfile.TemporaryDirectory() as tmp:
            o0, e0 = run(src, tmp)
            o1, e1 = run(src.replace(old, new.format(B=a.beta)), tmp)
        if e0 or e1:
            print("  FEHLER:", e0, e1); continue
        d = [l for l in difflib.unified_diff(o0, o1, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        print(f"  Zeilen der Ausgabe: {len(o0)}; geaendert: {sum(1 for l in d if l[0] == '+')}")
        for l in d:
            print("  " + l)


if __name__ == "__main__":
    main()
