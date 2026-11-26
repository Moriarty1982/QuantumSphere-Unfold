# Ergebnis H182: Der Tausch J erlaubt genau im Farbblock einen ladungsabhängigen Massenterm; die Winkel von Up und Down bleiben angepasst

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H182_Ladung_trennt_Up_und_Down.md` (Commit 70fdce1, vor der Rechnung; Teil a nicht blind).
Skripte `k385_test_h182.py` (`k385_out.txt`) und `k385b_gegenprobe.wl` (`k385b_out.txt`). Gemeinsame Größen stimmen überein.

Werkzeuge: Python (numpy, scipy) für explizite Oktonionen und die Zählung der Invarianten (Grad 2 per Nullraum über die Lie-Algebra, Grad 4 per
Nullraum über 5200 Zufallspunkte und Gruppenelemente, 3876 Monome; Probe an 50 neuen Punkten 1,7·10⁻¹³). Wolfram Language exakt für Teil a, die
Werte der ladungsungeraden Form auf den Feldern und den Zusatz. Qiskit nicht eingesetzt (keine Schaltung, kein Messablauf).

**Ergebnis in einem Satz:** Dieselbe Symmetrie J, die bei den Leptonen jede verschiedene Gewichtung der Ladungen 0 und 1 verbietet, lässt im
Farbblock genau eine hermitesche Form zu, die die Ladungen ⅓ und ⅔ verschieden gewichtet; damit ist erklärt, **warum** Up und Down verschiedene
Winkel haben dürfen und die zwei Lepton-Sektoren nicht, aber **wie groß** der Unterschied ist, bleibt angepasst.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H182a (nicht blind) | H = Q₀ − ½, eingeschränkt: im Farbblock JᵀHJ = +H, auf {1, U} JᵀHJ = −H (Fehler 0; Wolfram exakt). Dasselbe für die Oktonion-Konjugation | < 10⁻¹² | **bestätigt** |
| H182b | Invarianten vom Grad 2 (Farbe, Konjugation, J): 7; ladungsgerade 4, ladungsungerade 3, davon **2 im Farbblock und 1 im Farblosen** | keine im Farblosen | **widerlegt** (nach dem vorab festgelegten Kriterium) |
| H182c | (i) Für jede der 7 + 33 Invarianten bis Grad 4 ist 45° beim Leptonfeld stationär (5,6·10⁻¹²) und V(θ) = V(π/2 − θ). (ii) V_d − V_u spannt einen Raum der Dimension 2 auf | (i) < 10⁻⁹, (ii) ≥ 1 | **bestätigt** |
| H182d | (a_d, b_d, a_u, b_u) sind vier unabhängige Kombinationen, also zwei freie Verhältnisse für zwei Winkel | < 2 für eine Vorhersage | **verträglich, keine Bestätigung** |

## Zu H182b: Was die ladungsungerade Form im Farblosen ist (nachträglich)
Das Kriterium war zu grob gefasst. „Ungerade unter der komplexen Konjugation“ trifft zwei Arten von Formen:
- **hermitesche** (Ψ†HΨ; sie gewichten Ladungs-Eigenräume): ladungsungerade gibt es davon **eine im Farbblock und keine im Farblosen**. Insgesamt
  gibt es drei hermitesche Invarianten: |s|² (farblos), |c|² (Farbe) und h = Ψ†(Q₀ − ½)Ψ im Farbblock.
- **bilineare** (Typ Im(Ψ·Ψ)): je eine im Farblosen und im Farbblock. Die im Farblosen ist Im(x₀² + x_U²). Sie verschwindet auf beiden
  Ladungs-Eigenzuständen (1 ∓ iU)/√2 und auf jedem reellen Feld (Wolfram exakt), gewichtet die Ladungen also nicht.
Das Urteil „widerlegt“ bleibt für die Hypothese in der vorab geschriebenen Form stehen. Die Aussage, auf die es ankam (J lässt im Farblosen keine
verschiedene Gewichtung der Ladungen 0 und 1 zu), trägt in der engeren Fassung „hermitesch“ und ist zusätzlich durch H182c (i) gedeckt. Diese
engere Fassung ist nachträglich.

## Was die Rechnung zeigt
- **Grund.** Die komplexe Konjugation bildet Q₀ auf 1 − Q₀ ab, tauscht also 0 mit 1 und ⅓ mit ⅔. J und die Oktonion-Konjugation (komplex-linear
  fortgesetzt) tauschen im Farblosen ebenfalls 0 mit 1 (J bildet (1 − iU)/√2 auf −i(1 + iU)/√2 ab), im Farbblock aber erhalten sie die Ladung.
  Im Farblosen ist J damit eine Symmetrie zwischen den zwei Lepton-Sektoren; im Farbblock gibt es keine Symmetrie, die Up mit Down tauscht.
- **Folge für die Leptonen.** Neutrale und geladene Leptonen haben denselben Massenterm und denselben Fixpunkt 45°, also K_ν = K_e = ⅔, bis Grad 4
  unabhängig von allen Koeffizienten. Das passt zu H180 (Daten: K_ν = 0,660, erlaubt 0,634 bis 0,701).
- **Folge für die Quarks.** Auf Ψ_± = cos θ·1 + sin θ·n_± ist h = ±sin²θ/6 (Ladung ⅔: +, Ladung ⅓: −). Das Potential ist
  V_± = (A ± C) t + (B ± D) t² mit t = sin²θ, stationär bei t* = −(A ± C)/(2(B ± D)). Die Daten (M_Z) verlangen a_d/b_d = −1,1085 und
  a_u/b_u = −1,2489. Mit D = 0 gelesen: A/B = −1,179, C/B = −0,070, also ein ladungsungerader Anteil von 6 % des ladungsgeraden. Diese Zahlen
  sind angepasst.
- **Antilineare Fortsetzung (Bericht).** Setzt man J antilinear fort, kehrt sich alles um: Der Farbblock hätte keine ladungsungerade Form
  (θ_u = θ_d erzwungen, gegen 48,11° und 52,21°), und im Farblosen wäre die Gewichtung der Ladungen frei. Die Daten wählen also die komplex-lineare
  Fortsetzung. Das ist eine Folgerung aus den Daten, keine Herleitung.

## Lesart
- **Hergeleitet (unter den Setzungen):** Das Muster der vier Sektoren. Zwei Lepton-Sektoren mit demselben K = ⅔; zwei Quark-Sektoren, deren Winkel
  frei und voneinander verschieden sein dürfen. Dafür reicht HS(3) mit der Ladung; die Sedenionen werden dafür nicht gebraucht (Einschränkung von
  k380, siehe k384).
- **Angepasst:** die zwei Verhältnisse, die θ_d und θ_u festlegen. Gegenüber k378 („je Quarktyp ein eigenes A/B“) ist nichts an Zahlen gewonnen;
  gewonnen ist der Ort: Der Unterschied sitzt in genau einer ladungsungeraden Form (und ihrem Partner vom Grad 4).
- **Offen:** Was legt die Stärke C/B fest? Ein Wert von 6 % ist klein; ob er mit einer bekannten Größe des Projekts zusammenhängt, ist nicht geprüft
  und dürfte nur mit Vorab-Notiz geprüft werden. Ebenso offen: δ je Sektor (x_d, x_u).

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k378 | nichts Neues | Farbtriplett hat sin²α = 1; Farbe trennt Up und Down nicht | je Quarktyp ein eigenes A/B |
| k384 | U = e₇; Ladung in der k85-Form | S₃ verknüpft die Farbblöcke; die Ladung trennt sie nicht | Lesart „Block“ oder „Ladung“ (Autor: Ladung) |
| H182 | Feld in ℂ ⊗ 𝕆; J und Konjugation komplex-linear; Quarkfeld als Ladungs-Eigenzustand; Grad ≤ 4 | J verbietet die Ladungsgewichtung im Farblosen und erlaubt sie im Farbblock | Stärke der ladungsungeraden Form (C/B, D/B); komplex-linear gegen antilinear (von den Daten gewählt) |

Dritter Schritt in Folge mit „trägt teilweise“ zur selben offenen Voraussetzung (Quarkwinkel). Prüfung des Ziels: θ_d und θ_u sind Messwerte, keine
gesetzten Eingaben. Die Frage nach zwei getrennten Koeffizienten entsteht in der gewählten Zerlegung „ein Feld je Sektor mit einem Winkel gegen die
Einheit“. In ihr sind jetzt alle symmetrieerlaubten Terme bis Grad 4 gezählt; mehr als die Zahl der freien Koeffizienten gibt diese Zerlegung nicht
her. Eine Zahl kann nur aus einer zusätzlichen Eingabe kommen (Dynamik der Feldgleichung, Lauf der Kopplungen oder eine Beziehung zwischen C und
einer bekannten Größe).

## Grenzen
Ein Feld je Sektor, Grad ≤ 4, N = 1; das Quarkfeld hat seinen farblosen Anteil entlang 1 (reell), der Farbanteil ist reiner Ladungs-Eigenzustand.
Die U(1) der Ladung ist wie in H178 nicht gefordert. Winkel bei M_Z. δ nicht behandelt. Keine Übertragung in den Materie-Frame nötig (keine Aussage
„von Daten disfavorisiert“ außer θ_u ≠ θ_d, einer Verhältnisgröße je Sektor). Kein Vorzeichen gesetzt; das Vorzeichen von C folgt aus den Daten
(Up hat den größeren Winkel). Kein Guard berührt; OP3 und OP4 offen. Vergeben: H182, k385. Nächste frei: H183, k386 (vor Vergabe prüfen).
