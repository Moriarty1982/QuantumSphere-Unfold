# Ergebnis H242 (k458): Alte Kernel-Definition K₃ = K₁K₂ und die drei Kopien

**Datum:** 2026-11-28. **Vorab:** `Vorab_H242_Kernel_XOR.md`, Commit f48ba49, vor der Rechnung. **Rechnung:** `k458_test_h242.py` → `k458_out.txt`;
Gegenprobe `k458b_gegenprobe.wl` → `k458b_out.txt` (symbolisch).

**Frage 1 (gleiche Struktur): trägt, nicht blind.** **Frage 2: Die Regel folgt (g₁ + g₂ + g₃ ≡ 0 mod 3). Dass das physikalische Generationen sind, ist nicht
gezeigt.**

## Die alte Definition
Companion, Definition „Biquaternion kernel“: q = it + z₁e₁ + z₂e₂ + z₃e₃ mit komplexen z_k und **e₃ := e₁e₂**, daher senkrecht auf e₁ und e₂. Sektoren:
Materie K₁, Tachyon K₂ = J·K₁, Photon K₃ = e₁e₂ mit Re z₃ = 0. Das „XOR“ hat zwei Schichten:
- **Richtung:** e₁e₂ = e₃ ist in der Cayley–Dickson-Basis wörtlich das Index-XOR 1 ⊕ 2 = 3 (H241 B1). Geometrisch ist das das Kreuzprodukt, senkrecht auf
  beiden.
- **Phase:** Die komplexen Koordinaten z_k werden in 𝕊 zum Winkel auf dem Kreis der Kopien (i ↦ Wand e₈, gesetzt).

## Befunde
- **N1 (C):** K₃ := K₁K₂ steht für alle Phasen exakt senkrecht auf K₁ und K₂, und es gilt K₁K₂ = u_{−(α₁+α₂)}(e₃) (symbolisch). Die Kernel-Definition
  überlebt die Einbettung, und ihre Phase ist α₃ = −(α₁ + α₂).
- **N2 (A):** Der Schlussrest von span{1, K₁, K₂, K₃} ist exakt |sin(α₁ + α₂ + α₃)| (Wolfram symbolisch, Python an 2000 Tripeln). Das Kernel-Tripel ist also genau
  dann eine Quaternion-Unteralgebra von 𝕊, wenn **α₁ + α₂ + α₃ ≡ 0 (mod π)**. Zufallskontrolle: 0 von 2000 zufälligen Tripeln schließen.
- **N3:** Bei gemeinsamer Phase schließt das Tripel genau bei 0°, 60° und 120° (mod 180°). Das sind genau die drei G₂-Kopien.
- **N4 (B):** Von den 27 Belegungen der drei Kerne mit Kopien schließen genau 9, und zwar genau die mit g₁ + g₂ + g₃ ≡ 0 (mod 3): 3 mit allen Kernen in
  derselben Kopie und 6 mit je einem Kern in jeder Kopie (Python und Wolfram).

## Lesart
Marcs alte Definition „K₃ senkrecht auf den beiden anderen“ ist in 𝕊 dieselbe Struktur wie die drei Kopien. Die Richtung folgt dem Index-XOR
(e₁ ⊕ e₂ = e₃), die Phase der Regel „Summe null“. Die drei Kopien sind die Phasen, bei denen ein Kernel-Tripel mit einer einzigen Phase schließt. Weist man
jedem Kern eine Kopie g ∈ ℤ₃ zu, gilt die Erhaltungsregel g₁ + g₂ + g₃ ≡ 0 (mod 3). Formal ist das eine ℤ₃-Ladung, wie sie eine Generationensymmetrie hätte.

## Nur Bericht
- **Tachyon-Abbildung J = i** (α₂ = α₁ + 90°): K₃ = K₁K₂ hat α₃ = −(2α₁ + 90°). Das Photon-Kriterium Re z₃ = 0 gilt genau für α₁ ≡ 0 (mod 90°). Dieses
  Tripel (0°, 90°, 90°) schließt, ist aber kein Kopien-Tripel (90° ist keine Kopie). Die alten Sektoren und die Kopien sind also verschiedene Belegungen
  derselben Regel.
- **Brannen-Phasen −δ + 2πk/3:** Sie sind eine „je eine Kopie“-Belegung, verschoben um δ. Der Schlussrest ist |sin 3δ| = 0,618 (δ_Im) bzw. 0,993 (δ_Re).
  Ohne Versatz (δ = 0) schließt das Tripel. Der gemessene Versatz bricht den Schluss, wie in H238 C.

## Hergeleitet, gesetzt, offen
- **Hergeleitet:** die Phasenregel α₃ = −(α₁ + α₂), das Schlusskriterium |sin Σα| (symbolisch) und die 9 schließenden Kopien-Belegungen.
- **Gesetzt:** die Einbettung z·e_k ↦ (Re z·e_k, Im z·e_k), also i ↦ Wand e₈, und die Wahl e₁, e₂, e₃ = e₁e₂ in 𝕆.
- **Nicht blind:** N1 bis N4 folgen aus der Produktregel von H241.
- **Offen:** ob die ℤ₃-Ladung der Kerne die physikalischen Generationen sind. Dazu fehlen Massen, Mischung und eine Begründung, warum jeder Kern eine Kopie
  trägt. Offen ist auch, wie die alte Sektorbelegung mit J = i zu den Kopien steht.

## Werkzeuge und Grenzen
Python (Stichproben, Zufallskontrolle, 27 Belegungen) und Wolfram (symbolischer Schlussrest). Qiskit nicht einschlägig.
