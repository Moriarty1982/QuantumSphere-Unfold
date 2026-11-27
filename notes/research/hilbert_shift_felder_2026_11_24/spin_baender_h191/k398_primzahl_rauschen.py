"""k398 (Erkundung, kein Test): Primzahl-Rauschen auf der Schleife L3, verglichen mit Zufallsrauschen gleicher Streuung.
Aufruf aus dem Repo-Wurzelverzeichnis: python .../k398_primzahl_rauschen.py > .../k398_out.txt"""
import math, os, sys, time, numpy as np, mpmath as mp
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.abspath(os.path.join(here, "..", "..", "..", "..")))
from qam.examples.coprocessor.stufe2.qtape import QTape, PrimeNoise

def band(mode, eps, n):
    return f"""QTAPE 2
BUDGET {8 * n + 50}
INIT 1 0.9
READ b b
LOOP {n}
  SET x = (1 - b) / (1 + b)
  SET alpha = atan(sqrt(x))
  NOISE alpha {mode} {eps}
  ROT alpha
  HC
  SWAP x
  READ b b
END
HALT"""
print("== 1 Schleife L3 mit Rauschen auf dem Drehwinkel (3000 Runden, Mittel ueber die letzten 2500) ==")
pn = PrimeNoise(); v = np.array([pn.next("prime_gap")[1] for _ in range(3000)]); sd = v.std(); print(f"   Streuung der ersten 3000 Primzahl-Werte (normierte Luecke - 1): {sd:.4f}, Mittel {v.mean():+.4f}")
print(f"   {'eps':>6s} {'Quelle':>12s} {'Mittel b':>12s} {'Streuung':>10s} {'Mittel - 1/2':>13s}")
for eps in (0.0, 0.01, 0.05, 0.1):
    for mode, e in (("prime_gap", eps), ("random", eps * sd)):
        outs = []
        for seed in ((1,) if mode == "prime_gap" else (1, 2, 3)):
            m = QTape(band(mode, e, 3000), seed=seed, trace_every=1).run()
            if m.stop != "halted": print(f"   {eps:6.2f} {mode:>12s}  Maschine stoppt mit {m.stop} in Schritt {m.steps} (Startwert {seed}): {m.trace[-1]['warum']}; b war {m.trace[-1]['b']:.4f}"); continue
            bs = np.array([r["b"] for r in m.trace if r["zelle"].startswith("READ")])[500:]; outs.append((bs.mean(), bs.std()))
        if not outs: continue
        mean = np.mean([o[0] for o in outs]); spread = np.mean([o[1] for o in outs]); extra = "" if mode == "prime_gap" else f"  (drei Startwerte: {', '.join(f'{o[0]:.6f}' for o in outs)})"
        print(f"   {eps:6.2f} {mode:>12s} {mean:12.7f} {spread:10.2e} {mean - 0.5:+13.2e}{extra}")
        if eps == 0: break
print("   Erwartung aus der Formel: eine Runde vom Fixpunkt aus mit gestoertem Winkel, b' = (1 - x) cos(2 alpha + 2 d) b + x:")
x = 1 / 3; al = math.pi / 6
for eps in (0.01, 0.05, 0.1):
    d = eps * v[500:]; b1 = (1 - x) * np.cos(2 * al + 2 * d) * 0.5 + x
    print(f"      eps = {eps}: eine Runde vom Fixpunkt aus mit den Primzahl-Werten: Mittel {b1.mean():.7f} (Verschiebung {b1.mean() - 0.5:+.2e}; zweite Ordnung -(1-x) cos(2 alpha) b * 2 <d^2> = {-(1 - x) * math.cos(2 * al) * 0.5 * 2 * (d ** 2).mean():+.2e}, erste Ordnung {-(1 - x) * math.sin(2 * al) * 0.5 * 2 * d.mean():+.2e})")
print("   Die ganze Schleife verschiebt das Mittel nach oben, weil b' = 1 - 2b(1 - b) gekruemmt ist: + 2 Var(b). Mit den Zahlen oben (eps = 0.05):")
print(f"      2 * (2.2e-2)^2 = {2 * 0.0221 ** 2:+.2e}, dazu die eine Runde {-5.85e-4:+.2e}, zusammen {2 * 0.0221 ** 2 - 5.85e-4:+.2e}; gemessen +2.7e-04 (Primzahlen), +4.8e-04 (Zufall, Spanne der Startwerte 1.7e-04 bis 8.9e-04)")
print("   Lesart: Rauschen verschiebt das Mittel nur ueber Streuung und Mittel der Werte. Die Reihenfolge (das Muster der Primzahlen) geht in dieser Ordnung nicht ein;")
print("   Primzahl- und Zufallsrauschen gleicher Streuung sind innerhalb der Spanne der Startwerte nicht zu unterscheiden.")
print("\n== 2 Was ist an Position X exakt berechenbar? ==")
t = time.time(); pn = PrimeNoise(20_000_000); dt = time.time() - t
for X in (10, 1000, 100000, 1000000): print(f"   Primzahl Nr. {X}: {int(pn.p[X - 1])}")
print(f"   (Sieb bis 2*10^7 in {dt:.2f} s; das ist exakt und braucht keine Vermutung.)")
print("   Riemann-Vermutung als Fehlerschranke (Schoenfeld 1976): |pi(x) - li(x)| < sqrt(x) ln(x) / (8 pi) fuer x >= 2657")
for xx in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
    pi_x = int(np.searchsorted(pn.p, xx, side="right")); li = float(mp.li(xx)); bound = math.sqrt(xx) * math.log(xx) / (8 * math.pi)
    print(f"      x = {xx:>8d}: pi(x) = {pi_x}, li(x) = {li:.1f}, Abweichung {pi_x - li:+.1f}, Schranke {bound:.1f}")
print("   Die Schranke sagt, wie weit pi(x) hoechstens von li(x) abweicht. Sie gibt weder die n-te Primzahl noch die Teiler einer Zahl.")

print("\n== 3 Laesst sich bekanntes Rauschen aus der Ausgabe herausrechnen? ==")
m = QTape(band("prime_gap", 0.05, 200)).run(); bs = np.array([r["b"] for r in m.trace if r["zelle"].startswith("READ")])
pn = PrimeNoise(); b = 0.9; pred = [b]
for _ in range(200):
    xx = (1 - b) / (1 + b); a = math.atan(math.sqrt(xx)) + 0.05 * pn.next("prime_gap")[1]; b = (1 - xx) * math.cos(2 * a) * b + xx; pred.append(b)
print(f"   200 Runden mit eps = 0.05: Maschine gegen Vorhersage aus der bekannten Primzahlfolge: groesste Abweichung {np.abs(bs - np.array(pred)).max():.1e}")
m2 = QTape(band("prime_gap", 0.05, 200)).run(); print(f"   zwei Laeufe, gleicher Hash: {m.result()['hash'] == m2.result()['hash']}; letzter Wert b = {bs[-1]:.10f}")
print("   Lesart: Mit bekanntem Bauprinzip und bekannter Folge ist jede Runde exakt vorhersagbar. Das ist die Lage eines Angreifers, der den Schluessel schon hat.")
