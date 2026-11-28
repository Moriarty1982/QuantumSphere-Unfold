# Vorab-Notiz H221 (k434): Skala oder skalenfrei? Welcher Mechanismus gibt beiden Lepton-Sektoren denselben Versatz?

**Datum:** 2026-11-28 (vor der Rechnung committet). **Strang:** Feldgleichung, Frage nach der Skala.
**Anlass:** Autor 26.11.: „zuerst setzen und dann schauen was sich daraus ergibt, vielleicht finden wir dann einen grund wieso es skalenfrei sein muss“;
28.11. (über den Koordinator): „dann weiter“ — Feldgleichung, woher die Skala kommt, zuerst mit Skala als Setzung.
**Nummern:** H221, k434 (gegen `main` geprüft; zuletzt H220/k433). Einordnung `wiki/Gesamtbild.md`: T8/T13, OP3/OP4; Skala aus der Wirkung offen.

## Ausgangslage (aus den Vorbefunden)
H167 hat im geladenen Sektor (Im-Sektor, c = 1) zwei Wege gefunden, das Elektron aus dem Oktanten zu heben, beide mit genau einem kleinen Verhältnis, und
festgehalten: „die Daten trennen die beiden Wege nicht“:
- **Weg K (skalenfrei):** Konjugationsterm α cos 2δ (Ordnung 4, dimensionslos); δ* verlangt α/α′ = 0,0793204.
- **Weg S (Skala):** Term sechster Ordnung (β₃v²/Λ²) cos 3δ; δ* verlangt q/α′ = −0,0852479 mit q = β₃v₀²/Λ².
H168 fand: beide Sektoren liegen um **denselben** Versatz x unter ihrem Minimum (geladen π/12 − x, neutral π/6 − x), und eine gemeinsame feste Skala Λ scheidet
aus; zulässig bleibt nur eine Sektorskala Λ_s ∝ v_s, dann ist q in beiden Sektoren dieselbe dimensionslose Zahl. H213/H214: x_ν = 0,04336 ± 0,00213 aus R,
x_lepton = 0,039575 (Polmassen), Abstand 1,78σ — der gemeinsame Versatz ist verträglich.

**Idee dieses Tests:** Der zweite Sektor (Re-Sektor, c = 0) trennt die beiden Wege. Mit **universellen** dimensionslosen Koeffizienten (dieselben |α/α′| bzw.
|q/α′| in beiden Sektoren) muss der Weg auch im neutralen Sektor den Versatz x_ν liefern.

## Vorwissen geprüft
- `delta_h167/` (Ergebnis, `k362c_nachtrag_ordnung6.py`): Modell V_δ/v₀⁴ = α cos 2δ − α′ cos 2(δ − χ) + q cos 3δ, χ = arctan c; Zielwerte oben; bei Ordnung 6
  nur cos 3δ gerechnet, cos δ nicht.
- `delta_h168/Ergebnis_H168_Skala_und_Sektoren.md`: c = 0 hat Minima (gefaltet) 0, π/6, π/3; π/6 für das passende Vorzeichen von α′; gemeinsamer Versatz x;
  feste gemeinsame Skala ausgeschlossen (x_ν wäre 10⁻¹²); nachträglich: „Der Konjugationsterm kann den gemeinsamen Versatz nicht liefern: für c = 0 ist er
  dieselbe Funktion wie der Spin-1-Term und verschiebt nichts. Der gemeinsame Versatz passt besser zu einem gemeinsamen Drehwinkel der Mischung (χ → χ − x).“
- `generationszahl_h138/Ergebnis_H155_Skala_als_Setzung.md`: Skala als Setzung, K = ⅔ aus Tauschsymmetrie, δ als angepasster Parameter.
- `feldgleichung/` (H129, H133, H135, H136; Memory feldgleichung-rekursiv-k290): skalenfrei vs. Skala offen; keine Regel für κ; Stromkopplung = neue Skala.
- `versatz_spannung_h213/`, `massenschema_h214/`: Datenlage für x_ν und x_lepton.
- Zurückgestellte Ideen I1–I7 geprüft: I7 (Attraktor-Route OP5) nur bei DESI/Euclid-Auslöser; kein Auslöser trifft.

## Nicht blind (offen gesagt)
- **Teil a ist nicht blind:** Dass Weg K im neutralen Sektor nichts verschiebt, steht in H168.
- **Teil b ist teilweise nicht blind:** In der Vorüberlegung wurde linear entwickelt: am geladenen Zweig ist ε_e ≈ −(3√2/8)(q/α′), am neutralen Zweig
  ε_ν ≈ −(3/4)(q/α′_ν); bei universellem |q/α′| also |ε_ν|/|ε_e| ≈ √2. Erwartet wird daher, dass Weg S den neutralen Versatz um rund √2 zu groß gibt.
  Blind sind die exakten (nichtlinearen) Werte, das Vorzeichen-Verhalten und die Zahl in σ.
- **Teile c und d sind blind.**

## Teile und Entscheidungskriterien
Neutraler Sektor: V_ν(δ) = −α′_ν cos 2δ + q_ν cos 3δ (+ α_ν cos 2δ), Minimum nahe π/6 (gefaltet), Versatz x_ν,pred = π/6 − δ_min (gefaltet).
Das Vorzeichen von α′_ν wird so gewählt, dass c = 0 bei π/6 liegt (H168); beide Vorzeichen von q relativ dazu werden gerechnet.

**a (nicht blind) — Weg K universell.** |α/α′| = 0,0793204 in beiden Sektoren ⇒ x_ν,pred. Kriterium wie b.

**b (teilweise nicht blind) — Weg S universell.** |q/α′| = 0,0852479 in beiden Sektoren (Λ_s ∝ v_s) ⇒ |x_ν,pred| exakt.
Kriterium: Weg trägt, wenn |x_ν,pred − 0,04336| ≤ 2·0,00213 und das Vorzeichen stimmt (δ unter π/6). Sonst Abstand in σ(x_ν) und vorhergesagtes R.

**c (blind) — beide Terme universell (zwei Parameter).** Gibt es (α/α′, q/α′), die beide Versätze (x_lepton, x_ν) zugleich treffen? Wenn ja: Werte und ob sie
„natürlich“ sind (|·| < 0,3). Das ist ein Fit ohne Vorhersage und wird als angepasst geführt; nur die Existenz und die Größe werden berichtet.

**d (blind) — gemeinsame Drehung der Mischung (H168-Vorschlag).** χ → χ − x in beiden Sektoren ohne weitere Terme: Liegt das Minimum dann exakt bei π/12 − x
bzw. π/6 − x für **jedes** x (also ein skalenfreier Mechanismus, der gleiche Versätze erzwingt)? Kriterium: Abweichung < 10⁻⁹ für x ∈ {0,02; 0,04; 0,06}.
(Erwartung: ja, denn das Minimum des Spin-1-Terms folgt χ. Teil d prüft das am vollen Ausdruck mit Konjugationsanteil null.)

## Gesamturteil (vorab festgelegt)
- **Spricht für skalenfrei:** a und b scheitern (> 3σ), d trägt. Lesart: Ein Mechanismus mit Skala (Ordnung 6, Λ_s ∝ v_s) gibt den beiden Sektoren
  verschiedene Versätze; gleiche Versätze verlangen eine dimensionslose gemeinsame Drehung. Die Skala wäre dann nicht die Quelle des Versatzes.
- **Spricht für die Skala:** b trägt (≤ 2σ).
- **Unentschieden:** b zwischen 2σ und 3σ, oder c findet eine natürliche Lösung und d scheitert.
Urteil zur Hypothese H221 „Der Re-Sektor trennt Weg K und Weg S“: **trägt**, wenn mindestens einer der beiden Wege bei universellen Koeffizienten um > 3σ
scheitert und der andere nicht; **trägt teilweise**, wenn beide scheitern (dann trennt er sie nicht voneinander, schließt aber beide in universeller Form aus);
**widerlegt**, wenn beide innerhalb 2σ tragen.

## Werkzeuge
Python (`k434_test_h221.py` → `k434_out.txt`): exakte Minima auf feinem Gitter + Newton-Nachschärfung. Wolfram unabhängig (`k434b_gegenprobe.wl` →
`k434b_out.txt`): FindMinimum/NSolve für b und d, symbolische Lage des Minimums für d. Qiskit nicht einschlägig.

## Grenzen
Nur der Zirkulantensektor, Baumniveau, K = ⅔ fest (A = B), Ebenen-Lesart von J wie H167. Bei Ordnung 6 nur cos 3δ (cos δ würde einen weiteren freien Koeffizienten
bringen, siehe c). Universalität der dimensionslosen Koeffizienten zwischen den Sektoren ist eine Setzung (Λ_s ∝ v_s, |α′| gleich). Vorzeichen bleiben frei.
H99 (Brannen-Form für Neutrinos) vorausgesetzt. Kein Guard berührt; OP3/OP4/OP5 offen.
