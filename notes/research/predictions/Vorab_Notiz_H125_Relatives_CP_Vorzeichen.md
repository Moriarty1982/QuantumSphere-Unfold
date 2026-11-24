# Vorab-Notiz H125: Relatives Vorzeichen der CP-Verletzung zwischen Leptonen und Quarks

**Stand:** 24. November 2026, vor jeder Rechnung und vor jedem Datenabgleich festgelegt. Freigabe des Autors (Chat 24.11., 09:45 UTC): „mach weiter“. Auftrag (Projekt-Thread
„Drehsinn aus Lichtgewicht herleiten“, 24.11.): „pack alles rein“ auf die Frage, ob H125 zum relativen Vorzeichen zwischen Leptonen und Quarks
entworfen werden soll. Anlass: k250 (`../drehsinn_lichtgewicht_2026_11_24/`) zeigt, dass ein *absoluter* Drehsinn über ℂ eine Konvention ist
(Wahl von i bzw. ω). Ein *relativer* Drehsinn zweier Sektoren ist dagegen messbar. **Nummer:** H125 (gegen das Repo geprüft, frei).

**Blindheit, offen gesagt:** Stufe A ist eine Strukturrechnung, deren Ausgang ich vorab erwarte (siehe Erwartung); sie wird als „nicht blind“
geführt. Stufe B ist blind nur gegen **künftige** Daten. Die heutige Datenlage ist bekannt und wird hier vorab genannt: J_CKM > 0
(δ_CKM ≈ 66°); für die Leptonen liegt der NuFIT-Bestwert bei normaler Ordnung bei δ_CP ≈ 200°–220° (sin δ < 0), CP-Erhaltung (180°) ist
aber nicht ausgeschlossen. Die heutige Tendenz zeigt also schon auf „entgegengesetzt“, entscheidet aber nichts.

## Vorwissen geprüft
- **Orientierung der Sektoren:** r14.4 und `../op3_cs_dixon_map_2026_11_15/README.md` (Familien-su(2) von C⊗S landet bei der Linkswirkung von H,
  dem Lorentz-Spin aus r33.2: auf den Leptonen nur mit det −1 (24 Zuordnungen), auf den Quarks nur mit det +1 (24 Zuordnungen); eine einzige
  Abbildung für beide Sektoren gibt es nicht). Steht unter CT-003; die Lorentz-Lesart ist in r33.2 eine Lesart.
  `../op3_family_su2_right_action_2026_11_14.md` (dieselbe Gegenläufigkeit als su(2)_L ⊕ su(2)_Q).
- **Brannen-Phasen:** H1 (`../v4_8_0_r03_r12/llm/Ergebnis_H1_Koide_Phase.md`): δ in allen drei Gruppen in (0, π/3) bei aufsteigender
  Massenordnung. Das trägt keine Orientierungsinformation: Bei Zuordnung der Slots nach der Masse ist die Hälfte von δ mod 2π/3 durch die
  Ordnung selbst festgelegt. Deshalb ist die Brannen-Phase **kein** Prüfstein für H125.
- **CP-Phase im Bestand:** H8 (Cayley–Dickson-Involution: δ_CP ∈ {90°, 270°}, beide Vorzeichen strukturell erlaubt, die Daten wählten 270°),
  H43 (TM2-Lesart legt δ nicht fest), H5 (Hopf-Mischwinkel). Das Vorzeichen von δ_PMNS ist im Bestand nirgends hergeleitet, das relative
  Vorzeichen zu J_CKM nirgends gestellt.
- **Drehsinn:** H123 (Oktantvorzeichen = τε), k247 (τ_T = −τ_M), k249, k250 (a − b gerade unter ω ↦ ω²; offene Wahl = ε).
- **OP4 (#11):** H46, H100 offen; nicht berührt.
- Zurückgestellte Ideen I1–I7: kein Auslöser trifft zu.

## Rückwärtssuche (vor der Notiz, ohne Rechnung)
Ziel: ein Vorzeichen, das die Struktur festlegt und das nicht durch Umbenennung (i ↦ −i, Slotreihenfolge) verschwindet. Notwendig:
(1) eine Größe, die unter komplexer Konjugation ungerade ist; (2) die Größe ist in beiden Sektoren gleich gebaut; (3) die Konjugation eines
Sektors relativ zum anderen ist strukturell festgelegt. Kandidat für (1): die Jarlskog-Invariante, ein Bargmann-Quartett der Mischmatrix,
Im(V_us V_cb V_ub* V_cs*) bzw. Im(U_e1 U_μ2 U_e2* U_μ1*), konventionsfrei bei Ordnung der Generationen nach der Masse. Kandidat für (3):
r14.4. Eine Abbildung mit det −1 kehrt das Vorzeichen der Strukturkonstanten um, [J_a, J_b] = iε_abc J_c ↦ −iε_abc J_c; das ist die
Kommutatorrelation des komplex konjugierten Dubletts. Lücke: (2) ist nicht hergeleitet (siehe Setzung S1).

## Modell und Setzungen (festgelegt)
- **S1 (Setzung):** In beiden Sektoren entsteht die CP-Phase auf dieselbe Weise aus der Familienstruktur, also als dieselbe Funktion der
  Familien-su(2) relativ zum Lorentz-Spin. Dann ist die CP-Phase der Leptonen die komplex Konjugierte der der Quarks, und
  sign(J_PMNS) = −sign(J_CKM).
- **S2 (Setzung):** CT-003 und die Lorentz-Lesart von r33.2 gelten.
- Nicht gesetzt und nicht berührt: Betrag von J, Massenordnung der Neutrinos (Stufe B wertet beide Ordnungen getrennt aus).

## Stufe A: Strukturprüfung (nicht blind, Wolfram exakt)
Skript `k252_h125_orientierung.wl` im neuen Ordner `../h125_relatives_cp_2026_11_24/`:
1. Aus `op3_cs_dixon_map_2026_11_15/chirality_check.py` bzw. `search.py` je eine Lösung für Leptonen (det −1) und Quarks (det +1) übernehmen.
2. Prüfen, ob die übertragene Familien-su(2) auf dem Leptonblock die Kommutatorrelation mit umgekehrtem Vorzeichen relativ zur Linkswirkung
   trägt (A1) und ob es eine antiunitäre Abbildung Θ (komplexe Konjugation mal unitär) gibt, die den Leptonblock auf den Quarkblock abbildet
   und dabei die Familienoperatoren erhält (A2).
3. Für ein Testtripel/Testquartett von Zuständen die Bargmann-Invariante in beiden Blöcken berechnen und prüfen, ob Im das Vorzeichen wechselt
   (A3), über alle 24 + 24 Zuordnungen.

**Erwartung:** A1–A3 bestätigt. **Abbruch:** Ist A1 oder A3 auch nur für eine Zuordnung verletzt, gibt die Struktur kein festes relatives
Vorzeichen; H125 gilt dann als „trägt nicht“, Stufe B entfällt, Ergebnis als Erkundung.

## Stufe B: Datenvergleich (blind gegen künftige Daten)
**Vorhersage:** sign(J_PMNS) = −sign(J_CKM), also sin δ_PMNS < 0 bei δ_CKM ∈ (0°, 180°), Standardparametrisierung (PDG), Generationen nach
der Masse geordnet.

**Daten:** die erste globale Analyse nach diesem Commit, die das Vorzeichen von sin δ_PMNS auf mindestens 3σ festlegt (NuFIT oder eine
gleichwertige globale Analyse; einzelne Experimente wie DUNE oder Hyper-Kamiokande zählen, wenn sie für sich 3σ erreichen). Für die
Massenordnung gilt die von derselben Analyse bevorzugte; ist die Ordnung offen, muss das Vorzeichen in beiden Ordnungen gleich ausfallen.

**Kriterium:**
- **Bestätigt:** sin δ_PMNS ≥ 0 auf ≥ 3σ ausgeschlossen.
- **Widerlegt:** sin δ_PMNS ≤ 0 auf ≥ 3σ ausgeschlossen, oder CP-Erhaltung (sin δ = 0) als Bestwert mit sin δ < 0 auf ≥ 3σ ausgeschlossen.
- **Offen:** bis 31.12.2035; danach ohne 3σ-Entscheidung „entfällt“.

**Gewicht, offen gesagt:** Ein einzelnes Vorzeichen hat eine Grundwahrscheinlichkeit von ½. Eine Bestätigung wäre ein schwacher Beleg und
zeigte vor allem, dass S1 tragfähig ist; eine Widerlegung träfe S1 oder die Lesart von r14.4.

## Nachträglich erlaubt (als Erkundung, nicht Teil des Tests)
- Ob S1 aus einer Wirkung folgt (W1/W2, Yukawa-Konnektoren r44.1(b)).
- Ob dieselbe Gegenläufigkeit für die Majorana-Phasen etwas sagt.

## Grenzen
- Steht unter CT-003 und erbt dessen Guards; r14.4 gilt für zwei Generationen (Dublett), die dritte ist nicht erfasst.
- S1 ist die eigentliche Brücke und ist gesetzt. Kein Guard wird durch H125 berührt; OP3, OP4 bleiben offen.
