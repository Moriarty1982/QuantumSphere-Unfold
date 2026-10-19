# Vorab-Notiz H1: Koide-Phase gleich K/3

Festgelegt am 2026-10-20, **vor** jeder Berechnung für Quarks und für laufende Massen.
Diese Datei wird committet, bevor das Prüfskript läuft; der Git-Zeitstempel belegt die Reihenfolge.

## Herkunft

Bei den geladenen Leptonen (Polmassen) gilt δ = 0,2222248 und K/3 = 0,2222215, Abweichung 0,5 σ
(Kernkarte K12, Gespräch vom 2026-10-20). Idee des Autors: 2/9 · 3/2 = 1/3. Lesart: δ = K · (1/3).
Ob die 1/3 die Kernzahl 1/N oder β²_Hopf = 1/3 ist, bleibt offen; für Dreiergruppen (N = 3) sagen
beide Lesarten dasselbe voraus. **Der Leptonenwert ist Kalibrierung, kein Test.**

## Hypothese

**H1:** Für jede Dreiergruppe geladener Fermionen gilt δ = K/3.

**H1′ (Gegenhypothese):** δ = 2/9 für jede Dreiergruppe (feste Zahl). Für Quarks ist K ≠ 2/3,
H1 und H1′ machen dort also verschiedene Vorhersagen.

## Definitionen (verbindlich)

- v_k = √m_k, Reihenfolge **aufsteigend nach Masse**, k = 0, 1, 2; alle Wurzeln **positiv**.
- t = (v_0 + v_1 + v_2)/3, c = (√2/3) · Σ_k v_k ω^{−k}, ω = e^{2πi/3}; dann v = t + √2·Re(c ω^k).
- K = Σ m_k / (Σ √m_k)² .
- δ = arg(c), reduziert auf das Intervall [0, 2π/3).

## Daten (verbindlich)

**Primär:** laufende MS-bar-Yukawa-Kopplungen bei μ = M_Z im Standardmodell, Eq. (2.4) (PDG-2024-Eingaben) in
S. Antusch, K. Hinze, S. Saad, „Updated Running Quark and Lepton Parameters at Various Scales“,
arXiv:2510.01312 (2025). Massen ∝ Kopplungen, der Faktor kürzt sich in K und δ.

| | y | Fehler |
|---|---|---|
| u | 7.04e-6 | 0.15e-6 |
| c | 3.56e-3 | 0.06e-3 |
| t | 0.967 | 0.004 |
| d | 1.54e-5 | 0.02e-5 |
| s | 3.06e-4 | 0.04e-4 |
| b | 1.630e-2 | 0.009e-2 |
| e | 2.77713e-6 | 0.00036e-6 |
| μ | 5.85042e-4 | 0.00075e-4 |
| τ | 0.99378e-2 | 0.00014e-2 |

**Sekundär:** PDG-2024-Massen bei ihren Standardskalen (gemischt, daher nur ergänzend), aus derselben Quelle:
m_u(2 GeV) = 2.16 MeV, m_d(2 GeV) = 4.70 MeV, m_s(2 GeV) = 93.5 ± 0.5 MeV, m_c(m_c) = 1.2730 ± 0.0028 GeV,
m_b(m_b) = 4.183 ± 0.004 GeV, M_t = 172.4 ± 0.7 GeV; Fehler für m_u, m_d: ± 0.04 MeV wie dort angegeben.

## Verfahren und Kriterium (verbindlich)

- Fehlerfortpflanzung per Monte Carlo (10⁶ Ziehungen, unabhängige Gauß-Verteilungen).
- z = (δ − K/3)/σ, mit σ aus der Streuung von δ − K/3.
- **|z| < 2: H1 verträglich. 2 ≤ |z| ≤ 3: unentschieden. |z| > 3: H1 für diese Gruppe widerlegt.**
- Dasselbe für H1′ mit z′ = (δ − 2/9)/σ′.
- Getestet werden: Up-Quarks (u, c, t), Down-Quarks (d, s, b), geladene Leptonen bei M_Z.
- Entscheidend ist die Primärdatenreihe. H1 gilt als **gestützt**, wenn sie für beide Quarkgruppen
  verträglich ist; als **widerlegt**, wenn sie für mindestens eine Quarkgruppe widerlegt ist.
- Neutrinos sind ausgenommen (absolute Massen unbekannt).

Nach dem Commit dieser Notiz wird daran nichts mehr geändert. Abweichungen im Vorgehen werden im
Ergebnis ausdrücklich als solche gekennzeichnet.
