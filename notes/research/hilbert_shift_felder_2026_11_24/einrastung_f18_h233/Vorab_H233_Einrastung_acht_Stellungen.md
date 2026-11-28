# Vorab H233 (k447): Legt die Einrastung auf 8 Stellungen die feinen Winkel fest? (F18)

**Datum:** 2026-11-28. Vor der Rechnung geschrieben und committet. Auftrag: Marc 15:12 („2. dann 3.“) auf den Vorschlag des Koordinators, F18 aus der
Fragenliste zu rechnen. Werkzeuge: Python (`k447_test_h233.py`) als Hauptrechnung, Wolfram (`k447b_gegenprobe.wl`) unabhängig mit exakter Arithmetik
(Rationalisierung, Gitterreste). Qiskit nicht einschlägig.

## Frage (F18)
Marc, 27.11.: „Wir haben quasi 8 Bit, wobei jedes Bit die doppelte Anzahl an Informationen wie sein vorheriges tragen kann“ und „Heißt das nicht auch,
dass unsere Rotoren nur 8 Positionen haben?“ k407: Der Typ einer Stufe hat 8 Stellungen (Clifford-Uhr), jede Stufe verdoppelt die Dimension.
Die Frage hier: Rasten auch die **feinen** Winkel (φ, x_ν, die Mischungswinkel, Winkellesarten von β_sym) auf ein Gitter aus 8 Stellungen mit
Bit-Verfeinerung ein?

## Vorwissen geprüft
k407 (Clifford-Uhr, 8 Stellungen, a = n + 4 ab HS(3)), k254 (Periode 4 als Obergrenze), H192 (8 Oktanten auf der Sphäre, Vermutung), H167/H171
(Baumwerte aus Achteldrehungen: Spin-1-Achse χ = π/4, Polarwinkel π/4 für K = ⅔, zusammen Oktant; Phase π/12 = (π/4)/3 über die ℤ₃-Klasse von δ),
H168 (Baumwerte π/12 geladen, π/6 neutral, gemeinsamer Versatz φ), H224/H228/H230 (φ trifft keine Winkelabbildung, keinen Schleifen-Fixpunkt, kein
Frame-Bild). Keine frühere Rechnung zu dyadischen Gittern.

## Gitter (festgelegt)
Eine Stellung ist π/4 (8 Stellungen je Umlauf). „Jedes Bit verdoppelt“ heißt: Stufe k teilt die Stellung in 2^k, k = 0 … 8 (8 Bit).
- **Gitter A** (Winkel ohne ℤ₃): Q ∈ (π/4)·2^(−k)·ℤ.
- **Gitter B** (Winkel mit ℤ₃-Klasse, die Spektralvariable ist 3δ): Q ∈ (π/12)·2^(−k)·ℤ.
Jede Größe wird auf beiden Gittern geprüft (18 Gitter je Größe).

## Größen und Fehler (festgelegt)
| Größe | Wert | σ |
|---|---|---|
| φ = x (geladene Leptonen) | 0,0395773407 | 7,8·10⁻⁷ |
| x_ν (aus R) | 0,04336 | 0,00213 |
| θ₁₂ (sin² = 0,3036 ± 0,0064) | arcsin √0,3036 | fortgepflanzt |
| θ₁₃ (sin² = 0,02248 ± 0,00056) | arcsin √0,02248 | fortgepflanzt |
| θ₂₃ (sin² = 0,470 ± 0,015) | arcsin √0,470 | fortgepflanzt |
| δ_CP | 212° ± 34° (symmetrisiert) | |
| arctan β_sym, arcsin β_sym (Lesarten, gesetzt) | β = 0,5494056 | σ_β = 0,00018 (2σ-Fenster aus k358) |

## Teil A (nicht blind)
Die Baumwerte π/12 und π/6 liegen auf Gitter B bei k = 0 (bzw. π/6 = 2·π/12), und die Achteldrehungen aus H171 liegen auf Gitter A bei k = 0. Das ist
bekannt und wird nur als Kontrolle ausgegeben. Offenlegung: Vor dem Schreiben habe ich φ/(π/12) = 0,1512 gesehen (aus H232), die gröbsten Stufen von
Gitter B (k ≤ 2) treffen φ also sicher nicht. Feinere Stufen und alle anderen Größen sind nicht vorab gerechnet.

## Teil B (blind): Einrasten
Für jede Größe Q, jedes Gitter und jedes k: Treffer, wenn |Q − nächster Gitterpunkt| ≤ 2σ_Q **und** der Gitterabstand Δ ≥ 10σ_Q (sonst ist das Gitter zu fein,
um etwas zu sagen). Zufallswahrscheinlichkeit je Versuch p = 4σ_Q/Δ; Erwartung λ = Σp über alle zulässigen Versuche; Poisson-Wahrscheinlichkeit für
die beobachtete Trefferzahl.

## Teil C (blind): φ als Rastfehler
Ist φ der Rest eines natürlichen stetigen Winkels nach dem Einrasten auf die nächste Stellung? Kandidaten (festgelegt): arctan β_sym, arcsin β_sym,
arccos β_sym, ε₀ = artanh β_sym, 2ε₀, 1/γ_L, β_sym (als Bogenmaß gelesen). Rest r = A mod s und s − r für s = π/4 und s = π/12 (28 Reste).
Treffer, wenn |r − x| ≤ 2σ_x. Locker: innerhalb 1 % (mit Zufallserwartung bei gleichverteilten Resten).

## Entscheidung
- **trägt:** φ rastet ein (B-Treffer für φ mit Poisson-p < 0,05 über die φ-Versuche) oder C-Treffer innerhalb 2σ_x.
- **trägt teilweise:** φ nicht, aber die übrigen Größen rasten zusammen häufiger ein als der Zufall (p < 0,05), oder C nur locker mit p < 0,05.
- **widerlegt:** sonst.

## Gesetzt
8 Stellungen = π/4 (Lesart der Rotoren), Verfeinerung durch Halbierung bis 8 Bit, ℤ₃-Teilung für δ-artige Winkel, Winkellesarten von β_sym, Kandidatenliste C.
