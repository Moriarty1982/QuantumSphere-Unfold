# Erkundung: Trägt die Brücke in P2? (Zählregel je Frame über Unruh-Temperatur und Modularfluss)

**7. November 2026. Status: Erkundung, analytisch, ohne Kriterium.** Anlass: offene Brücke aus v4.10.0-r09.2. Dort soll der Tachyon-Frame
„am Boden“ nur die kleinste Flächenanregung zählen (j = ½), der Materie-Frame alle Stufen. Die Brücke zwischen der Energie des Tachyons am
Boden (r63.3) und der Horizontenergie eines Beobachters war ungeprüft.

## Vorwissen geprüft
- v4.10.0-r09.2, `Erkundung_Zaehlregel_Prinzip.md`: Prinzip P (P1 Unschärfesättigung, P2 Energiebedingung), Brücke über das lokale erste Gesetz.
- v4.10.0-r06.1, r07.2: Dorau–Much-Kette; Modulargruppe des Vakuums = Boost (KMS bei 2π); die Tachyon-Abbildung z ↦ iz vertauscht mit dem
  Boost und lässt das Vakuum fest (r20.1), relative Entropie und Fluss sind in M und T gleich.
- v4.9.0-r64.1(b): unter der Zähl-Lesart sitzt der ganze Frame-Unterschied in γ, nicht in ħ, G_N, ℓ_P.
- v4.10.0-r07.4: Normierung des Flächengesetzes fällt im Verhältnis heraus.
- Literatur: Frodden–Ghosh–Perez (2013), lokales erstes Gesetz E = A/(8πℓ) für einen Beobachter im Abstand ℓ, Temperatur T_U = 1/(2πℓ);
  Ghosh–Perez (2011): Zustandszählung als Statistik der Durchstoßpunkte bei dieser Temperatur.

## 1. Die Zählgleichung ist eine Unruh-Statistik, und ℓ fällt heraus
Ein Durchstoßpunkt mit Spin j trägt die Fläche 8πγ a(j) (ℓ_P = 1), nach dem lokalen ersten Gesetz also die Energie E_j = γ a(j)/ℓ. Mit der
Unruh-Temperatur des Beobachters ist der Boltzmann-Exponent
  E_j / T_U = 2πℓ · γ a(j)/ℓ = 2πγ a(j),
**unabhängig vom Abstand ℓ** (numerisch bestätigt für ℓ = 0,5 bis 1000). Die Zählgleichung Σ g(j) e^{−2πγ a(j)} = 1 ist genau diese Statistik. Alle
statischen Beobachter, egal wie nah am Horizont, zählen deshalb gleich: Eine höhere oder niedrigere Energie verschiebt E_j und T_U im selben
Verhältnis.

## 2. Der Tachyon-Frame hat dieselbe Modularstruktur
Nach r07.2 vertauscht die Tachyon-Abbildung mit dem Boost und lässt das Vakuum fest. Ein T-Beobachter sieht also dasselbe Vakuum mit derselben
Modulargruppe, also dieselbe KMS-Temperatur 1/(2πℓ). Ein „Boden“ im Sinn von r63.3 (Teilchenenergie E → 0 bei festem Invariant) ist eine
Eigenschaft eines Tachyon-Teilchens, keine Eigenschaft des Zustands, den ein Beobachter am Horizont sieht.

## Ergebnis
- **Die Brücke in P2 trägt in dieser Form nicht.** Über das lokale erste Gesetz und die Unruh-Temperatur zählen M und T gleich: ℓ fällt heraus, und
  die Modularstruktur ist in beiden Frames dieselbe. Die Lesart „T erreicht nur die kleinste Anregung, weil es am Boden sitzt“ bräuchte einen
  T-Zustand, der bezüglich des Boosts nicht thermisch ist (etwa Temperatur null); das Vakuum ist es nicht.
- **Was übrig bleibt, ist r64.1(b) in schärferer Form.** Wenn beide Frames dieselbe Statistik und dieselbe Geometrie sehen (r07.2) und beide
  S = A/4 erfüllen (r06.2), kann sich nur das Flächenquantum unterscheiden: γ_T = γ_string, γ_M = γ_BI. Die Zählregel je Frame ist dann gleichwertig
  mit einem **frame-abhängigen Barbero–Immirzi-Parameter**: Das kleinste Flächenquantum ist im T-Frame um den Faktor γ_L kleiner als im M-Frame.
  Die klassische Fläche und G bleiben gleich.
- **Folge für Prinzip P (r09.2):** P1 (Unschärfesättigung) bleibt eine Lesart; P2 als Energiebedingung ist über diesen Weg nicht gestützt und sollte
  durch die ehrlichere Form ersetzt werden: „jeder Frame hat sein eigenes Flächenquantum“. Das ist eine Annahme, keine Herleitung. Die Sonderstellung
  aus H98 bleibt davon unberührt.
- **Offene, schärfere Frage:** Warum sollte das Flächenquantum vom Frame abhängen, wenn die Geometrie frame-blind ist? Im Companion ist γ_L
  der Lorentzfaktor zwischen M und T (F1). Eine Begründung müsste zeigen, dass der Flächenoperator unter der Frame-Abbildung mit γ_L skaliert, obwohl
  der Energie-Impuls-Tensor invariant bleibt. Für die Dualitätsdrehung allein ist das ausgeschlossen (sie lässt alles Geometrische fest); es bräuchte
  den Boost-Anteil der Frame-Abbildung (T als Boden des Spiegel-Frames, r63.4), der aber den Horizont nur umparametrisiert.

## Einordnung
Das ist ein negatives Teilergebnis. Es präzisiert die Annahme Z1, statt sie zu begründen: Z1 ist gleichwertig mit γ_M/γ_T = γ_L. Die drei
Vorhersagen am γ_L-Kern (H15, H46, H96) hängen damit an der Annahme eines frame-abhängigen Flächenquantums. Ein Kandidat für die nächste Runde
(Korrektur zu r09.2: P2 über das erste Gesetz nicht tragfähig).
