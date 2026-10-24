# Ergebnis H37: Kopplungen aus der Triality-Form erklären die Quark-Mischung nicht; die Leptonen nur bei Neutrinomassen, die die Kosmologie ausschließt

Vorab-Notiz: `Vorab_Notiz_H37_Kopplung_aus_Triality.md`, Commit e1ee9ec (2026-10-24 04:12 MESZ), vor der Rechnung. Vorab offengelegt: Spurfreiheit der
reinen Triality-Kopplung, grobe Schätzung m₁* ≈ 0.035 eV. Skript `k93_test_h37.py`, Ausgabe `k93_out.txt`; der erste Lauf (`k93_out_erstlauf.txt`) hat
dieselben Kriteriumswerte, danach wurde nur die Nachkontrolle angehängt.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H37a reine Triality-Kopplung | **widerlegt** | u, d, e: m₃ − (m₁ + m₂) = 99.6 %, 98.0 %, 94.1 % von m₃ (null wäre nötig). Dirac-Neutrinos: m₁* = 0.028 eV, Massen (0.028, 0.030, 0.058) eV, Σm = 0.115 eV, über der DESI-Grenze 0.0642 eV |
| H37b Norm + Triality, ohne Maske | **Teilbefund nach Kriterium (nur Leptonen)** | Quarks: 0 von 8 448 Paaren innerhalb ±20 %, nächster Fall 82 % daneben. Leptonen: 264 von 13 651 456 Paaren in den 3σ-Bereichen, aber nur bei m₁ = 0.05 und 0.1 eV |
| H37c H/H̃-Lesart | **widerlegt** | u, ν in S und d, e in K: 0 von 98 064, nächster Fall 37 %; umgekehrt: 0 von 102 528, nächster Fall 40 %; keine PMNS-Treffer |

## Nachkontrolle (nach der Auswertung, kein Kriterium)

1. Die Quark-Kurven waren dünn besetzt (nur ein schmaler Teil des v₁-Gitters ist zulässig). Dicht abgetastet (12 800 Punkte je Sektor, 1.6·10⁸ Paare):
   wieder 0 Treffer, nächster Fall 80 % daneben.
2. Die Lepton-Treffer von H37b liegen nur bei m₁ = 0.05 und 0.1 eV, also Σm = 0.17 bzw. 0.31 eV. Das ist durch DESI DR2 (< 0.0642 eV) ausgeschlossen;
   zudem sind es 0.002 % aller Paare.

## Einordnung

1. **Eine Kopplung nur aus der Triality-Form ist verboten.** Sie koppelt nur verschiedene Plätze, ist also spurfrei und verlangt m₃ = m₁ + m₂. Das widerlegen
   alle geladenen Sektoren, und für Neutrinos verlangt es Σm ≈ 0.115 eV, was die Kosmologie ausschließt. Das ist ein echtes Verbot aus der Struktur, kein
   Anpassungsergebnis: Die Massen brauchen einen Diagonalteil, also eine Kopplung innerhalb eines Platzes.
2. **Norm + Triality** (die beiden Invarianten der Struktur) gibt die Quark-Mischung nicht (nächster Fall 80 % daneben) und die Lepton-Mischung nur bei
   quasi-entarteten Neutrinos, die die Kosmologie ausschließt. Formal ein Teilbefund nach dem Kriterium, physikalisch keiner.
3. **Die H/H̃-Lesart** ändert gegenüber H36 kaum etwas (37 % statt 36 %).
4. Stand der Mischungsfrage: Am nächsten bleibt die Kongruenzform D C D mit zirkulantem C (H36, 36 %). Keine der aus der Struktur nahe liegenden Kopplungen
   erklärt die Mischung; die Herkunft der Mischung bleibt offen.
