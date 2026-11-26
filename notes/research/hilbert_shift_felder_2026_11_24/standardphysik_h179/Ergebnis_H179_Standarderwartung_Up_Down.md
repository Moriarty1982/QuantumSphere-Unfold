# Ergebnis H179: Die Down-Quarks sitzen dort, wo die Leptonen mit den Faktoren 3 und ⅓ landen, aber nur auf wenige Prozent

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H179_Standarderwartung_Up_Down.md` (Commit a986b29, vor der Rechnung). Skripte k379 (Python, 10⁵ Ziehungen,
Seed 20261126) und k379b (Wolfram, Zentralwerte). Zentralwerte stimmen überein. Qiskit nicht eingesetzt.
**Berichtigung zur Vorab-Notiz:** Dort steht, Froggatt-Nielsen komme im Repo nicht vor. Die Suche zeigt eine Erwähnung in H36/r52 (Textur der Kopplungsform).
Georgi-Jarlskog kommt tatsächlich nicht vor (die übrigen Treffer betreffen die Jarlskog-Invariante).

**Ergebnis in einem Satz:** Nach den vorab gesetzten Kriterien ist die Georgi-Jarlskog-Relation **widerlegt** (K_d 6,7σ daneben im Bereich der hohen Skalen);
zugleich trifft sie die Down-Konfiguration ohne freien Parameter auf 0,3 bis 5 %, viel näher als jede andere geprüfte Beziehung.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H179a | Vorhersage aus (3m_e, m_μ/3, m_τ): K = 0,74542, δ = 0,10507, θ = 48,03°, x = 0,0606. Gemessen bei M_Z: K = 0,74779 (+2,1σ; +0,3 %), δ = 0,10013 (−5,2σ; −4,7 %). Bei 2·10¹⁶ GeV: K = 0,73620 (−8,0σ; −1,2 %), δ = 0,10705 (+1,9σ; +1,9 %). Im Bereich 10¹³ GeV bis M_Planck: min \|z_K\| = 6,7 | beide < 3σ bei gemeinsamem I | **widerlegt** |
| H179b | Doppelverhältnisse (3m_s/m_μ)/(m_b/m_τ) und (m_d/3m_e)/(m_b/m_τ): bei M_Z 0,947 und 1,095; bei 2·10¹⁶ GeV 1,071 (+4,7σ) und 1,238 (+13,6σ) | beide < 3σ | **widerlegt** |

## Bericht (nicht blind)
- Einfache Gleichheit Down = Leptonen (K_d = ⅔): ausgeschlossen (0,74).
- Ein-Parameter-Gesetze in der Ladung (Up zu Down wie 2 oder 4): gemessen 2,31 / 2,34 / 2,72 bei M_Z und 2,71 / 2,74 / 3,26 bei 2·10¹⁶ GeV. Keines trägt.
- Potenzgesetz Up-Hierarchie = (Down-Hierarchie)^p: p = 1,70 aus der leichtesten und 1,41 aus der mittleren Masse (35σ auseinander). Kein gemeinsames p.
- **Eichladungen** (Ladung, Hyperladung, Isospin) wirken generationsblind und ändern K, ρ, δ gar nicht. Das ist der Grund, warum die übliche Physik für
  den Unterschied zwischen Up und Down keine Vorhersage hat: Im Standardmodell sind die Yukawa-Kopplungen freie Zahlen.

## Lesart
- **Was die übliche Physik liefert.** Nur eine parameterfreie Beziehung, und sie betrifft Down gegen Leptonen, nicht Up gegen Down. Für den Up-Sektor gibt
  es keine vergleichbare Standardrelation.
- **Wie nah die Relation liegt.** In den Stellgrößen des Projekts: Die Leptonen sitzen bei 45,00°; mit den Faktoren (3, ⅓, 1) landet derselbe Vektor bei
  48,03°. Gemessen sind 48,11° (M_Z) und 47,71° (2·10¹⁶ GeV). Der J-Abstand der Down-Quarks (3,1°) wird also zu 97 % von diesen beiden Faktoren erzeugt.
  In den einzelnen Massen ist die Relation deutlich schlechter (5 bis 24 %); K und δ sind gegen solche Abweichungen unempfindlich. Beides gehört zusammen
  berichtet.
- **Warum das für das Projekt interessant ist.** Die Faktoren 3 und ⅓ sind in der üblichen Herleitung die Zahl der Farben. Zusammen mit H178 (J legt nur
  farblose Felder fest) wäre das eine Lesart: Die Down-Quarks sind „Leptonen mal Farbzahl“. Das ist **nachträglich** gelesen und kein Ergebnis; die
  vorab gesetzten Kriterien sind verfehlt.
- **Messfehler gegen Theorieunschärfe.** Die Kriterien benutzen nur die Messfehler (0,15 % in K). Die Relation selbst gilt in der Literatur nur bis auf
  Schwellen- und Laufeffekte von mehreren Prozent, und das Laufen wurde hier nur im Standardmodell gerechnet. Das war in der Vorab-Notiz als Grenze genannt;
  das Urteil bleibt trotzdem „widerlegt“, weil die Kriterien so festgelegt waren.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k378 | nichts Neues | Farbe trennt Up und Down nicht | ρ_d, ρ_u als freie Zahlen |
| H179 | Georgi-Jarlskog-Faktoren als Zahlenrelation | Eichladungen ändern K nicht; kein Ladungsgesetz trägt | Down hängt näherungsweise an den Leptonen (Faktoren 3, ⅓); Up bleibt frei |

## Grenzen
Laufen im Standardmodell, eine Schleife, Top-Dominanz; Leptonverhältnisse skalenunabhängig genommen. Yukawa-Werte bei M_Z aus k14/k367.
Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen. Vergeben: H179, k379. Nächste frei: H180, k380.
