# Vorab-Notiz H197: Erzwingt eine Symmetrie D = B (ist „Down linear" eine Auswahlregel oder ein Fit)?

**Datum:** 27.11.2026. **Nummern:** H197 (Test), k406 (Rechnung). **Strang:** Quarkmassen; offener Punkt aus H196.
**Anlass:** „mach das" des Autors (27.11., 10:25): suchen, ob eine Symmetrie D = B erzwingt.
(Diese Notiz wurde vor der Rechnung als k405 committet, Commit 7d39915; die Rechnung ist auf **k406** umnummeriert, weil ein
paralleler Thread „HS(−1)" k405 belegt hat. Inhalt unverändert.)

## Worum es geht
H196 fand mit dem Modell m_s(k) = [A·l_k + B·l_k² + s·(C·l_k + D·l_k²)]/(l_i+l_j)² (s = +1 Up, −1 Down) als besten Fit
**D ≈ B** (D = 3,32·10⁻², B = 3,29·10⁻²). Das bedeutet b_up = B+D stark, b_down = B−D ≈ 0: das quadratische l_k²-Glied ist für
Down abgeschaltet, für Up verdoppelt — genau „Up quadratisch, Down linear". H196 hat ausdrücklich offengelassen, ob D ≈ B **erzwungen**
oder **gefittet** ist. Das ist die Frage hier.

**D = B ⇔** der l_k²-Beitrag koppelt mit dem Up-Typ-Projektor P_up = (1+s)/2 (0 für Down, 1 für Up), denn
B·l_k² + s·D·l_k² = B(1+s)·l_k² wenn D = B.

## Teilaussage, die analytisch feststeht (darum: teils nicht blind)
Dass D und B aus **unabhängigen** Kopplungen stammen, folgt schon aus H186/H195 und ist damit kein blinder Test, sondern eine
Einordnung bestehender Rechnungen:
- **B (ladungsgerades l_k²)** braucht eine F4-invariante Potenz vom **Grad 5** (H195, k403c: l_k² erscheint erst bei n = 5).
- **D (ladungsungerades l_k²)** existiert schon bei **Grad 4**: die ladungsungeraden Krümmungen c4/c5, c7/c9, c11 (H186) tragen
  l_k² auf dem Vakuum (−l_k²/3, +l_k²/6, −l_k²/6).

Zwei Terme von verschiedenem Grad und verschiedener Invarianz haben **unabhängige** Koeffizienten. Dann ist D/B eine freie Zahl,
und keine Symmetrie bindet sie. Das will ich sauber nachrechnen und, falls es doch eine Bindung gibt, finden.

## Was dennoch ein echter Test ist
Wenn kein Symmetriezwang D = B liefert, ist die scharfe Gegenfrage: **welche** D/B-Werte erzeugen die symmetrie­ausgezeichneten
Kopplungen, und sind die von den Daten erlaubt? Die drei durch die Ladungsstruktur ausgezeichneten Fälle:
- **ladungsblind** (nur F4-invariant): D = 0 ⇒ b_up = b_down (kein Up/Down-Unterschied im l_k²).
- **lineare Ladung** (Term ∝ Ψ†Q₀Ψ, die einzige natürliche lineare Ladungsgewichtung neben Q₀−½): gerade ∝ ½(Q_up+Q_down) = ½,
  ungerade ∝ ½(Q_up−Q_down) = ⅙ ⇒ **D/B = ⅓** ⇒ b_up/b_down = (1+⅓)/(1−⅓) = **2**.
- **reine J-Form** (Term ∝ h = Ψ†(Q₀−½)Ψ, die von J ausgezeichnete ladungsungerade Form, H182): rein ungerade ⇒ B_dieser Term = 0,
  der l_k²-Anteil ist **antisymmetrisch** |b_up| = |b_down| ⇒ b_up/b_down = **−1** (bzw. D ohne eigenes B).

D = B (b_down = 0) entspricht **keinem** dieser Fälle, sondern dem Up-Typ-Projektor P_up = 3(Q₀−⅓). Prüfung, ob P_up von J
ausgezeichnet ist: unter J gilt Q₀ → 1−Q₀, also Q₀−½ → −(Q₀−½) (Eigenform, ladungsungerade, = h), aber Q₀−⅓ → ⅔−Q₀, **keine**
Eigenform; J bildet P_up auf P_down ab (vertauscht Up und Down). Genau diese Vertauschung gibt es im Farbblock **nicht** (der Kern
von H182). P_up ist also erlaubt, aber als **freie** Kopplung, von keiner Symmetrie erzwungen.

## Teile und Kriterien
- **H197a (nicht blind).** Reduktion der ladungsgeraden (F4, Grad 2–6) und ladungsungeraden (H186, Grad 4) Krümmungen auf Polynome
  in l_k; Nachweis, dass ein ladungsungerades l_k² bei Grad 4 existiert, wo das ladungsgerade l_k² (Grad 5) null ist. Damit sind die
  Quellen von B und D getrennt. Rang der (gerade, ungerade)×l_k²-Beiträge = 2 ⇒ D/B frei.
- **H197b (Test — Daten gegen die symmetrieausgezeichneten D/B).** Fit der sechs Massen mit **festem** D/B ∈ {0, ⅓, −1} (je ein
  freier Gesamtmaßstab plus A, C; also D an B bzw. das Vorzeichen gebunden) gegen den freien 4-Parameter-Fit (D/B frei).
  - **Befund „ja, Symmetrie erzwingt D = B":** einer der symmetrieausgezeichneten Fälle trifft die Daten (alle sechs < 3σ) **und**
    liefert D/B = 1, oder es findet sich eine Symmetrieoperation, unter der der ladungsgerade Grad-5- und der ladungsungerade
    Grad-4-Term dieselbe Kopplung tragen.
  - **Befund „nein, D = B ist ein Fit":** die symmetrieausgezeichneten D/B (0, ⅓, −1) sind von den Daten ausgeschlossen (≫ 3σ),
    nur der freie Fit mit D/B ≈ 1 trifft, und D/B = 1 = P_up ist nicht J-kovariant. Dann ist „Down linear" eine empirische
    Auswahlregel, die der Rahmen **nicht** erzeugt.
- **H197c (Bericht).** χ²(D/B) als Kurve: wie scharf verlangen die Daten D/B ≈ 1? 2σ-Fenster für D/B.
- **Kontrolle.** 2000 erfundene Massenpaare durch denselben festen-D/B-Fit, Trefferquote eichen.

## Erwartung (offen gelegt, teils nicht blind)
Ich erwarte **„nein"**: B (Grad 5, gerade) und D (Grad 4, ungerade) sind unabhängig, die symmetrienahen D/B ∈ {0, ⅓, −1} liegen
alle fern der Daten (die b_up/b_down ≈ 680 verlangen), und D = B = P_up ist nicht J-kovariant. Ein echter Gegenbefund wäre eine
Symmetrie, die den Grad-5-geraden und den Grad-4-ungeraden l_k²-Term koppelt — danach suche ich ausdrücklich (Zerfall der
ladungsabhängigen Krümmung unter der Ladungs-U(1) und unter J), nicht nur bestätigend.

## Werkzeuge
Python (numpy, sympy) für die Reduktionen, die Rang- und die festen-D/B-Fits, die Kontrolle; Wolfram Language für die J-Abbildung
der Ladungsformen (Q₀−½, Q₀−⅓, P_up) und die exakten l_k²-Koeffizienten als Gegenprobe. Qiskit nicht nötig (keine Schaltung).

## Vorwissen geprüft
- `.../ladung_h182/` (H182): h = Ψ†(Q₀−½)Ψ ist die **einzige** von J zugelassene ladungsungerade hermitesche Form im Farbblock;
  J: Q₀ → 1−Q₀; im Farbblock keine Up↔Down-Symmetrie.
- `.../ladungsterm_h186/` (H186, k389): ladungsungerade Krümmungen c1–c11; c4/c7/c11 tragen l_k² schon bei Grad 4.
- `.../feldgleichung_form_h195/` (H195, k403c): ladungsgerades l_k² erst ab Potentialgrad 5; Nenner (l_i+l_j)² hergeleitet.
- `.../ladung_zaehler_h196/` (H196, k404): D ≈ B gefittet (nicht erzwungen), D/C = −14,9 trifft keinen festen Kandidaten.
- `.../h188_form_h194/` (H194): b_up/b_down ≈ 680 (Up quadratisch, Down linear).
- Memory: Ladungsterme als Massenquelle H184–H190 widerlegt; Quark-Strang Nenner hergeleitet, Koeffizienten frei.

## Bilanz der Setzungen (Pflicht nach ≥ 2× „teilweise" zur selben Voraussetzung)
Vierte Runde in Folge zur selben offenen Voraussetzung (Quark-Koeffizienten A,B,C,D): H193 (getrennte Felder, widerlegt),
H194 (H188-Form, Spezifität bestätigt, Form nachträglich gewählt), H195 (Nenner hergeleitet, Zähler frei), H196 (Up/Down-Ort =
Ladungsvorzeichen, Koeffizienten frei). **Diese Runde ist bewusst eine Richtungsprüfung, kein weiterer Fit:** sie fragt, ob das Ziel
(D = B) eine gesetzte Eingabe ist. Prüfung des Ziels: D = B ist **kein** Messwert, sondern ein Fit-Ergebnis aus H196 — also eine
abgeleitete Beziehung, deren Herkunft (Symmetrie oder Zufall) hier geklärt wird. Stillschweigend gewählte Weggabelung, die dem
Autor nach dieser Runde vorzulegen ist, falls „nein": der Rahmen liefert die Up/Down-Asymmetrie der Stärke nicht; weiter lohnt dann
nur eine **neue Eingabe** (Dynamik/Lauf der Kopplungen, oder eine Beziehung P_up ↔ bekannte Projektgröße), nicht ein weiterer
Term im selben Baukasten.

## Grenzen (vorab)
Dieselbe Zerlegung wie H182/H186/H195/H196 (ein Feld, zweite Variation um das ruhende Vakuum, Krümmung/Norm). Die ladungsungeraden
Krümmungen sind aus H186 übernommen. Es wird keine neue Dynamik eingeführt. OP3/OP4 bleiben offen; kein Guard berührt.
