# OP1: Setzung (S1) geprüft – Strang = Quant von χ? (Erkundung, nicht blind)

16. November 2026. Auftrag des Autors: „(S1) prüfen“, nach `../op1_u1_check_2026_11_16/`. Skript `s1_check.py`, Ausgabe
`run/s1_check_stdout.txt`. Keine H-Nummer.

## Vorwissen geprüft
- `../op1_frame_irreducibility_2026_11_15/README.md` (r17.3–r17.6): Annahme (A) – die Frame-Abbildungen wirken auf einer Punktierung mit Spin j
  über dieselbe SU(2) wie auf χ, als $\exp(-i\pi J_k)$; Nachtrag Penrose-Bündel: (A) folgt, wenn ein elementarer Strang ein Quant von χ ist =
  **(S1)**. Daraus r17.3: T irreduzibel → j = ½, M invariantes Extremdublett → Gewicht 2 (H98-Paar, γ_L = 1,864700).
- r24.4 (`../op1_i1_crossing_2026_11_16/`): T zählt Querungen, eine Querung ein Strang; braucht (S1) weiter („eine Querung = ein Quant“).
- r16.3: χ = (√s₊, √s₋) ist Lorentz-invariant; r16.3(a): ebene Wellen haben s₊ = s₋ = 0, „light has no point“; r16.3(b): R hält das
  Helizitätsvorzeichen, T und J_B kehren es um.
- `../op1_u1_check_2026_11_16/`: U1 = Helizitätsachse der Dualität.

## Ergebnis
**1. (S1)/(A) kann keine Gleichheit der Gruppen sein.** Die räumliche Drehgruppe, also die SU(2), deren Casimir die Fläche einer Punktierung gibt,
lässt s₊ und s₋ fest (500 zufällige Drehungen, Abweichung $1{,}5\cdot10^{-14}$; wie r16.3). χ ist ein Singulett dieser Gruppe. Die SU(2), in der die
Frame-Abbildungen als Pauli-Matrizen wirken, ist eine **innere** SU(2) des Dubletts (Dualität und Frame-Abbildungen), nicht die Drehgruppe der
Punktierung. (A) setzt also zwei verschiedene SU(2) gleich und braucht eine **Verriegelung** zwischen ihnen.

**2. Eine natürliche Verriegelung: masselose Stränge (S1′).** Ein masseloses Quant hat Spin parallel zum Impuls, Helizität λ = J·p̂. Bei Photonen
ist positive Helizität genau der selbstduale Anteil (F₋ = 0), also ein Pol von χ und ein Port (U1). Quert ein solcher Strang den Horizont entlang
der Normalen ν, dann ist $J_\nu=\lambda$, und die kleine Gruppe masseloser Teilchen lässt je Spin j nur **±j** zu. Das liefert beide Bedingungen
zugleich:
- U1: die Achse an der Punktierung ist die Normale, ihre Ladung die Helizität (Pol von χ, Port);
- U2: nur die Extremzustände ±j, Gewicht 2 je j, also die DL-Zählung (γ = 0,237533). Massive Punktierungen hätten 2j + 1 Zustände (GM, 0,274).

**(S1′): Ein elementarer Strang ist ein masseloses Quant, das den Horizont entlang der Normalen quert.** Dann ist die U(1)-Zählung des Frames M
keine Eichfixierung, sondern die Zustandszahl masseloser Querungen.

**3. Was (S1′) mit (A) macht: Widerspruch.** An einer festen Normalen ν (nachgerechnet an zirkular polarisierten Wellen):

| Abbildung | Helizität | Ausbreitungsrichtung (Poynting) | $J_\nu=\lambda\,(\hat p\cdot\nu)$ |
|---|---|---|---|
| R | bleibt | bleibt | bleibt |
| T | kehrt um | kehrt um | **bleibt** |
| J_B | kehrt um | kehrt um | **bleibt** |

Unter (S1′) lassen alle drei Frame-Abbildungen $J_\nu$ fest; sie wirken auf den Punktierungszustand abelsch (bis auf Phasen), nicht als
$\exp(-i\pi J_k)$ um drei senkrechte Achsen. T und J_B machen aus einem auslaufenden Strang einen einlaufenden mit umgekehrter Helizität. (A) gilt
dann nicht, und mit ihr fällt die Begründung von r17.3 für die T-Regel (Irreduzibilität). Die T-Regel stützt sich dann allein auf r24.4
(Querungen, ein Strang).

**4. Eine weitere Spannung.** Ebene Wellen sind Nullfelder und haben nach r16.3(a) keinen Punkt auf der χ-Kugel. Ein masseloser Strang ist also kein
„Quant von χ“ im Sinn eines nicht-null Feldes, sondern ein Quant des Nullsektors P. Die Zählung des Frames M wäre unter (S1′) eine Zählung von
P-artigen Querungen, abgelesen in der Helizitätsachse, die der Frame M über seinen Kompensator-Port auszeichnet. Ob das mit Konvention F verträglich
ist (M ist ein nicht-null Dublett-Zustand), ist offen.

## Folgerung
- (S1) in der Form „derselbe SU(2)“ ist nicht haltbar: χ ist unter Drehungen ein Singulett.
- (S1′) (masselose Querung entlang der Normalen) begründet U1 und U2 **zusammen** und liefert die DL-Zählung ohne weitere Wahl. Das ist die bisher
  stärkste Stütze für die Zählregel des Frames M, und sie macht den Einwand der Literatur (U(1) als Eichfixierung) gegenstandslos, falls die
  Stränge wirklich masselos sind und normal queren.
- Der Preis: (A) fällt unter (S1′), also die r17.3-Begründung der T-Regel, und die Stränge gehören zum Nullsektor P, nicht zu einem χ-Punkt.
- Damit ist OP1 an einer neuen, schärferen Stelle: **Sind die Punktierungs-Stränge masselos, und queren sie normal?** Die Literatur zur
  Horizontzählung (ob die U(1)-Zählung als masselose Helizitätszählung gelesen worden ist) ist hier **nicht geprüft**.

## Grenzen
Nicht blind: DL- und GM-Werte waren bekannt. Die Verriegelung ist eine Lesart, kein Beweis; die Tabelle unter 3 prüft nur Vorzeichen an
Vertreterwellen. OP1 offen; H98, H102 unverändert.
