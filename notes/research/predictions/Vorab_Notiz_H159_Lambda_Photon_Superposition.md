# Vorab-Notiz H159: Ist Λ im Photon-Frame eine Superposition (Netto null, Anteile ungleich null, Verhältnis γ_L⁵), und löst das das HC-Problem am Photon?

**Stand:** 2026-11-26, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 26.11.2026, 07:29 UTC: „jage das mal durch den hc, ich habe so die vermutung das sich dann auch das problem mit dem hc auf dem photon frame
auf einmal auflösen könnte“. Gemeint ist die Idee, die zwei Aussagen der Folgerung „Cosmological constant revisited“ (Vakuumdichte im Photon-Frame null **und**
ρ_vac(photon)/ρ_vac(matter) = γ_L⁵) als Superposition zu lesen: Erwartungswert null, Anteile nicht null, Verhältnis der Anteile γ_L⁵.
Skripte **k350** (Python sympy) und **k350b** (Wolfram Language, unabhängig). Der Block k350–k359 ist für diesen Faden belegt (k342–k349 bleiben dem parallelen
Faden zur Generationszahl). Qiskit nicht vorgesehen: keine Schaltung, kein Messablauf; die „Superposition“ ist hier eine Zerlegung einer klassischen Feldlösung.
Kein HDL/MMA-Vergleich (kein RUN_TAPE-Bezug, kein endlicher Auswahlablauf). Kein Guard wird berührt.

## Vorwissen geprüft
- **Die Folgerung und ihr Status:** `sec:phase-constants`, Folgerung „Cosmological constant revisited“ mit Statusvermerk der 4.10-Konsolidierung (beide
  Aussagen zusammen sind keine konsistente Herleitung einer Vakuumgröße). **v4.8.0-r03 F1:** das Verhältnis ist γ_L⁵ statt γ_L⁶, und es kommt allein aus der
  Gewichtsregel k(ρ_vac) = k(ħ) − 4·k(l_P) = 1 − 6 = −5 (Lemma v4.8.0-r03.1). **v4.9.0-r69.3(c):** für ein und dieselbe Größe können nicht beide gelten; eine
  Unterscheidung von Netto- und Bruttodichte „müsste definiert werden“. **r69, Frames:** Der alte „Photon-Frame“ dieser Stellen ist **R** (β_sym = 0, v4.9.0-r24),
  nicht der Photonpunkt P; „P ist ein entarteter Grenzfall und braucht eine eigene normierte Observable“ (r69.1(a)).
- **Λ im Bestand:** Eingabe bzw. Integrationskonstante (v4.10.0-r04, r06.3); ρ_Λ = Λ/κ (r61). H96 (Ω_M = β_sym²) offen. OP5 offen.
- **HC im Feldgleichungs-Faden:** k292 (Ellipse a·e^{iωt} + b·e^{−iωt}, μ = b/a, K = (a + b)/(a − b) = γ_L; HC legt die Form fest, nicht die Größe), k297
  (Tausch = μ → 1/μ; V = η(B − μ²A)²; Fluss: fest ist nur λ_B/λ_A = 1, also μ = 1), H132/k298 (auf der HC-Richtung kein masseloses Eichfeld; HC-Potential
  nicht SU(2)-invariant), k299 (Strom J = ψ̄Dψ, J_i = ω(a² − b²), |J_⊥| = 2abω; Fassung F und Fassung S), H136/k305 (mit SU(2) keine Rückwirkung über einen
  ruhenden Winkel). `thm:hc-quasiconformal` mit Statusvermerk r23.
- **Tausch J:** antilinear, z ↦ i·z̄ (r63/r64, H149: θ = π/4 ist Fixpunkt). Postulat der Frame-Gleichberechtigung (Autor, 26.11.2026): J ist Symmetrie.
- **Photonpunkt:** k250 (bei P ist ρ = I/2, keine unitäre HC-Dynamik stört a = b), k253 (lineare Polarisation = zwei gegenläufige Kreisanteile), r23 (keine
  endliche Kaskade erreicht P), „HC je Frame“ (Forschungsstand: P trägt seit r63 keine Zählung).
- **H78/H79, I4** (das T-Bild sieht −V): geprüft als mögliche Quelle einer unter J ungeraden Vakuumgröße; I4 ist seit dem 6.11. unter den geltenden Lesarten gescheitert.
- Suche nach „Netto“, „Brutto“, „net density“, „bare density“ zusammen mit Vakuum unter `notes/research`, `wiki`, `analysis` (26.11.): keine Definition vorhanden.

## Welches HC-Problem am Photon ist dokumentiert?
Vier Stellen, die zusammengehören:
1. **Entartung:** Der HC ist als quasikonforme Abbildung nur für |μ| < 1 erklärt. Am Fixpunkt des Tauschs ist μ = 1, K = ∞, die Ellipse ist eine Linie, die
   Ladung ω(a² − b²) null (k292, k297, r69.1(a)).
2. **Keine Wirkung:** Bei P kann keine unitäre HC-Dynamik a = b stören (k250).
3. **Licht und HC schließen sich aus:** Mit dem HC-Potential bleibt kein Eichfeld masselos, und das Potential verträgt sich nicht mit SU(2) (H129, H132).
4. **Zwei „Photon-Frames“:** Die alten Aussagen (Λ = 0, HC trivial mit K = 1, Licht masselos) gehören zu R (μ = 0), der Fixpunkt des Tauschs ist P (μ = 1).

## Aufbau
- ψ = e^{iωt}(a + b·j), Schatten in ℂ: z = a·e^{iφ} + b·e^{−iφ}. Frames über μ = b/a: R: 0, M: β_sym² (eingesetzt, OP1), P: 1, T: 1/μ_M.
- **Teil 1 (Tausch):** J: z ↦ i·z̄ auf den Koeffizienten; Fixpunktmenge; C = ½(1 + J) als reell-lineare Projektion und ihr Bild.
- **Teil 2 (Netto und Brutto):** quadratische Größen der Lösung nach ihrer Parität unter J sortieren (N-Mittel a² + b², Ladung ω(a² − b²), |J_⊥|, Energie
  der Drehung, K₁ = Q²). Netto := J-ungerader Teil, Brutto := die zwei Anteile einzeln.
- **Teil 3 (γ_L⁵):** Verhältnisse der Anteile (in P und in M) und Verhältnisse P : M und R : M für jede Größe aus Teil 2 und für die Terme V = η(B − μ²A)²,
  Fassung F, Fassung S, jeweils bei drei Normierungen (gleiches a² + b², gleiches a, gleiche Fläche a² − b² für R : M). Vorab festgelegter Suchraum; geprüft
  wird, ob eines dieser Verhältnisse als Identität in μ gleich K⁵ = ((1 + μ)/(1 − μ))⁵ ist.
- **Teil 4 (HC am Photon):** (a) Fassung F im Grenzfall μ → 1 nach Umskalierung (Bedingung J_i = 0): Invarianz, Eichfeldmassen im Vakuum, Kosten einer
  Abweichung. (b) Massenmatrix aus H132 Stufe A bei θ = 45°. (c) Welche μ macht V = η(B − μ²A)² J-symmetrisch, und was ist dann V im M-Zustand?

## Hypothese H159
Im HC-Formalismus ist der Photon-Zustand eine Superposition zweier gegenläufiger Anteile. (i) Es gibt eine Vakuumgröße, deren Netto-Wert dort null ist, während
die Anteile nicht null sind; (ii) das Verhältnis der Anteile ist γ_L⁵; (iii) in dieser Lesart ist der HC am Photon regulär, und Licht bleibt masselos.

## Entscheidungskriterien
- **K-a (Netto null, Anteile nicht null):** Es gibt im Formalismus eine J-ungerade quadratische Größe, die auf der Fixpunktmenge verschwindet, mit zwei
  gleich großen Anteilen ungleich null: bestätigt. Gibt es sie, ist aber die Zuordnung zur Vakuumdichte eine Setzung: „trägt teilweise“. Sonst widerlegt.
- **K-b (γ_L⁵):** Eines der Verhältnisse aus Teil 3 ist als Identität K⁵: bestätigt. Entsteht K⁵ nur, wenn der Exponent über die Gewichtsregel von außen
  eingesetzt wird: widerlegt (das Verhältnis folgt dann nicht aus der Superposition). Erscheint eine andere reine Funktion von γ_L für das Verhältnis
  P : M oder R : M der Vakuumgröße: wird berichtet, zählt nicht als Bestätigung.
- **K-c (HC-Problem):** (c1) Fassung F ist bei μ = 1 nach Umskalierung endlich, invariant unter SU(2) links × U(1) rechts, gibt im Vakuum keine Eichfeldmassen
  und hat die Lösung a = b als Minimum mit **quadratischen** Kosten einer Abweichung: bestätigt. Sind die Kosten erst von vierter Ordnung (keine Rückstellkraft
  in führender Ordnung): „trägt teilweise“. (c2) Die Massenmatrix aus H132 Stufe A hat bei θ = 45° einen Eigenwert null: bestätigt, sonst widerlegt.
  K-c ist bestätigt, wenn c1 und c2 bestätigt sind; „trägt teilweise“, wenn c1 mindestens teilweise trägt und c2 widerlegt ist; sonst widerlegt.
- **Gesamturteil:** bestätigt nur, wenn K-a, K-b und K-c bestätigt sind. „Trägt teilweise“, wenn K-a mindestens teilweise trägt und K-b oder K-c scheitert.

## Vorab offengelegt (kein Teil der Vorhersage)
Überschlag beim Aufschreiben (im Kopf, ungeprüft):
- J vertauscht die Koeffizienten: (a, b) ↦ (i·b̄, i·ā). Fixpunkte haben |a| = |b|: lineare Polarisation längs der 45°-Linie. C = ½(1 + J) bildet **jeden**
  Zustand auf diese Linie ab. K-a ist damit für die Ladung Q = ω(a² − b²) so gut wie sicher; Q ist aber eine Ladung und keine Energiedichte.
- Die Energie der Drehung und a² + b² sind J-gerade. Eine J-ungerade Energiedichte sehe ich im Ansatz nicht.
- Alle Terme der Lagrangedichte haben geraden Grad in den Amplituden. Verhältnisse der Halbachsen geben K^(Grad), also gerade Potenzen oder rationale
  Funktionen von μ. Eine fünfte Potenz erwarte ich nicht.
- Fassung F: τ = 2μ/(1 − μ²) → ∞; P/τ⁴ → η₂·J_i⁴/N². Mit J_i ≈ −2a²ω·d sind die Kosten vermutlich ∝ d⁴. Die quadratische Variante J_i²/N ist die Form von
  Fassung S, die ρ verschiebt (k299).
- H132: Determinante 4g_L²g_R²·A·B ist bei A = B am größten.
- V = η(B − μ²A)² ist nur für μ = 1 unter A ↔ B symmetrisch. Dann ist V(P) = 0 und V(M) = η·f⁴·cos²2θ mit cos 2θ = (1 − μ²)/(1 + μ²). Der Zahlenwert
  cos²2θ ≈ 0,694 stand schon in k299 (Tabelle). **Die Nähe zu 1 − β_sym² ≈ 0,698 (H96) ist mir beim Aufschreiben aufgefallen**; ob sie eine Identität ist,
  ist nicht geprüft (vermutlich nicht: ((1 − β⁴)/(1 + β⁴))² gegen 1 − β²).

## Vorhersage
- K-a: **trägt teilweise** (Netto null und Anteile ungleich null gibt es, für die Ladung; die Zuordnung zur Vakuumdichte wäre gesetzt).
- K-b: **widerlegt** (γ_L⁵ kommt aus der Gewichtsregel, nicht aus dem Verhältnis der Anteile).
- K-c: **trägt teilweise** (c1 trägt teilweise: regulär und SU(2)-verträglich, aber weiche Rückstellung; c2 widerlegt).
- Gesamt: **trägt teilweise**. Offen vor der Rechnung: ob der Überschlag stimmt; ob eines der Verhältnisse aus Teil 3 doch K⁵ gibt; die Ordnung der Kosten
  in Fassung F; ob die Zahl 0,694 eine Identität mit 1 − β_sym² ist; was unter dem Postulat der Frame-Gleichberechtigung für μ im HC-Potential folgt.

## Grenzen (vorab)
Klassische Lösung und klassische Massenmatrix, nur ℂ → ℍ, ohne Fermionen, ohne Schleifen. Die Fassungen des HC als Potential (k297) und als Strombedingung
(k299) sind Setzungen. β_sym und γ_L sind eingesetzt (OP1). Die Gleichsetzung „Photon-Frame = Fixpunkt des Tauschs“ ist die Lesart des Autors für diese
Hypothese; der Bestand führt die alten Photon-Frame-Stellen als R. Λ bleibt Eingabe (r04, r06.3); OP5 bleibt offen.
