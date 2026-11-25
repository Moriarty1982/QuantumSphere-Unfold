# Ergebnis H151: Die Koide-Verschiebung aus H150 hängt weder mit δ = 2/9 noch mit einer anderen Setzung zusammen, und die Frame-Differenz kann sie nicht aufheben

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H151_Verschiebung_und_Zwei_Neuntel.md` (Commit 8fc75b5; Nachtrag Setzungsliste 4676bce vor der Rechnung; zweiter Nachtrag
Frame-Differenz ed80585, nach dem Lauf zu a–d, vor der Rechnung zu e). Skripte `k334_verschiebung_setzungen.py` (`k334_out.txt`), `k334b_gegenprobe.wl`
(`k334b_out.txt`, Wolfram). Status: a, c, d, e bestätigt; b teilweise (kein Fixstrahl mit κ < 0, der Grenzwert kommt vom Strahl κ = 0).**

Anlass: Autor „schau mal, ob diese 0.06 mit den 2/9 zusammenhängen könnten“, dann „sonst prüfe nochmal einen zusammenhang zu allen werten die wir bisher von hand einsetzen
müssen“ und „eine andere quelle könnte die frame differenz sein“. Gelesen als: die Verschiebung K ≈ 0,672 statt ⅔ aus H150. Eine feste Zahl 0,06 kommt dort nicht vor
(siehe unten). Werkzeuge: Python (sympy, scipy), Wolfram unabhängig; alle gemeinsamen Werte stimmen auf sieben bis zehn Stellen. Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H151a | V(Drehung in der Kopien-Ebene) − V = 0; β-Funktionen kennen nur λ_A, κ, λ_B | exakt | **bestätigt**: der Fluss erzeugt δ nicht |
| H151b | Fixstrahlen (1, 2): λ_A/λ_B = 10/9 mit κ = 0; 1 mit κ/λ_B = 2 (volle Norm); 0,8008 mit 2,7313. Für (1, 7): 5/3, 1, 1,6348. **Keiner mit κ < 0.** Für κ₀ → 0⁻ läuft der Fluss auf den Strahl κ = 0: K* = 1/3 + √10/9 = 0,684698 (n_B = 2), (1 + √(5/3))/3 = 0,763665 (n_B = 7) | einen anziehenden Fixstrahl mit κ < 0 bzw. Grenzwert, algebraisch | **teilweise**: Grenzwert algebraisch ohne π, aber kein Fixstrahl mit κ < 0 |
| H151c | 48 Vergleiche gegen Funktionen von δ = 2/9: kein Treffer; nächster tan²θ* − 1 = 0,0541 gegen δ/4 = 0,0556 (2,6 %); Zufallserwartung 0,05 | < 0,5 % | **bestätigt**: kein Zusammenhang mit 2/9 |
| H151d | 540 Vergleiche gegen 15 Setzungen in sechs Formen: 2 Treffer, beide dieselbe Zahl θ* − π/4 = 0,013169 ≈ γ_M/18 = 0,013196 (−0,21 %); Zufallserwartung 0,58, 99-%-Quantil 3 | auffällig nur über dem 99-%-Quantil | **bestätigt**: nicht auffällig |
| H151e | Form S: K exakt invariant. Boost auf (φ, χ): erhält ReΨ² = cos 2θ, hält θ = π/4 fest; der Fluss-Punkt liegt raumartig (ReΨ² = −0,026), K = ⅔ für kein endliches ε. Mit +artanh β_sym: K' = 0,6718, mit −artanh β_sym: 0,7329. 1 Treffer in 1080 Vergleichen (Zufall 1,15) | K' = ⅔ für keine Rapidität | **bestätigt** |

## Lesart
- **δ und die Verschiebung sind verschiedene Winkel.** θ ist der Polwinkel zwischen HS(0)-Einheit und Kopien-Ebene, δ der Azimut in der Ebene. Der Fluss sieht nur die Norm
  in der Ebene und ist unter Drehungen darin invariant. Die 1:2-Asymmetrie verschiebt θ, nie δ.
- **Die Verschiebung ist keine feste Zahl.** Auf einem physikalischen Bereich (Start mit κ₀/λ zwischen −1,9 und −0,1) liegt sie zwischen 0 und 0,011 in K. Einen festen
  Wert gibt es nur als Grenzwert κ₀ → 0⁻ auf dem Strahl λ_A/λ_B = 10/9, also ΔK = 0,0180. Dieser Grenzwert braucht aber einen extrem langen Fluss (τ > 10⁶; bei
  |κ₀|/λ ≤ 10⁻³ ist das Ereignis im Rechenbereich nicht erreicht, die Ausgabe nennt dann das Ende des Bereichs, das Verhältnis ist aber schon auf dem Strahl).
- **Kein Zusammenhang mit den Setzungen.** Der einzige Treffer γ_M/18 (−0,21 %) ist zwei exakte Größen, die sich unterscheiden, und liegt in der Zufallserwartung.
- **Frame-Differenz:** Form S ändert K nicht. Ein Frame-Boost erhält die lichtartige Form ReΨ², hält also π/4 fest und kann einen Zustand nicht über den Lichtkegel
  schieben. Der Fluss-Punkt liegt auf der raumartigen Seite (Anhang stärker als Vorstufe, tan θ > 1), also auf der Tachyon-Seite in der Sprache von k297. Ein Boost in
  Richtung Materie-Frame bringt K von 0,6847 auf 0,6718 näher an ⅔, aber nie darauf. Das stimmt zu H150: Koide sitzt genau auf dem Lichtkegel, und nur die Tausch-Symmetrie
  hält den Zustand dort.
- **„0,06“:** Kein fester Wert der Rechnung ist 0,06. In der Nähe liegen θ* − π/4 = 0,064 (n_B = 7), tan²θ* − 1 = 0,054 (n_B = 2) und K' − ⅔ = 0,066 nach einem Boost mit
  −artanh β_sym. Keiner davon hängt mit 2/9 zusammen (H151c). Welche Zahl gemeint war, wird beim Autor nachgefragt.

## Grenzen
- Eine Schleife, ohne Eichfelder; die Komponentenzahl der Kopienrichtung (2 oder 7) ist eine Lesart. Der Boost auf (φ, χ) ist eine Modellform der Frame-Übertragung neben
  Form S, nicht aus dem Companion übernommen.
- Die Setzungsliste ist dimensionslos; die Skala 9,8 GeV und der freie Drehwinkel der Mischung sind nicht verglichen.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H151, k334. Nächste frei: H152, k335.
