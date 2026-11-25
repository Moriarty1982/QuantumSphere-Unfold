# Ein-Feld-Prinzip für das Flavon-Potential (Erkundung k278, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Ist der Flavon **ein einziges Element** der Albert-Algebra, gleich in welcher Mischung mit seiner Ladungsdrehung
(Z_a = X(v) + a·C·X(v)), dann hängt jedes Potential nur von |v|² und xyz ab. Das Prinzip legt den Σvᵢ⁴-Koeffizienten damit auf **null** fest.
Die Ausrichtung ist dann zwingend (1,1,1) mit Restgruppe **ℤ₃**, oder es gibt gar keine Ausrichtung. **ℤ₂ (die Neutrino-Lesart) verlangt ein zweites, unabhängiges Feld.**

Auftrag: Autor („ja bitte“ nach r60; „dann weiter rechnen“), Frage aus r60.5 nach einem Prinzip für die Koeffizienten. **Nicht blind:** Dass ein Element
einer kubischen Jordan-Algebra nur die Invarianten Tr, Tr(·)², N hat, ist Lehrbuch (Cayley–Hamilton). Neu ist die Anwendung auf den Flavon und die
Ladungsmischung. Skripte **k278, k278b**.

Werkzeuge: Python (numpy, scipy) mit der Albert-Algebra aus k276 (Invarianten, Cayley–Hamilton, gedämpfte Dynamik wie k274). Wolfram Language exakt für
Tr Z², N(Z), Tr Z⁴ als Funktion von a (k278b). Qiskit nicht eingesetzt.

## Vorwissen geprüft
r60.4/r60.5 (k277: xyz = N(CX), gemischte Invarianten bringen Σv⁴), k274 (nichtlineares Feld, Duffing), H39 (ℤ₃ für Dirac-Sektoren, ℤ₂ für Neutrinos),
Literatur (Altarelli–Feruglio: zwei Flavons φ_T, φ_S für geladene Leptonen und Neutrinos).

## Ergebnisse
1. **Invarianten eines Felds (k278 A, k278b):** Z_a hat die Einträge (−a + i)vₖ. Exakt gilt Tr Z² = 2(1 + a²)|v|², **N(Z) = 2(3a − a³)·v₁v₂v₃**, Tr Z⁴ = 2(1 + a²)²|v|⁴ = (Tr Z²)²/2.
   Kein Σv⁴, für jedes a. Cayley–Hamilton gilt in der Algebra auf 4·10⁻¹⁶.
2. **Zwei Felder (k278 B):** Werden X und CX als getrennte Felder behandelt, oder treten zwei Flavons v, w auf, dann gibt es Richtungsabhängigkeiten über |v|²
   und xyz hinaus (Tr((X∘Y)²) = |v|⁴ − Σv⁴).
3. **Dynamik (k278 C):** Der gedämpfte Fluss Ẍ = −∇V − γẊ mit V = −μ²/2·Tr Z² + κN(Z) + λ/4·Tr Z⁴ endet in allen 80 Läufen (vier Parameterpunkte,
   a = 0,5 … 3,7, κ beider Vorzeichen) bei (1,1,1) mit Restgruppe ℤ₃.
4. **Ohne wirksamen kubischen Term (k278 D):** Für κ = 0, und ebenso für **a ∈ {0, ±√3}** (dort ist N(Z_a) ≡ 0), endet der Fluss auf einer Schale fester |v| in
   beliebiger Richtung. Dann gibt es keine Ausrichtung.

## Bewertung
- **Ein Prinzip, das die Koeffizienten festlegt:** „ein Flavon = ein Element“. Es ist natürlich, weil die Turm-Dynamik (k274) für *ein* Feld formuliert ist.
  Es setzt den Σv⁴-Koeffizienten auf null und erzwingt ℤ₃. Das ist die Lesart G_D = ℤ₃ der Dirac-Sektoren (H39). Das ist bekannt und nicht blind,
  aber jetzt aus einem Prinzip und nicht aus Parametern.
- **Folgerung für die Neutrinos:** ℤ₂ (TM2 nach H39, oder TM1 über K∘S₀ nach k256/H8) ist mit einem Feld unmöglich. Die Neutrinos brauchen ein **zweites,
  unabhängiges Feld**. Das entspricht dem Zwei-Flavon-Aufbau der Literatur, ist hier aber eine Folgerung: Geladene Leptonen und Neutrinos können nicht dasselbe
  Vakuum lesen.
- **Neu ist die Ladungsmischung a.** Bei a ∈ {0, ±√3} (Phase des Eintrags −a + i bei π/2, π/6 oder 5π/6) verschwindet der kubische Term, und das Vakuum bleibt
  unausgerichtet. Ob eine dieser Phasen ausgezeichnet ist, etwa durch den Projektor ½(1 + iL_e₇) aus r42 (a = 1, Phase 3π/4, kubischer Term ungleich null), ist offen. Normiert auf |Z|³
  ist der kubische Term ∝ cos 3φ mit der Phase φ des Eintrags: maximal bei φ = π/3 oder 2π/3 (a = ∓1/√3), null bei π/6, π/2, 5π/6.
- Weiter gesetzt: der Flavon in den e₇-Anteilen, die drei Plätze als Generationen, alle Skalen. OP3 und OP4 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- Ein **blinder Test** wird jetzt denkbar: Wenn ein zweites Feld für die Neutrinos nötig ist, wo sitzt es in H₃(𝕆)? Kandidat ist der Spin-2-Teil (Realteile,
  5 → 1′ ⊕ 1″ ⊕ 3 unter A₄). Die Frage wäre, ob ein Ein-Feld-Potential dort ℤ₂ statt ℤ₃ ergibt. Das wäre eine echte Vorhersage, vorher Vorab-Notiz (H128).
- Prüfen, ob r42 die Ladungsmischung a festlegt.

## Dateien
`k278_ein_feld_prinzip.py` (`k278_out.txt`; benutzt `../h127/k276_test_h127.py`), `k278b_ein_feld_exakt.wl` (`k278b_out.txt`, Wolfram).
