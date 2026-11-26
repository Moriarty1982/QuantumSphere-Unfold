# Erkundung k378: Der Farbanteil ist nicht frei, und die Farbrichtung allein verschiebt δ nicht

**Stand:** 26.11.2026. **Erkundung, nicht blind** (beide Hauptaussagen standen vor der Rechnung aus der Darstellungstheorie bzw. der Alternativität fest).
Anlass: Autor, 26.11.2026, „mergen und weiter“ (Farbanteil herleiten, Wirkung auf δ prüfen). Skripte k378 (Python, explizite Oktonionen) und k378b
(Wolfram, trigonometrischer Teil und Zahlen). Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Ein Farbtriplett liegt vollständig in den sechs Farbrichtungen, der in H178c gesetzte gebrochene Farbanteil hat also keine
Grundlage; damit trennt die Farbe Up und Down nicht, und bei gleich ausgerichteten Nebendiagonalen verschiebt sie auch die Phase δ nicht.

## 1. Farbanteil
- Der(𝕆) hat Dimension 14 (g₂); die Derivationen mit D(e₇) = 0 bilden su(3)_c (Dimension 8). Ihr gemeinsamer Kern ist genau span{1, e₇}; der Rest zerfällt
  in 3 ⊕ 3̄ (Casimir 0, 0 und sechsmal 4/3).
- **Folge (Schur):** Ein Feld, das als Farbtriplett transformiert, hat keinen Anteil entlang 1 oder e₇. Für beide Quarktypen ist sin²α = 1.
- **Berichtigung zu H178c:** Die Regeln R1 und R2 (Farbanteil ⅓ oder ⅔ je nach Ladung) sind mit einem Farbmultiplett nicht verträglich. Das Urteil
  „verträglich“ aus H178c gilt nur für die dort gesetzte Parametrisierung und trägt als Lesart nicht. H178a und H178b sind davon nicht berührt.
- Mit reiner Farbe gibt das Potential aus H178 für beide Quarktypen denselben Winkel, sin²θ = −A/(2B). Gemessen sind 0,554 (d) und 0,625 (u). Jeder
  Quarktyp braucht also ein eigenes Verhältnis A/B: −1,108 (d) und −1,249 (u). **Das sind zwei freie Zahlen für zwei Messgrößen.**

## 2. Phase δ
- Kubischer Term der Albert-Algebra t = Re((x₁x₂)x₃). Für gleiche Einträge x_i = cos φ + sin φ·n ist t = cos 3φ für **jede** imaginäre Richtung n
  (2000 Zufallsfälle, 2·10⁻¹⁵; die von einem Element erzeugte Unteralgebra ist ℂ). Die Farbrichtung als solche verschiebt δ nicht.
- Für verschiedene Richtungen gilt exakt t = cos³φ − cos φ sin²φ·(n₁·n₂ + n₂·n₃ + n₁·n₃) − sin³φ·Φ(n₁, n₂, n₃), Φ die assoziative 3-Form.
  Erst wenn die drei Kopien in **verschiedene** Farbrichtungen zeigen, wandert die Nullstelle (von π/6 bis π/4 beim assoziativen Tripel, bis π/2 sonst).
  Das wäre eine neue Setzung (welche Kopie welche Farbrichtung trägt) und ist hier nicht weiterverfolgt.

## 3. Abstand vom masselosen Punkt
| Sektor | ρ | masseloser Punkt δ₀ | gemessen δ | Abstand x |
|---|---|---|---|---|
| e | 1,000 | 0,2618 (π/12) | 0,2222 | 0,0396 |
| d | 1,115 | 0,1633 | 0,1001 | 0,0632 |
| u | 1,290 | 0,0568 | 0,0518 | 0,0050 |

Der kleine Wert von δ bei den Quarks ist zum größten Teil eine Folge des größeren ρ: Der Punkt, an dem die leichteste Masse verschwindet, rückt mit ρ
nach unten. Der Abstand x misst nur, wie klein die leichteste Masse ist. Die Stellgrößen je Sektor sind also besser (ρ, x) als (K, δ); x ist für die
drei geladenen Sektoren 0,040 / 0,063 / 0,005 und zeigt kein gemeinsames Muster.

## Lesart
- **Was steht.** J legt 45° nur für farblose Felder fest (H178a, b). Für Quarks ist der Winkel frei.
- **Was nicht trägt.** Die Farbe erklärt weder den Unterschied zwischen Up und Down noch die Phase. Was Up und Down trennt, muss farbblind sein
  (Ladung, schwacher Isospin). Im Potential heißt das: Die Koeffizienten hängen vom Sektor ab.
- **Stand der Konfigurationen:** Leptonen: ρ = 1 aus J (Postulat), x angepasst. Quarks: ρ_d, ρ_u, x_d, x_u alle vier gemessen und unerklärt.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H178 | U = e₇; Farbanteil α je Sektor nach Regel | J legt θ nur für α = 0 fest | zwei Koeffizienten und α |
| k378 | nichts Neues | α ist für ein Farbtriplett nicht frei (sin²α = 1); Farbrichtung verschiebt δ nicht | je Quarktyp ein eigenes A/B: die offene Wahl ist wieder bei zwei freien Zahlen (ρ_d, ρ_u) |

Zwei Schritte in Folge mit „trägt teilweise“ zur selben offenen Voraussetzung (Quarkwinkel). Prüfung des Ziels: ρ_d und ρ_u sind Messwerte, keine
gesetzten Eingaben. Die stillschweigend gewählte Weggabelung in H178c war, den Sektorunterschied in den Farbanteil zu legen; sie ist hiermit zurückgenommen.
**Frage an den Autor:** Soll der Unterschied Up gegen Down über die Ladung in den Koeffizienten gesucht werden, oder über die HS-Stufe der Sektoren?

## Grenzen
Ein Feld je Sektor in 𝕆; in ℂ ⊗ 𝕆 (Leiteroperatoren) nicht gerechnet, die Schur-Aussage gilt dort ebenso. Abschnitt 2 behandelt nur den kubischen Term,
nicht die volle Dynamik. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen. Vergeben: k378. Nächste frei: H179, k379.
