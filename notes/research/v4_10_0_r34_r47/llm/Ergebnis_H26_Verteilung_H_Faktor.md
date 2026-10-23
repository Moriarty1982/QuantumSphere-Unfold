# Ergebnis H26: Mit Lorentz links, schwacher SU(2) rechts und Generationen auf der Triality ist ℍ nicht mehr überbelegt; das Ladungsmuster der Dubletts entsteht, die Singuletts fehlen

Vorab-Notiz: `Vorab_Notiz_H26_Verteilung_H_Faktor.md`, Commit 1876b55 (2026-10-23 20:01 MESZ), vor der Rechnung. Die Muster von H26b und
H26c waren dort **vorab analytisch offengelegt**; die Rechnung prüft sie an den Matrizen und ist kein Vorhersagetest. Skript
`k82_test_h26.py`, Ausgabe `k82_out.txt`.

## Aufteilung D

Lorentz SL(2,ℂ) von links auf ℂ⊗ℍ, schwache SU(2) von rechts auf ℍ (T₃ = −(i/2)R_k), Farbe auf 𝕆, Frames auf ℂ, Generationen auf den
Triality-Plätzen. Hyperladung Y/2 := Q − ½, elektrische Ladung Q_em := T₃ + Y/2.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H26a Verträglichkeit | **bestätigt** | Schwache SU(2) vertauscht mit Lorentz, Farbe, Q; Lorentz-Drehungen unter T fest, Boosts von T umgekehrt |
| H26b Ladungsmuster | **bestätigt** | siehe Tabelle |
| H26c Frame = Ladungskonjugation | **bestätigt** | T Q_em T⁻¹ = −Q_em, T (Y/2) T⁻¹ = −Y/2 |
| H26d keine Singuletts | **bestätigt** (negativ für D) | Kein schwaches Singulett; T² = 3/4 auf dem ganzen Raum |
| H26e Generationen auf den Plätzen | **bestätigt** | Die Generationen-ℤ₃ vertauscht mit L_q, R_q, Farbe und Q |

| Q-Sektor (Farbe) | Y/2 | T₃ = +½ | T₃ = −½ | Lesart |
|---|---|---|---|---|
| 0 (Singulett) | −1/2 | 0 | −1 | Lepton-Dublett (ν, e) |
| 2/3 (Triplett) | +1/6 | 2/3 | −1/3 | Quark-Dublett (u, d) |
| 1/3 (konj. Triplett) | −1/6 | 1/3 | −2/3 | Antiquark-Dublett (d̄, ū) |
| 1 (Singulett) | +1/2 | 1 | 0 | Antilepton-Dublett (e⁺, ν̄) |

## Einordnung

1. **Die Überbelegung des ℍ-Faktors ist in D aufgehoben**, durch die Seiten und durch das Auslagern der Generationen:
   - Lorentz sitzt links (vorne), die schwache SU(2) rechts (hinten), die Generationen auf den Triality-Plätzen.
   - Alle Rollen vertauschen dort, wo sie es müssen.
   - Die Zoomstufen trennen dabei nur Frames von Generationen, nicht Lorentz von der schwachen SU(2); das tun die Seiten.
2. **Test 4 der Bestandsaufnahme ist in D positiv, unter einer Wahl.** Mit Y/2 = Q − ½ ergibt Q_em = T₃ + Y/2 genau die Hyperladungen
   und Ladungen der linkshändigen Dubletts des Standardmodells und ihrer Konjugierten, mit der richtigen Farbe:
   - Leptonen sind Singuletts, Quarks Tripletts, Antiquarks konjugierte Tripletts.
   - Die Wahl Y/2 = Q − ½ ist durch das Muster motiviert, nicht von der Struktur erzwungen.
   - Die Zuordnung der Sektoren ist die von Furey; vergleichbare Muster kennt die Literatur zu ℂ⊗ℍ⊗𝕆. Neu ist hier die Einbettung in
     die Seiten und Frames des Companion.
3. **Der Frame-Wechsel T ist in D genau die Ladungskonjugation C.** Das klärt H19d: Dort war Q ↦ 1 − Q „Ladungskonjugation mit
   Verschiebung“. Die Verschiebung ist genau der Hyperladungs-Versatz ½. Auf Q_em wirkt T als reines Q_em ↦ −Q_em. Materie- und
   Tachyon-Frame verhalten sich in D also wie Teilchen und Antiteilchen.
4. **D ist unvollständig:**
   - Jeder Zustand ist ein schwaches Dublett. Die rechtshändigen Singuletts u_R, d_R, e_R, ν_R fehlen, also die Hälfte der Fermionen
     einer Generation.
   - Alle Zustände tragen denselben Lorentz-Index von links. Die Chiralität, also dass die schwache SU(2) nur auf linkshändige Teilchen
     wirkt, ist damit nicht erklärt.
   - Um die Singuletts zu bekommen, müsste die schwache SU(2) auf einem Teil des Raums trivial wirken. Das verlangt eine Struktur, die
     ℍ von rechts allein nicht hat, etwa einen Projektor, der links und rechts koppelt.
