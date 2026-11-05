# Vorab-Notiz H52: Formale Integrabilität des ϑ-geeichten Systems ab Ordnung 6

Festgeschrieben vor der Rechnung (3. November 2026). Betrifft nur das OP5-Vergleichsmodell, nicht das QSC-Modell. OP5
bleibt offen.

## Ausgangslage

- H51 (bestätigt): Das Symbol g' von (F, G, dg), Ω und der Eichung s = Ψ†K₂Ψ ist bei p = 6 involutiv,
  dim g'_6 = 481, dim g'_7 = 606.
- Für die Involution des Systems fehlt die formale Integrabilität. Gemeint ist: Ab Ordnung 6 entstehen keine weiteren
  Bedingungen, die nicht schon in (F, G, dg), Ω und der Eichung stecken.
- Bekannt: Der Keim (70 Stellen, Grad ≤ 5, `precision-fifth-gate-repair-result.json`) erfüllt R bis Grad 4. Der alte,
  nicht reparierte Grad-4-Jet (`precision-omega-repair-result.json`) ließ sich nicht auf Grad 5 fortsetzen.

## Rechnung

- Reihenauswerter `k138_tps_d.py` (beliebiger Grad). Abgleich mit `k135_tps.py` an einem Zufallsfeld: 5,5e-12 bei
  |R| ≈ 500.
- Linearisierung L = A^μ(x)∂_μ + B(x) am Keim, mit A, B bis Grad 2 aus Sondenrechnungen (Fünfpunkt-Stencil, h = 1e-3).
  Weil die Unbekannten erst ab Grad 6 beginnen, ist das Fortsetzungsproblem exakt linear bis Grad 10.
- **Fortsetzungssystem E_N:** Der Keim-Jet bis Grad 5 ist fest. Unbekannt sind die Koeffizienten c₆ … c_N. Gleichungen
  sind die R-Koeffizienten der Grade 5 … N − 1 und die Eichung s(Ψ) = S(x) in den Graden 6 … N. S wird aus dem festen
  Jet gebildet, die rechte Seite der Eichzeilen ist also 0. Zeilen und Spalten werden normiert.
- Ränge werden an der größten Singulärwertlücke abgelesen. Eine Lücke gilt als sauber, wenn das Verhältnis ≥ 1e4 ist.
- **Verträglichkeit κ:** Anteil der rechten Seite im Linkskern von E_N, relativ zur rechten Seite.
- **Projektionen:** P₆ = Dimension der Projektion von ker E_N auf c₆; P₆₇ = Dimension der Projektion auf (c₆, c₇).

## Referenz und Kontrolle (Grad 4 fest, N = 5)

- **Referenz ε_ref:** κ mit dem reparierten Grad-4-Jet. Dieser ist bekannt fortsetzbar.
- **Positivkontrolle κ_pos:** κ mit dem alten Grad-4-Jet. Dieser ist bekannt nicht fortsetzbar.

## Hypothese H52

Das geeichte System ist am Keim ab Ordnung 6 formal integrabel:

- **T1:** Der Jet bis Grad 5 lässt sich fortsetzen. κ(E₇) ≤ 100·ε_ref und κ(E₈) ≤ 100·ε_ref.
- **T2:** Über dem festen Jet bis Grad 5 hat die Faser der 6-Jets die Dimension des Symbols:
  P₆(E₇) = P₆(E₈) = 481. Die zusätzlichen Gleichungen vom Grad 7 erzeugen also keine neue Bedingung an 6-Jets.
- **T3:** P₆₇(E₈) − P₆(E₈) = 606 = dim g'_7.

## Kriterium

- **Bestätigt:** T1, T2 und T3 gelten.
- **Widerlegt:** Eine der drei Aussagen gilt nicht. Das umfasst Nichtfortsetzbarkeit, eine Faserdimension ungleich 481
  oder 606 sowie eine Abweichung zwischen E₇ und E₈.
- **Ungültig:** κ_pos < 1e4·ε_ref (Test unempfindlich) oder keine saubere Lücke in einem verwendeten Rang.

## Grenzen

- Geprüft wird nur an einem Punkt, dem Keim, und nur bis Grad 8, in float64. Das ist kein Beweis der formalen
  Integrabilität in einer Umgebung und kein Existenzsatz. Der Keim ist einer von vielen; T2/T3 sprechen über die Faser.
- A und B stammen aus Differenzenquotienten. Ihr Fehler (etwa 1e-12 relativ) liegt unter den erwarteten Lücken.
