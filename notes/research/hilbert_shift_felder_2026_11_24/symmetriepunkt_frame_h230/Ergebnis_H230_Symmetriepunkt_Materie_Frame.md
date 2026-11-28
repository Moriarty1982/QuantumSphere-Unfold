# Ergebnis H230 (k444): Der Symmetriepunkt π/8 wird durch keine Frame-Abbildung zum Messwert – abgehakt

Stand 28.11.2026. Vorab-Notiz `Vorab_H230_Symmetriepunkt_Materie_Frame.md` (Commit b61335a, vor der Rechnung). Hauptrechnung `k444_test_h230.py` mit
Ausgabe `k444_out.txt`, Gegenprobe in Wolfram `k444b_gegenprobe.wl` mit Ausgabe `k444b_out.txt`.

## Frage

Der Symmetriepunkt π/8 der gemeinsamen Vakuumenergie (H225) liegt im Ruheframe R. Er war bisher direkt mit dem Messwert x = 0,0395773 verglichen
worden, obwohl dieser im Materie-Frame M gemessen wird. Der Autor wollte den fehlenden Schritt nachholen, damit er abgehakt werden kann: Wird π/8 (oder 0)
durch eine der erklärten Frame-Abbildungen zum Messwert?

## Urteil: widerlegt – der Schritt ist erledigt

| Teil | Ergebnis |
|---|---|
| A: Maske auf das Spektrum (Formen K, linear, S; ±ε₀, ±2ε₀) | Kein Treffer. Form S lässt das Spektrum stehen (δ′ = π/24 in beiden Sektoren, wie in R); Form K und linear verletzen K = ⅔ (K′ = 0,744 bis 23,7) und geben δ′ von 0,0003 bis 0,83, nirgends die Datenphase 0,2222 |
| B: Winkel-Abbildungen (Aberration, Kontraktion, Maske, je mit β_sym oder tanh 2ε₀; Lesarten φ, 2φ, 3φ) | Kein Treffer. Die 36 Bilder liegen zwischen 0,116 und 1,200; das kleinste (Aberration mit tanh 2ε₀) ist dreimal so groß wie x (97 000σ). Kein Bild unter 0,1, also auch kein lockerer Treffer |
| Punkt 0 | Unter allen Winkel-Abbildungen fest (Bild 0); im Spektrum schon in H166d ohne Treffer gerechnet, hier zur Kontrolle wiederholt (gleiche Werte) |
| Grenzfälle | Lichtpunkt P (β → 1) bildet auf 0 oder π ab, der Dual-Frame T (z ↦ iz) verschiebt um π/2; beides gibt nur rationale Vielfache von π |

**Gesamturteil nach Vorab: widerlegt.**

## Lesart

- Der Abstand zwischen π/8 und x lässt sich nicht als Frame-Effekt deuten. Die Frame-Abbildungen verschieben π/8 höchstens bis 0,116. Um bis 0,04 zu
  kommen, bräuchte es Rapiditäten weit über 2ε₀, und der Rahmen liefert keine.
- Die Abbildung, die die Spektralform erhält (Form S, Ähnlichkeit), lässt die Phase in jedem Frame gleich. Das wusste schon H166, für π/8 ist es jetzt
  ausdrücklich geprüft. Formen, die die Phase verändern, zerstören zugleich K = ⅔. Eine frame-abhängige Phase bei festem Koide-Wert gibt es in diesem
  Rahmen also nicht.
- Damit sind die zwei Fragen getrennt: Der Wert von φ ist kein Übersetzungsproblem zwischen R und M. Er braucht einen echten Brecher des Sektortauschs.

## Gegenprobe

Wolfram rechnet Teil B mit 30 Stellen nach (alle Bilder gleich, die fünf nächsten auf 12 Stellen) und Teil A für Form K über die Eigenwerte von DCD (K′ und δ′
auf 7 Stellen gleich). cosh 2ε₀ = γ_L auf 4·10⁻¹⁶. Qiskit war nicht geeignet.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt:** die Liste der Abbildungen (aus H45/H134, H166, r57, den Frame-Rapiditäten ε₀ und 2ε₀), die Lesarten φ, 2φ, 3φ, ρ² = ½.
- **Nicht blind:** vier Werte aus Teil B (Aberration von π/8 und π/4 mit β_sym) waren bei der Planung überschlagen; der Punkt 0 war in H166d gerechnet.
- **Nachträglich:** keine weitere Abbildung geprüft.

## Folgerung

Der Schritt „Symmetriepunkt in den Materie-Frame übertragen“ ist erledigt und kann abgehakt werden: Kein Frame-Wechsel macht aus π/8 oder 0 den Messwert.
Offen bleiben die beiden anderen Richtungen aus dem Vorschlag nach H229: die Rückwärtssuche nach dem Brecher des Sektortauschs und die Ladung (Photonschleife nur
im Im-Sektor) mit fester Stärke α. OP3 bleibt offen.

Vergeben: H230, k444. Nächste frei: H231, k445 (vor Vergabe gegen `main` prüfen).
