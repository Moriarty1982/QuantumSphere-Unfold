# Ergebnis H38: Mit einem ε je Sektor trifft die Ähnlichkeitsform beide Mischungen, aber nur im Ausläufer

Vorab-Notiz: `Vorab_Notiz_H38_Ein_eps_je_Sektor.md`, Commit d3555bf (2026-10-24 04:52 MESZ), vor der Rechnung. Die Notiz korrigiert eine Zählung aus
H36/r52: Je Familie sind es zwei ε für drei Winkel, eine Vorhersage bleibt. Skript `k94_test_h38.py`, Ausgabe `k94_out.txt`; der erste Lauf
(`k94_out_erstlauf.txt`) hat dieselben Kriteriumswerte, danach wurde nur die Nachkontrolle angehängt.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H38a Form K, Quarks | **widerlegt** | 0 von 28 830 816; nächster Fall 20.2 % daneben (ε_u = 1.43, ε_d = 1.38: 0.180, 0.034, 0.0044) |
| H38b Form K, Leptonen | **bestätigt** | 1 728 von 54 670 896 (0.003 %), m₁ = 0.001 oder 0.003 eV; Region ε_e ∈ [0.81, 1.74], ε_ν ∈ [0.34, 0.53] |
| H38c Form S, Quarks | **bestätigt** | 294 von 32 091 264 (0.0009 %); Region ε_u ∈ [1.36, 1.63], ε_d ∈ [1.42, 1.47]; bester Fall 7 % daneben (ε_u = 1.58, ε_d = 1.47: 0.2225, 0.0448, 0.0040) |
| H38d Form S, Leptonen | **bestätigt** | 1 008 von 10 986 624 (0.009 %), alle drei zulässigen m₁; Region ε_e ∈ [0.44, 0.82], ε_ν ∈ [0.27, 0.55]; z. B. m₁ = 0, ε_e = 0.47, ε_ν = 0.40: sin²θ = (0.338, 0.572, 0.021) |

Nach dem Kriterium ist Form S für Quarks und Leptonen bestätigt (Anteil unter 1 %, Region schmal), also ein Kandidat für eine Lesart mit vier ε.

## Nachkontrolle (nach der Auswertung, kein Kriterium), Form S

1. Die passenden Punkte bilden je Zweigpaar eine zusammenhängende Region (30 Quark-, 96 Lepton-Zweigpaare, je eine Komponente).
2. **Die dritte Größe ist nicht festgelegt.** Unter allen Kombinationen, die |V_us| und |V_cb| auf ±20 % treffen (34 068), liegt |V_ub| zwischen 0.0034 und
   0.029, Median 0.018, fünfmal zu groß; nur 0.9 % treffen auch |V_ub|. Bei den Leptonen liegt sin²θ₁₃ bei passenden θ₁₂, θ₂₃ zwischen 0 und 0.99, Median 0.26;
   0.8 % liegen im 3σ-Bereich.

## Einordnung

1. **Formal bestätigt, inhaltlich schwach.** Form S mit vier ε (ε_u ≈ 1.4–1.6, ε_d ≈ 1.45, ε_e ≈ 0.4–0.8, ε_ν ≈ 0.3–0.55) trifft CKM und PMNS innerhalb der
   Toleranzen, mit kosmologisch zulässigen Neutrinomassen. Aber die Vorhersage, die je Familie bleibt, ist nicht scharf: Die typische Vorhersage für |V_ub| ist
   fünfmal zu groß, die Treffer liegen im Ausläufer einer breiten Verteilung. Das ist eher eine gelungene Anpassung als eine Erklärung.
2. **ε_u und ε_d liegen nahe beieinander** (Bereiche 1.36–1.63 und 1.42–1.47), aber kein Treffer liegt auf der Diagonale ε_u = ε_d: Mit gleichem ε für u und d
   fand H36c keinen Treffer (nächster Fall 40 %). Bei den Leptonen ist ε_e > ε_ν.
3. Form K verfehlt die Quarks knapp (20.2 %), trifft die Leptonen.
4. Offen: warum diese ε-Werte, und ob eine Kopplung von C an die Struktur die dritte Größe schärfer festlegt.
