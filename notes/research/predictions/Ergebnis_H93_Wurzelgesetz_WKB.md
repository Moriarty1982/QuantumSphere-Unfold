# Ergebnis H93: Die WKB-Herleitung trifft. c = 2√π Γ(3/4)/Γ(1/4)·Re√L auf 0,013 %, keine Konstante, Grenzwert −Re L/2 im vollen Problem auf ≤ 0,009. Formal ist der Test ungültig wegen einer Genauigkeitskontrolle bei Drehsinn +, kΔ = 600

Vorab-Notiz `Vorab_Notiz_H93_Wurzelgesetz_WKB.md`, Commit `a4b1d17` (teilweise nicht blind). Code `k208_wkb_pruefung.py` (Python/scipy). Ausgaben: Lauf 2 in `k208_out.json` und `k208_log.txt`, Lauf 1 in `k208_out_lauf1.json` und `k208_log_lauf1.txt`.

## Offenlegung: zwei Läufe, die Gültigkeitsbedingung ist in beiden nicht ganz erfüllt
- **Lauf 1:** Die lokale Kontrolle (Weg 0,7·h, Rand 2S) war bei Drehsinn + 0,20 (kΔ = 300) bzw. 1,0 (600), bei Drehsinn − 4,4·10⁻⁵ (600). Ursache ist der Weg 0,7·h. Er liegt bei Drehsinn + so nah an der wesentlichen Singularität von e^{λ/σ}, dass er Stellen verliert. 1,3·h und 2S weichen dort nur um 2·10⁻⁹ … 2·10⁻⁵ ab.
- **Lauf 2:** Kontrollweg 1,3·h statt 0,7·h und rtol 10⁻¹³ lokal, nach Kenntnis von Lauf 1 geändert. Die Kontrollen sind dann ≤ 3·10⁻⁹ bei Drehsinn − und bei kΔ = 300 (+), aber **1,4·10⁻⁵ bei Drehsinn +, kΔ = 600**. Das liegt über der Bedingung 10⁻⁶. Auch der Vergleich der Drehsinne (d) liegt dort bei 1,2·10⁻⁵ in ln|r|.
- **Formal sind a–d damit ungültig** (Wortlaut der Vorab-Notiz). Die folgenden Zahlen sind trotzdem berichtet. Die Abweichungen liegen um drei bis vier Größenordnungen unter den inhaltlichen Kriterien. Für Drehsinne − und für das volle Problem ist jede Kontrolle erfüllt.
- Ein dritter Bedienfehler (Lauf 2 zunächst im falschen Ordner gestartet, nicht gerechnet) hat keine Zahlen erzeugt.

## Zahlen (Lauf 2)
| | Drehsinn + | Drehsinn − | Kriterium |
|---|---|---|---|
| a: Steigung (ln|r(600)| − ln|r(300)|)/(√600 − √300) | 1,808965 (−0,013 %) | 1,808966 (−0,013 %) | c = 1,809205 ± 0,3 % |
| b: ln|r| − c√(kΔ) bei 300 / 600 | +0,00572 / +0,00399 | +0,00572 / +0,00400 | ≤ 0,05, fallend |
| c: ln|C| + πkΔ − c√(kΔ) + 0,599001 bei 80 / 100 / 120 | −0,0028 / −0,0085 / −0,0045 | gleich | ≤ 0,02 bei 100, 120 |
| Konturen voll (120) | 3,4·10⁻⁷ | 5,1·10⁻⁷ | ≤ 10⁻⁶ |
| lokale Kontrolle (600) | **1,4·10⁻⁵** | 1,0·10⁻⁹ | ≤ 10⁻⁶ |

Inhaltlich erfüllt jeder Teil sein Kriterium: a mit Faktor 20 Abstand, b mit Faktor 10, c mit Faktor 2–4. Für Drehsinn − ist der Test vollständig gültig und bestätigt.

## Was damit hergeleitet ist
Für die Beimischung am Urknall-Übergang (tanh-Profil, Dauer Δ) gilt asymptotisch
  **ln|C| = −πkΔ + c√(kΔ) − ½ln(a/b) + O((kΔ)^{−1/2}),  c = 2√π Γ(3/4)/Γ(1/4)·Re√L = 1,809205,**
mit L = ln(a/b) ∓ iπ. Die drei Teile kommen aus drei Quellen:
- **Exponent π:** die Lage der Singularität t₀ = iπΔ/2 von tanh;
- **Wurzelterm:** die wesentliche Singularität von w = e^{Ls} dort, also das lokale Problem mit dem Pol vierter Ordnung im effektiven Potential. Der Umkehrpunkt η = −i gibt die Konstante 2√π Γ(3/4)/Γ(1/4) = 1,19814 (Betafunktion);
- **Konstante −½ln(a/b):** die adiabatische Amplitude w^{−1/2} zwischen den Gewichten 1 und e^L vor und nach dem Übergang.

Die Korrektur erster Ordnung (Term −λ/σ³) ist eine reine Phase (−π/4), daher fehlt eine weitere Konstante. Die Wellen aus H91 stammen nach der Herleitung vom subdominanten Umkehrpunkt (relativ e^{−0,563√(kΔ)}, Periode ≈ 2,06 in √(kΔ)). Das ist nicht eigens geprüft. Damit sind die offenen Punkte aus H87 (Steigung unter π), H91 (Wellen, Exponent) und H92a (Faktor ≈ 0,54) erklärt.

## Folge
- Die Abschneideskala der Beimischung ist 1/(πΔ), verschoben um einen Faktor, der nur wie e^{1,8√(kΔ)} wächst. Δ bleibt frei; die Physik ändert sich nicht.
- Die Beimischung hängt über a/b und L nur von β_sym ab (Gewichte a, b; Drehsinn über ∓iπ). Für die Photon-Gewichte (a = b) wird L = ∓iπ, und es bliebe c = 1,19814·Re√(∓iπ) = 1,19814·√(π/2) = 1,502 bei −½ln(a/b) = 0. Das ist eine nachträgliche Folgerung, nicht gerechnet.
