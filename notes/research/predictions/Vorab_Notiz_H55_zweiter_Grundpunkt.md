# Vorab-Notiz H55: Vier versteckte Bedingungen an 6-Jets auch an einem zweiten Grundpunkt

Festgeschrieben vor der Rechnung (3. November 2026). Betrifft nur das OP5-Vergleichsmodell. OP5 bleibt offen.

## Ausgangslage

Runde r72: Über dem reparierten 4-Jet gibt F₇ P₅₆ = 852, F₈ P₅₆ = 848. Spencer erlaubt höchstens 4 versteckte
Bedingungen (H^{5,2}(g') = 4). Eine Weyl-Schranke spricht für genau 4, formal unbestätigt (H54 ungültig). Ein echter Test
braucht neue Daten. Aus H52 bis H54 gelernt: Lückenforderungen nur an ungestörte Matrizen; Schranken so wählen, dass sie
nicht durch die Konstruktion unerreichbar sind.

## Der zweite Grundpunkt (vollständig festgelegt)

- Fest bleibt der Keim bis Grad 3. Lineares System F³₅: Unbekannte c₄, c₅; Gleichungen R vom Grad 3 und 4 und die Eichung
  vom Grad 4 und 5 (exakt linear, weil Produkte zweier Unbekannter erst ab Grad 7 auftreten).
- Neuer 4-Jet: c₄' = c₄(rep) + α·z₄. z₄ ist der c₄-Anteil eines Kernvektors z = N·r von F³₅ (N Orthonormalbasis des
  Kerns, r normalverteilt mit Seed 55). α ist so gewählt, dass ‖α z₄‖ = ½‖c₄(rep)‖. Damit erfüllt c₄' die Gleichungen
  vom Grad 3 und ist bis Grad 5 fortsetzbar, liegt aber deutlich vom reparierten Punkt entfernt.
- A und B bis Grad 3 werden für den neuen Punkt neu berechnet (Grad ≤ 2 hängt nur vom Jet bis Grad 3 ab, bleibt gleich).

## Hypothese H55

Am zweiten Grundpunkt gilt dasselbe wie am ersten:

- **T1:** κ(F₇) ≤ 100·ε_ref', wobei ε_ref' = κ(F⁴₅) am neuen Punkt (Grad 4 fest, N = 5).
- **T2:** P₅₆(F₇) = 852.
- **T3:** P₅₆(F₈) = 848.

## Kriterium

- **Bestätigt:** T1, T2 und T3.
- **Widerlegt:** Eine der drei Aussagen gilt nicht, bei gültigem Lauf. Insbesondere P₅₆(F₈) = 852 (keine versteckten
  Bedingungen) oder ein anderer Wert.
- **Ungültig, wenn:**
  - eine der vier verwendeten Ranglücken (F₇, F₇ ohne c₅/c₆, F₈, F₈ ohne c₅/c₆; alle ungestört) unter 1e3 liegt;
  - oder der kleinste gezählte Singulärwert von F₈ ohne c₅/c₆ weniger als das 100-Fache von dessen Fehler η_red beträgt;
  - oder der kleinste Nicht-Null-Wert von F₈ weniger als das 100-Fache von dessen Fehler η beträgt (η, η_red wie in H54:
    Streuung der vier Einzelschätzungen; für A vom Grad 3 die B-Streuung vom Grad 3 als Ersatz);
  - oder die Positivkontrolle versagt: c₄' plus eine zufällige Störung von 1e-3 relativ (Seed 56) muss in F⁴₅
    κ ≥ 1e3·ε_ref' geben.

## Grenzen

Ein zweiter Punkt, Grad ≤ 8, float64. Bestätigt hieße: Die vier Bedingungen sind nicht an den ersten Punkt gebunden. Sie
sind damit weiterhin nicht ausdrücklich bestimmt; kein Existenzsatz.
