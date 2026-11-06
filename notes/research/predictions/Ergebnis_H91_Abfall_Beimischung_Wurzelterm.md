# Ergebnis H91: ungültig nach Kriterium a (Planungsfehler); auch b–d wie formuliert verfehlt; die Steigung schwankt und steigt bis kΔ = 60 nur auf 3,026

Vorab-Notiz `Vorab_Notiz_H91_Abfall_Beimischung_Wurzelterm.md`, Commit `a49ed7e` (teilweise nicht blind). Code `k206_abfall_wurzelterm.py` (Python/scipy, lokal; Ausgabe `k206_out.json`, Laufzeit 81 s). Offenlegung: Im lokalen Python fehlte scipy. Es wurde nachinstalliert (scipy 1.18.1) und der Lauf wiederholt, ohne Änderung am Code.

## Ergebnisse
- **H91a nicht erfüllt, Ursache ein Planungsfehler.** Die beiden Konturen (h = 0,90 und 0,95·πΔ/2) stimmen für alle kΔ ≤ 60 auf 1·10⁻¹⁰ überein, weit unter 10⁻⁶. Die Abweichungen von den H87-Werten sind −9,5·10⁻⁵, −1,2·10⁻⁴, +1,1·10⁻⁵, +1,0·10⁻⁴, −3,2·10⁻⁴ (kΔ = 10–30) und liegen damit über dem Kriterium 10⁻⁵. H87 hat seine Werte aber nur vierstellig festgehalten (z. B. 1,304·10⁻³⁷, Rundung bis 3,8·10⁻⁴). Alle Abweichungen liegen innerhalb dieser Rundung. Das Kriterium war schärfer als die verfügbaren Vergleichswerte. **Nach der Vorab-Notiz gelten b–d damit als ungültig, nicht als widerlegt.** Ihre Zahlen werden trotzdem berichtet; wie formuliert verfehlen sie die Kriterien ohnehin.
- **H91b (wie formuliert verfehlt):** Der Fit ln|C| = c₀ + c₁√x + q ln x − s x auf [20, 60] gibt s = 3,0486, 3,0 % unter π (Kriterium 1 %). Dazu kommen c₁ = −0,38, q = 3,16 und ein großer Rest von 0,020 (rms in ln|C|).
- **H91c (wie formuliert verfehlt):** Bei s = π ist der Rest mit Wurzelterm 0,022, ohne 0,14, also nur das 6,5-Fache (Kriterium 10).
- **H91d (wie formuliert verfehlt):** Die Steigung zwischen kΔ = 50 und 60 ist 3,021, 3,8 % unter π (Kriterium 3 %).
- Beide Drehsinne geben dieselben Zahlen (siehe unten).

## Lokale Steigungen −Δln|C|/ΔkΔ (Drehsinn +, Schritt 2,5)
| kΔ | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 |
|---|---|---|---|---|---|---|---|---|---|---|
| Steigung | 2,934 | 2,908 | 2,948 | 2,982 | 2,993 | 2,993 | 3,000 | 3,011 | 3,020 | 3,026 |

Die Steigung steigt nicht gleichmäßig. Sie hat flache Stellen und kleine Rückgänge (bei 17,5–20, bei 35–40), überlagert von einem langsamen Anstieg (etwa 0,0017 je Einheit kΔ zwischen 50 und 60). Ein glatter Vorfaktor aus Potenz und Wurzelterm beschreibt das nicht. Der große Fit-Rest von 0,02 kommt von diesen Wellen. Ob die Steigung gegen π läuft, lässt sich aus dem Bereich bis 60 nicht entscheiden.

## Nachträglich (nicht vorregistriert)
- **|C| ist für beide Drehsinne gleich:** Die Differenz in ln|C| beträgt ≤ 10⁻¹⁰ bei kΔ = 10–60 und ≤ 3·10⁻¹⁰ bei kΔ = 0,5, 2, 5 (auch auf der reellen Achse). Die Asymmetrie der Drehsinne aus H86d betrifft also nur D, nicht C. Eine Herleitung dieser Gleichheit fehlt.
- **Lesart der Wellen:** Wellen in der lokalen Steigung deuten auf zwei sich überlagernde Beiträge hin. Kandidaten sind die beiden Umkehrpunkte nahe dem Pol vierter Ordnung des effektiven Potentials oder weitere Pole von sech² bei iπΔ(n + ½). Das ist eine Vermutung, nicht geprüft.

## Folge
- Die Zahlen bis kΔ = 60 sind gesichert (zwei Konturen auf 10⁻¹⁰, verträglich mit H87).
- Der Abfall ist exponentiell mit einer Rate nahe 3 je Einheit kΔ, die bis 60 auf 3,03 steigt. Die Abschneideskala ≈ 1/(πΔ) aus r86 bleibt als Größenordnung richtig.
- **Ob der asymptotische Exponent genau π ist, bleibt offen.** Ein glattes Fit-Modell trägt wegen der Wellen nicht. Ein neuer Test bräuchte eine analytische Vorhersage des Vorfaktors (lokales Problem am Pol, Stokes-Konstante) statt eines Fits, oder deutlich größere kΔ.
- Für die physikalische Aussage (die Beimischung verschwindet oberhalb von 1/Δ, Δ frei) ändert sich nichts.
