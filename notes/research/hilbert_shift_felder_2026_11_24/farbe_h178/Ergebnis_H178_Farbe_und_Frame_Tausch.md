# Ergebnis H178: Der Frame-Tausch J legt den Winkel nur für farblose Felder fest

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H178_Farbe_und_Frame_Tausch.md` (Commit 93e6e75, vor der Rechnung; Teil a nicht blind). Skripte k377
(Python: explizite Oktonionen, sympy) und k377b (Wolfram, stationäre Punkte exakt). Gemeinsame Größen stimmen überein. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** J muss bei den Quarks gar nicht gebrochen sein: Dasselbe J, das die Leptonen auf θ = 45° (K = ⅔) festlegt, stellt an ein Feld mit
Farbanteil keine solche Bedingung; wie weit der Winkel dann wandert, bleibt aber eine angepasste Zahl.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H178a (nicht blind) | Mit U = e₇: J² = +1 auf {1, U}, J² = −1 auf den sechs Farbrichtungen (Fehler 0). J tauscht x₀ und x_U und erhält \|c\|² und N (10⁻¹⁴). Die Ebene {1, c} wird auf {U, Uc} abgebildet, nicht auf sich | exakt | **bestätigt** |
| H178b | Allgemeinstes Potential bis Grad 4 (SU(3)_c, Konjugation, J) auf N = 1: V = A q + B q² + κ p. Stationär bei sin²θ = (A sin²α + κ cos²α) / (2(κ cos²α − B sin⁴α)). Für α = 0 exakt ½, unabhängig von A, B; für α ≠ 0 abhängig von A, B | Abhängigkeit für α ≠ 0 | **bestätigt** |
| H178c, R1 (sin²α = 1 − \|Q\|) | A/\|κ\| = −1,070, B/\|κ\| = +1,375; alle drei Sektoren in stabilen Minima, im ganzen 3σ-Band | stabile Lösung | **verträglich**, keine Bestätigung |
| H178c, R2 (sin²α = \|Q\|) | A/\|κ\| = −0,291, B/\|κ\| = +0,200; stabil im ganzen 3σ-Band | stabile Lösung | **verträglich**, keine Bestätigung |
| Farbe allein (vorab bekannt) | gleiches α für u und d gäbe θ_u = θ_d; gemessen 4,09° Unterschied (92σ) | – | ausgeschlossen |

Zählung zu c: zwei Messgrößen (θ_d, θ_u), zwei freie Verhältnisse, dazu die gesetzte Regel für α. Das ist eine Anpassung.

## Lesart
- **Was hergeleitet ist.** Der Unterschied zwischen Leptonen und Quarks in K braucht keine neue Eingabe, die J bricht. Er folgt aus dem, was schon gesetzt
  war: J als Symmetrie und die Farbe als Stabilisator von U. J ist nur in der farblosen Ebene eine Spiegelung mit Fixpunkt 45°. Auf den Farbrichtungen
  ist J eine Vierteldrehung (J² = −1) ohne Fixrichtung. Damit ist erklärt, **warum** K = ⅔ nur bei den Leptonen gilt. Das beantwortet die Frage aus k376.
- **Was angepasst ist.** Wie groß die Abweichung bei den Quarks ist (3,1° und 7,2°). Sie hängt an zwei Koeffizienten des Potentials und am Farbanteil α
  je Sektor. Beides ist nicht hergeleitet.
- **Farbe allein reicht nicht.** Up und Down tragen dieselbe Farbe und haben verschiedene Winkel. Es muss eine zweite Größe eingehen, die die beiden trennt.
  Hier ist sie als Farbanteil α modelliert und über die Ladung gesetzt; das ist die schwächste Stelle.
- **Unterschied der beiden Regeln (Bericht).** Unter R1 wäre ein Feld mit Q = 0 reine Farbe und säße bei 38,6° (K = 0,546); das passt nicht zu einem farblosen
  Neutrino und spricht gegen R1 als Lesart. Unter R2 ist Q = 0 farblos und sitzt bei 45° wie die geladenen Leptonen (verträglich mit K_ν = ⅔, das in H176
  gesetzt ist). Unter R2 wächst der Winkel monoton mit dem Farbanteil (sin²α = ½ gibt 50,0°).
- **Variante ⟨J⟩ ohne Konjugation:** drei weitere Koeffizienten (x₀x_U und Produkte); π/4 bleibt für α = 0 stationär. Keine schärfere Aussage.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k376 | nichts Neues | K ≠ ⅔ ist kein Bruch der Dreiersymmetrie | Was unterscheidet Quarks von Leptonen in θ? |
| H178 | U = e₇ (farblos = Ebene {1, U}); Potential bis Grad 4; α je Sektor nach Regel | J legt θ nur für α = 0 fest; für α ≠ 0 ist θ frei | zwei Koeffizienten (A/κ, B/κ) und der Farbanteil α je Sektor |

Das Ziel selbst geprüft: K_d und K_u sind Messwerte, keine gesetzten Eingaben. Die Zerlegung „ein Feld = Winkel θ gegen die Einheit, Farbanteil α“ ist
gewählt; in ihr entsteht die Frage nach α. Eine Herleitung von α (etwa aus der Besetzungszahl der Farbleiter) wäre der nächste Schritt und ist nicht gemacht.

## Grenzen
α gesetzt, nicht dynamisch. Ein Feld je Sektor, Grad 4, N = 1. Die Forderung κ < 0 (Leptonen im Minimum) ist das offene Vorzeichen 2a − b aus H149, hier als
Konsistenzbedingung benutzt, nicht hergeleitet. Winkel bei M_Z (an der Planck-Skala 47,7° und 52,4°; ändert die Urteile nicht, nur die Koeffizienten).
δ ist nicht behandelt. Kein Guard berührt; OP3 und OP4 offen. Vergeben: H178, k377. Nächste frei: H179, k378.
