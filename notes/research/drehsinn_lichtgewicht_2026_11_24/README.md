# Drehsinn aus dem Lichtgewicht? (Erkundung, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Die Störung des Lichtgewichts a ≠ b wählt den Drehsinn nicht. a − b ist reell und diagonal, also gerade unter
der Orientierungsumkehr (ω ↦ ω², z ↦ z̄). Es ändert in der Referenzwahl r14.2 nur den Betrag der Bargmann-Phase und K, nicht das Vorzeichen.
Das Vorzeichen von a − b ist das Frame-Etikett (M: a > b, T: a < b) und spielt die Rolle von τ. Zusammen mit einer orientierten Größe ergibt
es wieder die Relation τε aus H123. Die offene Wahl wandert zu ε, also zur Wahl von i bzw. ω.

Auftrag des Autors (Chat 24.11.2026): „drehsinn herleiten“, Anschluss an das Gedankenexperiment vom selben Tag (Punkt 15 der Notizen:
„HC stört das Lichtgewicht leicht“; Rückfrage, ob a − b ein Drehmoment ist). **Erkundung, nicht blind:** Die Vorzeichenfrage ist analytisch
entschieden, bevor gerechnet wird (Perron–Frobenius und Symmetrie). Deshalb keine Vorab-Notiz; **H125 bleibt frei**. Vergeben: Skript **k250**.
Keine Runde (nur auf Entscheidung des Autors).

Werkzeuge: Wolfram Language (exakt, symbolisch in a, b) für k250. Qiskit nicht eingesetzt: kein Schaltkreis und kein Messablauf, die Aussage
ist eine Symmetrieaussage über einen reellen Zustand. Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf). Die
Matter-Gewichte wurden in k250 bewusst **nicht** eingesetzt, damit der Betrag (Abschnitt 5) für einen blinden Test offen bleibt.

## Vorwissen geprüft
- **Frame-Gewichte:** r81.6 (a: neutrale Paarung = Photon-Mischung P, Rest ∝ p₊ − p₋ = 1/γ bei Matter-Gewichten; b: R = σ_y und T = σ_z
  tauschen beide die Port-Gewichte auf der Kompensator-Achse), r81.8(c) (Gewichte a, b für T_M, T_T), r85 (a − ib als teilweise
  Wick-Drehung um arctan(b/a), 45° bei Photon-Gewichten), `op5_field_readout_inventory_2026_11_06.md` (Photon: a = b, c = 0, ρ = I/2).
- **r82/r83:** r82.1(b) Vakuumenergie (a − b)V_min, in r83 zurückgezogen (Lesart B: a·V_min); r82.2 (H74): direkte Kopplung zerstört die
  Auslöschung, Stabilität braucht Verstimmung. Dort tritt kein HC auf; „HC stört a = b“ ist die Lesart des Autors aus dem Gedankenexperiment.
- **Referenzwahl:** r14.2 (Grundzustand von H = −(aQ + bR), K = ⅔ genau bei a = b), r14.3 (keine Quelle für a = b; (d) a, b als
  Frame-Gewichte = Photon-Gewicht), r14.5 (Biegung bei festem Überlapp ½), r14.4 (entgegengesetzte Orientierung auf Leptonen und Quarks).
- **HC:** `v470/07_qam_infrastructure.tex` (ass:v3360-r16-hc-activation-first-boundary: HC = Heisenberg-Kompensator am ersten
  Randshift), `v470/10_sphaera_and_physics.tex` (Kompensatorstrom J^(HC)).
- **Drehsinn bisher:** `licht_vermittler_zeit_2026_11_24/` (k247–k249: überall gesetzt; τ_T = −τ_M über das Lichtsignal),
  H123 (Oktantvorzeichen = τε), `hopf_gap_2026_11_23/` (k245, gerade Größe), Holonomie k246 (Projektdateien).
- Zurückgestellte Ideen I1–I7: kein Auslöser trifft neu zu (I1 bereits mit H123 vorgelegt).

## 1. Am Photonpunkt kann der HC a = b unitär nicht stören
Bei P ist ρ = I/2 (a = b, c = 0). Jede unitäre Abbildung lässt I/2 fest (k250: U(I/2)U† − I/2 = 0). Eine vom HC erzeugte Dynamik
(Generator ∝ iε = −σ_y) bewegt ρ nur, wenn schon Kohärenz c = ⟨σ_x⟩ ≠ 0 da ist; dann ist d(a − b)/dt ∝ κ·c und das Vorzeichen hängt am
Vorzeichen von κ·c. Von P weg führt nur eine nicht-unitäre Abbildung (Dämpfung, Messung), und deren Richtung legt fest, welcher Pol anzieht.

## 2. a − b ist unter Orientierungsumkehr gerade
a und b sind Diagonaleinträge (⟨σ_z⟩). Komplexe Konjugation (z ↦ z̄, ω ↦ ω²) lässt sie fest. Ein Umlaufsinn ist darunter ungerade.
Eine lineare Kopplung „Drehmoment ∝ (a − b)“ braucht deshalb einen zweiten Faktor, der unter Orientierungsumkehr ungerade ist (ε).
Unter dem Tausch M ↔ T (R = σ_y wie T = σ_z, r81.6(b)) ist a − b dagegen ungerade. Es hat also die Parität von τ, nicht von ε. Das
Produkt ist die Relation τε aus H123. Das Vorzeichen von a − b ist in M per Definition positiv (p₊ − p₋ = 1/γ > 0); es ist das Frame-Etikett.

## 3. Referenzwahl r14.2 mit a ≠ b (k250)
- Grundzustand von −(aQ + bR) ist v = (x, 1, 1) mit x = (3a − b + √(9a² − 6ab + 9b²))/(2b) > 0 für alle a, b > 0 (Perron–Frobenius: −H hat
  nichtnegative Einträge). Er ist reell für jedes Gewichtsverhältnis.
- Bargmann-Invariante des S-Orbits (S = diag(1, ω, ω)): (x² + 2ω)³. Für reelles x ist Im(x² + 2ω) = √3 > 0, die Phase 3·arg(x² + 2ω)
  hat also für **alle** a, b dasselbe Vorzeichen. Mit dem konjugierten S = diag(1, ω², ω²) ist Im = −√3: das Vorzeichen kommt allein aus ω.
- Überlapp |⟨v|Sv⟩|²/|v|⁴ = (x⁴ − 2x² + 4)/(x² + 2)²; er ist ½ (K = ⅔) nur bei x = 1 ± √3. x = 1 + √3 ist a = b; x = √3 − 1 < 1 liegt
  außerhalb des Bereichs x ∈ (1, ∞). **K = ⅔ verlangt in diesem Modell a = b.**

Lesart: a ≠ b ist in der Sprache des Gedankenexperiments eine *gerade* Störung (Betrag und Kammhöhe), wie die Hopf-Lücke.

## 4. Drei-Mulden-Ring
Eine statische Störung ist auf dem Ring periodisch, ∮ τ dθ = 0; sie kann kein Netto-Drehmoment geben. Ein Drehsinn aus einer statischen
Asymmetrie geht nur als Ratsche: spiegelasymmetrisches V(θ) plus Rauschen außerhalb des Gleichgewichts (HS(0)-Feld). Die Richtung folgt
dann aus der Spiegelasymmetrie von V, also wieder aus einer orientierungsungeraden Eingabe. (Lesart aus Standardphysik, nicht gerechnet.)

## Bilanz der Setzungen (nach k245–k250 zur selben Frage)
| Schritt | gesetzt | hergeleitet | offene Wahl danach |
|---|---|---|---|
| H123 | Vorzeichen des Oktantschritts | = τε | τ und ε |
| k247 | Auslese durch ein Lichtsignal | τ_T = −τ_M, τ in M frame-fest | ε |
| k249 | Vorzeichen von γ in c = −1 + iγ | Einfang übernimmt den Drehsinn | Vorzeichen von γ |
| k245 | – | Hopf-Lücke ist gerade | Drehsinn |
| k246 | γ_M als Kopplung | Randzyklus gibt −π | Umlaufsinn des Zyklus |
| k250 | – | a − b gerade unter ω ↦ ω², ungerade unter M ↔ T | ε = Wahl von i bzw. ω |

Prüfung nach AGENTS.md: Das Ziel „Drehsinn“ ist im Bestand eine gesetzte Eingabe. Über ℂ ist die Wahl von i eine Konvention
(komplexe Konjugation ist ein Automorphismus); ein absoluter Drehsinn ist nur gegenüber einer anderen orientierten Größe messbar.
Die Frage entsteht in der Zerlegung „Drehsinn absolut“. In der Zerlegung „Drehsinn relativ zu einer zweiten Orientierung“ wäre sie
prüfbar. Kandidat im Bestand: r14.4 (entgegengesetzte Orientierung der linken ℍ-Wirkung auf Leptonen und Quarks).

## 5. Was blind bleibt
- Der **Betrag**: Bargmann-Phase und K bei Matter-Gewichten b/a = (γ_L − 1)/(γ_L + 1). In k250 nicht eingesetzt. Bekannt ist vorab nur,
  dass K ≠ ⅔ wird (Abschnitt 3).
- Ein **relatives Vorzeichen**: ob die Struktur den Umlaufsinn der Leptonen gegen den der Quarks (r14.4) oder gegen die schwache
  Chiralität festlegt.

## Grenzen
- Erkundung, nicht blind. Abschnitt 4 ist Lesart aus Standardphysik.
- Das Modell für „a, b im Dreier-Raum“ ist die Referenzwahl r14.2 (dort a, b als Frame-Gewichte gelesen, r14.3(d)); eine andere Einbettung
  von a, b in die drei Sektoren ist nicht geprüft. Für jede reelle, diagonale Einbettung gilt Abschnitt 2.
- OP1, OP3, OP5, Q1a offen; kein Guard berührt.

## Dateien
`k250_drehsinn_lichtgewicht.wl` (Ausgabe `k250_out.txt`).
