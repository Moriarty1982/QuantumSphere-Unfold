# Vorab-Notiz H182: Erlaubt der Tausch J einen ladungsabhängigen Massenterm bei den Quarks und verbietet ihn bei den Leptonen?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026, Entscheidungskarte nach k384: Up gegen Down als „Ladungsanteil im Block“
weiterverfolgen (nicht als Farbblock der Sedenionen). Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3 (Konfigurationen je Sektor).
Vergeben: H182, k385 (geprüft: frei).

## Vorwissen geprüft
- k384 (`../sedenion_symmetrien_k384/`): Die Ladung Q₀ = ½ − (i/6)L_U − (i/3)R_U hat auf {1, U} die Werte 0, 1 und auf dem Farbblock ⅓ (dreifach),
  ⅔ (dreifach). ℂ ⊗ 𝕆 hat vier hermitesche Formen, die mit Farbe und Ladung vertauschen. Der komplex-linear fortgesetzte Tausch J erfüllt auf {1, U}
  J Q₀ J⁻¹ = 1 − Q₀ und erhält auf dem Farbblock die Ladung. **Teil a unten ist damit nicht blind.**
- H178 (`../farbe_h178/`): reelles Feld, Potential bis Grad 4 unter SU(3)_c, Konjugation, J: V = A q + B q² + κ p; 45° nur für farblose Felder fest.
- k378 (`../farbanteil_k378/`): Farbtriplett hat sin²α = 1; reines Farbfeld gibt sin²θ = −A/(2B) für beide Quarktypen; nötig wären A/B = −1,108 (d)
  und −1,249 (u). „Was Up und Down trennt, muss farbblind sein (Ladung, schwacher Isospin).“
- H179 (`../standardphysik_h179/`): Eichladungen als Faktoren ändern K nicht (generationsblind). Hier geht es nicht um Eichkopplungen, sondern um
  einen Term im Potential, der die zwei Ladungs-Eigenräume verschieden gewichtet.
- H180 (`../neutrino_k_h180/`): Daten stützen K_ν ≈ ⅔, also gleiche Konfiguration für neutrale und geladene Leptonen.
- H156, H149 (`../generationszahl_h138/`): K = ⅔ aus J als Symmetrie des Potentials.
- k85-Form der Ladung: aus H140/k323 übernommen.
- Nicht gefunden: eine Zählung der Invarianten auf ℂ ⊗ 𝕆 (komplexes Feld) unter Farbe, Konjugation und J.

## Suchrichtung (rückwärts)
Ziel: θ_d ≠ θ_u bei gleicher Farbe, zugleich K_ν = K_e = ⅔. Notwendig: ein Term, der die Ladungs-Eigenräume ⅓ und ⅔ im Farbblock verschieden gewichtet
(ungerade unter der komplexen Konjugation von ℂ, die Q₀ auf 1 − Q₀ abbildet), der mit J verträglich ist, und kein entsprechender Term im Farblosen.
Statt Terme anzusetzen, werden alle Invarianten gezählt.

## Setzungen dieser Notiz
- Feld Ψ ∈ ℂ ⊗ 𝕆 (16 reelle Komponenten). Symmetriegruppe des Potentials: SU(3)_c (Stabilisator von U = e₇), Oktonion-Konjugation und J: ψ ↦ Uψ̄,
  alle **komplex-linear** fortgesetzt. Die U(1) der Ladung wird wie in H178 **nicht** gefordert (der Term κp aus H178 bricht sie).
- Potential: reelles Polynom bis Grad 4 in Real- und Imaginärteilen.
- „Ladungsungerade“ heißt: ungerade unter der komplexen Konjugation von ℂ.
- Quarkfeld als Ladungs-Eigenzustand: Ψ_± = cos θ·1 + sin θ·n_±, n_± normiert im Eigenraum ⅓ bzw. ⅔ des Farbblocks. Leptonfeld: cos θ·1 + sin θ·U.
- Zuordnung: Eigenraum ⅓ = Down-Sektor, ⅔ = Up-Sektor (K ist für Teilchen und Antiteilchen gleich).

## Hypothesen und Kriterien
- **H182a (exakt; nicht blind, siehe Vorwissen):** Die ladungsungerade hermitesche Form ist auf dem Farbblock J-invariant und auf {1, U} J-ungerade.
  Kriterium: J†HJ = +H (Farbe) und −H (farblos), Fehler < 10⁻¹²: **bestätigt**; sonst **widerlegt**.
- **H182b (Ausgang offen):** Unter den Invarianten vom Grad 2 gibt es mindestens eine ladungsungerade mit Träger im Farbblock und keine im Farblosen.
  Kriterium: Zählung per Nullraum. Keine im Farbblock: **widerlegt** (die Ladungs-Lesart kann Up und Down nicht durch einen J-verträglichen Term
  trennen). Eine im Farblosen: **widerlegt** (J schützt K_ν = K_e nicht). Sonst **bestätigt**.
- **H182c (Ausgang offen):** Mit dem allgemeinsten invarianten Potential bis Grad 4 (i) ist θ = 45° für das Leptonfeld stationär, unabhängig von allen
  Koeffizienten, und (ii) hängen die stationären Winkel von Ψ₊ und Ψ₋ von verschiedenen Koeffizientenkombinationen ab. Kriterium: (i) Ableitung nach θ
  bei 45° für jede Invariante < 10⁻⁹; (ii) der Raum der Funktionen V₊(θ) − V₋(θ) hat Dimension ≥ 1. Beides: **bestätigt**; (i) verletzt: **widerlegt**
  (K = ⅔ ginge verloren); (ii) verletzt: **widerlegt** (θ_u = θ_d erzwungen, gegen die Daten 48,11° und 52,21°).
- **H182d (Zählung; Ausgang offen):** Zahl der unabhängigen Koeffizientenverhältnisse, die θ_d und θ_u bestimmen. Kleiner als 2: es gibt eine
  Vorhersage, sie wird gegen θ_d = 48,114° ± 0,039° und θ_u = 52,207° ± 0,021° (M_Z) geprüft (innerhalb 3σ **bestätigt**, sonst **widerlegt**).
  Gleich 2 oder größer: **verträglich, keine Bestätigung** (Anpassung), sofern stabile Minima existieren; ohne stabile Minima **widerlegt**.
- **Bericht (kein Kriterium):** die antilineare Fortsetzung von J; welche Koeffizienten die Daten verlangen; Wirkung der Oktonion-Konjugation auf die Ladung.

## Werkzeugwahl
Python (numpy, scipy): explizite Oktonionen, Invarianten per Nullraum (Grad 2 über die Lie-Algebra, Grad 4 über Zufallspunkte und Gruppenelemente).
Wolfram Language als unabhängige exakte Kontrolle von Teil a und der Einschränkung der Invarianten auf die Feldfamilien. Qiskit nicht geeignet (keine
Schaltung, kein Messablauf). Ausgaben werden neben den Skripten abgelegt.

## Grenzen (vorab)
Ein Feld je Sektor, Grad ≤ 4; δ nicht behandelt; Winkel bei M_Z. Kein Vorzeichen wird gesetzt. OP3 und OP4 bleiben offen.
