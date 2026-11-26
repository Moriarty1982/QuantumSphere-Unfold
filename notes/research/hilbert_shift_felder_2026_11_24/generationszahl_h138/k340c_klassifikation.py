"""k340c (H157c, nachtraeglich): Klassifikation der Minima aus k340 nach phi und theta.
Gleiche Zufallsfolge wie k340 (Seed 340), gleiche Potentiale. Anlass: k340 meldete bei Ordnung <= 10
innere delta; Vermutung nach Sicht der Ausgabe: das sind Minima mit phi = 0, wo alle cos3delta-Terme
(Faktor phi^(3k)) verschwinden und delta flach ist. Aufruf: python3 k340c_klassifikation.py
"""
import importlib.util, sys, io, contextlib
import numpy as np
spec = importlib.util.spec_from_file_location("k340", "k340_postulat_delta.py")
# nur die Funktionen laden, ohne den Hauptlauf: Quelltext bis zur Stichprobe ausfuehren
src = open("k340_postulat_delta.py").read()
head = src.split('rng = np.random.default_rng(340)')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(head, "k340_head", "exec"), ns)
make_V, global_min, readout = ns['make_V'], ns['global_min'], ns['readout']

rng = np.random.default_rng(340)
for Dmax in (10, 12):
    cls = {"phi=0": 0, "theta=pi/4 Endpunkt": 0, "theta=pi/4 innen": 0, "sonst Endpunkt": 0, "sonst innen (phi!=0)": 0, "r=0": 0}
    flat_checks = []
    for i in range(300):
        V, basis = make_V(Dmax, rng)
        x = global_min(V, rng)
        ro = readout(x)
        if ro is None:
            cls["r=0"] += 1
            continue
        d, theta, rr, f = ro
        s = abs(np.sin(3 * d))
        if abs(f) < 1e-4:
            cls["phi=0"] += 1
            # delta flach? V bei gleichem r fuer andere delta
            vals = [V([f, rr * np.cos(t), rr * np.sin(t)]) for t in np.linspace(0, 2 * np.pi / 3, 7)]
            flat_checks.append(max(vals) - min(vals))
        elif abs(theta - np.pi / 4) < 1e-5:
            cls["theta=pi/4 innen" if s > 1e-4 else "theta=pi/4 Endpunkt"] += 1
        else:
            cls["sonst innen (phi!=0)" if s > 1e-4 else "sonst Endpunkt"] += 1
    print(f"Dmax={Dmax}: {cls}")
    if flat_checks:
        print(f"   phi=0: max Spannweite von V ueber delta bei festem r: {max(flat_checks):.3e} (flach)")
