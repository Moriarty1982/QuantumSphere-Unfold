# Vorab-Notiz H47: β_sym als Verhältnis zweier Horizontzählungen – welche Zählung legt die Leptonmischung fest?

Festgelegt am 2026-10-25, **vor** jeder Rechnung dieser Notiz. Autor: „ja mach das“ (auf die Frage, was β_sym eigentlich misst).
Bezug: r03 F11 (Herkunft von γ_L), K36.2/r18.1 (Frames bei +η, 0, −η; γ_L = cosh 2η ist der Boost Materie–Tachyon),
r61 (Frame-Prüfung OP1; Fenster β_sym ∈ [0.545, 0.570] aus der Leptonmischung, `llm/k101_fenster_eta.py`), H15 (Meissner-Wert).

## Offenlegung (Vorwissen)

- r03 F11 hat die Lesart schon angeboten und nicht übernommen: γ_string ist der ABCK-Wert (nur Spin j = ½ an den Durchstoßpunkten),
  γ_BI der korrigierte Wert von Domagała–Lewandowski und Meissner (alle Spins); γ_L wäre dann das Verhältnis einer Minimal-Spin- zu einer
  Voll-Spin-Lesung. r03 sah darin einen Gegensatz zur Lorentz-Lesart.
- Neu in dieser Notiz ist nur: (i) Nach K36.2 ist γ_L = cosh 2η der Boost zwischen den **Gegenüberliegenden** Materie und Tachyon.
  Die Zähl-Lesart und die Lorentz-Lesart sind vereinbar, wenn der Tachyon-Frame minimal (j = ½) und der Materie-Frame voll zählt.
  (ii) Es gibt mehr als eine „volle“ Zählung; die Leptonmischung könnte zwischen ihnen unterscheiden.
- Bekannte Zahlen vor der Notiz: γ_ABCK = ln2/(π√3) = 0.12738; γ_DL/M = 0.237532957966 (H15). Aus dem Gedächtnis, ungeprüft:
  Ghosh–Mitra ≈ 0.274. Kopfschätzung vor dieser Notiz: damit γ_L ≈ 2.15, β ≈ 0.60, also außerhalb des Fensters. **Teil B ist daher nicht blind.**
- Das Fenster [0.545, 0.570] ist selbst nachträglich aus den Daten gewonnen (r61). Es hängt an der Lesart r55, r57, r60.

## Festgelegte Zählgleichungen (aus der Literatur, nicht angepasst)

Flächenspektrum a(j) = √(j(j+1)), j = ½, 1, 3/2, … Der Parameter γ ist die positive Lösung von

- **Z_min (ABCK, Tachyon-Frame):** 2·exp(−2πγ·a(½)) = 1, also γ = ln2/(π√3).
- **Z_DL/M (Materie-Frame, Variante 1):** Σ_j 2·exp(−2πγ·a(j)) = 1 (Gewicht 2 je Spin: nur m = ±j; Meissner gr-qc/0407052).
- **Z_GM (Materie-Frame, Variante 2):** Σ_j (2j+1)·exp(−2πγ·a(j)) = 1 (alle m; Ghosh–Mitra-Zählung).

Beide vollen Zählungen reduzieren sich, auf j = ½ abgeschnitten, auf Z_min. Weitere Varianten werden nicht nachgeschoben.
γ_L = γ_voll/γ_min, β = √((γ_L−1)/(γ_L+1)). Summen bis j_max mit Restabschätzung < 1e−12.

## Prüfungen

**A (Kontrolle):** Z_DL/M ergibt 0.2375330 (|Δ| < 1e−6) und γ_L = 1.86444. Sonst ist eine Gleichung falsch übernommen; dann Abbruch und Bericht,
keine Anpassung.

**B (Beobachtung, nicht blind, Versuchsfaktor 2):** β für Z_DL/M und Z_GM gegen das Fenster [0.545, 0.570].
- „Trennt“, wenn genau eine Variante im Fenster liegt. Erwartet (offengelegt): DL/M drin, GM draußen.
- Liegen beide drin oder beide draußen, stützt das Fenster die Zähl-Lesart nicht.

**C (nicht Teil der Rechnung):** Ob die Struktur selbst begründet, dass der Tachyon-Frame nur j = ½ und der Materie-Frame alle Spins mit Gewicht 2
zählt, bleibt die umformulierte Frage zu OP1. Eine Prüfung dazu braucht eine eigene Vorab-Notiz.

## Was ein Ergebnis bedeutet

Auch wenn B trennt, ist das kein Beleg: Es zeigt nur, dass β_sym unter dieser Lesart eine reine SU(2)-Zahl ist, abhängig von einer Zählkonvention,
und dass die Leptondaten unter der Lesart r55–r60 die Konvention DL/M auswählen. OP1 wird dann von „eine Zahl herleiten“ zu „zwei Zählregeln aus den
Frames herleiten“. Guards bleiben unverändert.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
