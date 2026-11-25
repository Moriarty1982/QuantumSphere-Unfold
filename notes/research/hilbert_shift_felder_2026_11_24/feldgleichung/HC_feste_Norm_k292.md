# Lesart A oder B: der HC legt die Form fest, nicht die Amplitude (Erkundung k292, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Bei HS(1) gilt Lesart A. Der HC ist eine quasikonforme Projektion mit Dilatation γ_L, und in der Sprache der HS(1)-Ellipse heißt das
b/a = β_sym² = 0,3018: Er legt das Achsenverhältnis fest und lässt die Größe frei. Eine feste Norm ist damit bei HS(1) sogar ausgeschlossen, denn sie verlangt b = 0, also
γ_L = 1. Von Lesart B bleibt aber ein Teil richtig: Bei HS(2) kann der gegenläufige Anteil in den Anhang wandern, und dann ist die Norm fest und gleich dem Zeitmittel
a² + b² von HS(1). Die Skala f wird also von HS(1) geerbt, wirksam wird sie erst im nächsten Schritt.

Auftrag des Autors (25.11.2026): „prüfe, ob es eher A oder B ist“. **Kein blinder Test, sondern Erkundung:** Beim Aufschreiben der Vorab-Notiz stand das Ergebnis fest. Der HC ist
linear, C(λf) = λ·C(f), und eine lineare Abbildung kann keine Amplitude auszeichnen. Dass die Ellipse a·z + b·z̄ den Beltrami-Koeffizienten b/a hat, ist Standard. Keine H-Nummer,
keine Runde. Vergeben: Skripte **k292, k292b**.

Werkzeuge: Python mit sympy (exakt). Wolfram Language unabhängig, mit Quaternionen als 2×2-Matrizen (k292b). Qiskit nicht eingesetzt. Kein HDL/MMA-Vergleich: Der erste
Randschritt 0_mask → 1_mask ist ein Schritt der Auslese-Grammatik und kein RUN_TAPE-Ablauf; hier wird nur die Projektor-Eigenschaft des HC benutzt.

## Vorwissen geprüft
- HC: C(f) = ½(f + Jf), C² = C (`def:biquaternion`, Nomenklatur); quasikonforme Projektion mit μ = β_sym² = (γ_L − 1)/(γ_L + 1) und K = γ_L (`thm:hc-quasiconformal`,
  Statusvermerk r23: im Tachyon-Frame |μ| > 1 und Orientierungsumkehr); Randnormalisierer am ersten Randschritt (`ass:v3360-r16-hc-activation-first-boundary`, gesetzt,
  ausdrücklich ohne physikalische Beförderung).
- k253 (HS(1)-Familie a·e^{iωt} + b·e^{−iωt}, Halbachsen a + b und a − b, die zwei Kreisanteile als sym/antisym-Trennung des HC; lineare Polarisation am Äquator der Hopf-Sphäre,
  Kreisanteile an den Polen), k250, k290, k291. β_sym wird eingesetzt, nicht hergeleitet (OP1).
- Suche nach „Beltrami“ in den Notizen zum Turm: keine Fundstelle. Die Zuordnung μ = b/a ist neu.

## Ergebnisse
1. **Der HC in der Sprache der Ellipse (k292 1, k292b X1):** Die Abbildung z → a·z + b·z̄ hat den Beltrami-Koeffizienten μ = b/a und die Dilatation K = (a + b)/(a − b), das
   Verhältnis der Halbachsen. Mit μ = β_sym² ist K = γ_L exakt. In Zahlen: b/a = 0,3018, Halbachsen im Verhältnis 1,8644. Unter ψ → λψ bleibt μ gleich.
   Der Statusvermerk aus r23 passt dazu: |μ| > 1 heißt b > a, also umgekehrter Drehsinn.
2. **Die Norm bei HS(1) ist nicht fest (k292 2, X2):** N(ψ) = a² + b² + 2ab·cos 2ωt, zwischen (a − b)² und (a + b)², Zeitmittel a² + b². Fest ist sie nur für ab = 0.
   Mit γ_L = 1,8644 schwankt sie um den Faktor γ_L² = 3,48.
3. **Auch ein verformter Kreis rettet B nicht (k292 3, X3):** Hält man das Feld auf der Ellipse fest, hat die harmonische Bewegung den Rest −2abω²·sin 2ωt in der
   Bewegungsgleichung. Die Regel ψ̈ = −ω²ψ aus k253 und ein festgehaltenes Feld vertragen sich nur für ab = 0.
4. **Bei HS(2) wird die Norm fest (k292 4, X4, X5):** ψ = a·e^{iωt} + (b·j)·e^{−iωt} ist dieselbe Formel mit dem gegenläufigen Anteil in der neuen Richtung j. Es gilt
   ψ = e^{iωt}(a + b·j), N(ψ) = a² + b² fest, und ψ̇ = ωiψ. Beide Anteile drehen jetzt von links gesehen gleichsinnig. Der Schatten in ℂ (ψ₁ + χ̄) ist die Ellipse aus k253.
   Die Ladung der Linksdrehung ist ω(a² + b²), die der Rechtsdrehung ω(a² − b²), also die Ladung von HS(1). Der Punkt auf der Hopf-Sphäre hat cos ϑ = (a² − b²)/(a² + b²);
   a = b ist der Äquator, b = 0 der Pol, wie in k253.

## Bewertung
- **Eher A, und zwar aus zwei unabhängigen Gründen:** Der HC ist skalenfrei, und die HS(1)-Familie mit b ≠ 0 hat keine feste Norm. In ℂ haben zwei gegenläufige Kreisanteile
  keinen Platz, um senkrecht aufeinander zu stehen. Das Licht von HS(1) bleibt in diesem Ansatz masselos (kein m_A = e·f aus k291 Punkt 5).
- **Was von B bleibt:** die Aussage, dass zwischen HS(1) und HS(2) keine neue Skala liegt. f² = a² + b² ist bei HS(1) schon da, als Zeitmittel einer schwankenden Norm, und wird
  bei HS(2) zur festen Norm. Das ist eine genaue Fassung der „Protomasse“: vorhanden, aber erst nach dem nächsten Schritt wirksam. Die Ruhemasse aus k291 (M ≈ 103,2·f·√c₁)
  und die Eichfeldmassen bei HS(2) hängen dann an diesem f.
- **Der HC wirkt ab HS(1), sichtbar wird er anders bei HS(2):** Bei HS(1) ist μ = b/a die Form der Ellipse. Bei HS(2) ist dasselbe Verhältnis die Breite auf der Hopf-Sphäre,
  mit β_sym² ein Winkel von 33,6° vom Pol. Diese Zahl ist nur ausgerechnet. Eine Zuordnung zu einer Messgröße ist nicht geprüft und wird hier nicht behauptet.
- Der Urknall liegt in dieser Lesart bei HS(2), wie in k253 angenommen (erste Holonomie, erste feste Norm, erste gebundene Ruhemasse).

## Grenzen
- Die Aussage gilt für den Ansatz k290/k291 und für den HC als quasikonforme Projektion des Bestands. β_sym und γ_L sind eingesetzt (OP1 offen).
- Dass der gegenläufige Anteil bei HS(2) in den Anhang wandert, ist eine Möglichkeit, die der Schritt eröffnet. Dass er es muss, ist nicht gezeigt. Eine Lösung mit b in ℂ gibt es
  bei HS(2) weiterhin.
- Der Randnormalisierer des QAM (0_mask → 1_mask) ist eine Aussage über die Auslese-Grammatik. Seine Lesart als Feldnorm wäre eine physikalische Beförderung, die der Bestand
  ausdrücklich nicht erlaubt, und ist hier nicht benutzt.
- Woher a und b selbst kommen, bleibt offen (k272: Amplitude frei). OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Möglicher blinder Test
Die Frage „muss der gegenläufige Anteil in den Anhang?“ lässt sich als Test fassen: In L₂ mit den Termen aus k290 die Energie der beiden Lösungen (b in ℂ gegen b in ℂ·j) bei
gleichem a, b, ω vergleichen und vorab festlegen, welche Zusatzterme zählen. Das Ergebnis steht nicht vorab fest, sobald K₁ und K₂ mit Ortsabhängigkeit beitragen. Dafür wäre H129 frei.

## Dateien
`k292_hc_feste_norm.py` (`k292_out.txt`), `k292b_gegenprobe.wl` (`k292b_out.txt`).
