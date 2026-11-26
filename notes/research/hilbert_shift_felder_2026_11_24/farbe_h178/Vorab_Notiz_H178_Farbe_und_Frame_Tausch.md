# Vorab-Notiz H178: Bricht die Farbe den Frame-Tausch J, und nur bei den Quarks?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026, „ja bitte“ auf die Frage, ob die Farbe als Kandidat für den J-Bruch der Quarks als Test
mit Vorab-Notiz angesetzt werden soll. Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3. Vergeben: H178, k377 (geprüft: frei).

## Vorwissen geprüft
- H149 (`../generationszahl_h138/`): J: ψ ↦ Uψ̄ bildet in der Ebene {1, U} θ auf π/2 − θ ab; Fixpunkt π/4, dort K = ⅔.
- H155/H156: K = ⅔ folgt aus J als Symmetrie des Potentials; geeignet sind ⟨J⟩ und D₄ = ⟨L_U, Konjugation⟩. Grenze dort: „im vollen Raum von 𝕆 führt L_U aus dem
  Drei-Felder-Raum heraus (nur benannt)“. Genau diese Lücke wird hier gerechnet.
- H128 und Trialität (`../kollaps_h128/`, `../rueckwaerts/trialitaet/`): Farbe su(3)_c = Stabilisator von e₇ in G₂.
- H127/k277: SO(3)-äquivariante Konstruktionen sind auf den Quarks invariant (kein Massenaufspalt daraus).
- H148a: Gram-Auslesung gibt für Farbrichtungen K = ½, nicht die gemessenen Werte.
- H172, H177, k376: Quarkwinkel θ_d = 48,11°, θ_u = 52,21° (M_Z), fast skalenstarr; K ≠ ⅔ ist ein J-Bruch bei erhaltener Dreiersymmetrie.

## Suchrichtung (rückwärts)
Notwendige Bedingung aus k376: eine Eingabe, die J bricht, die Dreiersymmetrie erhält und nur bei Quarks wirkt. Statt neue Terme zu erfinden, wird geprüft, ob
das bereits postulierte J auf Feldern mit Farbanteil überhaupt dieselbe Bedingung stellt wie in der Leptonebene.

## Setzungen dieser Notiz
- U ist die Einheit, die die Farbe festhält (U = e₇). Begründung: Ein Feld in der Ebene {1, U} ist genau dann farblos.
- Ein Feld mit Farbanteil: Ψ = cos θ·1 + sin θ·(cos α·U + sin α·c), c eine Einheit senkrecht zu 1 und U, N(Ψ) = 1.
- Potential: allgemeinstes Polynom bis Grad 4 in den Komponenten, invariant unter SU(3)_c, Konjugation und J (also D₄ aus H156, auf ganz 𝕆 fortgesetzt).
- Für Teil c: **ein** Potential für alle Sektoren; die Sektoren unterscheiden sich nur im Farbanteil α, nach einer vorab festen Regel:
  R1: sin²α = 1 − |Q| (e: 0, u: ⅓, d: ⅔). R2: sin²α = |Q| für Quarks (d: ⅓, u: ⅔), e: 0. Beide Regeln sind Setzungen ohne Herleitung.

## Hypothesen und Kriterien
- **H178a (exakt; nicht blind):** J² = +1 in der Ebene {1, U}, aber J² = −1 auf den Farbrichtungen; J bildet die Ebene {1, c} nicht auf sich ab. Erwartung vor
  der Rechnung (aus der Antikommutation von U und c im Kopf hergeleitet): trifft zu. Kriterium: explizite Oktonionen (Fehler < 10⁻¹²) und symbolisch.
- **H178b (exakt; Ausgang offen):** Das J-invariante Potential legt θ nur für α = 0 auf π/4 fest. Kriterium: Für α ≠ 0 hängt der stationäre Winkel von
  Koeffizienten ab (**bestätigt**), oder er bleibt π/4 (**widerlegt**: dann bricht die Farbe J nicht).
- **H178c (Verträglichkeit; Ausgang offen):** Mit einem gemeinsamen Potential und Regel R1 bzw. R2 gibt es Koeffizienten, die θ_d und θ_u (M_Z, ± 3σ)
  als **stabile Minima** liefern, bei denen zugleich π/4 für α = 0 ein Minimum ist. Kriterium je Regel: keine stabile Lösung = **widerlegt**; stabile
  Lösung = **verträglich**. Verträglich ist keine Bestätigung, wenn die Zahl der freien Koeffizientenverhältnisse die Zahl der Messgrößen (zwei) erreicht;
  das wird mit der Zählung berichtet.
- **Vorab bekannt (nicht blind, kein Kriterium):** „Farbe allein“ (beide Quarktypen mit demselben α) sagt θ_u = θ_d voraus und ist durch 48,1° gegen 52,2°
  bereits ausgeschlossen.
- **Bericht:** der Winkel, den dasselbe Potential für ein Feld mit Q = 0 nach der jeweiligen Regel gäbe; die Variante ⟨J⟩ ohne Konjugation.

## Werkzeugwahl
Python (numpy, explizite Oktonionen über Cayley-Dickson; sympy für die Invarianten) und Wolfram Language als unabhängige exakte Kontrolle der stationären
Punkte. Qiskit nicht geeignet (keine Schaltung).

## Grenzen (vorab)
α wird gesetzt, nicht dynamisch bestimmt. Nur ein Feld je Sektor, Grad 4, N = 1. Kein Vorzeichen wird gesetzt, außer der Konsistenzforderung, dass die
Leptonen in einem Minimum sitzen (das ist das offene Vorzeichen 2a − b aus H149, hier als Bedingung benutzt und so benannt). OP3/OP4 bleiben offen.
