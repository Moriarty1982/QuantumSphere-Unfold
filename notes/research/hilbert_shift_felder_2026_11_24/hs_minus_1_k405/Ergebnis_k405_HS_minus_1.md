# k405: Wie sähe ein HS(−1) aus? (Erkundung, nicht blind, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test, keine Runde. Die Mathematik ist Standard; neu ist nur die Zuordnung zum Turm, und die ist
eine Lesart. Abschnitt 4 ist nachträglich. **Anlass:** Frage des Autors vom 27.11.2026 („wie würde ein HS(−1) aussehen?“) und Auftrag, die drei
genannten Lesarten zu erkunden: (1) nur das Vorzeichen ℤ₂, (2) Körper mit einem Element, (3) leerer oder punktförmiger Rand des Turms als
Ur-Seed. Vergeben: **k405** (k405, k405b).

**Ergebnis in einem Satz:** Die Regel des Turms selbst hat keine Stufe unter ℝ; die drei Lesarten sind aber keine drei Alternativen. Das
Vorzeichen und der Randpunkt fallen zusammen (der Nullpunkt, auf dem das Vorzeichen unsichtbar wirkt, hat als einziges Objekt die „Größe“ ½),
die linearisierte Fassung ist eine Spiegelstufe gleicher Größe wie ℂ mit einer Einheit j² = +1, und der Körper mit einem Element liegt nicht
unter dem Turm, sondern quer dazu. Eine neue Zahl entsteht nicht; β_sym wird nicht hergeleitet.

**Werkzeuge:** Python (numpy) für die Strukturrechnung an den Cayley–Dickson-Algebren bis Dimension 32, die Clifford-Proben und die Zählregel
(`k405_hs_minus_1.py`, Ausgabe `k405_out.txt`); Wolfram Language als unabhängige exakte Kontrolle der Schleife, von Cl(1,1), der Zählregel und
der q-Zahlen (`k405b_gegenprobe.wl`, Ausgabe `k405b_out.txt`; alle symbolischen Reste 0, keine Warnungen). Qiskit nicht eingesetzt: Es gibt keine
neue Schaltung; die Schleife L3 liegt als Schaltung aus k395 vor und wird hier nur umgeschrieben. Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein
endlicher Auswahlablauf).

## Vorwissen geprüft

- k253 (`../README.md`): Regel ψ̇ = uωψ in A_n; in der Tabelle steht für HS(0) bereits „Wahl von u: keine (nur ±, S⁰ der Werte)“. Das
  Vorzeichen ist dort also schon als Teil von HS(0) geführt.
- k254 (`../hs4/README.md`): Zahl verträglicher Kreisachsen 0, 1, 3, 7, 8, 9, 11, 15 (Radon–Hurwitz), im Turm Periode 4 (Bott).
- r67 (Zählregel als Postulat), H47, k396 (Gewichte p_k, glatter Vergleichsfall j + ½, p₁ = 2^(1−γ_L) ≈ β_sym nachträglich und ungeklärt).
- r69.4 und r70 (Frames als Port-Gewichte R 1:0, M 1:x, T x:1, P 1:1; HC des Dubletts = ½(1 + σ_x)).
- k395 (Schleife L3: b′ = 1 − 2b(1 − b), Fixpunkt ½, vergisst den Ur-Seed).
- Suche nach „HS(−1)“, „Körper mit einem Element“, spaltkomplexen Zahlen in `notes/`, `wiki/`, `sources/`: kein Vorbefund.

## 1 Die Regel des Turms hat keinen Schritt unter ℝ (exakt)

Der Schritt nach unten ist in jeder Stufe derselbe: A_n trägt die Spiegelung s(a, b) = (a, −b), sie ist ein Automorphismus (geprüft für
n = 1 bis 5, Fehler 0), und A_{n−1} ist ihr festgehaltener Teil (Dimension 2^(n−1)). Die Aussage „ℝ ist, was die Konjugation in ℂ festlässt“
ist der Fall n = 1 davon; für n ≥ 2 lässt die Konjugation nur ℝ fest, der richtige Schritt ist s. Auf ℝ gibt es nur die Identität als
Automorphismus. Der ungerade Teil ist {0}, der Schritt läuft ins Leere.

Zwei weitere Folgen derselben Art:

| Stufe n | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| Dimension 2ⁿ | ½ | 1 | 2 | 4 | 8 |
| Einheiten \|x\| = 1 | keine Sphäre S^(−½) | S⁰ = {±1} | S¹ | S³ | S⁷ |
| Wahl von u (imaginäre Einheiten) | keine | S^(−1) = leer | S⁰ | S² | S⁶ |
| Zahl imaginärer Einheiten 2ⁿ − 1 | −½ | 0 | 1 | 3 | 7 |
| verträgliche Kreisachsen (k254, Periode 4 rückwärts fortgesetzt) | 7 − 8 = −1 | 0 | 1 | 3 | 7 |

Zwei Dinge folgen. Erstens liegt das Vorzeichen ℤ₂ = S⁰ nicht unter HS(0), es **ist** die Einheitssphäre von HS(0). Zweitens ist schon bei
HS(0) der Raum der Wahlen leer; die leere Menge ist also nicht HS(−1), sondern steht bereits in der Zeile von HS(0). Die Nullalgebra
(Dimension 0) läge bei n = −∞.

## 2 Lesart 1: das Vorzeichen

### 2a Als Algebra: eine Spiegelstufe, nicht eine kleinere (exakt)

Macht man aus ℤ₂ eine Algebra, erhält man ℝ[ℤ₂] = ℝ ⊕ ℝ·j mit j² = +1 (spaltkomplexe Zahlen). Sie ist im genauen Sinn das Gegenstück zu
ℂ: Eine Einheit e mit e² = −1 und eine antikommutierende Einheit j mit j² = +1 erzeugen zusammen alle reellen 2×2-Matrizen (Rang 4 von 4,
Python und Wolfram), und M₂(ℝ) zählt in der Clifford-Uhr wie ℝ. In dieser Zählung hat ℂ den Index +1 und ℝ[ℤ₂] den Index −1. Dazu passt die
letzte Zeile der Tabelle (−1 Achse). In der Bott-Uhr ist Stufe −1 dieselbe wie Stufe 7: Die sieben Linksmultiplikationen der Oktonionen
antikommutieren, quadrieren zu −1 und erzeugen nur M₈(ℝ) (Rang 64 von 128 Worten); ihr Produkt ist −1, das der Rechtsmultiplikationen +1.
Stufe 7 besteht also aus zwei gleichen Hälften, die nur ein Vorzeichen unterscheidet: wieder ℝ ⊕ ℝ.

Diese Stufe hat aber Dimension 2, nicht ½. Sie liegt neben ℂ, nicht unter ℝ. Was sie von ℂ unterscheidet:

- Die Bahnregel ψ̇ = uωψ mit u = j gibt e^(jt) = cosh t + j sinh t: keine Kreisbahn, sondern eine Hyperbel (Schub statt Drehung), erhaltene
  Größe x² − y².
- Es gibt Nullteiler e± = ½(1 ± j) mit e₊e₋ = 0. In der Darstellung j = σ_x ist **e₊ genau der HC-Projektor ½(1 + σ_x) aus r70**. Die Algebra,
  die der HC erzeugt, ist also diese Spiegelstufe; ihre zwei Idempotente sind die zwei Ports.
- Ein Element p·e₊ + q·e₋ hat die Norm p·q. Mit den Port-Gewichten aus r69.4: R (1, 0) ist ein Idempotent (Norm 0), P (1, 1) ist reell,
  M (1, x) und T (x, 1) gehen durch die Konjugation j ↦ −j ineinander über und haben die Rapidität ±½ ln(1/x) = ±ln(1/β_sym) = ±0,598918.

**Grenze dieser Lesart:** Die Rapidität 0,5989 ist nicht der Schub des Modells, ε = artanh β_sym = 0,6175 (Verhältnis 0,970). Dass der HC ein
Idempotent dieser Algebra ist, gilt für jeden Projektor ½(1 + σ); es zeichnet nichts aus. Der Tausch M ↔ T als Konjugation ist dieselbe
Aussage wie r70.2, nur anders geschrieben.

### 2b Mit Dimension ½: der Nullpunkt mit unsichtbarem Vorzeichen (Lesart)

Die einzige saubere Zählung, die ½ = 2^(−1) liefert, ist die Zählung „Menge geteilt durch Symmetrie“ (ein Punkt zählt 1/Größe seines
Stabilisators). Die zwei Vorzeichen {+1, −1} geteilt durch den Vorzeichentausch geben 1; der Nullpunkt {0}, den der Tausch festhält, gibt ½;
die Zahlen −2 … 2 geben 5/2 (`k405_out.txt`). **Größe ½ hat also nicht das Vorzeichen, sondern der Punkt, auf dem das Vorzeichen wirkt, ohne
etwas zu ändern.** Damit fallen Lesart 1 und Lesart 3 zusammen: HS(−1) wäre der Randpunkt (Lesart 3) mit einem unsichtbaren Vorzeichen
(Lesart 1). ℝ zerfällt in Vorzeichen mal Betrag; unter ℝ bleibt der Betrag ohne Vorzeichen, die Halbgerade r ≥ 0. Das passt zur Atlas-Lesart
von HS(0) als „radialer Kern“, ist aber nur eine Zählung, keine Algebra: Auf der Halbgeraden kann man nicht subtrahieren.

Ein Vorzeichen, das wirkt, ohne sichtbar zu sein, ist die Eigenschaft eines Spinors (ψ und −ψ sind derselbe Zustand). Insofern passt „ein Bit
bei j = ½“. Das ist Wortgleichheit, kein Befund.

## 3 Lesart 2: der Körper mit einem Element

Benutzt sind die üblichen Faustregeln (Tits, Connes–Consani); ein allgemein anerkanntes Objekt F₁ gibt es nicht.

- Der Turm hat die Basis 2: Die Einheiten von A_n sind mit den Punkten von 𝔽₂ⁿ beschriftet, e_a e_b = ± e_(a xor b) (geprüft bis n = 5), und die
  2ⁿ − 1 imaginären Einheiten sind die Punkte des projektiven Raums über 𝔽₂ (n = 3: die sieben Punkte der Fano-Ebene). Ersetzt man 2 durch q, hat
  Stufe n die Dimension qⁿ und (qⁿ − 1)/(q − 1) Einheiten. **Bei q = 1 hat jede Stufe die Dimension 1:** Der Turm fällt auf HS(0) zusammen
  (Wolfram: Grenzwerte −2, −1, 0, 1, 2, 3, 4 Einheiten für n = −2 … 4; |GL_n(𝔽_q)|/(q − 1)ⁿ → n!).
- F₁ liegt also nicht eine Stufe unter ℝ. Es ist eine andere Richtung: nicht die Stufe n wird kleiner, sondern die Basis. Für n = −1 gibt die
  Formel bei q = 2 genau −½ imaginäre Einheiten, also Dimension 1 − ½ = ½, im Einklang mit Abschnitt 2b; mehr sagt sie nicht.
- Die Lesart „ℝ ohne Betrag“ gibt es in dieser Welt genau: ℝ geteilt durch die positiven Zahlen ist der Vorzeichen-Hyperkörper {0, +1, −1}
  mit (+1) + (−1) = {−1, 0, +1} (durch Stichproben nachgestellt); sein multiplikativer Teil ist die „quadratische Erweiterung“ von F₁. Teilt man
  noch das Vorzeichen heraus, bleibt {0, 1}: nur noch „null oder nicht“. Kette: ℝ → nur Vorzeichen (3 Elemente) → null oder nicht (2 Elemente).

Befund: Lesart 2 enthält Lesart 1 als Zwischenglied und liefert für das Modell keine Größe.

## 4 Lesart 3: der Rand als Ur-Seed (Abschnitt nachträglich)

**Exakt:** Die selbstjustierende Schleife L3 aus k395, b′ = 1 − 2b(1 − b), ist in der Variablen c = 2b − 1 die Quadrierabbildung **c ↦ c²**
(Wolfram: Rest 0; n Runden geben c^(2ⁿ)). Daraus folgt alles, was k395 an ihr fand: c = 0 (b = ½) zieht quadratisch an, c = 1 (b = 1) stößt ab
(Steigung 2), und der erste Schritt löscht das Vorzeichen von c: +c und −c sind danach gleich. „Die Schleife vergisst den Ur-Seed“ heißt genau:
erst ein Bit (das Vorzeichen), dann den Betrag.

**Lesart:** Eine Runde der Schleife ist derselbe Vorgang wie der Schritt von ℝ zur Halbgeraden in Abschnitt 2b (Vorzeichen vergessen). Rückwärts
(Wurzelziehen) verdoppelt jeder Schritt die Zahl der Vorgänger: 1, 2, 4, 8, 16, 32 nach 0 bis 5 Schritten, so viele wie die Dimension von HS(0)
bis HS(5). Aufwärts braucht jeder Schritt ein Bit Wahl, abwärts geht eines verloren. Der Rand unten ist deshalb das Ende der Schleife (ihr
Attraktor), nicht ihr Anfang; ein Ur-Seed lässt sich von dort nicht ablesen. Das deckt sich mit k253: Auf jeder Stufe bleibt eine Wahl gesetzt.

**Grenzen:** Die Verdopplung der Vorgänger gilt für jede Abbildung vom Grad 2 und ist für sich kein Hinweis auf den Turm. Reell bleiben immer
nur zwei Vorgänger; die volle Verdopplung braucht komplexe c, während b in k395 ein reeller Erwartungswert ist. Die Schleife landet weiter bei
b = ½ und nicht bei 1/γ_L.

## 5 Negative Stufen in der Zählregel (nachträglich, Lesart)

Das Gewicht eines Durchstoßpunkts mit Spin j = k/2 ist p_k = 2^(1 − γ a_k); die Zählregel verlangt Σ p_k = 1.

| k | j | glatt (a = j + ½, γ = 2): p_k | log₂ p_k | Casimir (γ_L): p_k | log₂ p_k |
|---|---|---|---|---|---|
| 1 | ½ | 0,5 | −1 | 0,549161 | −0,8647 |
| 2 | 1 | 0,25 | −2 | 0,242315 | −2,0450 |
| 3 | 3/2 | 0,125 | −3 | 0,111137 | −3,1696 |
| 4 | 2 | 0,0625 | −4 | 0,051683 | −4,2742 |

Im glatten Vergleichsfall ist p_k = 2^(−k) exakt die formale Dimension von HS(−k), und die Zählregel lautet: Die Dimensionen aller negativen
Stufen summieren sich zur Dimension von HS(0), ½ + ¼ + ⅛ + … = 1. Ein Spin-½-Durchstoßpunkt hätte dann genau die Größe von HS(−1): zwei
Zustände (das Vorzeichen-Bit) gegen zwei Bit Flächenkosten. Mit der Casimir-Fläche des Postulats liegen die „Stufen“ nicht bei ganzen Zahlen
(−0,865; −2,045; −3,170; …).

**Einordnung:** Das ist die geometrische Reihe, anders gelesen. Die Zuordnung „Spin k/2 ↔ Stufe −k“ ist gesetzt, nicht hergeleitet, und sie
passt nur im glatten Fall, also gerade nicht für die Zahl des Modells (β = 1/√3 statt β_sym). Die Nähe p₁ = 0,54916 zu β_sym = 0,54941 (0,045 %)
steht schon in k396 und bleibt ungeklärt.

## Was hergeleitet ist und was Lesart

| Aussage | Status |
|---|---|
| Kein Schritt unter ℝ in der Cayley–Dickson-Regel; ℤ₂ ist die Einheitssphäre von HS(0); Wahlraum bei HS(0) leer | exakt (Standard) |
| ℝ[ℤ₂] ist das Clifford-Gegenstück zu ℂ (Index −1, Bott-Stufe 7); HC-Projektor ist ihr Idempotent | exakt (Standard) |
| Größe ½ hat der Nullpunkt mit unsichtbarem Vorzeichen | exakte Zählung; als „HS(−1)“ Lesart |
| L3 ist c ↦ c² | exakt, neu gegenüber k395 |
| Schleife = Abstieg im Turm, Turm = Wurzelziehen | Lesart, nachträglich |
| Negative Stufen = Spins der Zählregel | Lesart, nachträglich, passt nur im glatten Fall |
| Zahl für β_sym, γ_L, Winkel oder Massen | keine |

## Grenzen

- Nicht blind, kein Entscheidungskriterium. Nichts hier ist ein Test.
- „Dimension ½“ ist in keiner der drei Lesarten die Dimension eines Zahlbereichs. Sie erscheint nur als Zählgröße (Punkt geteilt durch
  Symmetrie, q-Zahl, Gewicht in der Zählregel).
- Die Spiegelstufe ℝ[ℤ₂] trifft den Schub des Modells nicht (0,5989 gegen 0,6175).
- OP1 (Herkunft von β_sym, Grund für die Casimir-Fläche) bleibt offen; kein Guard berührt.

## Möglicher nächster Schritt

Ein Test mit Vorab-Notiz wäre nur an einer Stelle sinnvoll: ob eine Schleife, die statt c ↦ c² die Hyperbel-Regel der Spiegelstufe benutzt
(Schub statt Drehung), einen Fixpunkt abseits von ½ hat und wo er liegt. Dafür wäre eine H-Nummer nötig.
