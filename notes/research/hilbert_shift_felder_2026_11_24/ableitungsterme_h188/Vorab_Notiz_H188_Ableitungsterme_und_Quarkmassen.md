# Vorab-Notiz H188: Geben die Ableitungsterme der Feldgleichung den Farbschwingungen die Quarkmassen?

**Stand:** 27.11.2026, vor der Rechnung. Anlass: Autor, 27.11.2026, Entscheidungskarte nach H187: „Ableitungsterme einbeziehen“. Einordnung:
`wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H188, k391 (geprüft: frei).

## Vorwissen geprüft
- k290 (`../feldgleichung/README.md`): Bausteine der Feldgleichung. Kinetischer Term ½⟨D_μψ, D^μψ⟩; K₁ (Fläche), K₂ (Kommutator), K₃ (Assoziator),
  K₄ (Normdefekt), alle aus X_μ = D_μψ, vierter oder höherer Ordnung in X und antisymmetrisch in den Richtungen μ, ν.
- k291: K₁ auf S³ ist der Skyrme-Term; Ruhemasse erst bei ausgedehnten Lösungen (Igel), nicht bei kleinen Schwingungen.
- H184 bis H187 (`../schwingungen_h184/` bis `../adjunkte_h187/`): Frequenzquadrate der Farbschwingungen aus dem Potential allein; Funktionsmenge R
  (neun Funktionen der Vakuum-Eigenwerte je Paar); weder eine noch zwei Funktionen je Sektor geben die Quarkmassen. Dort wurde der kinetische Term
  stillschweigend als Einheitsform genommen.
- k253: Regel erster Ordnung ψ̇ = uωψ (rotierende Lösung); hier nicht gerechnet (siehe Grenzen).
- Nicht gefunden: eine feldabhängige kinetische Form auf H₃(𝕆) und ihre Wirkung auf die Frequenzen.

## Suchrichtung (rückwärts)
Ziel: Masse² (oder die gewählte Lesart X) je Generation und Ladung. Für kleine Schwingungen δW um ein ruhendes Vakuum ist die Bewegungsgleichung
Z·δẄ = −H·δW mit der kinetischen Form Z und der zweiten Variation H des Potentials; X = h/z je Eigenrichtung. Notwendig für eine Wirkung der
Ableitungsterme: Sie müssen in zweiter Ordnung in δW beitragen. Das wird zuerst geprüft (H188a), dann die einzige verbleibende Möglichkeit (H188b, c).

## Setzungen dieser Notiz
- Feld, Vakuum (reelle Zirkulante, K = ⅔, δ = 2/9, Eingabe, **ruhend und homogen**), Farbe, P, Farbphase wie H185 bis H187.
- Kinetische Form: invariant unter denselben Symmetrien, in ∂W̄ und ∂W je einmal, Koeffizienten aus dem Vakuum bis Grad 2. Sie hat auf den
  Farbrichtungen dieselbe Bauart wie die zweite Variation eines Potentials, also dieselbe Funktionsmenge R wie in H187:
  l_k, l_k², l_i l_j, l_i l_j − ½ l_k², 1, l_i + l_j, l_i² + l_j², ½(l_i² + l_j²) + l_i l_j, l_k(l_i + l_j).
- Je Sektor eigene Koeffizienten (wie H187). Zuordnungen A, B und Lesarten X = √m, m, m² wie H187. Daten bei M_Z aus k376.

## Hypothesen und Kriterien
- **H188a (nicht blind):** K₁ bis K₄ tragen zu kleinen Schwingungen um ein ruhendes homogenes Vakuum nichts bei (sie sind mindestens von vierter
  Ordnung in δW). Kriterium: zweite Variation von K₁ und K₂ (auf H₃ mit dem Jordan-Produkt bzw. eintragsweise) am Vakuum exakt null:
  **bestätigt**; sonst **widerlegt**.
- **H188b (Ausgang offen):** Ein Quotient genügt: Je Sektor gibt es f, z ∈ R mit X ∝ f/z, sodass beide Verhältnisse X₁/X₃, X₂/X₃ innerhalb von 3σ
  liegen, für beide Sektoren bei derselben Lesart und Zuordnung. Zufallskontrolle wie H187 (2000 erfundene Datensätze). Kriterium: Treffer und
  Zufallsquote < 5 %: **bestätigt** (als Kandidat für einen eigenen Vorab-Test); Treffer bei Quote ≥ 5 %: **ohne Urteil**; kein Treffer: **widerlegt**.
- **H188c (Ausgang offen):** Zwei Potentialfunktionen über einer kinetischen: X ∝ (a·f + b·g)/z mit f, g, z ∈ R (eine Vorhersage je Sektor),
  det[X·z, f, g] = 0 innerhalb von 3σ für beide Sektoren. Kriterium wie H188b.
- **Bericht:** bester Abstand je Sektor, Zahl der verglichenen Kombinationen, Zufallsquoten.

## Werkzeugwahl
Python (numpy, sympy): H188a symbolisch (Ordnung in δW) und numerisch an einem Beispiel; H188b, c als Suche über die Funktionsmenge mit linearer
Fehlerfortpflanzung. Wolfram Language für H188a exakt (Reihenentwicklung in der Störung). Qiskit nicht geeignet. Ausgaben neben den Skripten.

## Grenzen (vorab)
Nur ruhendes, homogenes Vakuum. Die rotierende Lösung (ψ̇ = uωψ, k253), bei der K₁ bis K₄ in zweiter Ordnung beitragen können, ist **nicht**
gerechnet und wird als eigene offene Möglichkeit geführt. Kinetische Formen höheren Grades und Mischungen mehrerer kinetischer Funktionen geben
keine Vorhersage mehr und werden nicht verglichen. Massen bei M_Z ohne Laufen. Kein Vorzeichen gesetzt. OP3, OP4 bleiben offen.
