# Vorab-Notiz H193: Getrennte Felder je HS-Stufe statt gemeinsamer Geometrie

**Datum:** 27.11.2026. **Nummern:** H193 (Test), k401 (Rechnung). **Strang:** Quarkmassen nach H190, gewählte Richtung
„Lesart wechseln" (Quarks auf eigener HS-Stufe statt Farbschwingung). **Anlass:** „ja" des Autors (27.11., 09:03 UTC) zur
Weggabelung „getrennte Felder je HS-Stufe statt gemeinsamer Geometrie" — die zweite Gabel nach H192 (gemeinsame Sphäre, teilweise).

## Frage
H184 bis H190 lasen die Quarks als **Schwingungen eines gemeinsamen Objekts** (ein Vakuum, eine Albert-Algebra) und scheiterten
immer am selben Hebel: ein Mechanismus macht **ein** Verhältnis klein, die Quarks brauchen je Sektor **zwei** große Verhältnisse,
und Up ≠ Down ließ sich nicht trennen. H192 las sie als **Lagen auf einer gemeinsamen Sphäre** (teilweise: Oktant ja, kleine
Winkel angepasst). Die jetzige Lesart dreht das um: **jede HS-Stufe trägt ein eigenes Feld.** Die drei Generationen eines Sektors
sind dann keine Moden eines Oszillators mehr, sondern drei getrennte Felder auf drei Stufen des HS-Turms (HS(0) bis HS(4):
ℝ, ℂ, ℍ, 𝕆, 𝕊; Dimensionen 1, 2, 4, 8, 16).

**Kernfrage:** Kauft die Trennung selbst etwas, oder verschiebt sie nur die freien Parameter? Genau dann trägt sie, wenn die
**Stufe die Skala festlegt** — wenn das Massenverhältnis zweier Generationen aus einer stufeneigenen Größe (Dimension, Casimir,
Zählregel-Gewicht) folgt und nicht je Feld eingestellt wird.

## Modell
Quark-Masse m = (Einheit) · S(Stufe) · (Sektorfaktor). Die drei Generationen eines Sektors liegen auf drei aufsteigenden Stufen.
Zwei Lesarten:
- **(i) stufenfest, kein Fit:** S(Stufe) folgt einer festen Regel aus einer stufeneigenen Größe, null freie Zahlen je Feld
  (höchstens eine Gesamteinheit je Sektor).
- **(ii) frei, gefittet:** S(Stufe) ist je Stufe eine freie Zahl.

Stufeneigene Größen (alle schon im Projekt, keine neue Setzung):
- Dimension d_k = 2^k (ℂ=2, ℍ=4, 𝕆=8, 𝕊=16),
- Casimir-Fläche a_k = √(k(k+2)/3) (r67),
- Zählregel-Gewicht w_k = 2^(1−γ_L·a_k) (r67, γ_L = 1,8646998),
- Stufenindex k selbst.

Vorab festgelegte Kandidatenliste der Skalenregeln S (keine nachträgliche Erweiterung): S ∈ {d_k, d_k², 2^(d_k), exp(a_k),
a_k, w_k, k, k!} und ihre Kehrwerte; Zuordnung Generation → drei aufeinanderfolgende Stufen in beiden Reihenfolgen
(aufsteigend/absteigend), Startstufe ℂ, ℍ oder 𝕆.

## Daten (wie H187/H190, dieselben Quellen)
Up PDG (GeV): [2,16·10⁻³, 1,2730, 172,4], σ [0,04·10⁻³, 0,0028, 0,7].
Down PDG (GeV): [4,70·10⁻³, 93,5·10⁻³, 4,183], σ [0,09·10⁻³, 0,5·10⁻³, 0,007].
Zusätzlich die laufenden M_Z-Werte (Yukawa) up [7,04·10⁻⁶, 3,56·10⁻³, 0,967], down [1,54·10⁻⁵, 3,06·10⁻⁴, 1,630·10⁻²].
Dimensionslose Generationsverhältnisse (einheitsfrei, der eigentliche Prüfstein):
- Up PDG: c/u = 589, t/c = 135. Up M_Z: 506, 272.
- Down PDG: s/d = 19,9, b/s = 44,7. Down M_Z: 19,9, 53,3.

## Teile und Kriterien
- **H193a (nicht blind, Kontrolle).** Die stufeneigenen Verhältnisse direkt: Dimension gibt je Schritt Faktor 2; Casimir
  a_{k+1}/a_k und Gewicht liegen bei 1,2 bis 1,6. Die beobachteten Verhältnisse sind 20 bis 589. Dieser Größenabstand ist
  **analytisch vorhersehbar**, daher nicht blind geführt; er dient als Kontrolle, dass die einfachsten stufenfesten Regeln die
  Hierarchie um ein bis drei Größenordnungen verfehlen.
- **H193b (Test).** Über die vorab festgelegte Kandidatenliste (Regel × Zuordnung × Reihenfolge), Lesart (i): Gibt es **eine**
  stufenfeste Regel, die mit höchstens einer Gesamteinheit je Sektor und **ohne** Fit je Feld alle sechs Massen trifft?
  - **bestätigt:** ja, beide Sektoren alle drei Massen < 3σ, mit einer Regel, die zugleich eine Projektbedeutung hat.
  - **teilweise:** die Ordnung stimmt und ein Sektor < 3σ, der andere nicht; oder eine Regel trifft die Verhältnisse eines
    Sektors innerhalb Faktor 1,5, nicht beide.
  - **widerlegt:** weder noch (keine Regel bringt beide Sektoren in die Nähe).
- **H193c (Bericht, Parameterzählung).** Lesart (ii): freie Skala je Stufe je Sektor = sechs Zahlen für sechs Massen. Zeigen,
  dass die Trennung dann **inhaltsleer** ist (exakter Fit ohne Aussage). Die Trennung trägt nur über H193b.
- **Kontrolle.** 2000 erfundene Massensätze (gleiche Größenordnung, zufällige Hierarchie) durch dasselbe H193b-Raster, um zu
  messen, wie leicht das Kriterium „teilweise" zufällig erfüllt wird.

## Erwartung (offen gelegt)
Ich erwarte **widerlegt** oder knapp **teilweise**: Die stufenfesten Verhältnisse (Faktor 1 bis 2) verfehlen die beobachteten
(20 bis 589) deutlich, und eine einzige Regel kann die ungleichen Up- und Down-Verhältnisse nicht zugleich tragen (derselbe
Up-≠-Down-Widerstand wie H184–H190). Große Verhältnisse entstehen nur mit einer exponentiellen Regel samt freier Rate — die wird
als Parameter gezählt, und eine Rate trifft nicht beide Sektoren. Der Wert des Tests liegt im sauberen Schließen der Gabel, nicht
im Treffer. Ein echter (Teil-)Treffer wäre, wenn eine stufeneigene Regel ohne Fit die vier Verhältnisse eines Sektors trifft.

## Werkzeuge
Python (numpy, scipy) für die Rastersuche über Regeln und Zuordnungen und die σ-Abstände; Wolfram Language für die exakten
stufeneigenen Größen (Casimir a_k, Gewicht w_k) und die exakten Verhältnisse als Gegenprobe. Qiskit nicht nötig (keine
Schaltung, kein Messprozess). Die Coprozessor-Maschine (Baustufe 2) ist hier nicht das richtige Werkzeug: H193 ist ein
Zahlen-Fit über feste Regeln, kein Bandlauf mit Drehung/Messung; das wird in der Ergebnis-Notiz so vermerkt.

## Vorwissen geprüft
- `notes/research/hilbert_shift_felder_2026_11_24/generationsdrehung_h190/` (H190): Drehung in den Generationen, ein Hebel,
  Up nie < 3σ. Gemeinsames Objekt.
- `.../schwingungen_h184/`, `.../adjunkte_h187/`, `.../bewegtes_vakuum_h189/`: alle Wege „Quarks als Farbschwingung" geprüft
  und widerlegt (Potential, Ladung, Adjunkte, Ableitung, bewegtes Vakuum, Generationsdrehung).
- `.../baender_hs_stufen_h192/` (H192): gemeinsame Sphäre, HS-Stufen als Großkreise — Oktant ja, kleine Winkel angepasst.
- `.../ladungsachse_h162/` (k360): Teilchenarten mit Dimension und Casimir (nu, e+, u, dbar: Dim 2,2,6,6). Belegt die
  Zuordnung Teilchen → Stufe/Dimension.
- r67 (`sources/research/parts/v4100-post-release-layers.tex`): Zählregel, Casimir-Fläche a_k, Gewicht 2^(1−γ a_k).
- Memory: H178–H182 (K_ν = K_e = ⅔ geschützt, Up ≠ Down erlaubt), H188 nachträglicher Kandidat m ∝ (a l_k + b l_k²)/(l_i+l_j)².

## Grenzen (vorab)
Fester Satz Regeln und Zuordnungen, keine kontinuierliche Funktionensuche (die wäre ein verkappter Fit). Keine Dynamik, nur
Skalenzuordnung. OP3/OP4 (Quarkmassen) bleiben offen, unabhängig vom Ausgang.
