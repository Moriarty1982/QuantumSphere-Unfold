# Ergebnis H201 / k411 — Ist die Chiralität der Quintik eine Grad-Selektion?

**Datum:** 2026-11-27
**Vorab:** `Vorab_H201_Grad_Selektion.md` (committet vor der Rechnung)
**Skripte:** `k411_test_h201.py` (sympy + numpy), `k411b_kontrolle.wl` (Wolfram, unabhängig)
**Ausgaben:** `k411_out.txt`, `k411b_out.txt`
**Freigabe:** Autor „ja bitte" (27.11., 11:26 UTC)

## Verdikt: **nein zur Grad-Selektion** (Kriterium K2)

„Nur der Top-Grad ist chiral" ist **kein Strukturprinzip**. Die Chiralität der Quintik (D ≈ B)
ist eine **gradübergreifende Near-Equality** zwischen einer Grad-4-ungeraden und einer
Grad-5-geraden Kopplung, keine Grad-Ordnung. Der lineare Term ist unabhängig ladungsgespalten
(C ≠ 0 bei 91σ), weder blind noch chiral. Damit bleibt die Quark-Massenquelle offen; die
Quintik-Chiralität ist eine isolierte Koinzidenz.

## (A) Strukturelle Grad-Zerlegung (sympy und Wolfram exakt einig)

Beiträge zu den vier Koeffizienten je Feldgrad, auf dem Vakuum (Tr = 3, Vakuum-Identitäten):

**Ladungsgerade F4-Krümmung v = xⁿ** (→ A: l_k, B: l_k²):

| Grad n | A-Beitrag (l_k) | B-Beitrag (l_k²) |
|---|---|---|
| 3 | −6 | 0 |
| 4 | −24 | 0 |
| 5 | −60 | **−30** |
| 6 | −108 | −234 |

→ gerades l_k (**A**) zuerst bei **Grad 3**; gerades l_k² (**B**) zuerst bei **Grad 5**.

**Ladungsungerade H186-Krümmungen (Grad 4)** (→ C: l_k, D: l_k²):

| Form | C-Beitrag (l_k) | D-Beitrag (l_k²) |
|---|---|---|
| c2 | −1/3 | 0 |
| c4/c5 | 0 | **−1/3** |
| c7/c9 | −1 | +1/6 |
| c11 | −1 | −1/6 |

→ ungerades l_k (**C**) ab c2 (Grad ≤ 4); ungerades l_k² (**D**) ab c4/c5 (**Grad 4**).

**Grad-Karte (erstes Auftreten):** A → Grad 3, C → Grad ≤ 4, **D → Grad 4, B → Grad 5**.

**Kernbefund:** B (gerades l_k²) und D (ungerades l_k²) liegen in **verschiedenen Graden**
(5 bzw. 4). Ein chiraler Term (P_up) verlangt gleiche gerade und ungerade Anteile *desselben*
Operators, also B und D aus **einem** Grad. Da sie aus verschiedenen Graden kommen, kann
„Top-Grad = chiral" keine Grad-Ordnung sein — D = B ist eine Gleichsetzung **über die Grade hinweg**.
(Dass B erst bei Grad 5, D schon bei Grad 4 erscheint, war aus H197 bekannt — nicht blind; neu ist
die Zerlegung des linearen Terms und die Schlussfolgerung für die Grad-Selektion.)

## (B) Fit-Test der sauberen Grad-Selektion (blind)

| Modell | Param | χ² | dof | p |
|---|---|---|---|---|
| (1) C = 0 & D = B (saubere Grad-Selektion) | 2 | **11 206** | 4 | 0 |
| (2) D = B, C frei (= H200-Modell 2) | 3 | 320,7 | 3 | 0 |
| (3) frei A, B, C, D (Referenz) | 4 | 7,91 | 2 | — |

Freier Fit: A = 1,082e-3 ± 2,4e-5, C = −2,224e-3 ± 2,4e-5, B = 3,291e-2, D = 3,320e-2.
**C/A = −2,056; |C|/σ_C = 91** — der lineare Term ist scharf ladungsgespalten, C = 0 bei 91σ
ausgeschlossen. Das saubere Grad-Selektions-Modell (C = 0, D = B) ist mit χ² = 11 206 (Δχ² = 11 199
gegenüber dem freien Fit) katastrophal verworfen.

## Einordnung und Übergang zu Schritt (2)

- Die „Grad-Selektion" aus H200 ist **kein Prinzip**: Chiralität ist nicht „der höchste Grad ist
  chiral". Die l_k²-Chiralität (D ≈ B) setzt eine **Grad-4-ungerade** Kopplung (D) mit einer
  **Grad-5-geraden** (B) gleich — eine Koinzidenz über die Grade hinweg, mit ~0,9 % Rest.
- Der **lineare Term** hat seinen eigenen, unabhängigen ladungsungeraden Anteil (C/A = −2,056),
  ist also weder blind noch chiral. Die beobachtete Struktur ist „ladungsgespaltener linearer Term
  (generisch) + l_k²-Term mit D ≈ B", nicht „blind + chiral nach Grad geordnet".
- **Nachträglich (kein Test):** C/A = −2,056 liegt nahe −2, aber nicht exakt; a_up/a_down =
  (A+C)/(A−C) = −0,345 ≈ −1/3. Beide sind Beobachtungen für eine spätere Idee, nicht gerechnet.
- **Schritt (2) ist damit scharf gestellt:** Der ~0,9-%-Rest D/B − 1 = +0,0085 ist der
  Zahlen-Versatz zwischen der Grad-4-ungeraden Kopplung D und der Grad-5-geraden Kopplung B. Die
  nächste Frage ist, ob dieser Versatz (und evtl. C/A) aus den konkreten Grad-4/Grad-5-Koeffizienten
  der Invarianten folgt oder frei bleibt.

## Werkzeuge, Bereich, Grenzen

- **Werkzeuge:** sympy (symbolische Grad-Zerlegung in e1/e2 bzw. s/pr, Vakuum-Reduktion) + numpy
  (geschachtelte χ²-Fits, Parameter-Kovarianz für σ_C); Wolfram Language als unabhängige Kontrolle
  der Grad-Zerlegung (exakt gleich). Qiskit nicht einschlägig.
- **Geprüfter Bereich:** F4-Krümmung Grad 2–6 (gerade) und die fünf H186-Formen (ungerade, Grad 4);
  Fits am festen M_Z-Datensatz, Zuordnung B, Nenner (l_i+l_j)².
- **Erste/entscheidende Abweichung:** C = 0 bei 91σ ausgeschlossen; B und D aus verschiedenen Graden.
- **Grenzen / offene Voraussetzungen:** die H186-Krümmungen und der Grad-5-Term sind die bekannten
  Bausteine (H186/H197); die Funktionsform (l_k, l_k²) und Zuordnung B sind gesetzt. Der Test
  widerlegt die Grad-Selektion, leitet aber nicht her, warum D ≈ B (das ist Schritt 2).
- Keine symbolischen Nullreste (exakte rationale Koeffizienten), keine Warnungen.

Nächste freie Nummern nach H201/k411: H202, k412 (vor Vergabe gegen `main` prüfen; Parallel-Thread
HS(−1) vergibt ebenfalls k-Nummern).
