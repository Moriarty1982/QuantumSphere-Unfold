# OP3: Abbildung C⊗S → C⊗H⊗O über Farbe und Ladung, Lage der Familien-su(2)

15. November 2026, Claude Opus. **Erkundung, nicht blind** (Rückwärtssuche). Auftrag des Autors: „C⊗S ↔ C⊗H⊗O suchen“.
Einordnung T5/T7/T8, OP3. Keine H-Nummer, kein CT-Eintrag, keine Guard-Änderung. Alles hier steht unter dem
Platzhalter CT-003 (Ladungsachse e8 auf den Sedenionen) und erbt dessen Guards.

## Anlass und Ziel

Nachtrag 9 von `../op3_action_balance_search_2026_11_14/README.md`: Dasselbe Quaternionentripel tritt zweimal auf.
- **In r33 (Dixon C⊗H⊗O, Standardladung):** Die Generationen sind die Achsen i, j, k selbst. Es gibt drei, sie sind
  aber nicht ladungsneutral.
- **Unter CT-003 (C⊗S, Ladung über e8):** Die Rechtswirkung von H_n = span(1, e7, e8, e15) ist neutral, trägt aber
  nur zwei Generationen als Dublett.

Gesucht war eine Abbildung zwischen beiden Rahmen und die Lage von H_n relativ zum r33-Faktor H. Bisher fehlte
eine solche Abbildung ganz (`../op3_majorana_vector_n_2026_11_14.md`).

**Notwendige Bedingungen (Rückwärtssuche):** Φ ist linear und injektiv, Φ: C⊗S (16 komplex) → C⊗H⊗O (32 komplex).
- **B1:** Φ vertauscht mit der Farbalgebra su(3)_c. Auf beiden Seiten ist das der Stabilisator von e7 in g2, mit
  derselben Oktonionentafel (geprüft: O ist die erste Hälfte von S).
- **B2:** Φ Q_* = Q_em Φ. Dabei ist Q_* die e8-Ladung (`../op3_sedenion_charge_2026_11_13.md`) und
  Q_em = T3 + Q8 − ½ mit T3 = −(i/2) R_k ⊗ 1 (Konvention k85, `../v4_10_0_r34_r47/llm/k85_test_h29.py`).
- **B3, wahlweise:** Φ R_u = F(u) Φ für die neutrale Familien-su(2) R_e7, R_e8, R_e15
  (`../op3_family_su2_right_action_2026_11_14.md`). Als Ziel F dienen die drei nativen su(2) des H-Faktors, jeweils
  in allen 48 vorzeichenbehafteten Zuordnungen (e7, e8, e15) → (i, j, k):
  - die Linkswirkung (in r33.2 der Lorentz-Spin),
  - die Rechtswirkung (in k85 der schwache Isospin),
  - die Konjugation x ↦ q x q̄ (die Slotdrehung von r33.1(b)).

## Vorwissen geprüft
- **r33** (v490, Zeilen 4601–4730): Generationen in (Im H)⊗O. Der Lorentz-Spinor wirkt von links. Der Konflikt mit
  der Spinorlesart löst sich nur, wenn man die Generationen rechts liest.
- **k85:** Isospin als Rechtswirkung von H, Chiralität C = (1 + i L_e7)/2.
- **Notizen vom 13. und 14.11.:**
  - Sedenionen: Ladung über e8, Generationen unter Q_*, Familien-su(2), Hurwitz-2T.
  - `../op3_hopf_octant_2026_11_13.md`: Der neutrale Dixon-Teil hat die Signatur (2,1).
- Eine Abbildung C⊗S ↔ C⊗H⊗O ist in keiner Notiz gerechnet. QAM-Leseserver in dieser Sitzung nicht verbunden.

## Ergebnis

**1. Ladungsinhalt.** Gezählt nach (Farb-Casimir, Ladung):

| Ladung | 0 | 1 | −1 | 1/3 | 2/3 | −1/3 | −2/3 |
|---|---|---|---|---|---|---|---|
| C⊗S, Q_*: Singulett | 2 | 2 | – | | | | |
| C⊗S, Q_*: Triplett | | | | 6 | 6 | – | – |
| C⊗H⊗O, Q_em: Singulett | 4 | 2 | 2 | | | | |
| C⊗H⊗O, Q_em: Triplett | | | | 6 | 6 | 6 | 6 |

C⊗S ist also {ν, e⁺, u, d̄} zweifach. Auf der Dixon-Seite hat jede dieser Klassen mindestens die Vielfachheit zwei.

**2. Eine farb- und ladungstreue Abbildung gibt es, aber keine eindeutige.** Die Lösungen von B1 und B2 bilden einen
20-dimensionalen Raum (nach Schur 8 + 4 + 4 + 4), und injektive Φ (Rang 16) sind darunter. Die naheliegende
Cayley-Dickson-Einbettung a + b e8 ↦ 1⊗a + u⊗b erhält die Farbe exakt, die Ladung aber nicht (Fehler 0,5 bzw. 1).
Das Bild liegt in keiner Chiralitätshälfte. ν, e⁺ und d̄ liegen in N = 1 − C, u liegt in C. Ganz in C geht höchstens
Rang 8, ganz in N höchstens Rang 10.

**3. Die Familien-su(2) landet beim Lorentz-Spin, nicht bei Isospin oder Generationsslots.**

| Ziel F auf C⊗H⊗O | H_n (Leptonen), Rang | farbig, Rang | gesamt |
|---|---|---|---|
| Linkswirkung von H (Lorentz-Spin) | 4/4 (24 Zuordnungen, alle mit det −1) | 12/12 (24 Zuordnungen, alle mit det +1) | höchstens 12/16 |
| Rechtswirkung (Isospin) | 0 | 0 | 0 |
| Konjugation (r33-Slotdrehung) | 0 | 0 | 0 |

- **Isospin:** Die Rechtswirkung vertauscht nicht mit Q_em, und die Familien-su(2) vertauscht mit Q_*. Deshalb geht
  diese Zuordnung nie.
- **r33-Slotdrehung:** Die Konjugation wirkt auf H als 1 ⊕ 3 (Spin 0 und 1), die Familien-su(2) als Dublett (Spin ½).
  Außerdem vertauscht sie nicht mit Q_em.
- **Lorentz-Spin:** Die Linkswirkung vertauscht mit Q_em. In jedem Ladungsblock ist sie auf der Dixon-Seite die native
  su(2) auf dem zweifachen Vielfachheitsraum. Die Familien-su(2) lässt sich sektorweise darauf abbilden, aber nur mit
  entgegengesetzter Orientierung: auf den Leptonen spiegelnd (det −1), auf den Quarks erhaltend (det +1). Das ist
  dieselbe Gegenläufigkeit wie su(2)_L ⊕ su(2)_Q in der Familien-Notiz. Eine einzige Abbildung, die beide Sektoren
  zugleich trägt, gibt es deshalb nicht.

## Lesart und Einschränkungen

- **Was die zwei Generationen von C⊗S im Dixon-Rahmen sind:** Vergleicht man über Farbe und Ladung, besetzen sie den
  Platz der zwei Spinzustände des Lorentz-Dubletts (Linkswirkung von H). Farbe und Ladung allein können Generation und
  Spin nicht unterscheiden. Die Lesart „zwei Generationen“ unter CT-003 braucht also eine weitere Unterscheidung, die
  hier nicht vorliegt. **Das schwächt Weg A:** Sein Dublett könnte ebenso gut Spin sein.
- **Lage von H_n zum r33-Faktor H:** Es sind verschiedene Wirkungen auf demselben Faktor.
  - H_n entspricht der Linkswirkung (neutral, Spin ½).
  - Das r33-Generationstripel ist der Vektor Im H unter der Konjugation (Spin 1), und diese enthält den geladenen
    Rechtsanteil.

  Damit ist der Rollentausch aus Nachtrag 9 strukturell erklärt. Das neutrale Tripel ist ein Dublett (Spin ½), das
  Generationstripel ein Vektor (Spin 1). Ein Träger, der beides ist, müsste Spin ½ und Spin 1 auf denselben drei
  Achsen vereinen, und das leistet eine einzige su(2) nicht.
- **Einschränkungen:**
  - Die Abbildung ist nicht eindeutig: 20 Dimensionen, ohne Vorschrift über Farbe und Ladung hinaus.
  - Die sektorweise Zuordnung zum Spin folgt im Wesentlichen aus Schur. Nicht trivial sind die Orientierungen und
    der Ausschluss von Isospin und Slotdrehung.
  - Alles steht unter CT-003.
  - Die Lorentz-Lesart der Linkswirkung stammt aus r33.2 und ist dort Lesart.
- **Für das Physik-Paper** (Kandidat für eine spätere Ergänzung, Abschnitt „particles“): Farbe und Ladung trennen
  Generation und Spin nicht; ein Generationsträger braucht eine zusätzliche Unterscheidung.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert. Ideen I1–I5 geprüft: kein Auslöser getroffen.

## Nachweis

```
python notes/research/op3_cs_dixon_map_2026_11_15/search.py
cd notes/research/op3_cs_dixon_map_2026_11_15 && python chirality_check.py
```

- Numerisch, Toleranz 1e-9.
- Ränge sind bei zufälligen Linearkombinationen bestimmt (Seed 1511).
- Ausgaben in `run/search_stdout.txt` und `run/chirality_stdout.txt`.
- Ein erster Lauf löste die Familienbedingung im vollen Raum. Er war zu langsam und wurde abgebrochen; ein Ergebnis
  lag nicht vor.
- Bei der Slotdrehung waren die Generatoren zuerst mit dem Faktor ½ falsch normiert. Der Fehler ist berichtigt, und
  das Ergebnis (Rang 0) ist in beiden Fällen gleich.
