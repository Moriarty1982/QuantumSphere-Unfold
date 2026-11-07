# Annahmenliste des Companion

**7. November 2026. Status: Bestandsaufnahme, keine Rechnung, keine Hypothese.** Anlass: Arbeitsweise aus Dorau–Much (v4.10.0-r06/r07):
wenige, offen gesetzte, unabhängig begründete Annahmen; Ergebnisse als bedingte Sätze; die Buchführung (QAM) zeigt, worauf jedes Ergebnis ruht.
Diese Liste wird fortgeschrieben; neue Annahmen kommen mit Datum und Herkunft dazu.

## Kategorien
- **V** – vorher gesetzt, mit eigenem Grund (vor Kenntnis der Folgen).
- **R** – nachher gesetzt: Auswahl oder Reparatur, nachdem eine Folge bekannt war oder nicht passte.
- **K** – Korrektur eines Fehlers (Rechen- oder Vorzeichenfehler); keine Wahl.
- **A** – Arbeitsannahme, ausdrücklich vorläufig.
- **L** – Eingabe aus der Literatur.
- **S** – stillschweigend vorausgesetzt, bisher nirgends festgelegt.

R ist kein Makel, aber eine Vorhersage, die auf R ruht, ist um diese Auswahl weniger blind.

## A. Die Kette zur offenen Vorhersage H96 (Ω_M = β² = 0,30185)

| Kürzel | Annahme | Herkunft | Kat. |
|---|---|---|---|
| L1 | γ_BI = 0,237533 (U(1)-Zählung aller Spins, Domagała–Lewandowski/Meissner) | Literatur; kalibriert auf S = A/4 (r07.4) | L |
| L2 | γ_string = ln 2/(π√3) (nur j = ½, Ashtekar–Baez–Corichi–Krasnov, überholt) | Literatur; kalibriert auf S = A/4 | L |
| Z1 | M zählt alle Spins, T nur j = ½; U(1)- statt SU(2)-Behandlung | r63/H47 (nicht blind), r68: die Literatur bevorzugt SU(2), das Leptonfenster wählt U(1) | R |
| F1 | γ_L = γ_BI/γ_string ist der Lorentzfaktor des Frame-Versatzes T → M | thm:frame-offset; r16 „frame-offset strukturell“ (Autor); v4.8.0-r03 F11: Verhältnis zweier Bestimmungen desselben Parameters | A |
| F2 | β_sym = tanh(η/2) mit cosh η = γ_L, also β² = (γ_L − 1)/(γ_L + 1) | Kern (T6, OP1: eingesetzt, nicht hergeleitet) | A |
| K1 | Ω_M = β² als Verzweigung der Kaskade | thm:dark-energy; r31 (stationäre Flussanteile β², 1 − β²); r67 (Vertauschung Λ/Ω_M korrigiert) | A, mit K |
| E1 | Epoche der Auslesung: heute | Autor 6.11.; Werte um 0,30 waren bekannt (H96-Offenlegung); v4.8.0-r17 Ausweg (a) | R |

**QAM-Prüfung** (`llm/qam_annahmen_H96.tex`, Export `.qam`; mit `qam.sty` ohne Meldung):
- `OmegaM`: Status **reading**, Frame M, Eingaben {gBI, gstr, countrule, epoch}.
- Die schwächste Prämisse ist eine Lesart; nach der Statusregel kann Ω_M = β² nicht höher stehen als „Lesart“, bis F1, F2, K1 hergeleitet sind.
- Gegenprobe: γ_L ohne die erklärte Abbildung T → M gebildet meldet die QAM als Frame-Vermischung (`gstr` in T, `gBI` in M). γ_L ist also
  nur über F1 definiert; die Abbildung, die es misst, ist zugleich die Lesart, die es begründet.

**Bilanz H96:** Die Vorhersage hat keinen freien Parameter, ruht aber auf zwei R-Annahmen (Z1, E1) und drei Lesarten (F1, F2, K1). Sie ist gegen
die künftigen Daten blind (DESI DR3, Euclid), die Wahl ihrer Bestandteile war es nicht ganz. Unabhängig vom Programm W1/W2: keine Annahme aus
Abschnitt C geht ein.

## B. Strukturannahmen des Kerns

| Kürzel | Annahme | Herkunft | Kat. |
|---|---|---|---|
| B | Lesart B: z = E + iB in ℂ³, Lorentzgruppe SO(3,ℂ), s = z·z | v4.8.0 (Arbeitslesart) | A |
| F | Konvention F: Frames M, T (Bild unter z ↦ iz), P (Fixpunkt) | v4.9.0-r22, korrigiert r28; eingeführt, um Widersprüche des Hauptkorpus als Ein-Frame-Artefakte aufzulösen (r24) | V/R |
| F7 | komplexe Einheiten nennen (innen J = L_{e₇}, außen i) | r36 (Autor) | V |
| D | Dixon-Ablage ℂ⊗ℍ⊗𝕆 als Register | r33 (Autorabsicht) | V |

## C. Dynamik-Programm W1/W2 (seit v4.10.0-r05 eingefroren)

| Kürzel | Annahme | Herkunft | Kat. |
|---|---|---|---|
| W-E1…E5 | Koframe eigenes Feld; reelle Wirkung R, K parallel; Einstein–Cartan ohne Λ; Dixon mit U(1)_J; P_C7 := C_ch | Bestandsaufnahme, 4.11., „vor jeder Rechnung“ | V (E5: Wahl, nicht hergeleitet) |
| W-sign | Gravitationswirkung −(1/2κ)∫e R | 6.11., nach H90 (Abstoßung) | K |
| W-L2 | T-Anteil = dasselbe Feld in zweiter Lesart | 5.11., nach H76 (Vakuumzerfall bei eigenem T-Feld) | R |
| W-hol | holomorphe Adjungierte (Bildterm −L_M) | 5.11. („wenn es nicht passt, suchen wir was anderes“) | A |
| W-F3 | F3-Gewicht 1 der Weyl-Kinetik | 5.11. | A |
| G2 | M nach, T vor dem Urknall | 5.11., nach H84 (Quantenmoden bei τ* singulär) | R |
| Δ | Dauer des Übergangs Δ ≲ ℓ_P | 6.11., nach H94 (Norm nur außerhalb k ~ 1/Δ erhalten) | R |
| Pg | Gravitation trägt Photon-Gewichte am Übergang | 6.11., nach ΔN_eff ≈ 3,6; Begründung im Nachtrag nur teilweise tragfähig | R |
| U | **gleiches Gewicht a für alle nicht-gravitativen Felder nach dem Urknall** | nirgends festgelegt; nötig für ein universelles G (aktive = passive Masse); `Erkundung_Quelle_Gravitation_Gewichte.md` | S |

## D. Gravitation (v4.10.0-r06/r07)

| Kürzel | Annahme | Herkunft | Kat. |
|---|---|---|---|
| DM1 | lokal flach, führende Ordnung | Dorau–Much | L |
| DM2 | Flächengesetz S = δA/4 | Bekenstein–Hawking, bei Dorau–Much gesetzt | L |
| — | Einstein-Gleichung in M und T (Maxwell) | r07.2: hergeleitet aus DM1, DM2 und Dualitätssymmetrie | Ergebnis, conditional |

## Beobachtungen
1. Abschnitt C hat sieben R/A-Einträge in zwei Tagen; das ist die „Reparatur-Serie“ aus der Rückschau v4.10.0-r05.2. Sie ist eingefroren und berührt
   H96 nicht.
2. H96 hängt an den Lesarten F1, F2, K1. Wer H96 stärken will, muss eine davon herleiten, nicht eine neue Zahl finden. Nach r07.4 kann F1
   nur ein Verhältnis liefern; das ist für Ω_M ausreichend (dimensionslos), für G nicht.
3. Neu sichtbar: Annahme U war stillschweigend. Sie ist plausibel (sonst Verletzung des Äquivalenzprinzips), muss aber ausgesprochen werden.
4. Nächster Ausbau: H15 (m_W), H42/H46 (θ₂₃) in derselben Form; dann ist für jede offene Vorhersage sichtbar, worauf sie ruht.
