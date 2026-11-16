# OP1: Woher käme die Statistik je Frame? Rückwärtssuche zu (S2)

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind** (alle Ergebnisse stehen analytisch fest), ohne Kriterium, keine
H-Nummer. Auftrag des Autors: „Ja, OP1“. Nach AGENTS ist bei Wiederaufnahme die Suchrichtung zu prüfen; hier rückwärts: Ziel und
notwendige Bedingungen zuerst, dann Kandidaten aus dem Bestand. Skript `statistics_backward.py`, Ausgabe
`run/statistics_backward_stdout.txt`. OP1 bleibt offen.

## Vorwissen geprüft
- **H98 (r09.1):** Nur das Paar „M alle Spins, Gewicht 2; T nur j = ½“ trifft alle drei Datenfenster. **H104 (r14.1):** Bei freiem
  Flächenspektrum gibt es ein zweites Paar (widerlegt).
- **r09.2, r10.2–r10.4:** P1 (Sättigung) gibt das Gewicht 2; P2 (Energie) trägt nicht; eine T-Regel muss eine eingeschränkte,
  nicht umkehrbare Auslesung sein; die Regel ist gleichwertig zu einem frame-abhängigen Flächenquant.
- **r17.3 (`../op1_frame_irreducibility_2026_11_15/`):** Unter Annahme (A) wirken die Frame-Abbildungen nur bei j = ½ irreduzibel;
  „T irreduzibel, M invariantes Extremdublett“ gibt das Paar aus H98.
- **r17.5:** Als Penrose-Bündel gelesen: bosonische Stränge geben alle j (M), fermionische nur j = ½ (T); ausgerichtete Bündel sind das
  Extremdublett. Setzungen (S1) Strang = Quant von χ, (S2) T fermionisch, M bosonisch, (S3) M zählt nur ausgerichtete Bündel.
- **r17.6:** Die Begründung von (S2) über R² = −1 ist zurückgenommen (sie führt auf Kramers); die Frame-Abbildungen sehen die Statistik
  nicht.
- **Hauptkorpus `thm:origin`(ii), T11:** C = ½(1 + J) „bosonisch“, A = ½(1 − J) „fermionisch“. **v4.9.0-r03.1:** Für antilineares J ist
  das eine Zerlegung in Real- und Imaginärteil. **Berichtigung zu CT-004:** T11 meint J-Parität, nicht Austausch.
- **v4.9.0-r28, r20.4:** Die Tachyon-Abbildung vertauscht die Ports C und A; M liest C, T liest A. **r23.2:** Kompensation macht rein.
- **I1 und CT-004** (`../op1_i1_string_endpoints_2026_11_15/`): T zählt Endpunkte einzelner offener Strings.

## Ziel und notwendige Bedingungen
Ziel ist ein Grund für (S2). Ein Mechanismus muss
- **(N1)** auf dem **Austausch** von Strängen wirken (Sym gegen Λ), nicht nur auf einem einzelnen Strang;
- **(N2)** M und T unterscheiden, also von der Tachyon-Abbildung R vertauscht werden, wie die Ports C und A;
- **(N3)** nicht auf die Kramers-Regel führen (alle halbzahligen j; β = 0,337, ausgeschlossen).

## Kandidaten
| Kandidat | (N1) Austausch | (N2) von R vertauscht | (N3) | Urteil |
|---|---|---|---|---|
| K1: Frame-Abbildungen je Strang | nein: U^{⊗n} vertauscht mit dem Strangtausch (n = 2, 3 geprüft) | ja | – | scheidet aus (wie r17.6) |
| K2: R² = −1 | nein | – | verletzt (Kramers) | scheidet aus (r17.6) |
| K3: Port-Parität J (C bosonisch, A fermionisch) | nein: J_B wirkt auf (F₊, F₋) eines Feldes als σ_y (F₊ ↦ iF₋, F₋ ↦ −iF₊), nach Umphasung als Tausch der beiden Helizitätskomponenten **eines** Strangs | ja (r28) | – | scheidet aus: J-Parität ist ein Einzelstrang-Begriff |
| K4: Kompensator strangweise | nein: C^{⊗n} bildet jeden Bündelzustand auf das ausgerichtete Bündel \|c⟩^{⊗n} ab, das in Sym^n liegt; A^{⊗n} ebenso auf \|a⟩^{⊗n}; nie Λ^n | ja | – | gibt kein (S2), aber eine Lesart für (S3) |

## Ergebnisse
1. **Kein Kandidat aus dem Bestand erfüllt (N1) und (N2) zugleich.** Alles, was die Tachyon-Abbildung vertauscht (Frame-Abbildungen,
   Ports, Kompensator), wirkt strangweise und vertauscht deshalb mit dem Austausch zweier Stränge. Sym^n und Λ^n bleiben unter jeder
   solchen Abbildung getrennt. (S2) ist damit nicht nur unbegründet, sondern aus der Frame- und Portstruktur des Bestands **nicht
   begründbar**: Dafür bräuchte es eine Auslesung, die auf den Austausch wirkt.
2. **Die Port-Parität des Hauptkorpus ist kein Austausch.** J_B tauscht die beiden Helizitätskomponenten eines Feldes (bis auf Phasen).
   „C bosonisch, A fermionisch“ in `thm:origin`(ii) und T11 ist also, wie die Berichtigung zu CT-004 sagt, eine Einzelobjekt-Parität.
   Auf einem Bündel wirkt sie strangweise.
3. **Nebenbefund zu (S3):** Strangweise Kompensation macht aus jedem Bündel ein ausgerichtetes Bündel, \|c⟩^{⊗2j} oder mit dem
   Partnerport \|a⟩^{⊗2j}. Das sind genau die beiden Zustände \|j, ±j⟩ entlang der Portachse, also das Extremdublett von M mit Gewicht 2.
   (S3) „M zählt nur ausgerichtete Bündel“ lässt sich so als „M liest jeden Strang durch einen Port“ lesen; P1 (Sättigung) und die
   Selektivität des Kompensators (r23.2) sind dann dieselbe Eigenschaft. Das ist eine Lesart, keine Herleitung, und sie erklärt nicht,
   warum M beide Ausrichtungen zählt.

## Was offen bleibt, und ein möglicher Ausweg
- (S2) braucht eine Auslesung, die Stränge austauscht. Im Bestand gibt es keine. Weitere Varianten mit derselben Voraussetzung (eine
  Statistik aus Frame- oder Portabbildungen) sind nach diesem Befund ausgeschlossen.
- **Auslöser I1-3 ist berührt** (β_sym als γ_BI/γ_string). Die Idee I1 bietet einen Ausweg ohne Statistik: Zählt T Endpunkte einzelner
  offener Strings, dann trägt jeder Endpunkt genau **einen** Strang in der Fundamentaldarstellung, und j = ½ folgt aus der Einzahl,
  nicht aus fermionischem Austausch. Der Preis ist die bekannte Setzung „T = String-Sektor“ (Guard 1 von CT-004, ohne Stütze im
  Bestand). Dem Autor als möglicher Ausweg vorgelegt.
- H104 bleibt bestehen: Mit anderem Flächenspektrum gäbe jede dieser Regeln andere Werte.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert. Kein Test.
