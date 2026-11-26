# Vorab-Notiz H162: Bestehen Weg A und das relative CP-Vorzeichen auf der Ladungsrichtung e₇?

**26.11.2026, vor der Rechnung.** Auftrag des Autors vom 26.11. („alles Offene rechnen“); offener Punkt aus r64.2.
Einordnung: T5/T8, OP3/OP4. Skript **k360** (`notes/research/hilbert_shift_felder_2026_11_24/ladungsachse_h162/`).
**Weitgehend nicht blind:** Die Teile a, b und d lassen sich vor der Rechnung von Hand begründen (unten). Offen sind c und e.

## Anlass
- r13.1 setzt die Ladungsachse e₈ (Platzhalter CT-003), weil e₈ die einzige ψ-feste imaginäre Richtung ist.
  Daran hängen Weg A (zwei Generationen, r13.3), die Familien-su(2) (r13.4, r14.4) und H125 Stufe A (r59.6).
- H130 (r64.2): Oktonionische, farbstabile Träger gibt es in 𝕊 nur mit Ladungsrichtung senkrecht zu e₈ (e₇ und die
  beiden um 120° gedrehten Richtungen). CT-003 wird davon nicht gestützt.
- Frage: Was bleibt von den drei Aussagen, wenn die Achse e₇ ist?

## Vorwissen geprüft
- r12.4(c), r13.1: Die geerbte Ladung Q_S = ½ − (i/6)L_e7 − (i/3)R_e7 hat auf ℂ⊗𝕊 keinen neutralen Träger; ψ verschiebt ihre Achse.
  H103a widerlegt. `op3_sedenion_charge_2026_11_13.md`: Q_* = P₀(½ − (i/2)L_e8)P₀ + ⅔P₃ + ⅓P₃̄.
- r13.3, `op3_sedenion_generations_estar_2026_11_14.md`: unter Q_* zwei vollständige Generationen.
- r13.4, `op3_family_su2_right_action_2026_11_14.py`: R_e7, R_e8, R_e15 vertauschen mit su(3)_c und Q_*; Orientierung auf dem
  neutralen und dem farbigen Teil entgegengesetzt.
- r59.6, k252 (`h125_relatives_cp_2026_11_24/`): Bargmann-Invariante ¼ − i/4 (Leptonen) gegen ¼ + i/4 (Quarks), 24 + 24 Zuordnungen.
- H128, H130 (r64.1, r64.2), H140, H141 (r62.3, r62.4): je Kopie eine Generation, keine gemeinsame Ladung, 15 von 24 Zuständen.
- Suche nach „Q_u“, „Achse e7“, „e_7-Ladung“ unter `notes/research`, `wiki`: Die Form von Q_* mit der Achse e₇ ist nicht gerechnet.

## Aufbau
Für eine Einheit u ∈ span(e₇, e₈, e₁₅) sei **Q_u = P₀(½ − (i/2)L_u)P₀ + ⅔P₃ + ⅓P₃̄** (die Form von Q_*, Q_* = Q_{e8}).
P₀ projiziert auf H_n = span(1, e₇, e₈, e₁₅), P₃ und P₃̄ auf die Farb-Tripletts und -Antitripletts (wie in `fs.setup()`).
Geprüft werden u = e₇ (Hauptfall), u = −½e₇ ± (√3/2)e₁₅, u = e₈ (Kontrolle) und 200 zufällige Einheiten.

**Überlegung von Hand (deshalb nicht blind):** H_n ist assoziativ, also ist L_u² = −1 auf H_n und Q_u hat dort für jedes u die
Eigenwerte 0 und 1 je zweimal. Der farbige Teil von Q_u hängt nicht von u ab. Rechtsmultiplikationen vertauschen auf H_n mit L_u.
Erwartet wird deshalb, dass a und b für jedes u gelten und die Achse nur über [Q, ψ] = 0 ausgezeichnet ist.

## Vorhersagen und Kriterien
| Teil | Vorhersage | Kriterium |
|---|---|---|
| **H162a** (Weg A) | Q_{e7} hat das Spektrum 0 (2), ⅓ (6), ⅔ (6), 1 (2), vertauscht mit su(3)_c und erfüllt Q̄ = 1 − Q: zwei vollständige Generationen | bestätigt, wenn alle drei Reste < 10⁻¹⁰; sonst widerlegt |
| **H162b** (Familien-su(2), Orientierung) | R_e7, R_e8, R_e15 vertauschen mit Q_{e7}; [R_e7, R_e8] = −2R_e15 auf dem Leptonblock, +2R_e15 auf dem farbigen; Bargmann ¼ − i/4 gegen ¼ + i/4; ebenso für alle 200 Zufallsachsen | bestätigt, wenn Kommutatoren < 10⁻¹⁰ und die Bargmann-Werte auf 10⁻¹⁰ stimmen; sonst widerlegt |
| **H162c** (Zuordnungen zur Dixon-Seite, wie k252 A3) | Mit Q_{e7} statt Q_* gibt es wieder 24 Zuordnungen vollen Rangs je Sektor, alle mit det −1 (Leptonen) und +1 (Quarks) | bestätigt bei 24/24 mit diesen Vorzeichen; widerlegt bei anderer Anzahl oder gemischten Vorzeichen. **Offen** (die Verflechtung mit Q_em ist nicht von Hand geprüft) |
| **H162d** (Verträglichkeit mit der Kopie) | Q_{e7} lässt ℂ⊗𝕆₀ (𝕆₀ = span(e₀…e₇)) invariant und ist dort gleich Q₈ = Q_S\|_𝕆 (eine Generation); Q_* nicht. Auf den Kopien 𝕆₁₂₀, 𝕆₂₄₀ leckt Q_{e7} | bestätigt, wenn Rest < 10⁻¹⁰ auf 𝕆₀ und Leck > 10⁻³ für Q_* und auf den anderen Kopien |
| **H162e** (was verloren geht; ohne Kriterium, Erkundung) | [Q_{e7}, ψ] ≠ 0; ψ bildet den neutralen Kern N₇ = ker Q_{e7} nicht in sich ab; die Konstruktion aus r13.2 (ρ² = ½) braucht statt ψ eine andere Ordnung-3-Abbildung | Messwerte angeben |

## Was das Ergebnis bedeuten würde
- a, b, c bestätigt: Weg A und H125 Stufe A hängen nicht an der Wahl e₈, sondern nur an der Form der Ladung; „bedingt unter CT-003“
  wäre zu „bedingt unter der Form Q_u“ abzuschwächen. Die Zahl der Generationen bliebe zwei, also weiter nicht drei.
- d bestätigt: Die Achse e₇ ist die einzige, bei der die Sedenionen-Ladung die oktonionische Ladung einer Kopie fortsetzt.
- Eine Vorhersage gegen Messdaten entsteht in keinem Fall. H125 Stufe B (sin δ_PMNS < 0) bleibt offen bis 2035.

## Werkzeuge
Python (numpy) auf der vorhandenen Infrastruktur (`op3_family_su2_right_action_2026_11_14.py`, `op3_cs_dixon_map_2026_11_15/search.py`).
Wolfram Language exakt für a, b und d (unabhängig aufgebaute Sedenionentafel). Qiskit nicht geeignet (keine Schaltung, kein Messablauf).
Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf). Guards unberührt.
