# Ergebnis H175 mit Erkundung k372 und Nachtrag k373: Term aus der Ladungsrichtung

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H175_Term_aus_Ladungsrichtung.md` (Commit 9135e83, vor der Rechnung). H175a bis c blind.
k372 ist eine Erkundung (nicht blind, in der Vorab-Notiz angekündigt), k373 ein Nachtrag (nachträglich, nicht vorab festgelegt).
Skripte k371 (Python), k371b (Wolfram, fünf Punkte unabhängig nachgerechnet, stimmen überein), k372, k373 (nur Python). Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Ein Term aus der Ladungsrichtung kann die Mischung treffen, ist dafür aber nicht nötig und nicht ausgezeichnet; die Eingaben
zerfallen sauber in solche, die θ₁₃ bewegen, und solche, die θ₁₂ und die Massen bewegen; nachträglich gefunden ist ein Fall mit einer einzigen Zahl, der alle
vier Messgrößen trifft, aber einen anderen Versatz verlangt als die geladenen Leptonen.

## H175 gegen die Kriterien
| Teil | Befund | Urteil |
|---|---|---|
| H175a (blind) | Ladungsrichtung, zwei freie Zahlen: κ₁ = 0,0291, κ₂ = 0,0424; χ² = 1,99; sin²θ₁₃ = 0,02250, sin²θ₁₂ = 0,30365, sin²θ₂₃ = 0,4940 (+1,4σ), sin δ = 0,980. Vergleichsklassen: symmetrisch A-ungerade (2 Zahlen) χ² = 0,57; symmetrisch A-gerade (3 Zahlen) χ² = 0,00; antisymmetrisch A-gerade (1 Zahl) χ² = 40 | **verträglich**, aber nicht ausgezeichnet: zwei andere Klassen passen ebenso |
| H175b (blind) | Eine Richtung allein: K₂ mit κ = 0,0439 gibt χ² = 8,1 (θ₁₃ +0,1σ, θ₁₂ +2,5σ, θ₂₃ +1,4σ); K₁ allein χ² = 40 | **trägt nicht** (θ₁₂ außerhalb 2σ) |
| H175c (blind) | 16 Fälle (die Vorab-Notiz nennt irrtümlich 24). Mit x: kein Fall verträglich; zwei mit θ₁₃ innerhalb 3σ. K₂ mit κ = +tan x: θ₁₃ −1,5σ, θ₁₂ +2,5σ. K₁ mit κ = −tan 2x: θ₁₂ +10σ, nicht verträglich. Kontrolle x_R: ein Fall verträglich, κ = +tan x_R in Richtung (K₁ + K₂)/√2: 0,02152 (−1,7σ), 0,30288 (−0,1σ), 0,4956 (+1,5σ) | mit x **nicht entschieden**; mit x_R ein verträglicher Fall unter 16 |

Zum Mehrfachvergleich: Die 16 Fälle streuen in sin²θ₁₃ von 0,004 bis 0,031. Dass zwei bis vier davon in ein Fenster von ±3σ fallen, ist auch zufällig zu erwarten.

## Erkundung k372: welche Eingabe bewirkt was (nicht blind)
Es gibt acht unabhängige Terme, die ℤ₃ brechen können (reell symmetrisch S oder imaginär antisymmetrisch K, je gerade oder ungerade unter A). Ableitungen bei x:

| Eingabe | sin²θ₁₃ | sin²θ₁₂ | sin²θ₂₃ | Koide-Wert und Phase des zirkulanten Teils |
|---|---|---|---|---|
| S⁺b (wie b in N̂) | −0,154 | +0,106 | −0,103 | unverändert |
| S⁻q | +0,154 | −0,106 | −0,125 | unverändert |
| K⁻₂ (Ladungsrichtung) | +0,167 | −0,114 | −0,135 | unverändert |
| S⁺c | +0,022 | +0,499 | +0,342 | ändern sich |
| S⁺d | −0,022 | −0,499 | +0,181 | ändern sich |
| S⁻p | +0,015 | +0,353 | +0,242 | ändern sich |
| K⁺ | +0,017 | +0,382 | −0,014 | ändern sich |
| K⁻₁ (Ladungsrichtung) | −0,024 | −0,540 | +0,019 | ändern sich |

- **Zwei Gruppen.** Drei Eingaben (S⁺b, S⁻q, K⁻₂) bewegen θ₁₃, lassen die Massenstruktur in erster Ordnung unberührt und halten sin δ = 1. Fünf Eingaben bewegen vor allem θ₁₂
  und verschieben dabei Koide-Wert und Phase des zirkulanten Teils. Deshalb reicht keine einzelne Eingabe: Man braucht je eine aus beiden Gruppen.
- **Stochastische Suche** (abgekühlte Metropolis-Suche, 48 Läufer, alle acht Richtungen): Die verträgliche Menge ist nach Abzählung fünfdimensional; drei Kombinationen
  sind durch die drei Winkel festgelegt, der Rest ist frei. Keine Symmetrieklasse wird bevorzugt (Anteile 0,35 / 0,28 / 0,11 / 0,27).
- **Kleinster Term, der alle drei Winkel genau trifft:** Norm 0,061 (x) bzw. 0,060 (x_R), verteilt auf S⁺c, S⁺d, S⁻p, S⁻q und K⁻₂; Anteil der Ladungsrichtung 16 bis 18 %.
  Die Daten verlangen die Ladungsrichtung also nicht.

## Nachtrag k373 (nachträglich, Richtung nach Ansicht der 16 Fälle gewählt)
Ein einziger Parameter x für das Neutrino-Spektrum (R), die Stärke κ = tan x in Richtung (K₁ + K₂)/√2 und alle drei Winkel:
x = 0,04478 ± 0,00091, **χ² = 2,86 bei vier Messgrößen und einer Zahl** (ohne Term: χ² = 67,1). R −0,7σ, sin²θ₁₃ = 0,02229 (−0,3σ), sin²θ₁₂ = 0,30185 (−0,3σ),
sin²θ₂₃ = 0,4954 (+1,5σ), sin δ = ±0,977. Die anderen sieben Varianten: χ² zwischen 9 (K₂ allein) und 517.
- **Preis:** Der Versatz der geladenen Leptonen x = 0,039577 liegt 5,7σ daneben (χ² = 34,5 dort). Der gemeinsame Versatz aus H168 gälte dann nicht; das Verhältnis wäre 1,13.
- **Geometrie (Beobachtung):** K₁ und K₂ spannen als Achsenvektoren genau die Ebene senkrecht zur festen TM1-Spalte (1, 0, 1)/√2 auf; (K₁ + K₂)/√2 liegt in dieser
  Ebene in der Mitte zwischen den beiden Baum-Eigenrichtungen der Neutrinos (45°). Ob das mehr als Zufall ist, ist nicht geprüft.
- **Was daraus prüfbar würde:** sin²θ₁₂ = 0,302, sin²θ₂₃ = 0,495, |sin δ_CP| = 0,977. Das wäre vor neuen Daten als eigener Test festzuschreiben.

## Bilanz der Setzungen (Strang 3)
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H173 | Ein-Feld-Form, Brannen-Spektrum | Winkel aus der Phase | θ₁₃ zu klein |
| H174 | Beimischung der neutralen Form | nötiger Term halb imaginär-antisymmetrisch | Herkunft dieses Terms |
| H175 | s–v-Kopplung, A-ungerade | zwei Gruppen von Eingaben; Ladungsrichtung möglich, nicht nötig | Richtung in der K-Ebene und Stärke; ob Neutrino- und Lepton-Versatz gleich sind |

Angepasst, nicht hergeleitet: alle Stärken in H175a und b, die Richtung (K₁ + K₂)/√2, der Wert x in k373. Hergeleitet (Lineare Algebra): die erlaubten Terme und die Ableitungen.

## Grenzen
- Nur das ungerade Element A aus k262b; gleiche Normierung von Ĉ und Zusatzterm; Polmassen; keine Maske (Materie-Frame). Bei einem verträglichen Befund ist die Maske
  nachzuholen; mit dem postulierten ε ist sie nach H173c allerdings weit weg.
- k373 ist eine nachträgliche Auswahl aus acht Varianten und kein Test. χ² = 2,9 bei drei Freiheitsgraden ist unauffällig gut, nicht mehr.
- Erste Fassung von k372 Teil 3 (Powell-Suche) lief zu lange und wurde durch eine Suche mit Nebenbedingungen ersetzt; Teile 1 und 2 unverändert neu gelaufen.
- OP3 und OP4 bleiben offen. Kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H175, k371, k372, k373. Nächste frei: H176, k374.
