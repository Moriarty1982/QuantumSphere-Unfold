# Vorab-Notiz H53: Fortsetzung des ϑ-geeichten Systems über dem reparierten Jet bis Grad 4

Festgeschrieben vor der Rechnung (3. November 2026), nach H52 (ungültig). Betrifft nur das OP5-Vergleichsmodell. OP5
bleibt offen.

## Was sich gegenüber H52 ändert

1. **Fester Jet nur bis Grad 4.** Der gespeicherte Jet bis Grad 5 ist nicht fortsetzbar: Er erfüllt die abgeleitete
   Ω-Bedingung der Ordnung 5 nicht (Ergebnis H52, E₆ mit sauberer Lücke). Deshalb bleiben jetzt c₅ … c_N frei.
2. **Exakte Linearisierung** (`k140_fortsetzung_exakt.py`). A und B bis Grad 2 werden aus symmetrischen Sonden
   d = x^{m e_ν} e_i mit m = 4, 5 gewonnen, als (R(Ψ₃ + d) − R(Ψ₃ − d))/2. Quadratische Terme heben sich auf, kubische
   beginnen oberhalb von Grad m + 2. Methodenprüfung am alten System E₇: Die vier unabhängigen B-Schätzungen stimmen auf
   2e-9 (|B| ≈ 100) überein, A(0) − J = 2e-13. Das Rauschniveau sinkt von 1e-12 auf 3e-14, die Ranglücke wird sauber
   (2e4 statt 4e2). Die Ergebnisse von H52 werden dadurch nicht nachträglich umbewertet.

## Rechnung

- **Fortsetzungssystem F_N:** Der reparierte Jet bis Grad 4 (`precision-fifth-gate-repair-result.json`) ist fest.
  Unbekannt sind c₅ … c_N. Gleichungen sind die R-Koeffizienten der Grade 4 … N − 1 und die Eichung s = Ψ†K₂Ψ in den
  Graden 5 … N, mit rechter Seite 0. Zeilen und Spalten werden je einmal normiert.
- Rang an der größten Singulärwertlücke; sauber, wenn das Verhältnis ≥ 1e4 ist. Verträglichkeit κ und Projektionen
  P₅, P₅₆, P₅₆₇ wie in H52.
- **Referenz und Positivkontrolle:** wie in H52 (Grad 4 fest, N = 5; reparierter bzw. alter Grad-4-Jet), jetzt mit der
  exakten Linearisierung neu gerechnet.

## Hypothese H53

Über dem reparierten Jet bis Grad 4 ist das geeichte System bis Grad 8 fortsetzbar, und die Fasern haben die
Dimensionen des Symbols g' aus H51. Es gibt also keine Bedingungen außer (F, G, dg), Ω und der Eichung:

- **T1:** κ(F₇) ≤ 100·ε_ref und κ(F₈) ≤ 100·ε_ref.
- **T2:** P₅ = 371 = dim g'_5 und P₅₆ − P₅ = 481 = dim g'_6, jeweils in F₇ und F₈.
- **T3:** P₅₆₇ − P₅₆ = 606 = dim g'_7 in F₈.

Zusammen mit H51 hieße das: Am Keim ist das geeichte System ab Ordnung 6 involutiv, soweit bis Grad 8 prüfbar.

## Kriterium

- **Bestätigt:** T1, T2 und T3 gelten.
- **Widerlegt:** Eine der drei Aussagen gilt nicht.
- **Ungültig:** κ_pos < 1e4·ε_ref oder ein verwendeter Rang ohne saubere Lücke.

## Grenzen

Wie H52: ein Punkt, Grad ≤ 8, float64, kein Existenzsatz. Bestätigt wäre nur, was bis Grad 8 sichtbar ist.
