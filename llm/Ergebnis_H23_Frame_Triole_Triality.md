# Ergebnis H23: Die Frame-Triole Materie–Photon–Tachyon hat die Form der ℤ₂-Seite der Triality

Vorab-Notiz: `Vorab_Notiz_H23_Frame_Triole_Triality.md`, Commit 55043f8 (2026-10-23 19:34 MESZ), vor der Rechnung.
Skript `k79_test_h23.py`, Ausgabe `k79_out.txt`. Kriterium unverändert.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H23a ρ äußer, ℤ₂ | **bestätigt** | ρ bildet 𝔤 auf sich ab, Ordnung 2; Platz 1 behält seine Klasse, Platz 2 und 3 tauschen ihre Klassen |
| H23b feste Gruppe Spin(7) | **bestätigt** | ρ-feste Unteralgebra Dimension 21 (𝔰𝔬(7)). Platz 1: 1 ⊕ 7 mit invarianter Geraden ℝ·1, 7er-Teil irreduzibel. Platz 2 und 3: je irreduzibel 8, untereinander äquivalent |
| H23c Parität | **bestätigt** (trivial) | Zulässige Vorzeichen: (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1) = ℤ₂ × ℤ₂; auf dem festen Platz trivial ist (1,−1,−1) |
| H23d S₃ | **bestätigt** (Kontrolle) | ℤ₃: eine Bahn der Länge 3; jede Transposition: ein Fixpunkt, eine Bahn der Länge 2 |
| H23e Farbe fest unter ganz S₃ | **bestätigt** | 𝔤₂ = {(A, A, A)} ist ρ-fest und liegt in 𝔰𝔬(7) |

## Einordnung

1. **Zwei Triolen, eine S₃.** Die 120°-Triole ist die ℤ₃-Bahn der Triality τ. Die Frame-Triole der Originalarbeit (Photon als
   Gleichgewicht, Materie und Tachyon gespiegelt) hat genau die Form einer Transposition ρ: ein fester Platz, zwei vertauschte.
   Beide sind Ansichten derselben Gruppe S₃ auf den drei Triality-Plätzen. In der Autorlesart wählt der Zoom die Untergruppe.
2. **Photon = Vektor-Platz, Materie und Tachyon = Spinor-Plätze** (Lesart):
   - Unter der von ρ festgelassenen Gruppe Spin(7) hat der Photon-Platz eine ausgezeichnete Richtung, die reelle Einheit (1 ⊕ 7).
   - Materie- und Tachyon-Platz sind gleich (je 8) und werden von ρ vertauscht. Das passt zu „Tachyon = Spiegelbild der Materie“.
   - Die Parität (1, −1, −1) trennt den Photon-Platz von den beiden anderen, wie (−1)^F Bosonen von Fermionen. Sie folgt trivial aus
     der Trilinearität. Bemerkenswert ist nur, dass sie zur Lesart Photon = Vektor, Materie = Spinor passt.
3. **Welcher Platz das Photon ist, ist eine Wahl.** S₃ hat drei Transpositionen, jede hält einen anderen Platz fest. Das stimmt mit
   Konvention F überein (Photon = entarteter Fixpunkt) und mit der Autorabsicht, dass die Gestalt beim Zoom gewählt wird.
4. **Farbe ist unter der ganzen S₃ fest** (H23e). Sie liegt in G₂ = Fixgruppe von Triality und Spiegelung, also unter beiden
   Triolen-Formen unverändert.
5. **Spannung, offen:** Die drei Plätze können auf derselben Ebene nicht zugleich die Frames (H23) und die Generationen (H22-Lesart)
   tragen. Nach der Autorabsicht wären das zwei Zoomstufen. Welche Ebene welche Rolle trägt, ist nicht gezeigt. Die Dixon-Ablage hat
   mit Im ℍ einen zweiten Dreier-Träger (v4.9.0-r33), der eine der beiden Rollen übernehmen könnte.
6. **Chiralität (Bestandsaufnahme Test 3):** Die beiden Spinor-Plätze sind in acht Dimensionen das Chiralitätspaar. Liest man Materie
   und Tachyon als diese beiden, ist der Frame-Wechsel M ↔ T ein Chiralitätswechsel. Das ist eine Spur für Test 3, nicht gerechnet.
