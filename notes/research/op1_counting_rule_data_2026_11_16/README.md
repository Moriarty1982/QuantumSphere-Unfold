# OP1/OP3: Grunddaten von H102 und die Zählregel des Frames M (Erkundung, nicht blind)

16. November 2026. Auftrag des Autors: „H102 könnte von falschen Grunddaten ausgehen, gehe auch bitte die Zählregel an.“ Skript
`counting_data.py`, Ausgabe `run/counting_data_stdout.txt`. Literatur über alphaXiv: Barbero G. und Pranzetti, „Black Hole Entropy in Loop
Quantum Gravity“, arXiv:2212.13469 (Übersicht 2022). Datenstand m_τ über die PDG-Listings 2026. Keine H-Nummer, H102 unverändert.

## Vorwissen geprüft
- `../predictions/Vorab_Notiz_H102_Tau_Masse_aus_gamma.md`, `k224_test_h102.py`: φ = π/4 − γ_M/2, γ_M = 0,237533 aus
  $\sum_j 2e^{-2\pi\gamma\sqrt{j(j+1)}}=1$; m_e, m_μ (CODATA), PDG 2024 m_τ = 1776,93 ± 0,09; nachträglich in einem Scan mit 154 Versuchen gefunden.
- `../op3_guarded_core_flux_2026_11_15/README.md` (Literaturprüfung ABK, ENP; Punkt 1: Kern = Quant des Beobachter-Frames).
- r08–r10 (Zählregel je Frame, H98: das Paar ist unter 36 natürlichen das einzige, das drei bekannte Werte trifft), r17 ((S1)–(S3)),
  r24 (T zählt Querungen; r24.2: strangweise Port-Auslesung gibt das Extremdublett |j, ±j⟩).
- Wiki „Offene Probleme“, gemeinsamer Kern Punkt 5: „Ein Randterm, der nur eine U(1) zählt. Die innere Einheit J = L_e7 wählt in SU(2) genau eine
  U(1) aus“ (Vermutung).

## 1. Die Messdaten sind in Ordnung
| Quelle | m_τ (MeV) | 3δ | z für H102 (1777,134) |
|---|---|---|---|
| PDG 2022 | 1776,86 ± 0,12 | 0,666689 | +2,28 |
| PDG 2024 = PDG 2026 | 1776,93 ± 0,09 | 0,666674 | +2,27 |
| Belle II 2023 | 1777,09 ± 0,14 | 0,666641 | +0,31 |
| BESIII 2020 | 1776,91 ± 0,15 | 0,666678 | +1,49 |

H102 hat mit PDG 2024 gerechnet; die Listings 2026 geben denselben Mittelwert. m_e und m_μ sind CODATA-Werte. Die Spannung von +2,3σ kommt aus dem
Mittelwert; Belle II allein liegt bei +0,3σ. Entschieden wird wie vorab festgelegt mit der ersten PDG-Ausgabe nach dem 13.11.2026.
**Nebenbefund (eigener Fehler):** `../op3_chain_diagnosis_2026_11_16/chain.py` hat noch PDG 2022 benutzt (3δ = 0,666689 statt 0,666674). Die
Diagnose ändert sich dadurch nicht, die Zahl ist hiermit berichtigt.

## 2. Die eigentliche Grunddatenfrage: welche Zählung γ_M liefert
Die Zählregel des Frames M ist **genau die Zählung von Domagala–Lewandowski und Meissner** (U(1)-Horizont): Jede Punktierung trägt eine Ladung m,
und ihre Fläche ist die zu j = |m|; das ergibt Gewicht 2 je j (nur m = ±j). Die Zählung des Frames T ist die ursprüngliche von ABK (nur j = ½).

| Zählung | Gleichung | γ | φ = π/4 − γ/2 | m_τ aus H102-Beziehung |
|---|---|---|---|---|
| DL/Meissner (U(1), m = ±j) – Companion Frame M | $\sum_j 2e^{-2\pi\gamma\sqrt{j(j+1)}}=1$ | 0,237533 | 0,666632 | 1777,134 |
| Ghosh–Mitra (alle m, j ≥ \|m\|) | $\sum_j (2j+1)e^{-2\pi\gamma\sqrt{j(j+1)}}=1$ | 0,274067 | 0,648365 | 1868,2 |
| ABK (nur j = ½) – Companion Frame T | $2e^{-\pi\gamma\sqrt3}=1$ | 0,127384 | 0,721706 | 1541,4 |

**Was die Literatur sagt** (Barbero–Pranzetti 2022, Abschnitte 1.1 und 3.2): Der Wert 0,237 gehört zur U(1)-Behandlung. Die Prescription von
Ghosh–Mitra und die SU(2)-Behandlung (Engle–Noui–Perez) geben 0,274. Die U(1)-Randbedingungen lassen sich quantenmechanisch nur teilweise
auferlegen; das führt zu einer leichten Überzählung. Die SU(2)-Fassung gibt die logarithmische Korrektur −3/2, die auch unabhängige Rechnungen
(Kaul–Majumdar, Carlip) finden. Derselbe Wert 0,274 folgt außerdem aus einer effektiven Dynamik des Schwarzschild-Inneren. Die Festlegung von
γ über die Entropie ist selbst umstritten.

**Folgerung für H102.** Die Messdaten sind richtig. Aber das zweite Eingangsdatum, γ_M = 0,237533, ist der Wert der U(1)-Zählung, die die
Fachliteratur für Horizonte der Allgemeinen Relativität inzwischen als Näherung ansieht. Mit der SU(2)-Zählung (0,274) gäbe dieselbe Beziehung
φ = 0,648 und m_τ ≈ 1868 MeV, also nichts. H102 hängt damit ganz daran, dass der Frame M wirklich nur eine U(1) zählt. Dazu kommt: H102 wurde
nachträglich in einem Scan mit 154 Versuchen gefunden (0,34 Treffer zufällig erwartet).

**Reichweite über H102 hinaus.** Dieselbe Wahl trägt den Frame-Faktor des Companion: γ_L = γ_M/γ_T = 0,237533/0,127384 = 1,8647. Mit der
SU(2)-Zählung für M wäre γ_L = 0,274067/0,127384 = 2,1515. Nach r08 ruhen auch H15, H46 und H96 auf dieser Zuordnung. Die Frage „welche Zählung
gilt für M“ ist also OP1 selbst.

## 3. Die Zählregel: was sie voraussetzt
Die DL-Zählung für M folgt aus zwei Bedingungen, die im Bestand schon einzeln vorkommen:

| Bedingung | Inhalt | Stelle im Bestand | Status |
|---|---|---|---|
| U1 | Der Frame M liest an einer Punktierung nur eine U(1)-Ladung m | Wiki, gemeinsamer Kern Punkt 5: J = L_e7 wählt in SU(2) eine U(1) | Vermutung |
| U2 | Jede Ladung m wird mit der kleinsten Fläche realisiert, j = \|m\| (Extremzustand, „ausgerichtetes Bündel“) | (S3), r24.2 (strangweise Port-Auslesung → \|j, ±j⟩), Sättigung r63 | Lesart |
| T | Der Frame T zählt Querungen, eine Querung ein Strang, j = ½ | r24.4 | Lesart |

- **Mit U1 und U2** folgt DL für M ohne weitere Wahl. Das Gewicht 2 je j ist dann kein Statistik-Ansatz ((S2), r24.1 nicht begründbar), sondern
  die Zahl der Extremzustände ±j. Damit verschiebt sich die offene Frage von (S2) auf U1.
- **Ohne U1** (voller SU(2)-Horizont) zählt man alle m mit j ≥ |m|; das ist GM bzw. ENP mit 0,274. Ohne U2 (alle j ≥ |m| bei U(1)-Ladung) ebenso
  GM.
- **Was U1 physikalisch heißt.** In der Literatur ist die U(1) eine Eichfixierung, also eine Näherung. Im Companion müsste sie physikalisch sein:
  Der Materie-Frame liest über den Kompensator J (Port-Auslesung) wirklich nur eine Komponente. Das wäre eine Aussage über den Frame, nicht über die
  Horizontgeometrie, und die Literatur widerspricht ihr dann nicht. Es bleibt aber eine Annahme, und sie ist genau der Punkt, an dem die Wahl
  M = DL hängt.

## Ergebnis
1. H102 geht von korrekten Messdaten aus (PDG 2024 = PDG 2026). Die Spannung +2,3σ ist echt; Belle II allein wäre verträglich.
2. Das kritische Grunddatum ist γ_M: H102 und der Frame-Faktor γ_L = 1,8647 stehen auf der U(1)-Zählung von DL. Die neuere Literatur bevorzugt für
   Horizonte die SU(2)-Zählung mit 0,274; damit wären H102 (m_τ ≈ 1868 MeV) und γ_L nicht zu halten.
3. Die Zählregel des Frames M ist äquivalent zu U1 + U2. U2 hat eine Lesart im Bestand (Extremdublett der Port-Auslesung). **Offen ist U1: dass der
   Materie-Frame physikalisch nur eine U(1) liest** (J = L_e7). Das ist die präziseste Fassung von OP1, die der Bestand bisher hatte.
4. Nächster Schritt: U1 prüfen, also ob die Port-Auslesung über J an einer Punktierung nur die U(1)-Ladung sieht und den Rest von SU(2) nicht
   (Quellen: r17, r24.2, v4.9.0-r51, die Kompensator-Notizen). Das ist eine Frage an den Bestand, keine neue Rechnung mit Zielwert.

## Grenzen
Nicht blind: γ-Werte und Daten waren bekannt. Die Literaturaussagen stammen aus einer Übersicht, nicht aus den Originalarbeiten. H102, H15, H46 und
H96 bleiben unverändert (append-only); keine Aussage hier ändert ihren Status. OP1 und OP3 offen.

## Nachtrag (16.11.2026): Berichtigung zum Vorwissen
Der Befund „γ_M ist der U(1)-Wert, die Literatur bevorzugt SU(2) mit 0,274“ steht schon in v4.9.0-r68.3 und r68.4 (dort auch: ein SU(2)-Paar gibt
β_sym = 0,604, außerhalb des Fensters). Diese Notiz hatte r68 nicht als Vorwissen geführt. Neu ist hier nur die Zerlegung der Zählregel in U1 und
U2 und die Aufschlüsselung, was die SU(2)-Zählung für H102 bedeutete. Weiter in `../op1_u1_check_2026_11_16/`.
