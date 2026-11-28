# Vorab-Notiz H216 (k429): Ziehen die Umkehrschleifen β_sym an?

Stand 28.11.2026, vor der Rechnung festgeschrieben. Auftrag des Autors vom 28.11.2026, 00:08 („alles drei“), Folgetest 1 zu H215.

## Frage

H215 hat nachträglich gefunden, dass β_sym fast ein **abstoßender** Fixpunkt von E: b ↦ 2^(1−γ(b)) ist. Dieser Fixpunkt liegt bei
0,5493155 mit E′ = −1,716. Die Umkehrschleife E⁻¹ zieht denselben Punkt an. H216 testet das jetzt vorab für die ganze Klasse: Hat eine
Umkehrschleife β_sym exakt als anziehenden Fixpunkt, und häufen sich die Umkehrschleifen bei β_sym stärker als bei Kontrollwerten?

## Klasse und Zählung

- **Umkehrklasse:** Wörter der Länge 1 bis 5 über den Umkehrungen der neun H215-Operationen:
  - H⁻¹ mit zwei Ästen (1 ± √(2y − 1))/2;
  - S⁻¹ = R und R⁻¹ = S;
  - C⁻¹ = C;
  - A⁻¹ = W und W⁻¹ = A;
  - G⁻¹(y) = √((1 − y)/(1 + y));
  - D⁻¹ mit zwei Ästen sin(½ arcsin y) und cos(½ arcsin y);
  - E⁻¹(y) = √(L/(2 + L)) mit L = −log₂ y.
- **Gleichwertigkeit (exakt, vor der Rechnung):** x* ist genau dann anziehender Fixpunkt eines Astes von f⁻¹, wenn x* abstoßender Fixpunkt
  von f ist, denn (f⁻¹)′(x*) = 1/f′(x*). Gezählt werden deshalb die Wörter f der H215-Klasse mit einem Fixpunkt im Fenster und
  |f′(x*)| > 1 + 10⁻⁹. Die Äste eines Wortes zählen zusammen als ein Wort.
- **Fenster, Gitter, Kontrollen und Ausschluss** wie bei H215: relative Breite ±6,5·10⁻⁴ (k358), 20 001 Gitterpunkte, 2000 Zufallsziele in
  [0,35; 0,75] mit Startwert 215, benannte Werte ½, ⅓, 1/√3, 1/√2, 1/γ_L, 2^(1−γ_L), identitätsartige Wörter ausgeschlossen.
- **Exakt** heißt |f(β_sym) − β_sym| < 10⁻²⁰ bei 30 Stellen.

## Kriterium (ohne das Einzelwort E, das bekannt ist)

- **trägt:** mindestens ein exakter Treffer;
- **trägt teilweise:** kein exakter Treffer, aber N_inv(β_sym) liegt über dem 99. Perzentil der Zufallskontrollen;
- **widerlegt:** sonst.

## Nicht blind

- Teil a, E⁻¹ allein, ist bekannt: Der Fixpunkt liegt im Fenster, 9,0·10⁻⁵ unter β_sym, also nicht exakt. Er wird nur berichtet.
- Bekannt ist auch, dass die Klasse algebraische Werte bevorzugt (H215: N(½) = 530).
- Teil b, die Zählung über alle Umkehrwörter, ist blind.
- **Erwartung (keine Rechnung):** widerlegt, weil β_sym über eine unendliche Summe festgelegt ist.

## Prüfwege

Hauptrechnung in Python `k429_test_h216.py` mit Ausgabe `k429_out.txt`. Sie wertet für H216 und H217 einen gemeinsamen Fixpunkt-Katalog
aus, der in `k429_katalog.npz` zwischengespeichert, aber nicht eingecheckt wird. Gegenprobe in Wolfram `k429b_gegenprobe.wl`: Sie
rechnet die Umkehrwörter der Länge ≤ 2 direkt aus den Umkehroperationen samt Ästen und prüft so die Gleichwertigkeit. Ordner:
`notes/research/hilbert_shift_felder_2026_11_24/stabilitaet_folgetests_h216_h218/`.
