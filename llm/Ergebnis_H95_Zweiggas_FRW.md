# Ergebnis H95 widerlegt: Das dynamische Zweig-Gas (Variante A) erreicht nirgends gleichzeitig die dunkle Materie zur Rekombination und w ≈ −0,7 heute

Vorab-Notiz `Vorab_Notiz_H95_Zweiggas_FRW.md`, Commit `9eb4e40` (nicht blind, Widerlegung analytisch erwartet). Code `k212_zweiggas_frw.py`, Ausgabe `k212_out.json`. Ein Lauf.

## Ergebnis
- Gitter 60 (r) × 60 (a_th) × 40 (κ₁/a_th) = 144 000 Punkte. Davon erfüllen 12 780 die Positivität (Gesamtdichte > 0 auf a ∈ [10⁻⁸; 1], Ω_D > 0). **Kein Punkt erfüllt zugleich (i) dunkel/Baryonen bei z = 1090 in [4,32; 6,48] und (ii) w_eff heute in [−0,8; −0,6]. H95a widerlegt**; H95b entfällt.
- Nächster Punkt (Summe der Abstände): r = 0,10, a_th = 1,081, κ₁/a_th = 0,10 mit Verhältnis 58,5 und w₀ = −0,09. Das heißt: Wo die Spannung klein ist, gibt es zu viel dunkle Materie; wo die Spannung groß wird, bleibt es so.

## Nachträglich (nicht vorregistriert)
- Unter den positiven Punkten lässt sich w₀ beliebig negativ machen: Das Minimum ist w₀ = −151 bei a_th = 1,000001, also wenn die Schwelle gerade heute erreicht wird. Dabei ist das Verhältnis zur Rekombination aber 266 statt 5,4. Große heutige Spannung verlangt einen T-Zweig, der fast an der Schwelle steht. Dann ist seine Dichte heute fast null, Ω_D wird groß, und die dunkle Materie zur Rekombination ist viel zu groß.
- Das bestätigt die analytische Erwartung: Positivität und eine Spannung von der Größe Λ heute schließen einander bis auf eine Feinabstimmung auf die Schwelle aus, und diese Feinabstimmung zerstört das Verhältnis zur Rekombination.

## Folge
- **I3 ist auch dynamisch, in der einfachsten Form (frei strömendes Zweig-Gas mit negativer Energie im T-Zweig), ausgeschlossen.** Mit festen Gewichten war I3 bereits ausgeschlossen (`Erkundung_I3_mit_T_Zweig.md`).
- Damit bringt die Autorentscheidung „T-Zweig zulassen“ für Λ bisher keinen Gewinn, während ihr Preis (negative Energien, H76) bleibt. Dem Autor zur Neubewertung vorgelegt: Entscheidung zurücknehmen (zurück zur zweiten Lesart allein), oder ein anderes dynamisches Modell (Wechselwirkung der Zweige, Kondensation an der Schwelle) mit eigener Vorab-Notiz.
- Die Auslöser der zurückgestellten Ideen habe ich geprüft (Ansatz gescheitert): I1 (String-Brücke) hat keinen getroffenen Auslöser. I3 selbst ist damit in beiden geprüften Formen gescheitert.
