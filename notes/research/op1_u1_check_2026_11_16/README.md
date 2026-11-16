# OP1: Bedingung U1 – liest der Frame M eine native U(1)-Ladung? (Erkundung, nicht blind)

16. November 2026. Auftrag des Autors: „U1 prüfen“, nach `../op1_counting_rule_data_2026_11_16/`. Dort ist die Zählregel des Frames M
(DL, γ = 0,237533) zerlegt in **U1** (M liest an einer Punktierung nur eine U(1)-Ladung) und **U2** (j = |m|). Skript `u1_check.py`, Ausgabe
`run/u1_check_stdout.txt`. Keine H-Nummer.

## Vorwissen geprüft (mit Berichtigung)
- **v4.9.0-r68.3 und r68.4 (übersehen in der vorigen Notiz):** Schon r68.3 stellt fest, dass die Literatur die SU(2)-Behandlung (ENP, 0,274)
  für besser begründet hält und dass das Leptonfenster von r61.1(e) die U(1)-Zählung auswählt; die Lesart „die Daten wählen die korrigierte Zählung“
  (r63, Lesart 5) ist dort zurückgenommen. r68.4: ABCK und Meissner sind beide U(1)-Zählungen, das Paar ist in einer Behandlung konsistent; ein
  SU(2)-Paar gibt β_sym = 0,604, außerhalb des Fensters. Der Befund „γ_M ist der U(1)-Wert“ aus der vorigen Notiz ist also **nicht neu**; neu ist
  nur die Zerlegung in U1 und U2. Das ist dort hiermit berichtigt.
- r68.1(b): Meissner zählt die Zustände |j = |m|, m⟩; der Faktor 2 zählt ±m.
- `../qam_hc_flaechenquantum_2026_11_07.md`, „Gemeinsame Form der M- und T-Zählmasken“: Die M-Maske ist $P_M(u)=\mathbf 1_{\{0\}}(B_u-|J_u|)$ mit
  $B_u=J^2-J_u^2$; sie braucht eine **feste Achse u**. Eine einzelne U(1)-Komponente allein reicht nicht (es braucht auch $J^2$), und das Mittel über
  alle Achsen gibt kein scharfes Zählgewicht. Abschnitt „U(1)-Randladung“: Eine scharfe rechte Randladung auf dem Peter-Weyl-Block lässt genau eine
  Kopie von $V_j$; welche Ladung gewählt wird, ist dort offen.
- r16.2–r16.4, r16.7 (Frame-Abbildungen auf χ), Konvention F (r22: der Frame M ist über den Kompensator-Port definiert), r17 ((S1) Strang = Quant
  von χ), r24.2 (strangweise Port-Auslesung → Extremdublett).

## Präzisierung von U1
Nach der QAM-Notiz heißt U1 genau: **An jeder Punktierung gibt es eine ausgezeichnete Achse u**, deren Ladung $J_u$ der Frame M liest; die Fläche
liefert $J^2$. Dann ist $P_M(u)$ die M-Maske, mit Rang 2 je j (nachgerechnet bis j = 10), und ihre Spur mit $e^{-2\pi\gamma\sqrt{j(j+1)}}$ ist die
DL-Gleichung (γ = 0,237533). Ohne ausgezeichnete Achse (alle j ≥ |m|) kommt Ghosh–Mitra heraus (0,274067). Gesucht ist also eine native Achse,
keine bloße U(1)-Gruppe.

## Ergebnis: Der Bestand hat eine native Achse, die Helizitätsachse von χ
1. **Die Dualitätsdrehung ist die U(1) um die Helizitätsachse.** $z\mapsto e^{ia}z$ dreht χ um die Helizitätsachse (z-Achse von χ) um −2a und lässt
   die Helizitätskomponente fest (200 komplexe Felder, Abweichung unter $10^{-15}$, bis auf die Wurzelwahl von r16.3(c)). Die Tachyon-Abbildung
   R ist ihr Element a = π/2, also σ_z (r16.7). Selbstduale und antiselbstduale Felder sind die Pole.
2. **Die Pole sind die Ports.** Nach r16.2(b) und r16.4(b) gehen die Helizitäts-Eigenzustände in Kompensator- und Partnerport über (1 ± i e₇,
   Eigenzustände von $iL_{e_7}$). Die innere Einheit J = L_e7 und die Helizitätsachse bezeichnen also dieselbe Richtung.
3. **Der Frame M ist über diese Achse definiert.** Konvention F legt M als Dublett-Zustand mit dem Kompensator-Port fest; T ist das $J_B$-Bild mit
   getauschten Ports. Die Achse ist damit keine Wahl an der Punktierung, sondern die Achse, über die der Frame selbst erklärt ist.

Zusammen: **U1 hat im Bestand eine native Form.** Die U(1) ist die elektromagnetische Dualität, ihre Achse die Helizitätsachse, ihre Eigenzustände
die Ports, und der Frame M ist durch sie definiert. Mit (S1) (ein Strang = ein Quant von χ) liest M dann an einer Punktierung die
Helizitätsladung $m$ eines Strangbündels; mit U2 (ausgerichtetes Bündel, r24.2) folgt die DL-Zählung ohne weitere Wahl.

## Was das nicht zeigt
- **(S1) bleibt die tragende Setzung.** Dass der Spin einer Horizont-Punktierung (gravitative SU(2), Fläche $\sqrt{j(j+1)}$) dasselbe ist wie das
  χ-Qubit eines Strangs, steht in r17 als Setzung. Ohne (S1) ist die Helizitätsachse eine Achse im Feldraum, nicht an der Punktierung.
- **Dualität ist nur für das freie Feld eine Symmetrie** (r16.6): Mit Ladungen ist sie gebrochen. Für die Zählung am Horizont braucht es sie als
  Auslese-Achse, nicht als Symmetrie; ob das reicht, ist offen.
- **Zur Literatur:** Dort ist die U(1) am Horizont eine Eichfixierung (die Normalenrichtung wählt sie), und deshalb gilt die U(1)-Zählung als leichte
  Überzählung. Im Companion wäre sie eine physikalische Ladung (Helizität). Das entkräftet den Einwand der Literatur nicht von selbst; es verschiebt
  ihn auf die Frage, ob die Normalenrichtung des Horizonts mit der Helizitätsachse zusammenfällt. Das ist nicht geprüft.
- Warum T nur j = ½ zählt, beantwortet r24.4 (Querungen), nicht diese Notiz.

## Folgerung
Die Kette für das Auswahlgesetz lautet jetzt: Phase ← Kern γ_M ← DL-Zählung des Frames M ← U2 (Extremdublett, Lesart r24.2) und U1 (Helizitätsachse
der Dualität, nativ) ← **(S1)**. Offen bleibt als einzelne Setzung (S1): die Gleichsetzung des Punktierungsspins mit dem χ-Qubit eines Strangs,
zusammen mit der Frage, ob die Horizontnormale die Helizitätsachse ist. OP1 offen; H102 unverändert.
