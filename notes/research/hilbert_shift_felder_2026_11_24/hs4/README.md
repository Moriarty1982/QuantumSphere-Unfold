# Warum bringt HS(4) nichts Neues? (Erkundung k254, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** „Nichts Neues“ gilt nur für die stetige Symmetrie (Der bleibt g₂). Tatsächlich passiert bei HS(4) dreierlei:
Die Normmultiplikativität und die Alternativität brechen (Nullteiler = Lecks), es kommt eine endliche Symmetrie S₃ hinzu, die **drei
Oktonionen-Kopien** in 𝕊 vertauscht, und die Zahl verträglicher Kreisachsen wächst ab dort nur noch nach Radon–Hurwitz. Diese Zahl
wiederholt sich mit Periode 4 im Turm (Bott-Periodizität): HS(n + 4) hat genau 8 Achsen mehr als HS(n). Der Turm hört also nicht auf, er wird periodisch.

Auftrag des Autors (24.11.2026): „lass uns erst prüfen, wieso ab dem HS(4) nichts mehr passiert?“ Anschluss an k253
(`../README.md`). **Erkundung, nicht blind:** Hurwitz, Radon–Hurwitz, Aut(𝕊) = G₂ × S₃ (Brown 1967) und Moreno (Nullteiler) sind
Literatur; gerechnet wird nur die Bestätigung und die Lesart im Turm. Vergeben: Skripte **k254** (k254, k254b, k254c).

Werkzeuge: Python (numpy) für Identitäten, Nullteiler und Kreisachsen (k254, k254c); Wolfram Language exakt für den endlichen Teil von
Aut(𝕊) (k254b). Qiskit nicht eingesetzt (kein Zustand, keine Messung).

## Vorwissen geprüft
k253 (dim Der = 0, 0, 3, 14, 14, 14; L_u² ≠ −1 ab n = 4); `op3_dixon_times_sedenions_2026_11_16/` (Nullteiler, keine Alternativität,
Cl(8) und Trialität aus 𝕊); K28 `v4_8_0_r03_r12/llm/Trennung_Farbe_Generation.md` (𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2) unter G₂ × S₃);
r13 und `op3_sedenion_generations_estar_2026_11_14.md` (unter der Ladung Q_* ist der S₃-Zyklus eine Phase, kein Generationsschritt;
ℂ⊗𝕊 trägt zwei Generationen); Atlas r27.2 und HS(4)-Meta-Septum (Leckregister).

## Ergebnisse
1. **Welche Gesetze brechen (k254, Teil A, 300 Zufallstripel je Stufe).** Bis 𝕆 gelten Alternativität, Moufang-Identität und
   |xy| = |x||y| (Abweichung ≤ 6·10⁻¹⁴). Ab 𝕊 brechen alle drei (Alternativität 68, Moufang 340, Norm 5,9 bei n = 4). **Flexibilität und
   Potenzassoziativität bleiben** auf allen Stufen bis n = 6 (≤ 2·10⁻¹³). Hurwitz: Nur bei Dimension 1, 2, 4, 8 gibt es normierte
   Divisionsalgebren. Für den Turm heißt das: Bis HS(3) ist das Produkt zweier normierter Zustände wieder normiert, danach nicht mehr.
2. **Nullteiler sind die Lecks (Teil B).** a = (e₁ + e₁₀)/√2: L_a hat einen vierdimensionalen Kern. Diese Zustände verschwinden bei
   Multiplikation mit a. Die G₂-Bahn von a ist 11-dimensional, wie Moreno (Menge der Einheits-Nullteiler ≅ V₂(ℝ⁷), Dimension 11).
   Ein generisches Element ist kein Nullteiler (kleinster Singulärwert 0,30). Die Lecks bilden also eine eigene, von G₂ geordnete Fläche,
   keine neue Symmetrie. Das ist der Lecktest des Atlas mit konkretem Ort.
3. **Der endliche Teil S₃ (k254b, Wolfram exakt).** Genau 6 Automorphismen von 𝕊 vertauschen mit G₂: drei Spiegelungen (e₈ ↦ −e₈), zwei
   Drehungen um 120° (e₈ fest) und die Identität; nicht kommutativ, also S₃. Auf den zwei Kopien der 7 wirkt sie als zweidimensionale
   Standarddarstellung (Spuren 2, −1, 0), auf e₈ als Vorzeichen. **Neu:** Jede Spiegelung hält eine achtdimensionale Unteralgebra fest, und
   alle drei sind Oktonionen (abgeschlossen, alternativ, normmultiplikativ bis 2·10⁻¹⁴) mit paarweisem Schnitt nur ℝ (k254c). S₃ vertauscht
   diese **drei Oktonionen-Kopien**, und die 120°-Drehung führt sie zyklisch ineinander über. Das ist eine Dreierstruktur (Triole) und ein
   Kandidat für drei Generationen. **Dagegen steht der Bestand:** Unter der Ladung Q_* wirkt der S₃-Zyklus als Phase und nicht als
   Generationsschritt (r13). Die drei Kopien teilen sich außerdem nur die reelle Einheit, nicht ihre imaginären Richtungen. Ob sie als
   Generationen tragen, ist offen und nicht gerechnet. Nach Eakin–Sathaye (Literatur, hier nicht nachgerechnet) bringt jede weitere
   Verdopplung ein weiteres S₃.
4. **Verträgliche Kreisachsen (Teil C).** Gezählt wird die größte Menge paarweise antikommutierender L_{e_i} (Kreisachsen, deren
   Drehungen zusammenpassen). Ergebnis: 1, 3, 7, 8, 9 für n = 1 … 5, **exakt die Radon–Hurwitz-Zahl** ρ(2ⁿ) − 1. Bis 𝕆 sind alle
   2ⁿ − 1 Imaginären verträglich. Danach sind es nur noch 8 von 15 und 9 von 31. Fortgesetzt: 0, 1, 3, 7 | 8, 9, 11, 15 | 16, 17, 19, 23, also
   ρ(16N) = ρ(N) + 8. Das ist die Clifford-Periode 8 (Bott), im Turm eine Periode 4: **HS(4)–HS(7) wiederholen HS(0)–HS(3) auf einem vollen
   Oktonion-Block.** HS(6) hat 11 = 1 + 3 + 7 Achsen, genau die Imaginären von ℂ, ℍ, 𝕆 im Dixon-Träger, und steht an der Stelle von HS(2).
   Hurwitz und Bott haben dieselbe Wurzel: ρ(N) = N gilt genau für N = 1, 2, 4, 8.
5. **Was weiter wächst.** Die Lie-Algebra der Linksmultiplikationen wird ab 𝕆 voll: so(8) (28), so(16) (120) (k253). Das ist Wachstum ohne
   Struktur, denn jede Drehung wird erreichbar.

## Was heißt das für den Turm?
- Bis HS(3) bringt jeder Shift eine neue, voll verträgliche Kreisachse und eine größere stetige Symmetrie (U(1) → SU(2) → G₂ ⊃ SU(3)).
- Ab HS(4) kommt keine stetige Symmetrie mehr dazu. Neu sind Lecks (Nullteiler), eine diskrete Dreierstruktur (S₃ auf drei Oktonionen)
  und ein periodisches Muster der Kreisachsen. Die Vermutung „später einfacher, in bekannte Physik konvergierend“ wird damit genauer: Der
  Turm wird ab HS(4) **periodisch mit Periode 4**, und die neuen Elemente sind diskret (S₃, Kopien) statt stetig.
- Möglicher Anschluss an bekannte Physik: Bott-Periodizität ordnet in der Physik die Spinoren nach Dimension mod 8 und die topologischen
  Phasen (Zehnfach-Weg, Kitaev). Drei Kopien plus S₃ erinnern an die Generationen. Beides ist hier Lesart und nicht gerechnet.

## Grenzen
- Nicht blind; Algebra aus der Literatur, nur nachgerechnet. Die Turm-Lesart (Kreisachse = Feldrichtung) ist eine Setzung aus k253.
- Die Zählung der Kreisachsen über Basis-Einheiten ist eine untere Schranke für beliebige Richtungen; dass sie Radon–Hurwitz erreicht, sagt
  der Satz von Hurwitz–Radon (Obergrenze), nicht die Rechnung.
- Generationen aus S₃: nicht gezeigt, nach r13 eher nicht als Schritt; offen.
- OP1, OP3, OP5 offen; kein Guard berührt.

## Dateien
`k254_hs4_warum.py` (`k254_out.txt`), `k254b_s3_wolfram.wl` (`k254b_out.txt`), `k254c_drei_oktonionen.py` (`k254c_out.txt`).
Aufruf aus diesem Ordner; die Skripte lesen `../k253_cayley_dickson_turm.py`.
