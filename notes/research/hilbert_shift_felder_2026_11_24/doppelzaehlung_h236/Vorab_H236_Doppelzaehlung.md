# Vorab H236 (k451): Wer trägt den Versatz, der q-Fit aus H167 oder der Drehwinkel φ?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** In H235 (k450c) fiel nachträglich auf, dass das Modell seit H225 den Lepton-Versatz doppelt
setzt. Marc, 15:52: „dann kläre das erst“.

## Vorwissen geprüft
- **H167:** Im geladenen Sektor heben zwei Wege das Elektron aus dem Oktanten. Der eine ist der Konjugationsterm (α/α′ = 0,0793), der andere ein Term
  sechster Ordnung q cos 3δ mit **q/α′ = −0,0852 als Fit**. Dieser Fit allein liefert schon den ganzen Im-Versatz x, bei φ = 0.
- **H221:** Mit gleichem q in beiden Sektoren liegt der neutrale Versatz bei 0,0630, also +9,2σ (Faktor 1,59). Eine gemeinsame Drehung φ gibt dagegen
  exakt gleiche Versätze. Urteil: spricht für skalenfrei, φ trägt.
- **H222:** Nur das **Vorzeichen** von q zählt für die Zweigwahl, gerechnet im Grenzfall q = −ε, ε → 0.
- **H225:** Das globale Minimum liegt für jedes q bei π/8, also unabhängig vom Wert von q.
- **H226 Teil B, H232 Teil B, H235:** Gerechnet mit q = −0,0852 **und** φ zusammen. Das ist die Doppelzählung.
  - H232 Teil C hat q bereits variiert: Bei q = −0,001 liegt off_Re bei −1,30σ, aber x ist nirgends global.
  - H235/k450c: Bei kleinem q liegt x_ν bei −0,5σ bis −1,8σ, x ist nicht global.
- **H228:** Die Uhr t_x/τ hängt schwach von q ab (0,1310 bei q = −0,01, 0,1231 bei −0,0852, führende Ordnung 0,1321). Die Bemerkung „⅛ nur 1,5 %
  daneben“ gilt nur bei q = −0,0852.
- **H227 (Massen, Σm_ν = 59,30 meV), H229–H231, H233, H234, H223, H224, k436:** In den Skripten kommt q als Zahl nicht vor (grep nach 0852/Q0/q0).
  Ihre Rechnungen benutzen φ direkt als gemeinsamen Versatz, also die φ-Lesart.

## Lesarten (gesetzt)
- **Q:** q = −0,0852 trägt den Versatz, φ = 0.
- **Φ:** φ trägt den Versatz, q → 0⁻ (nur das Vorzeichen, H222).
- **M (Mischung):** Beide Größen sind frei und werden aus den zwei Daten x und x_ν bestimmt.

Baum-Modell wie H225: V_Im = −cos2(δ−π/4−φ) + q cos3δ, V_Re = cos2(δ−φ) + q cos3δ. Die Versätze sind o_Im = π/12 − fold(δ_Im),
o_Re = π/6 − fold(δ_Re).

## Teil A (Lesarten Q und Φ nicht blind, M blind)
- **Q:** x_ν,pred = o_Re(φ = 0, q = −0,0852). Bekannt aus H221: +9,2σ.
- **Φ:** x_ν,pred = x. Bekannt aus H213: −1,78σ.
- **M:** (φ, q) so bestimmen, dass o_Im = x und o_Re = x_ν gilt. Den 2σ-Bereich von q bestimmen, indem x_ν um ±2σ variiert wird
  (σ_x ist vernachlässigbar).
- **Kriterium A:** Liegt q = 0 im 2σ-Bereich von M **und** ist der Q-Wert q = −0,0852 außerhalb, dann trägt φ, und q ist nur ein Vorzeichen.
  Liegt −0,0852 im Bereich, ist die Frage nicht entschieden. Liegt 0 außerhalb, ist ein Teil des Versatzes Skala.

## Teil B (blind): Urteile in der Φ-Lesart nachrechnen
H226 Teil B (Terme T1–T3, nur Im-Sektor bzw. ungleiche Kopplungen) wird mit q ∈ {−10⁻³, −10⁻²} statt −0,0852 wiederholt, sonst unverändert.
- **Kriterium B:** Bleibt das Urteil von H226 (widerlegt: kein Term gibt x global und zugleich x_ν innerhalb 2σ), heißt das „Urteil bleibt“.
  Sonst „Urteil kippt“.

H232 und H235 werden nicht neu gerechnet. Ihre Variation von q liegt schon vor (Teil C bzw. k450c) und wird nur eingeordnet.

## Teil C (Bestandsaufnahme, keine Rechnung)
Eine Tabelle führt H221–H235 und H227 auf: benutzt q? Lesart? betroffen? Urteil bleibt oder kippt?

## Urteil
- **trägt:** A gibt „φ trägt“, und B gibt „Urteil bleibt“.
- **trägt teilweise:** A nicht entschieden oder B kippt.
- **widerlegt:** A zeigt, dass ein Skalenanteil nötig ist (q = 0 außerhalb 2σ).

## Werkzeuge
Python k451 und Wolfram k451b (FindRoot für M, unabhängig). Qiskit ist nicht einschlägig.
