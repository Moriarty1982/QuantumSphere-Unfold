# Erkundung: Suche nach der Form η im neutralen Sektor

13. November 2026, abends. Autorenauftrag: „mach das“ (nächster Schritt laut Übergabe), nach Festschreiben von H100
(Commit 9c77ddd). Erkundung, analytisch mit numerischer Selbstprüfung; **kein Datenvergleich** außer der bekannten
Zielgröße aus H99b. Keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung T8, OP3.
Skript `op3_eta_form_search_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_slot_u3_gauging_2026_11_13.md`, Nachtrag Neutrino-Block: ν_L und e_L teilen das linke Tripel X; geladen
  T_12 ∝ (XᵀX)*, neutral Ω_1 ∝ Xᵀ η X; der Sektorunterschied liegt ganz in η.
- `op3_indefinite_form_2026_11_13.md` (bilineare Form x^T y, Lesart B mit Signatur (3,3)), r10.2 (120°-Triole ist
  Nullvektor), r44.1(e) (zirkulante hermitesche Kopplung gibt die Brannen-Form), r55 (Majorana mit Z_2).
- Suche nach Bargmann, Pancharatnam, geometrischer Phase, Berry in notes/ und sources/: kein Treffer.

## Ergebnis

**1. Die Brannen-Phase ist ein Drittel der Bargmann-Phase der Plätze.** Für jede Gram-Matrix mit Einheitsdiagonale
(hermitesch, auch komplex) gilt

    s_k = 1 + 2ρ cos(θ + 2πk/3),   cos 3θ = Re(c_12 c_23 c_31)/ρ³

(numerisch 2·10⁻¹⁵). Haben die drei Überlappungen gleichen Betrag (zirkulanter Fall, Brannen-Form der geladenen
Leptonen nach r44.1(e)), ist 3θ = Φ = arg(c_12 c_23 c_31), die Bargmann-Invariante des Tripels, also seine
geometrische Phase. Sie hängt nicht von der Phasenwahl der einzelnen Plätze ab.

**2. H99 als Bedingung an die geometrische Phase.** Gleiche Überlappung und Verschiebung um den Bogenrand heißt:

    ΔΦ = Φ_ν − Φ_e = 3θ_b = π/4   (bei ρ² = 1/2).

NuFIT 6.1 verlangt 3 · 0,25802 = 0,774 statt π/4 = 0,785 (die Fassung bei einer Skala liegt dazwischen). Gesucht ist
also eine Form η, die jede Überlappung im Betrag erhält und die geometrische Phase des Tripels um π/4 dreht.

**3. Was dafür nicht in Frage kommt.**
- **Umphasen der Plätze** (x_a → e^{iφ_a} x_a): Φ ist invariant (numerisch geprüft). Eine bloße Konvention auf den
  Plätzen erzeugt keine Verschiebung.
- **η diagonal in der Eigenbasis** (Vorzeichenwechsel einzelner Eigenwerte) im zirkulanten Fall: Die Beträge der
  Wurzeln bleiben die der geladenen Leptonen; die Massenverhältnisse wären gleich. Ausgeschlossen.
- **Reelle Formen auf reellen Plätzen**: Φ ∈ {0, π}; θ ändert sich nur über die Beträge der einzelnen Überlappungen.
  Das ist möglich, bricht aber die zyklische Gleichheit der Beträge. Die zirkulante Lesart verlangt eine komplexe
  Struktur.
- **Lesart B allein** (geladen hermitesch x†y, neutral bilinear xᵀy auf denselben komplexen Plätzen): Bei 4000
  Tripeln mit ρ_e² = 0,50 streut ΔΦ mit 1,36 um null und Δρ² stark; keines erfüllt beide Bedingungen. Der Wechsel
  von hermitesch zu bilinear legt keine Verschiebung fest.

**4. Was die Bedingung verlangt.** Eine gleichmäßige Phase e^{iπ/12} auf jeder Überlappung erhält alle Beträge und
dreht Φ um 3 · π/12 = π/4. Bei hermiteschen Überlappungen ist das nicht möglich (c_ba = c_ab*), bei symmetrischen
(bilinearen, Majorana) schon. Der Neutrino-Block ist bilinear; die Bedingung passt also zur Art des Blocks. Gesucht
ist damit eine native Größe, die jedem Paar von Plätzen im neutralen Sektor die Phase π/12 gibt, gleichwertig eine
geometrische Phase π/4 je Umlauf über die drei Plätze.

## Bewertung
- Die Frage nach η ist auf eine geometrische Bedingung zurückgeführt: Bargmann-Phase π/4 bei erhaltenen Beträgen.
  Das ist neu im Projekt (kein Vorbefund) und in der zirkulanten Lesart äquivalent zu H99.
- Ausgeschlossen sind Umphasen, Vorzeichenwechsel in der Eigenbasis und der bloße Wechsel hermitesch → bilinear.
- Nicht gefunden: eine native Quelle für die Phase π/12 je Paar. Hinweise, ohne Rechnung: Der Neutrino-Block ist
  symmetrisch, also für eine gleichmäßige Phase geeignet; π/4 ist die Phase von (1 + i)/√2. Beides ist keine
  Herleitung und darf nicht als Treffer gezählt werden.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert. H100 ist davon unberührt (Kandidaten festgeschrieben).

## Nächste Fragen
- Gibt es im Companion eine Paar-Phase im neutralen Sektor, etwa aus dem Assoziator, aus Q_J = iL_e7 oder aus der
  Lesart B auf dem Kern, die auf jedem Paar gleich ist?
- Hat die geometrische Phase der geladenen Leptonen (Φ_e = 3θ_e = 0,667) selbst eine native Deutung?
