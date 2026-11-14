# Ergebnis H104: Bei freiem Flächenspektrum ist das Zählregel-Paar nicht mehr das einzige (widerlegt)

**14.11.2026.** Vorab-Notiz `Vorab_Notiz_H104_Zaehlregel_Flaechenspektren.md` (Commit c58f449), Skript
`k226_test_h104.py`, Ausgabe `k226_out.txt`. **Status: H104 widerlegt.** Nicht blind gegenüber den Daten.

## Zwei Läufe (offengelegt)
- **Lauf 1 war fehlerhaft.** Der Löser (`findroot`, Anderson) fand für sieben Regeln mit Gewicht 2j + 1 keine Lösung,
  obwohl sie eine haben; darunter (W, A, 2j + 1) mit γ = 0,2741, die H98 kennt. Mit nur 16 Regeln und 120 Paaren
  meldete dieser Lauf „bestätigt“. Die Ausgabe liegt als `k226_out_lauf1_fehlerhaft.txt` bei.
- **Lauf 2 gilt.** Der Löser ist eine Bisektion (die Summe fällt streng monoton in γ). Regelraum, Fenster und
  Kriterium sind unverändert die der Vorab-Notiz. Die neun W-Regeln aus H98 (`k218_out.txt`) kommen in Lauf 2 alle vor
  und stimmen auf die angegebenen zwölf Stellen überein.

## Ergebnis
Im Regelraum S′ gibt es 23 verschiedene Regeln und 253 gültige Paare, γ_L von 1,006 bis 5,31.

| Fenster | Paare im Fenster |
|---|---|
| Leptonfenster β ∈ [0,545; 0,570] | 13 |
| m_W, PDG 2025, 2σ | **2** |
| Ω_M, DESI DR2, 2σ | 17 |
| alle drei | **2** |

| M | T | γ_L | β | m_W / GeV | z(m_W) | Ω_M |
|---|---|---|---|---|---|---|
| W, A, g = 2 | W, S½ | 1,864700 | 0,54941 | 80,3615 | −0,58 | 0,3018 |
| L, A, g = 2j + 1 | E, H, g = 2j + 1 | 1,864824 | 0,54943 | 80,3627 | −0,49 | 0,3019 |

Nach dem Kriterium **widerlegt**: Ein weiteres Paar trifft alle drei Fenster.

## Das zweite Paar
Beide Werte sind geschlossen angebbar:
- (L, A, 2j + 1): Σ (k + 1) xᵏ = 1 mit x = e^{−πγ} gibt x = 1 − 1/√2, also γ = −ln(1 − 1/√2)/π = 0,390868.
- (E, H, 2j + 1): Σ 2n yⁿ = 1 mit y = e^{−2πγ} gibt y = 2 − √3, also γ = −ln(2 − √3)/(2π) = 0,209600.
- γ_L = 2 ln(1 − 1/√2)/ln(2 − √3) = 1,864824.

Die beiden γ_L unterscheiden sich um 1,2·10⁻⁴, in m_W um 1,2 MeV. Eine Messung müsste die W-Masse auf weit unter
1 MeV kennen, um sie zu trennen. Ein physikalischer Grund für das zweite Paar ist nicht bekannt: Es mischt zwei
Spektren (linear für M, äquidistant für T) und zählt alle m. Ich lese es als Zufallstreffer.

## Was das bedeutet und was nicht
- **Die Sonderstellung aus H98 hängt am festgehaltenen Spektrum.** Lässt man das Flächenspektrum frei, wie es die
  Lesart „frame-abhängiges Flächenquantum“ (r10.3) nahelegt, trifft ein zweites Paar dieselben drei Fenster.
- **Die Häufigkeit passt zum Zufall.** Im m_W-Fenster liegen 2 von 253 Paaren (0,8 %). Das Fenster ist in γ_L etwa
  ± 0,003 breit; bei 253 Paaren zwischen 1 und 5,3 erwartet man bei gleichmäßiger Streuung rund 0,4 Paare, in der
  dichter besetzten Gegend um 1,9 mehr. Ein oder zwei Treffer sind damit nicht auffällig.
- **H98 bleibt in seinem Regelraum bestätigt.** H104 ist ein eigener Test und ändert das nicht. Geändert ist das
  Gewicht des Arguments: Eine Seltenheitsaussage, die bei einer naheliegenden Erweiterung des Raums nicht hält,
  stützt die Zählregel kaum.
- **Die Vorhersagen H15, H46 und H96 sind nicht berührt.** Sie hängen an γ_L = 1,8647, nicht an der Einzigkeit des
  Paars.
- **Meine Erwartung war ungenau:** In der Vorab-Notiz standen „einige hundert Paare“ und „knapp ein weiteres Paar im
  m_W-Fenster“, beide Ausgänge etwa gleich wahrscheinlich. Es sind 253 Paare und genau ein weiteres.
- OP1 bleibt offen; ein Grund für die Zählregel je Frame fehlt weiter. Guards unverändert.

## Zurückgestellte Ideen
Auslöser 3 von I1 (eine Rechnung berührt β_sym als Verhältnis γ_BI/γ_string) trifft zu. I1 wurde am 14.11. in anderem
Zusammenhang schon verfolgt (`op3_i1_string_bridge_2026_11_14.md`). Als möglicher Ausweg für OP1 dem Autor genannt,
nicht umgesetzt.
