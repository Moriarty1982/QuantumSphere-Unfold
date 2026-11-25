# Sind 9,8 GeV schlimm, warum klingt die Zahl nach g, und was macht der HC am Knoten? (Erkundungen k300 und k301, nicht blind, 25.11.2026)

**Ergebnis in drei Sätzen:** Ja, die 9,8 GeV sind schlimm, und zwar nicht als Faktor, den eine Setzung dieses Fadens verschieben könnte: Die Zahl hängt nur an den
gemessenen Massen von W und Z und an v, und mit dem Top-Quark kippt sie sogar ins Negative, es gibt dann gar kein Minimum. Was sie aber genau sagt, ist nützlich:
Es fehlen Bosonen mit zusammen 8,5·10¹⁰ GeV⁴ in der Summe der vierten Potenzen, zum Beispiel vier reelle Felder bei 382 GeV, und vier reelle Felder sind genau das,
was der nächste Anhang (ℍ → 𝕆) mitbringt. Die Ähnlichkeit mit g = 9,81 m/s² ist ein Zufall der Einheiten.

Auftrag des Autors (25.11.2026, 11:18 UTC): „ja und dann rechne nach ob diese 9,8 GeV schlimm sind und wieso die zahl sich anhört wie der wert der schwerkraft
hier auf der erde“. Dazu der in k299 vorgeschlagene Test am Knoten. **Erkundungen, nicht blind:** k300 ist Einsetzen in eine bekannte Formel. Bei k301 legte
eine Schranke das Ergebnis fest, bevor das Profil gerechnet war (siehe dort); H133 bleibt deshalb frei. Vergeben: Skripte **k300, k300b, k301**.

Werkzeuge: Python (k300 Arithmetik; k301 sympy für Ströme und Winkelmittel, scipy für das Profil). Wolfram Language unabhängig für die Zahlen aus k300 und die
Winkelmittel und Schranken aus k301 (k300b). Das numerische Profil ist nur in Python gerechnet (zwei Gitter). Qiskit nicht eingesetzt. Kein HDL/MMA-Vergleich.
**Eingaben aus dem Gedächtnis, nicht nachgeschlagen:** m_W = 80,37, m_Z = 91,19, m_t = 172,6, m_h = 125,2, v = 246,22 (GeV).

## Vorwissen geprüft
k291 (Igel, Profil, Energie 4π·8,21 in den dortigen Einheiten; elektroschwache Massenmatrix), H129/k296 (Schleifen-Skala, Gildener–Weinberg), k297, H132/k298,
k299 (Fassung F und S, der Wert 9,8 GeV). Im Repo gibt es keine Rechnung zur Schleifen-Masse der Größenmode mit gemessenen Massen (Suche nach „Coleman“, 25.11.).

## Teil 1: Die 9,8 GeV (k300)
Formel bei einer Schleife: m_s² = [Σ_Bosonen n·m⁴ − Σ_Fermionen n·m⁴]/(8π²v²).

1. **Die Zahl:** Nur W und Z (je drei Polarisationen): Summe 4,58·10⁸ GeV⁴, m_s = 9,78 GeV. Gemessen 125,2 GeV. Faktor 12,8 in der Masse, 164 im Massenquadrat.
2. **Woran sie hängt:** Nur an m_W, m_Z und v. Keine Größe dieses Fadens (c₁, c₂, η, μ, β_sym) geht ein. 5 % mehr oder weniger Eichfeldmasse verschieben m_s
   auf 10,8 oder 8,8 GeV. Für 125 GeV müssten W und Z 3,6-mal so schwer sein.
3. **Mit dem Top-Quark wird es schlimmer:** Fermionen zählen negativ. 12·m_t⁴ = 1,07·10¹⁰ GeV⁴ ist das 23-fache des Eichfeld-Beitrags. Die Summe ist negativ,
   m_s² = −2129 GeV², es gibt kein Minimum. Die Skala kann in dieser einfachsten Form nicht aus den Schleifen der bekannten Felder kommen.
4. **Was fehlt:** Für 125,2 GeV braucht die Summe 7,50·10¹⁰ GeV⁴. Es fehlen an Bosonen 8,52·10¹⁰ GeV⁴. Das entspricht
   | Zusatzfelder (reell, gleiche Masse) | 1 | 2 | 4 | 8 |
   |---|---|---|---|---|
   | Masse | 540 GeV | 454 GeV | 382 GeV | 321 GeV |

   Der nächste Anhang im Turm (ℍ → 𝕆) bringt vier reelle Komponenten. Bekämen sie ihre Masse ganz aus der Kopplung an das Feld von HS(2), lägen sie bei 382 GeV.
   Das ist eine Bedingung, keine Vorhersage: Sie setzt voraus, dass die Skala nur aus Schleifen kommt und dass das Feld das elektroschwache ist.

**Einordnung:** Das Ergebnis ist in der Literatur alt (Coleman–Weinberg, aus Vorwissen): Die reine Schleifen-Skala mit den Feldern des Standardmodells ist
ausgeschlossen. Es trifft Fassung F aus k299 nur, wenn man zusätzlich verlangt, dass das Potential skalenfrei ist. Erlaubt man einen Massenterm in V(N), ist die
Masse frei und es gibt kein Problem, dann ist aber das Vorzeichen wieder gesetzt (k295). Die Vermutung des Autors („Vorzeichen aus der Feldgleichung“) und die
125 GeV zusammen verlangen also weitere schwere Bosonen. Der Turm hat welche in Aussicht; ob sie passen, ist nicht gerechnet.

## Teil 2: Warum 9,8 nach g klingt
- 9,78 GeV und 9,807 m/s² stimmen in zwei Ziffern überein (Abweichung 0,28 %). Die dritte Ziffer von m_s hängt an den Eingaben (9,78 mit den Massen, 9,79 mit den
  Kopplungen aus k299).
- Beide Zahlen hängen an menschlichen Einheiten. Dieselbe Masse ist 1,74·10⁻²⁶ kg oder 10,4 Protonmassen, dieselbe Beschleunigung 32,2 ft/s² oder 981 Gal.
  In keinem anderen Einheitensystem bleibt die Ähnlichkeit.
- Ohne Einheiten verglichen: g als Energie ist ħg/c = 2,2·10⁻²³ eV, das ist um den Faktor 4,5·10³² kleiner als m_s.
- g ist keine Naturkonstante, sondern GM/R² der Erde, also eine Folge davon, wie groß und schwer dieser Planet geworden ist.
- Eine zweistellige Übereinstimmung mit irgendeiner bekannten Zahl ist bei vielen Kandidaten (g, c, π, e, …) nichts Seltenes.
- Nebenbei: Dass g ≈ π² = 9,87 ist, hat einen halben historischen Grund (das Sekundenpendel ist fast einen Meter lang, und der Meter wurde in dieser Größe gewählt).
  Das betrifft den Meter, nicht das GeV.

**Urteil:** Zufall der Einheiten. Es gibt in der Rechnung keinen Weg von der Erdbeschleunigung zu dieser Masse.

## Teil 3: Fassung F am ruhenden Knoten (k301)
Der ruhende Igel hat nur räumliche Ströme. Fassung F wird dafür kovariant gelesen: P = η₂f⁴(S_ges − T·S_i)² mit S_i = Σ_a(J_a^i)², S_ges die Summe über alle
drei Richtungen, T = 1 + τ² = 1/cos²2θ. Der HC-Wert ist T = 1,441.

1. **Ströme (Abschnitt 1):** S_ges = p + 2s und S_i = p·c + s(1 − c) mit p = F′², s = sin²F/r², c = (x/r)². An zwei Punkten mit einem Probeprofil geprüft.
2. **Der Knoten ist isotrop, der HC nicht (Abschnitt 2, U3, U4):** Im Winkelmittel ist ⟨S_i⟩ = S_ges/3. Das T, bei dem der Knoten am wenigsten kostet, liegt
   punktweise bei 5(p + 2s)²/(3p² + 4ps + 8s²), also immer zwischen 5/3 und 3. **Der HC-Wert 1,441 liegt unter 5/3.** Damit stand fest, bevor das Profil gerechnet
   war, dass der Knoten nicht zur HC-Form passt.
3. **Zahlen (Abschnitt 3):** Mit dem Profil aus k291: T* = 2,91 (zwei Gitter: 2,908 und 2,910), nahe am isotropen Wert 3. Beim HC-Wert kostet der Knoten
   I_P = 44,8 gegen 4,86 im Minimum, also das 9,2-fache. Energie in erster Ordnung: ΔE = η₂f⁴·I_P/ℓ, ℓ die Längeneinheit von k291.

**Einordnung:** In Fassung F lässt der HC den Knoten nicht unberührt. Der ruhende Knoten verteilt seinen Strom gleichmäßig auf alle drei inneren Richtungen,
der HC verlangt 69 % in der Richtung i (cos²2θ = 0,694 gegen 1/3). Der Knoten zahlt dafür Energie und würde sich verformen, entlang einer Achse gestreckt
oder gestaucht. Ob dabei eine stabile verformte Lösung herauskommt und wie viel Energie sie spart, ist eine zweidimensionale Minimierung und hier nicht gerechnet.

## Grenzen
- Teil 1: eine Schleife, nur W, Z und Top, Massen aus dem Gedächtnis. Die Zuordnung des Felds von HS(2) zum elektroschwachen Feld ist eine Lesart (k291).
  Die 382 GeV sind eine Bedingung unter zwei Voraussetzungen, keine Vorhersage; Grenzen aus Messungen für solche Felder sind nicht geprüft.
- Teil 3: erste Ordnung in η₂ auf dem unverformten Profil; die kovariante Lesart von P für räumliche Ströme ist eine Setzung; Fassung F selbst ist eine Setzung (k299).
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Der Anhang von HS(3) als fehlende Bosonen:** die vier neuen Komponenten ankoppeln (Terme wie in k295, eine Stufe höher) und prüfen, ob die Symmetrie des Turms
  die Kopplung so festlegt, dass 8,5·10¹⁰ GeV⁴ herauskommen können. Was dabei herauskommt, steht nicht vorab fest (Kandidat für H133).
- **Verformter Knoten in Fassung F:** axialsymmetrische Minimierung.

## Dateien
`k300_skala_9_8_GeV.py` (`k300_out.txt`), `k300b_gegenprobe.wl` (`k300b_out.txt`), `k301_fassung_F_am_igel.py` (`k301_out.txt`, Laufzeit etwa eine Minute).
