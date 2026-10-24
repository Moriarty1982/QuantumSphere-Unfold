# Vorab-Notiz H44: Legt ein Strukturwert für ε die korrigierte TM2-Lesart fest?

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „prüfe das erst“ (auf den Vorschlag, die Korrekturstärke ε aus einem Strukturwert festzulegen). Bezug: r57/H41
(Varianten A und B), r58/H43 (δ frei), r56/H40 (Kandidatenliste).

## Offenlegung

Aus r57 bekannt: Treffer gibt es in Variante A für ε_e von 0.03 bis 0.64, in Variante B nahe ε ≈ 0.04–0.06 und 0.62–0.64. Um keine Werte nach diesem Wissen auszuwählen,
wird **ausschließlich die Kandidatenliste aus H40** verwendet, die vor r57 festgelegt war: 1/3, 1/2, 2/3, 3/4, 1, 1/√3, 1/√2, √3, 2/9, π/6, π/9, β_sym² = 0.3017,
β_sym = 0.5493, γ_L = 1.864.

## Verfahren

Modelle, Zuordnungen und Daten wie k97/k98 (θ₁₂ JUNO 2σ, θ₁₃ und θ₂₃ NuFIT 3σ, m₁ ∈ {0, 0.001, 0.003} eV). ε wird für jeden Kandidaten exakt gesetzt (Fortsetzung der
Zweige von ε = 0 über das Gitter und dann auf den Kandidatenwert). Frei bleibt nur φ (und die diskreten Wahlen: ℤ₂, Zuordnung, Zweig, Vorzeichen). Für jeden Kandidaten
und jede Variante: Zahl der Treffer, Spannweite von sin²θ₂₃ und |sin δ| unter den Treffern.

## Hypothesen

- **H44a:** Für mindestens einen Kandidaten in Variante A oder B gibt es Treffer, und unter diesen Treffern hat sin²θ₂₃ eine Spannweite < 0.05 und |sin δ| eine
  Spannweite < 0.3.

## Entscheidungskriterium (verbindlich)

- H44a bestätigt ⇒ Der Kandidat legt die Lesart fest; θ₂₃ und |sin δ| werden als Vorhersage H45 mit eigener Notiz festgelegt. Wegen 2 × 14 geprüfter Fälle wird
  mitberichtet, wie viele Kandidaten das Kriterium erfüllen; erfüllen es mehrere mit verschiedenen Vorhersagen, ist es keine Festlegung.
- H44a widerlegt ⇒ Auch ein fester Strukturwert für ε macht die Lesart nicht vorhersagekräftig; die verbleibende Freiheit (φ und die diskreten Wahlen) reicht schon.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
