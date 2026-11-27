# Runde v4.10.0-r71: Friedman-Koinzidenzindex als Ergänzung zum Kasiski-Abstandsscan

Fortsetzung der Krypto-Analogie-Schicht des Companion (Definition `def:kasiski-persistence-scan`,
`def:kasiski-style-recurrence-scan` und die Vernam-artige Heuristik). Die Runde wird an
[`sources/research/parts/v4100-post-release-layers.tex`](../../../sources/research/parts/v4100-post-release-layers.tex)
angehängt. **Keine Freigabe eines Guards; rein diagnostisch, dem strukturellen Admissibility-Kriterium untergeordnet (wie der Kasiski-Scan).**

## Worum es geht
Der **Kasiski persistence scan** erkennt wiederkehrende lokale Obstruktions-Muster im diskretisierten
Teichmüller-Persistenz-Strom Σ_pers über ihre **Abstände** (Häufung gemeinsamer Teiler). Der **Friedman
coincidence scan** ergänzt das **statistisch**: über den Koinzidenzindex IC = Σ n_i(n_i−1)/(N(N−1)).
Zerlegt man Σ_pers in L Spalten (Position mod L), hat die richtige Periode einen Spalten-IC weit über dem
Zufallswert 1/c. Friedman ist robuster gegen Rauschen und liefert eine Zahl (geschätzte Periode) statt nur
Kandidaten. Beide sind Diagnose-Filter und dürfen weder einen zweiten primitiven Träger einführen noch die
eingefrorene Gesamtkanal-Basislinie umwerfen.

## Rechen-Kontrolle (zwei Werkzeuge)
Beispielstrom (seed 71): N=420 über Alphabet {0=trigger-near, 1=persistence-fail, 2=admissibility-fail,
3=neutral}, zu 80 % ein Muster der **versteckten Periode 7**, sonst Rauschen.

| Methode | Ergebnis |
|---|---|
| Kasiski (Abstände) | dominanter Teiler **7** (Häufung 1941, klar vor 2/3/14/21); Abstand 7 kommt 121× vor |
| Friedman (Spalten-IC) | Ausreißer-Kamm bei L=7, 14, 21 (IC ≈ 0,734 vs Grundlinie ≈ 0,31); **fundamentale Periode = 7** |
| Friedman (Ein-Zahl) | mit κ_p = Spalten-IC(7) = 0,734: L ≈ 7,6 |
| globaler IC | 0,31357 (Zufall 1/c = 0,25000) |

Python (`k419_friedman_koinzidenz.py` → `k419_out.txt`) und **Wolfram** (`k419b_kontrolle.wl` →
`k419b_out.txt`) stimmen exakt überein (global IC 0,31357; Spalten-IC(7) 0,73374). Beide Methoden
zeigen die Periode 7; sie sind komplementär (Abstände vs. Koinzidenz-Statistik).

## Dateien
- `k419_friedman_koinzidenz.py` / `k419_out.txt` — Referenz-Implementierung (Kasiski-Abstände + Friedman-IC) und Ausgabe.
- `k419b_kontrolle.wl` / `k419b_out.txt` — unabhängige Wolfram-Kontrolle des IC.
