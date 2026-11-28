# Vorab-Notiz H225 (k439): Legt φ sich als dynamischer Modulus fest, wenn die Vakuumenergie beider Lepton-Sektoren minimiert wird?

**Datum:** 2026-11-28, vor der Rechnung committet. **Auftrag:** Marc 28.11., 09:45 (Karte: „φ als dynamischer Modulus“).
**Werkzeuge:** Python (`k439_test_h225.py` → `k439_out.txt`), Wolfram unabhängig (`k439b_gegenprobe.wl` → `k439b_out.txt`; Teil a und c symbolisch).
Qiskit nicht einschlägig (keine Quantenschaltung).

## Ausgangslage
- H221: Der gemeinsame Versatz beider Lepton-Sektoren ist eine Drehung χ → χ + φ des Mischungswinkels im H167-Potential
  V_s(δ) = −α′_s cos 2(δ − χ_s − φ) (Im-Sektor α′ = +1, χ = π/4; Re-Sektor α′ = −1, χ = 0). Bei q = 0 ist das Minimum jedes Sektors −1, **für jedes φ**:
  φ ist bis zu dieser Ordnung eine exakt flache Richtung, also ein Modulus.
- H222 + Wahl des Autors (28.11., 03:27): Der Zweig wird vom kubischen Term q cos 3δ mit **gesetztem** Vorzeichen q < 0 gewählt (Grenzfall q → 0⁻).
- H224: φ ist keine Wigner-Drehung der Frame-Boosts. Messwert unter J: φ = x = 0,0395773 (σ 7,8·10⁻⁷); mit freiem a 0,0395746 ± 0,0000063; x_ν = 0,04336 ± 0,00213.

## Idee (Hypothese H225)
Ist φ ein Modulus, dann hebt der einzige skalenfreie Term, der schon im Bild steht (der kubische Zweigwahl-Term), die Entartung in φ. φ stellt sich dort ein, wo die
**gemeinsame Vakuumenergie beider Sektoren** E(φ) = Σ_s min_δ V_s(δ; φ, q) minimal ist. Keine neue Zahl wird eingeführt: gleiche Koeffizienten in beiden Sektoren
(Universalität wie H221), gleiches q.

## Vorwissen geprüft
- H167 (Potential, q/α′ = −0,0852 als Fit im Im-Sektor), H168 (gleicher Versatz beider Sektoren), H221 (Drehung exakt, Universalität gesetzt), H222 (Zweigpaare
  nach der Drehung: Im π/12 − φ und π/4 + φ mit cos 3δ = ±cos(π/4 − 3φ); Re π/6 ∓ φ mit cos 3δ = ±sin 3φ), k436/H223 (Vorzeichen folgt nicht aus J), H224 (Wigner, kein Treffer).
- Wertsuchen ohne Treffer: H151d, H158d, H167d1, CT-002 (γ_M/6, unter J 15σ), H224.
- Suche „Modulus“ im Repo (`notes/research/`, `analysis/`): keine Fundstelle zu φ oder zum Lepton-Phasenversatz; nur fremde Zusammenhänge (OP5, HC-Hintergrund).

## Teile und Kriterien (vorab)
**a (nicht blind, führende Ordnung in q).** Aus H222 folgt E(φ) = −2 + q·[w·|cos(π/4 − 3φ)| + |sin 3φ|] + O(q²), w = Gewicht Im : Re (gesetzt w = 1: beide Sektoren
drei Zustände, gleiches |α′|). Mit q < 0 liegt das Minimum bei tan 3φ* = 1 + √2/w, für w = 1 also **φ* = π/8 = 0,3927**. Für jedes w > 0 gilt φ* ∈ (π/12, π/6).
Das steht vor der Rechnung analytisch fest; die Rechnung prüft es nur (Python numerisch, Wolfram symbolisch). Zusätzlich berichtet: Gewichte w ∈ {½, 1/√2, 1, √2, 2}.
**b (blind, endliches q).** Exakte Minimierung in δ (Zweige relaxieren) für q/α′ ∈ {−0,001; −0,01; −0,05; −0,0852; −0,2; −0,3}, w = 1, φ-Gitter über eine Periode
π/3 mit Nachschärfen. Gemessen: φ*(q), Wert E(φ*), Lage des Datenpunkts φ = x (Steigung, Rang in E).
**c (blind, Ordnung 6).** Gleiche Rechnung mit dem nächsten invarianten Term r cos 6δ allein (r = ±10⁻³, beide Vorzeichen, H222d: nur cos 3δ und cos 6δ invariant).
Gemessen: Lage aller Minima von E(φ) in einer Periode.
**Kriterium (für b und c einzeln, und für a):** Treffer, wenn ein globales Minimum φ* innerhalb 1 % von x = 0,0395773 liegt (σ unter J ist so klein, dass ein
strenger σ-Test bei einer Modellrechnung auf Baumniveau nichtssagend wäre; 1 % ist die Schranke aus H224 „locker“). Zusätzlich berichtet: Abstand in Einheiten von σ(x_ν).
**Urteil:** trägt, wenn b mit w = 1 einen Treffer liefert; trägt teilweise, wenn nur c oder nur ein w ≠ 1 trifft (dann mit freier Wahl); sonst **widerlegt**.
Eine Kombination aus cos 3δ und cos 6δ mit freiem Verhältnis wird nicht gewertet (ein Parameter für eine Zahl).

## Grenzen (vorab)
Zirkulantensektor, Baumniveau, keine Quantenkorrektur zur Modulus-Energie (kein Coleman-Weinberg-Term: der bräuchte Massenskalen μ_s und eine Renormierungsskala,
also Setzungen gegen die Skalenfreiheit aus H221). Universalität der Koeffizienten und w = 1 sind gesetzt. Ein Treffer wäre nur dann eine Herleitung, wenn die
Annahme „φ minimiert die gemeinsame Vakuumenergie“ selbst begründet ist; das ist hier die Hypothese, nicht ein Ergebnis.
