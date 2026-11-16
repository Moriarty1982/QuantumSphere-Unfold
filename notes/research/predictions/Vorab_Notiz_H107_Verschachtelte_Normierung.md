# Vorab-Notiz H107: Legt eine verschachtelte Normierung HS(8) = HS(7) ⊕ HS(6) ⊕ HS(6) das Singulettgewicht fest?

Festgelegt am 2026-11-16, **vor** der Rechnung. Idee und Auftrag des Autors: „lege erst den Test an … lass uns erst nach dem Mechanismus
suchen“; HS(8) lässt sich als ein HS(7) und zwei HS(6) verschachteln, ein HS(6) könnte eine Normierung sein, das HS(7) eine Normierung der
beiden HS(6), und entscheidend könnte sein, was man als Basis definiert. Einordnung OP3, r25, H106. Skript `k229_test_h107.py` (wird nach
dieser Notiz geschrieben; **ausgeführt erst nach Freigabe durch den Autor**).

## Anlass
H106 (widerlegt) zeigte: Ein gemeinsamer Singulettanteil w in den drei Generationszuständen verschiebt die Phase des Spin-1-Dreiecks;
w = 0 gibt 0,679042, w = ¼ gibt 0,640384. Die Lepton-Phase liegt dazwischen. Nachträglich (nicht gedeutet) traf w = 0,0979 die Lepton-Phase,
nahe am Kastengewicht 0,0976 aus r25.5. Gesucht ist ein Mechanismus, der w **ohne freien Parameter** festlegt.

## Vorwissen geprüft
- `Vorab_Notiz_H106_*`, `Ergebnis_H106_*`, `k228_nachtraeglich.txt`: Familie w zwischen 0 und ¼; nötiges w = 0,0979 nachträglich.
- `../op3_dixon_copies_2026_11_16/` (r25): Kästen |00⟩, |01⟩, |10⟩, |11⟩ des Kopienindex; Gewichte des Spin-1-Dreiecks 0,7927 / 0,0976 /
  0,0976 / 0,0120.
- r26: Verdopplungsregel; HS(8) = 2 × HS(7) = 4 × HS(6), verschachtelt.
- `../op3_guarded_core_flux_2026_11_15/README.md`: Lepton-Phase aus Polmassen 0,666665.
- Renormierung: Koide und die Phase 2/9 gelten nur für Polmassen (v4.8.0-r11, H1; `../op3_flux_two_thirds_2026_11_13.md`); ein Matching zu
  laufenden Massen fehlt (`../op3_mass_backsolve_2026_11_12/README.md`). Renormierung im Sinn laufender Massen ist **nicht** Teil dieses
  Tests; sie bleibt als nächster Weg, falls die Verschachtelung nicht trägt.

## Festgelegte Konstruktion
- **Basis:** Der Kopienindex C² ⊗ C² wird in der Basis der Zyklusachse z zerlegt, Kästen |00⟩, |01⟩, |10⟩, |11⟩. Das erste Bit legt die
  beiden HS(7)-Hälften fest, H₀ = {|00⟩, |01⟩} und H₁ = {|10⟩, |11⟩}. Die Zyklusachse ist die einzige Richtung, die die Symmetrie der drei
  Generationen auszeichnet; andere Basen werden nicht geprüft.
- **Generationszustände:** g_k = √(1 − w) |n_k⟩|n_k⟩ + √w ε, ε das Singulett, n_k auf dem Kegel mit halbem Öffnungswinkel ψ um z (wie H106).
- **Kastengewichte** p_b des Triplettanteils |n_k⟩|n_k⟩ (für alle k gleich): p₀₀ = cos⁴(ψ/2), p₀₁ = p₁₀ = cos²(ψ/2) sin²(ψ/2),
  p₁₁ = sin⁴(ψ/2).
- **Mechanismen (Verschachtelung, vor der Rechnung festgelegt):** w ist das Gewicht eines HS(6)-Kastens, unnormiert oder in seiner
  HS(7)-Hälfte normiert:

  | Name | Rolle | w |
  |---|---|---|
  | N1 | ein mittleres HS(6) | p₀₁ |
  | N2 | das leichte HS(6) | p₁₁ |
  | N3 | das schwere HS(6) | p₀₀ |
  | N4 | beide mittleren HS(6) | p₀₁ + p₁₀ |
  | N5 | mittleres HS(6), normiert in H₀ | p₀₁/(p₀₀ + p₀₁) |
  | N6 | mittleres HS(6), normiert in H₁ | p₁₀/(p₁₀ + p₁₁) |
  | N7 | leichtes HS(6), normiert in H₁ | p₁₁/(p₁₀ + p₁₁) |

- **Lösung:** Für jeden Mechanismus werden ψ und w gemeinsam aus zwei Bedingungen bestimmt: |⟨g_j|g_k⟩|² = ½ (K = 2/3) und w = F(ψ)
  (selbstkonsistent). Jede Lösung mit 0 ≤ w ≤ 1 zählt als eigener Versuch. Vorhersage ist die Bargmann-Phase φ.

## Entscheidungskriterium (vor der Rechnung festgelegt)
- **Zielwert:** Lepton-Phase aus Polmassen 0,666665 (2/3 auf 2·10⁻⁶).
- **bestätigt**, wenn genau ein Mechanismus eine Lösung mit |φ − 0,666665| ≤ 0,0002 rad hat.
- **mehrdeutig**, wenn mehr als ein Mechanismus trifft; dann wird keine Lesart gewählt.
- **widerlegt**, wenn keiner trifft.
- **Zufallserwartung, vorab abgeschätzt:** Die Phasen der Familie liegen zwischen etwa 0,62 und 0,68 (Breite 0,06). Ein Fenster von
  ±0,0002 deckt etwa 0,7 % davon; bei 7 Versuchen erwartet man durch Zufall etwa 0,05 Treffer.

## Offenlegung
- **Nicht ganz blind:** N1 ist durch den nachträglichen Befund aus H106 angeregt (w = 0,0979 nahe p₀₁ = 0,0976). Ein Treffer von N1 allein
  zählt deshalb nur eingeschränkt; das Ergebnis nennt das ausdrücklich. N2–N7 folgen aus der Verschachtelung ohne Bezug auf den Zielwert.
- Weil ψ sich mit w ändert, ist das selbstkonsistente w von N1 vor der Rechnung nicht bekannt.
- Ein Treffer wäre eine Lesart des Rests, keine Herleitung der Überlappung ½.

## Ergänzung vor der Rechnung (16.11.2026, Auftrag des Autors „Ja, erweitern“)
Die Hilfskonstruktion `tools/hs_partition.py` (PR #158) zählt in HS(8) zehn natürliche Beziehungen (Gewicht eines Knotens; Gewicht eines
Knotens normiert in einem Vorfahren), davon neun wertverschieden, weil p₀₁ = p₁₀. N1–N7 decken sechs davon ab, dazu N4, das kein Knoten
ist. **Vor jeder Rechnung** wird die Familie auf die volle Grammatik erweitert:

| Name | Rolle | w |
|---|---|---|
| N8 | ganze HS(7)-Hälfte H₀ | p₀₀ + p₀₁ |
| N9 | ganze HS(7)-Hälfte H₁ | p₁₀ + p₁₁ |
| N10 | schweres HS(6), normiert in H₀ | p₀₀/(p₀₀ + p₀₁) |

Die Beziehungen „HS(6)[10]“ und „HS(6)[10] in H₁“ haben dieselben Werte wie N1 und N6 und werden nicht doppelt gezählt. Die Familie ist damit
N1–N10 (neun Beziehungen der Grammatik und N4). Das Kriterium bleibt (genau ein Treffer auf 0,0002 rad an 0,666665); die Zufallserwartung
steigt auf etwa 10 × 0,007 = 0,07 Treffer. Gerechnet wurde vor dieser Ergänzung nichts.

## Ablauf
1. Diese Notiz committen.
2. `k229_test_h107.py` schreiben; Freigabe des Autors abwarten; dann ausführen (Ausgabe `k229_out.txt`).
3. Ergebnis-Notiz `Ergebnis_H107_Verschachtelte_Normierung.md`.
