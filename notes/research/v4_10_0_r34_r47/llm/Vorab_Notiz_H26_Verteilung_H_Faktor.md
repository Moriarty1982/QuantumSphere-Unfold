# Vorab-Notiz H26: Verteilung der Rollen des ℍ-Faktors, Hyperladung und elektrische Ladung

Festgelegt am 2026-10-23, **vor** der Rechnung. Bezug: Bestandsaufnahme K79.2 (ℍ dreifach belegt: Lorentz, schwache SU(2),
Generationen), Test 4 (Hyperladung, Q = T₃ + Y/2), H19/H20 (Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}, T Q T⁻¹ = 1 − Q), H22/r37 (Generationen auf den
Triality-Plätzen), H24/r39 (Frames grob, Generationen tief), H25/r40 (keine farbverträgliche SU(2) in der Triality; im ℍ-Faktor zwei,
links und rechts). Autor: „Versuch es mal“.

## Aufteilung D (Vorschlag, zu prüfen)

| Rolle | Träger | Seite / Ebene |
|---|---|---|
| Lorentz SL(2,ℂ) | L_q (Drehungen) und i·L_q (Boosts) auf ℂ⊗ℍ | vorne (links) |
| schwache SU(2) | R_q auf ℍ, T₃ := −(i/2)·R_k (i = äußere Einheit) | hinten (rechts) |
| Farbe SU(3)_c | Stab(e₇) auf 𝕆 | hinten |
| Frames D₄ | T, R, J_B auf ℂ | vorne, grobe Zoomstufe |
| Generationen | Triality-Plätze von 𝕆³ (nicht mehr Im ℍ) | tiefe Zoomstufe |

Hyperladung **Y/2 := Q − ½** (Q aus H19/H20 auf ℂ⊗𝕆), elektrische Ladung **Q_em := T₃ + Y/2**.

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

Aus den Q-Sektoren {0, 1/3, 2/3, 1} folgt Y/2 ∈ {−1/2, −1/6, 1/6, 1/2}, und mit T₃ = ±1/2 ergibt sich Q_em in den Sektoren
0 → {0, −1}, 2/3 → {2/3, −1/3}, 1/3 → {1/3, −2/3}, 1 → {1, 0}. Das ist das Muster der linkshändigen Dubletts (ν, e), (u, d) und
ihrer Konjugierten (d̄, ū), (e⁺, ν̄). Aus T Q T⁻¹ = 1 − Q und der Antilinearität von T folgt T (Y/2) T⁻¹ = −Y/2 und T T₃ T⁻¹ = −T₃.
**Diese Muster sind also nicht vorhergesagt, sondern vorab analytisch gesehen**; die Rechnung prüft sie nur an den Matrizen. Die
Wahl Y/2 = Q − ½ ist durch dieses Muster motiviert, nicht durch die Struktur erzwungen.

## Hypothesen

- **H26a (Verträglichkeit):** Auf W = ℂ⊗ℍ⊗𝕆: Die schwache SU(2) (R_q) vertauscht mit Lorentz (L_q, i·L_q), Farbe, Q und den
  Frame-Drehungen R. Lorentz-Drehungen L_q vertauschen mit ganz D₄; die Boosts i·L_q vertauschen mit R und antivertauschen mit T und J_B
  (T kehrt Boosts um).
- **H26b (Ladungsmuster):** Die gemeinsamen Eigenräume von (Q, T₃, Farbe) geben Q_em = T₃ + Y/2 genau im Muster der Offenlegung; in jedem
  Sektor unterscheiden sich die Dublett-Partner um 1; Farbe: Y/2 = −1/2 und 1/2 Singuletts, 1/6 und −1/6 Tripletts (zueinander konjugiert).
- **H26c (Frame = Ladungskonjugation):** T Q_em T⁻¹ = −Q_em und T (Y/2) T⁻¹ = −Y/2. Der Frame-Wechsel T ist in D die Ladungskonjugation C;
  die Verschiebung „Q ↦ 1 − Q statt −Q“ aus H19d ist genau der Hyperladungs-Versatz ½.
- **H26d (fehlende Singuletts, erwartet negativ):** In D ist jeder Zustand ein Dublett der schwachen SU(2); es gibt **keine** schwachen
  Singuletts (Anzahl 0). Die rechtshändigen Singuletts u_R, d_R, e_R, ν_R des Standardmodells fehlen; D liefert nur die Dublett-Hälfte.
  Chiralität ist damit nicht erklärt.
- **H26e (Überbelegung aufgehoben):** In D trägt ℍ nur Lorentz (links) und die schwache SU(2) (rechts); die Generationen-ℤ₃ liegt auf den
  Plätzen und vertauscht mit beiden und mit der Farbe (auf ℂ⊗ℍ⊗𝕆³ geprüft).

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹). Einordnung vorab:
- H26a, e bestätigt ⇒ Die Überbelegung des ℍ-Faktors ist in D aufgehoben, durch Seiten (links/rechts) und durch das Auslagern der
  Generationen auf die Triality. Die Zoomstufen trennen dabei nur Frames von Generationen, nicht Lorentz von schwacher SU(2).
- H26b, c bestätigt ⇒ Test 4 der Bestandsaufnahme ist in D **unter der Wahl Y/2 = Q − ½** positiv: Q = T₃ + Y/2 mit dem Muster der
  Dubletts, und der Frame-Wechsel T ist die Ladungskonjugation. Eine Herleitung der Wahl ist es nicht.
- H26d bestätigt ⇒ D ist unvollständig: Die Hälfte der Fermionen (die schwachen Singuletts) fehlt, Chiralität bleibt offen.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
