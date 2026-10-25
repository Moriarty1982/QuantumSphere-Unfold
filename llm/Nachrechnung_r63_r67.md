# Nachrechnung und Prüfung der Vermutungen aus H47 und r63–r67

Stand 2026-10-25, auf Bitte des Autors („rechne das nach und prüfe deine Vermutungen“). Eigener, neu geschriebener Code (`llm/k104_nachrechnung.py`,
`llm/k105_h46_exakt.py`), Literatur nachgeschlagen. Keine neue Vorhersage.

## Bestätigt

| Aussage | Nachrechnung |
|---|---|
| γ_ABCK = ln2/(π√3) = 0.127384 | scipy-Nullstelle, identisch |
| γ_DL/M = 0.237532957966 | identisch; Meissner (gr-qc/0407052) gibt 0.23753295796592 |
| γ_GM = 0.2740669 | identisch; Ghosh–Mitra (gr-qc/0411035) Gl. (7) mit λ ≈ 1.72, γ ≈ 0.274 |
| β = 0.549406 (DL/M), 0.604468 (GM) | identisch |
| Robertson: Sättigung genau für m = ±j | exakte Bruchrechnung für alle Zustände bis j = 10, keine Abweichung |
| Gewicht 2 = Zustände m = ±j | Meissner zählt Folgen von m-Labels, die Fläche hängt nur von \|m\| ab; der Faktor 2 sind die Vorzeichen ±m. Das entspricht \|j = \|m\|, m⟩ |
| γ_L = cosh 2η, tanh 2η = 0.844 | identisch auf 10⁻⁹ |
| Tachyon-Boden: E' = −γuμ, v' = −1/u; Boden des Spiegel-Frames in M bei −coth 2η | numerischer Boost per Matrix, identisch |
| Tachyon der Konvention F hat Rapidität −η + iπ/2 relativ zu R | r24.2 wörtlich so |
| Ω_M = (γ_M − γ_T)/(γ_M + γ_T) = 0.301847, Ω_Λ = 0.698153 | identisch |
| Seitenvertauschung β² ↔ Λ (r67.1) | durch Lesen bestätigt; dieselbe Zuordnung Λ_obs ∼ β² steht auch im Korollar „Cosmological constant revisited“ |
| Planck 2018 Ω_m | Abstract: 0.315 ± 0.007 (TT,TE,EE+lowE+lensing) |
| DESI DR2 BAO Ω_m | 0.2975 ± 0.0086 (zitiert in arXiv:2506.16022) |
| **H46** mit exaktem β (0.549406 statt 0.5493) | sin²θ₂₃ ∈ [0.4908, 0.4975] statt [0.4913, 0.4975]; Kontrolllauf mit 0.5493 reproduziert k100 exakt. Die registrierte Vorhersage [0.49, 0.50] bleibt gültig |

## Korrekturen und Einschränkungen

1. **γ_M + γ_T = |γ₃| ist eine Tautologie.** thm:triolic-gBI definiert γ₃ := −(γ_string + γ_LQG). Der Satz in r67.2 („the denominator is |γ₃|“) und die
   „Kuriosität“ im Chat sind kein Befund, sondern die Definition (bis auf die Rundung 0.2375).
2. **Welche Zählung die Literatur bevorzugt.** Die SU(2)-invariante Behandlung (Engle–Noui–Perez, Chern–Simons) gilt als besser begründet; die U(1)-Behandlung
   zählt Mikrozustände zu viel (logarithmische Korrektur −1/2 statt −3/2). Die SU(2)-Zählung gibt γ ≈ 0.274, also den Ghosh–Mitra-Wert. Das Leptonfenster
   wählt dagegen die U(1)-Zählung (0.2375). H47 bleibt numerisch richtig, aber die Lesart „die Daten wählen die richtige Zählung“ ist nicht gedeckt: Sie
   wählen die Zählung, die die neuere Literatur für weniger gut begründet hält. r03 F11 nennt 0.2375 „korrigiert“ und ABCK „überholt“; das entspricht dem Stand
   von 2004, nicht dem späteren.
3. **Konsistenz innerhalb einer Behandlung.** ABCK (nur j = ½) und DL/Meissner sind beide U(1)-Zählungen; das Paar ist in sich konsistent. Ein SU(2)-Paar gäbe
   denselben Boden (bei j = ½ ist 2j+1 = 2), also β = 0.604, außerhalb des Fensters.
4. **Unschärfe-Lesart.** In der U(1)-Zählung wird nur m gezählt; j = \|m\| ist die Zuordnung der minimalen Fläche. Dass die gezählten Zustände genau die
   unschärfe-sättigenden sind, stimmt mathematisch, ist aber eine Umdeutung, nicht Teil der Herleitung von Meissner.
5. **„Eigener Frame“ des Tachyons.** r24.2 nennt 1/β den Wert des Tachyons „in its own frame“; r63.4 nennt den Spiegel-Frame (E = 0) den ausgezeichneten Frame.
   Die Zahlen widersprechen sich nicht (1/β ist die Geschwindigkeit relativ zu R), aber „eigener Frame“ bezeichnet in beiden Runden Verschiedenes.
6. **H46-Trefferzahl.** Mit exaktem β steigt die Zahl der Treffer von 120 auf 168 (Variante A); η = 0.6175 liegt nahe am unteren Rand des Trefferfensters [0.611, 0.647] aus r61, daher reagiert die Trefferzahl empfindlich. Die Spannweite von
   sin²θ₂₃ ändert sich nur am unteren Ende um 0.0005.
