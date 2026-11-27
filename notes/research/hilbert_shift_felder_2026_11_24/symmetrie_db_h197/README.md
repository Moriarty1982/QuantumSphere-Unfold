# H197: Erzwingt eine Symmetrie D = B?

Test, **Befund: nein**. Ist „Down linear" (D ≈ B aus H196) eine Symmetrie-Auswahlregel oder ein Fit?

- `Vorab_Notiz_H197_Erzwingt_eine_Symmetrie_D_gleich_B.md` — Vorab (Commit 7d39915), mit Bilanz der Setzungen.
- `k406_test_h197.py` / `k406_out.txt` — Grad-Trennung B/D, Rang, J-Kovarianz, feste-D/B-Fits, Kontrolle.
- `k406b_out.txt` — Wolfram-Gegenprobe (exakt, einig mit sympy).
- `Ergebnis_H197_Erzwingt_eine_Symmetrie_D_gleich_B.md` — Befund.

**Kurz:** D = B ist von **keiner** Symmetrie erzwungen. Das ladungsgerade l_k² (B) braucht Grad 5, das ladungsungerade (D) gibt es
schon bei Grad 4 — getrennte, unabhängige Kopplungen (Rang 2 ⇒ D/B frei). Die einzige von J ausgezeichnete Ladungsform ist Q₀−½
(gibt antisymmetrisches l_k², D/B = −1); D = B entspricht dem Up-Typ-Projektor P_up = 3(Q₀−⅓), der **nicht** J-kovariant ist
(J: P_up → P_down). Die Daten verlangen scharf D/B = 1,009 ± 0,001; die symmetrienahen Werte {0, ⅓, −1} liegen bei Δχ² ≈ 6·10⁴.
„Down linear" ist eine empirische Auswahlregel, die der H182/F4-Rahmen nicht erzeugt; der nächste Schritt ist keine weitere
Baustein-Variante, sondern eine neue Eingabe (P_up ↔ bekannte Größe, oder Lauf der Kopplungen). Aufruf:
`python k406_test_h197.py > k406_out.txt`.
