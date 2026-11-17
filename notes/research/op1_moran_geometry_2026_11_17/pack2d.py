"""Passt das M-Fraktal (zwei Kopien je Skala r_n = 2^{-sqrt(n(n+2)/3)}) ueberlappungsfrei in das Einheitsquadrat?
Guillotine-Packung mit freien Rechtecken (beste Kurzseitenpassung).  Gelingt sie fuer alle Quadrate bis zu einer Groesse,
unter der der Rest der Flaeche sicher passt, dann gilt die offene-Mengen-Bedingung mit V = offenes Einheitsquadrat.
Restabschaetzung: Quadrate mit Seite <= s passen in jedes freie Rechteck mit kurzer Seite >= s, wenn ihre Gesamtflaeche
hoechstens (Flaeche - Randverlust) betraegt; hier konservativ: Restflaeche aller kleinen Quadrate <= 1/2 der groessten freien Rechteckflaeche
und groesstes freies Rechteck hat kurze Seite >= 2 s (Moon-Moser: Quadrate der Gesamtflaeche <= A/2 passen in ein Quadrat der Flaeche A)."""
import numpy as np

n = np.arange(1, 400001)
r = 2.0 ** (-np.sqrt(n * (n + 2) / 3))
sizes = np.repeat(r, 2)

def pack(sizes, cutoff):
    free = [(0.0, 0.0, 1.0, 1.0)]  # x, y, w, h
    placed = 0
    for s in sizes:
        if s < cutoff: break
        best = None
        for k, (x, y, w, h) in enumerate(free):
            if s <= w + 1e-15 and s <= h + 1e-15:
                score = min(w - s, h - s)
                if best is None or score < best[0]: best = (score, k)
        if best is None: return False, placed, free
        x, y, w, h = free.pop(best[1])
        # Guillotine-Schnitt entlang der kuerzeren Restseite
        if (w - s) < (h - s):
            free += [(x + s, y, w - s, s), (x, y + s, w, h - s)]
        else:
            free += [(x + s, y, w - s, h), (x, y + s, s, h - s)]
        free = [f for f in free if f[2] > 1e-15 and f[3] > 1e-15]
        placed += 1
    return True, placed, free

for cutoff in (1e-2, 1e-3):
    ok, placed, free = pack(sizes, cutoff)
    rest = np.sum(sizes[sizes < cutoff] ** 2)
    big = max(free, key=lambda f: min(f[2], f[3]) ** 2) if free else None
    side = min(big[2], big[3]) if big else 0
    print(f"Schwelle {cutoff}: gepackt {ok} ({placed} Quadrate); Restflaeche kleiner Quadrate {rest:.2e}; "
          f"groesstes freies Quadrat Seite {side:.4f} (Flaeche {side**2:.2e}); Moon-Moser-Bedingung Rest <= Flaeche/2 und Seite >= Schwelle: "
          f"{rest <= side**2 / 2 and side >= cutoff}")
