# Ergebnis H233 (k447): Die feinen Winkel rasten nicht auf 8 Stellungen ein; φ liegt mindestens 392σ neben jedem Gitterpunkt

**Datum:** 2026-11-28. **Vorab:** `Vorab_H233_Einrastung_acht_Stellungen.md` (Commit 7ff9745, vor der Rechnung). **Urteil: widerlegt.**
**Werkzeuge:** Python (`k447_test_h233.py` → `k447_out.txt`), Wolfram unabhängig mit exakten Eingaben (`k447b_gegenprobe.wl` → `k447b_out.txt`); alle Reste,
Treffer und Zufallserwartungen stimmen überein. Qiskit nicht einschlägig. Teil A nicht blind, B und C blind.

## Frage (F18)
Marc: „8 Bit, jedes Bit trägt doppelt so viel“ und „unsere Rotoren haben nur 8 Positionen“. Rasten die feinen Winkel auf ein Gitter aus 8 Stellungen (π/4)
mit Halbierung bis 8 Bit ein (Gitter A: (π/4)·2^(−k); Gitter B mit ℤ₃-Teilung: (π/12)·2^(−k); k = 0 … 8)?

## Ergebnis
| Teil | Befund | Kriterium | Entscheidung |
|---|---|---|---|
| A (nicht blind) | Baumwerte π/12, π/6, π/4 liegen auf Gitter B bei k = 0 (1, 2, 3 Stellungen); die Achteldrehungen aus H171 auf Gitter A | Kontrolle | bestätigt (bekannt) |
| B, φ | kein Treffer auf 18 Gittern; nächster Rest −3,06·10⁻⁴ rad bei k = 8 (13·π/1024 bzw. 39·π/3072) = **−392σ** | Treffer mit p < 0,05 | **nein** |
| B, übrige | 8 Treffer zu 3 verschiedenen Gitterpunkten: θ₂₃ ≈ π/4 (−2,0σ), θ₁₂ ≈ 3π/16 (−0,8σ), θ₁₃ ≈ 3π/64 (+1,7σ); x_ν, δ_CP, arctan β, arcsin β ohne Treffer (β-Lesarten ≥ 3,6σ). Zufallserwartung 5,7, P(≥ 8) = 0,22 | p < 0,05 | nein (Zufall) |
| C | φ als Rest eines natürlichen Winkels nach dem Einrasten: nächster β (Bogenmaß) mod π/12, −35 % (−17 655σ); kein Rest innerhalb 1 % | Treffer 2σ oder locker mit p < 0,05 | nein |

**Gesamturteil nach Vorab: widerlegt.**

## Lesart
- **Die groben Stellungen rasten, die feinen Winkel nicht.** Die Baumwerte des Leptonbilds (π/12, π/6 und die Achteldrehungen) sind genau Stellungen eines
  8er-Rotors mit ℤ₃-Teilung; das war bekannt (H167, H171) und passt zu Marcs Bild. Der Versatz φ = 0,0396 liegt aber zwischen den Stellungen, auch nach acht
  Halbierungen noch 392σ vom nächsten Punkt. Ein 8-Bit-Rotor kann φ nicht als Stellung tragen; φ ist ein stetiger Rest.
- **Mischungswinkel.** θ₂₃ nahe π/4 ist die bekannte Baumvorhersage (TM1, H173); θ₁₂ nahe 3π/16 und θ₁₃ nahe 3π/64 sind bei den heutigen Fehlern kein Befund
  (gleich viele Treffer erwartet der Zufall). Die Gitter sind verschachtelt, daher zählen Treffer und Erwartung jeden Punkt mehrfach; das Urteil hängt daran nicht.
- **Für F18:** Die Einrastung legt die Baumwerte fest, nicht die feinen Winkel. F18 ist damit beantwortet (nein für die feinen Winkel).

## Hergeleitet, gesetzt, nachträglich
- **Gerechnet:** Reste aller Größen auf allen Gittern (exakt in Wolfram), Zufallserwartung, Rastfehler-Kandidaten.
- **Gesetzt:** 8 Stellungen = π/4, Halbierung bis 8 Bit, ℤ₃-Teilung, Winkellesarten von β_sym, Kandidatenliste C, Datenwerte (JUNO θ₁₂, NuFIT θ₁₃, θ₂₃, δ_CP).
- **Nachträglich:** Die Mehrfachzählung bei verschachtelten Gittern war in der Vorab-Notiz nicht bedacht; ohne sie (3 Punkte) bleibt das Ergebnis Zufall.

## Grenzen
Nur dyadische Verfeinerung; andere Teilungen (z. B. durch 3 je Stufe oder die Clifford-Stunde n + 4) nicht gerechnet. Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H233_Einrastung_acht_Stellungen.md`, `k447_test_h233.py`/`k447_out.txt`, `k447b_gegenprobe.wl`/`k447b_out.txt`, `README.md`.

Vergeben: H233, k447. Nächste frei: H234, k448 (vor Vergabe gegen `main` prüfen).
