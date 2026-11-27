# Vorab-Notiz H195: Die H188-Form aus der Feldgleichung herleiten

**Datum:** 27.11.2026. **Nummern:** H195 (Test), k403 (Rechnung). **Strang:** Quarkmassen nach H194. **Anlass:** „ja" des Autors
(27.11., 09:40) zum Vorschlag, die Herleitung der H188-Form aus der Feldgleichung anzugehen (warum gerade
(a·l_k + b·l_k²)/(l_i+l_j)², und warum Up quadratisch, Down linear).

## Ausgangspunkt (aus H184/H188, bereits belegt)
- Jede Farbmode der Quarks gehört zu einem Paar (i,j) von Eigenrichtungen des Leptonvakuums W₀ ∈ H₃(𝕆) (Eigenwerte l_i, l_j;
  dritter l_k). Vakuum: Tr W₀ = 3 (gesetzt) und K = ⅔ ⇒ e₂ = Σ l_i l_j = 3/2 (hergeleitet); δ = 2/9 setzt e₃. l = [0,040350,
  0,580212, 2,379438].
- **Peirce-Eigenwert (verifiziert, exakt).** Ein Off-Diagonal-Oktonion X in Position (i,j) erfüllt W₀∘X = ½(l_i+l_j)·X (konstant
  über alle acht Komponenten). Prüfskript bestätigt das für alle drei Paare auf 6 Stellen.
- **Masse = Potentialkrümmung / kinetische Normierung** (die Lesart aus H188c).

## Die Herleitung (analytisch, nicht blind)
**Nenner (l_i+l_j)² aus einer W²-gewichteten kinetischen Normierung.** Mit W₀∘X = ½(l_i+l_j)X gilt für die Mode (i,j):
- flache Norm N₀ = Tr(X∘X) = const;
- W-gewichtet N₁ = Tr(X∘(W₀∘X)) = ½(l_i+l_j)·N₀;
- **W²-gewichtet N₂ = Tr((W₀∘X)∘(W₀∘X)) = ¼(l_i+l_j)²·N₀.**

Eine kinetische Form ∝ Tr((W∘∂W)∘(W∘∂W)) gibt der Mode (i,j) also den Normierungsfaktor ¼(l_i+l_j)². Damit erscheint der **Nenner
(l_i+l_j)²** der H188-Form, ohne ihn von Hand einzusetzen (numerisch verifiziert: N₂/N₀ = ¼(l_i+l_j)²).

**Zähler = Potentialkrümmung.** Die zweite Variation jeder F₄/Jordan-Invariante für die Mode (i,j) steht in H184 (Wolfram exakt).
Auf dem **festen** Vakuum (Tr = 3, e₂ = 3/2) wird jede symmetrische Funktion von (l_i,l_j) eine Funktion von l_k allein
(l_i+l_j = 3−l_k, l_i²+l_j² = 6−l_k², l_i l_j = 3/2−3l_k+l_k²). Eingesetzt (symbolisch, sympy):

| Invariante | Krümmung der Mode (i,j), auf dem Vakuum |
|---|---|
| Tr W² | 4 |
| Tr W³ | 18 − 6 l_k |
| Tr W⁴ | 60 − 24 l_k |
| (Tr W²)² | 48 |
| Tr W·Tr W³ | 54 − 18 l_k |
| (Tr W)² Tr W² | 36 |
| Tr W²·Tr W_U² | 24 |

**Alle Krümmungen sind konstant oder linear in l_k; keine einzige liefert l_k².** Die Feldgleichung gibt also als Zähler eine
Kombination **A + B·l_k**, nicht Zähler mit l_k². Die hergeleitete Massenformel lautet damit

  **m ∝ (A + B·l_k) / (l_i+l_j)²**   (A, B Kombinationen der Potentialkoeffizienten, je Sektor).

Das ist **nicht** die nachträgliche H188-Form (a·l_k + b·l_k²)/(l_i+l_j)²: dort fehlt der konstante Term und es steht l_k² statt
der Konstante.

## Test
Der eigentliche Prüfpunkt ist, ob die **hergeleitete** Form (A + B l_k)/(l_i+l_j)² die sechs Quarkmassen trifft, und wie sie sich
zur H188-Form verhält.
- **H195a (nicht blind, Herleitung).** Nenner (l_i+l_j)² aus der W²-Norm (verifiziert) und Zähler-Reduktion auf A+B·l_k (sympy,
  Wolfram-Gegenprobe). Das ist Herleitung, kein Fit.
- **H195b (Test).** Fit der hergeleiteten Form m = (A + B l_k)/(l_i+l_j)² je Sektor (zwei Zahlen A, B), Zuordnung B, Lesart X = m.
  Kriterium:
  - **bestätigt (hergeleitet):** beide Sektoren alle drei Massen < 3σ **und** mindestens so gut wie die H188-Form — dann hat die
    Feldgleichung eine tragende Form geliefert.
  - **teilweise:** die hergeleitete Form trifft einen Sektor < 3σ, nicht beide; oder sie trifft schlechter als die H188-Form (dann
    ist der Nenner hergeleitet, der Zähler aber nicht der von der Feldgleichung bevorzugte).
  - **widerlegt:** die hergeleitete Form trifft keinen Sektor.
- **H195c (Test — Up/Down und das l_k²).** Prüfen, ob das von H188 benötigte l_k² aus der Feldgleichung auf einem anderen Weg
  entsteht: (i) eine andere kinetische Gewichtung (W statt W², oder N₁), (ii) ein ladungsabhängiger (U-)Term, der Up und Down
  trennt. Kriterium: entsteht ein Zähler mit l_k² aus einem benannten Feldgleichungs-Baustein (bestätigt), oder bleibt l_k² ein
  reiner Fit ohne Feldgleichungs-Herkunft (widerlegt für diesen Punkt)?
- **Kontrolle.** 2000 erfundene Massensätze durch denselben Fit der hergeleiteten Form, um die Trefferquote zu eichen.

## Erwartung (offen gelegt)
Ich erwarte **teilweise**: Der **Nenner** (l_i+l_j)² ist sauber hergeleitet (Peirce + W²-Norm, verifiziert). Der **Zähler** der
Feldgleichung ist A + B·l_k (konstant + linear), nicht das linear + quadratisch der H188-Form. Ob die hergeleitete Form besser,
gleich oder schlechter trifft als die nachträglich geratene, entscheidet die Rechnung. Das l_k² der H188-Form hat in den
Standard-Invarianten keine Quelle; es müsste aus einer besonderen kinetischen oder U-abhängigen Form kommen, sonst bleibt es ein
Fit. Ein echter Befund wäre, wenn die hergeleitete Form gleich gut oder besser trifft — dann wäre die Feldgleichung die Quelle.

## Werkzeuge
Python (numpy, sympy) für die Krümmungs-Reduktion, die kinetischen Normen und die Fits; Wolfram Language für die exakten
Krümmungen und Normen als Gegenprobe; die Peirce-Eigenwerte und Normen sind über die H₃(𝕆)-Algebra aus k387 verifiziert. Qiskit
nicht nötig. Coprozessor-Maschine nicht einschlägig.

## Vorwissen geprüft
- `.../schwingungen_h184/` (H184, Zusatz): Krümmungstabelle der Invarianten, Regel 2(v′(l_i)−v′(l_j))/(l_i−l_j), F₄-stationär ⇒
  Farbmoden masselos, Massen aus U-abhängigen Termen.
- `.../ableitungsterme_h188/` (H188, k391/k391c): Herkunft der Form, kinetische Normierung aus dem Vakuum, Warnung „nur mit Vorab".
- `.../h188_form_h194/` (H194): Form bindet spezifisch an die leptonischen l_k (teilweise); kein gemeinsames b/a.
- k253 (`.../rueckwaerts-felder-k270` u. a.): bewegtes Vakuum, kinetische Terme K₁–K₄ aus k290.
- Peirce-Zerlegung der Jordan-Algebra H₃(𝕆): Off-Diagonal (i,j) im Peirce-Raum zum Eigenwert ½(l_i+l_j) (Standard; hier verifiziert).

## Grenzen (vorab)
Die Wahl der kinetischen Form (W²-Gewichtung) und der Potential-Invarianten bleibt eine Setzung; H195 zeigt, welche Form die
Feldgleichung **natürlich** gibt, nicht dass die Koeffizienten festliegen. Keine vollständige Lösung der Feldgleichung, nur
zweite Variation um das ruhende Vakuum. OP3/OP4 bleiben offen.
