# Vorab-Notiz H187: Geben Terme mit der Adjunkten und der Determinante der Albert-Algebra die sechs Quarkmassen?

**Stand:** 27.11.2026, vor der Rechnung. Anlass: Autor, 27.11.2026, „ja“ zum nächsten Schritt aus H186. Einordnung: `wiki/Gesamtbild.md`, T8/T13,
OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H187, k390 (geprüft: frei).

## Vorwissen geprüft
- H186 (`../ladungsterm_h186/`): Terme mit D = Q₀ − ½ aus Spurpotenzen geben nur symmetrische Funktionen der zwei Vakuum-Eigenwerte (l_i, l_j) des
  Paars: 1, l_i + l_j, l_i² + l_j², (l_i + l_j)². Kein Einzelterm trifft X(Up) − X(Down). Nachträglich dort: Der gemessene Unterschied liegt
  fast ganz auf l_i l_j; das reine Produkt trifft nicht (r₂ 1,41-fach). **Dieser Hinweis stammt aus denselben Daten.**
- H184 (`../schwingungen_h184/`): Regel für F₄-invariante Potentiale; Spurinvarianten mit l_k-Abhängigkeit ((Tr W²)², Tr W · Tr W³).
- H185 (`../updown_h185/`): ladungserhaltende und ladungsmischende Terme; Farbphase als Symmetrie nötig.
- k376 (`../quarks_k376/`): Massen bei M_Z mit Fehlern. H179: Georgi-Jarlskog nah, nach Kriterium widerlegt.
- Suche nach „Adjunkte“, „Freudenthal“, „W^#“ unter `notes/research/`: keine Vorbefunde.

## Suchrichtung (rückwärts)
Ziel: je Ladung drei Zahlen X_k (zwei Verhältnisse je Sektor, vier insgesamt, dazu Up/Down-Skala). Notwendig: Die Funktion der Vakuum-Eigenwerte, die
ein Term liefert, hat die Hierarchie des Sektors. Zuerst wird ohne Daten bestimmt, welche Funktionen die Terme liefern (Schritt 1); erst dann werden
diese Funktionen und nur diese gegen die Daten gehalten (Schritt 2).

## Setzungen dieser Notiz
- Feld, Vakuum (reelle Zirkulante, K = ⅔, δ = 2/9, Eingabe), Farbe, P, Farbphase wie H185/H186.
- Adjunkte W^# = W ∘ W − Tr(W)·W + ½(Tr(W)² − Tr(W ∘ W))·1; Kreuzprodukt A × B als ihre Polarisation (A × A = W^# für A = W).
- Kandidaten (Liste vorab fest), jeweils der ladungserhaltende Anteil der zweiten Variation auf den Farbrichtungen:
  gerade: a1 Re Tr(W^# ∘ W̄); a2 Tr(W^# ∘ W̄^#); a3 Tr((W × W̄) ∘ W_U); a4 Tr((W × W̄) ∘ (W_U ∘ W̄_U)); a5 Tr((W × W̄) ∘ W_U^#);
  a6 Tr((W × W̄) ∘ (W × W̄)); a7 Tr((W × W_U) ∘ (W̄ × W̄_U)); a8 Re Tr(W^# ∘ W̄_U^#);
  mit Ladungsoperator: d1 Re Tr((W̄ × DW) ∘ W_U); d2 Re Tr((W̄ × DW) ∘ (W_U ∘ W̄_U)); d3 Re Tr((W̄ × DW) ∘ W_U^#); d4 Re Tr((DW × W_U) ∘ (W̄ × W̄_U)).
- Funktionsmenge R für Schritt 2: alle verschiedenen Funktionen des Paars, die diese Kandidaten liefern, zusammen mit denen aus H184 und H186
  (1, l_i + l_j, l_i² + l_j², (l_i + l_j)², l_k², l_k(l_i + l_j)). Da (½ ± 3D) auf eine Ladung allein wirkt, darf jeder Sektor eigene Koeffizienten haben.
- Zuordnungen der Generationen: A (wie H186: nach l_i + l_j aufsteigend) und B (umgekehrt: Paar (e, μ) ↔ 3. Generation; natürlich für
  Funktionen von l_k). Lesarten X = √m, m, m². Daten bei M_Z aus k376.

## Hypothesen und Kriterien
- **H187a (Ausgang teils erwartet):** Mindestens ein Kandidat liefert das reine Produkt l_i l_j (ohne andere Anteile), und mindestens einer eine
  Funktion von l_k allein. Kriterium: beides gefunden (Rest der Anpassung < 10⁻⁹): **bestätigt**; sonst **widerlegt**.
- **H187b (Ausgang offen):** Eine Funktion je Sektor genügt: Für Up und für Down gibt es je eine Funktion f ∈ R (dieselbe Lesart und Zuordnung für
  beide Sektoren), deren zwei Verhältnisse X₁/X₃, X₂/X₃ innerhalb von 3σ der Daten liegen. Kriterium: erfüllt für beide Sektoren: **bestätigt**;
  sonst **widerlegt**.
- **H187c (Ausgang offen):** Zwei Funktionen je Sektor genügen (eine Vorhersage je Sektor): Es gibt f, g ∈ R mit det[X, f, g] = 0 innerhalb von 3σ,
  für beide Sektoren bei derselben Lesart und Zuordnung. Zufallskontrolle: dieselbe Suche auf 2000 erfundenen Datensätzen (Verhältnisse logarithmisch
  gleichverteilt im Bereich der echten, gleiche relative Fehler). Kriterium: Treffer in den echten Daten **und** Trefferquote der Kontrolle < 5 %:
  **bestätigt** (als Kandidat für einen eigenen Vorab-Test, nicht als Befund); Treffer bei Quote ≥ 5 %: **ohne Urteil** (mit Zufall verträglich);
  kein Treffer: **widerlegt**.
- **Bericht:** Liste der Funktionen je Kandidat; bester Abstand je Sektor; Zahl der verglichenen Kombinationen.

## Werkzeugwahl
Python (numpy, scipy): wie k389. Wolfram Language exakt für die Funktionen der Kandidaten im reduzierten Modell (Quaternion-Unteralgebra, Vakuum
diagonal). Qiskit nicht geeignet. Ausgaben neben den Skripten.

## Grenzen (vorab)
Kandidatenliste nicht vollständig; Zuordnung und Lesart sind Setzungen (sechs Kombinationen werden durchsucht, das wird in der Kontrolle
mitgezählt); Massen bei M_Z ohne Laufen; Stabilität des Vakuums und Vorzeichen der Frequenzquadrate nicht geprüft; ohne Ableitungsterme.
Kein Vorzeichen gesetzt. OP3, OP4 bleiben offen.
