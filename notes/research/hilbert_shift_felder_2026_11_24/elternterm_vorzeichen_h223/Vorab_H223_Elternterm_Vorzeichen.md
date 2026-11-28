# Vorab-Notiz H223 (k437): Bindet ein Elternterm das Vorzeichen des Zweigwahl-Terms?

**Datum:** 2026-11-28, vor der Rechnung committet. **Auftrag:** Marc 28.11., Karte „Elternterm suchen“ (nach H222 und Erkundung k436).
**Werkzeuge:** Python/sympy (`k437_test_h223.py` → `k437_out.txt`), Wolfram unabhängig (`k437b_gegenprobe.wl` → `k437b_out.txt`). Qiskit nicht einschlägig.

## Ausgangslage
H222: Die Regel „größeres cos 3δ“ (Grenzfall q → 0⁻) wählt in beiden Lepton-Sektoren den Zweig der Daten. k436: Das Vorzeichen folgt weder aus J noch aus Stabilität;
unter J ist bei Ordnung 6 nur β₃ φ³r³ cos 3δ (und c₄ φ³r³ cos δ) erlaubt; N² ist nicht J-erlaubt. Gesucht: ein Elternterm, aus dem β₃ mit festem Vorzeichen folgt.

## Suchrichtung (rückwärts)
Notwendige Bedingungen zuerst, dann Kandidaten. Ein Elternterm in Form eines Quadrats u² (positiv, also durch Stabilität mit festem Vorzeichen) eines kubischen Bausteins u
liefert nach J-Projektion β₃ = 2·X·Z, wobei X der φ³-Koeffizient und Z der r³ cos 3δ-Koeffizient von u auf dem Zirkulantensektor ist. Das Vorzeichen von β₃ ist dann das
von X·Z, also eine Eigenschaft des Bausteins.

## Vorwissen geprüft
- H149/H155 (`generationszahl_h138/`): δ sieht nur die kubische Norm; V = αN + βN² wurde mit Fit gerechnet (H155), Entartung Σc ≷ 0 nachträglich bemerkt.
- H158c (k341): J-erlaubte Klassen; ungerade Ordnungen leer; Ordnung 6: φ³r³ cos δ, φ³r³ cos 3δ.
- H167 (k362/k362c): Zweigwahl erst bei Ordnung 6; q/α′ < 0 wählt den Oktant-Zweig im Im-Sektor.
- H221: α′ hat in den Sektoren entgegengesetzte Vorzeichen (Im +1, Re −1), die Daten verlangen q mit gleichem Vorzeichen.
- H222, k436 (dieser Strang): siehe oben. N² = … + 4φr³(φ² − 3r²) cos 3δ + 2r⁶ cos 6δ (k436).
- predictions/: nichts zu Elterntermen für das Vorzeichen.

## Offen gelegt: was vor der Rechnung schon überschlagen ist
- Für u = N und u = Tr W³ sind X und Z beide positiv (N = φ³ − 3φr² + 2r³ cos 3δ; Tr W³ = 3φ³ + 18φr² + 6r³ cos 3δ). Nach J-Projektion gäbe das β₃ > 0, also den
  **falschen** Zweig. Im vollen N² (ohne J) überwiegt bei K = ⅔ (φ² = 2r²) der J-verbotene Teil −12φr⁵ cos 3δ, Summe negativ, also der richtige Zweig.
  **Teil b ist deshalb nicht blind.**

## Teiltests und Kriterien (vorab festgelegt)
- **a (nicht blind, analytisch):** Ein Elternterm mit β₃ = κ·α′ und sektorunabhängigem κ ist ausgeschlossen (α′ wechselt das Vorzeichen, q nicht). Kriterium: Bestätigung
  durch Rechnung der Zweigwahl für β₃ = ±α′ in beiden Sektoren (genau ein Sektor falsch).
- **b (nicht blind):** u ∈ {N, Tr W³}: Zweigwahl nach J-Projektion von u² und für das volle u² (ohne J), beide Sektoren, φ = x_lepton, K = ⅔.
- **c (blind):** allgemeiner kubischer Invariantenbaustein u = x (Tr W)³ + y Tr W · Tr W² + z det W (Basis aller kubischen Invarianten einer 3×3-Matrix). Benannte Kandidaten,
  vorab festgelegt: (i) det W, (ii) Tr W³, (iii) (Tr W)³, (iv) det der spurfreien Matrix W − (Tr W/3)·1, (v) Tr W · Tr W², (vi) Tr(W³) − (Tr W)³/9 (spurbereinigte dritte Potenz),
  (vii) e₁e₂ − 9e₃ mit den elementarsymmetrischen Funktionen (verschwindet bei drei gleichen Eigenwerten). Für jeden: X, Z, Vorzeichen von β₃ nach J-Projektion und Zweigwahl;
  dazu der Anteil der Richtungen (x, y, z) mit β₃ < 0.
- **d (blind):** Kann ein solcher Baustein auch den cos δ-Term (c₄) oder den Spin-1-Term α′ liefern? Kriterium: Koeffizient von φ³r³ cos δ und von cos 2(δ − χ) in u² auf dem
  Zirkulantensektor aus Spur- und Determinanteninvarianten.

## Gesamturteil (vorab)
- **trägt:** mindestens ein benannter Kandidat aus c gibt nach J-Projektion β₃ < 0 (Daten-Zweig in beiden Sektoren), mit einem Grund, warum gerade er der Elternterm ist.
- **trägt teilweise:** benannte Kandidaten mit β₃ < 0 existieren, aber ohne ausgezeichneten Grund; oder nur unbenannte Kombinationen.
- **widerlegt:** kein benannter Kandidat gibt nach J-Projektion β₃ < 0.

## Grenzen (vorab)
Nur Elternterme der Form u² mit u kubisch aus Spur und Determinante (H₃(ℂ)-Zirkulante); χ-abhängige Bausteine (Konjugation σ) nur in d. Baumniveau, K = ⅔, H99.
