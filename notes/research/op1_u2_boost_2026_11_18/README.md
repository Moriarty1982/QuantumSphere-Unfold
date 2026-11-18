# OP1: Liest ein geboosteter Beobachter an einer Punktierung nur Extremzustände? (Erkundung, nicht blind, 18.11.2026)

**Ergebnis in einem Satz:** Nach der vorab festgelegten Lesart **graduell.** Ein Boost mit der Rapidität des Frames M entlang der Horizontnormalen
stört die Extremzustände |k, ±k⟩ am wenigsten, er wählt sie aber nicht aus. U2 folgt aus Lesart (B) allein nicht.

Auftrag des Autors: „U2 unter (B) prüfen“. Verfahren vor der Rechnung festgelegt: `Methoden_Notiz.md` (Commit 4ee7618). Skript `k236_u2_boost.py`,
Ausgabe `run/k236_stdout.txt`. Keine H-Nummer.

## Aufbau (kurz)
Punktierung mit Spin k als niedrigster Block der SL(2,ℂ)-Hauptreihe (k, ρ), γ = γ_M = 0,237533; Boost e^{−iηK₃} entlang der Normalen
(Naimark-Form); Verbleib P_m = |⟨k,m|e^{−iηK₃}|k,m⟩|² und Dispersion D_m = ⟨(K₃ − γL₃)²⟩. Abschneiden bei j ≤ k + 60, gleich mit k + 120 (< 10⁻⁹).

## Ergebnis bei η_M = artanh β_sym = 0,6175 (ρ = γ(k+1); mit ρ = γk um weniger als 0,01 anders)
| k | P(±k) | größtes P mit \|m\| < k | Abstand |
|---|---|---|---|
| ½ | 0,820 | – | – |
| 1 | 0,789 | 0,728 | +0,06 |
| 3/2 | 0,769 | 0,672 | +0,10 |
| 2 | 0,756 | 0,636 | +0,12 |
| 5/2 | 0,746 | 0,610 | +0,14 |
| 3 | 0,739 | 0,592 | +0,15 |

- In jeder Zeile haben die Extremzustände das größte P und die kleinste Dispersion. Die Reihenfolge wird also bestätigt, wie analytisch erwartet
  (Faktor √((k+1)² − m²) der Leckage in den Block k + 1).
- Die Schranken für „scharf“ (P(±k) ≥ 0,9 und P ≤ 0,5 für |m| < k) werden in beide Richtungen verfehlt: Extremzustände verlieren schon bei η_M
  18–26 %, die übrigen behalten 49–73 %.
- Auch für die Extremzustände gilt K = γL nicht scharf (D(½) = 0,53): Die Simplizität ist schwach, wie in der EPRL-Literatur.

## Nachträglich (nach dem Sehen der Ausgabe)
- Die Trennung wächst mit der Rapidität: bei η = 1,5 und k = 3 ist P(±3) = 0,21 gegen P(m = 0) = 0,02, also Faktor 10. Bei η → ∞ blieben relativ nur
  die Extremzustände; das wäre die masselose Grenze von (S1′). Für die endliche Rapidität von M ist es nur eine Bevorzugung.
- Transversale Boosts zeichnen nichts aus: Über drei Komponenten summiert ist die Leckage nach Wigner–Eckart von m unabhängig (nicht gerechnet).
  Eine Auszeichnung braucht also den Boost **entlang der Normalen**; das ist eine Zusatzannahme (Bianchis Rindler-Horizont nimmt sie).

## Lesart
- U2 bleibt eine Lesart. Lesart (B) mit Boost entlang der Normalen gibt den Extremzuständen den Vorzug, zählt die übrigen aber nicht weg. Gewicht 2
  bräuchte eine Auswahlregel wie „der Frame zählt nur den am wenigsten gestörten Zustand je Richtung“, die selbst wieder gesetzt wäre.
- Damit ist von den drei Kennzeichnungen der Extremzustände (Unschärfe, Invarianz, Helizität) keine durch (B) erzwungen. Am nächsten kommt die
  Helizität, aber nur in der masselosen Grenze η → ∞, die M nicht hat.
- OP1 offen; H98, H102, H112 unverändert.
