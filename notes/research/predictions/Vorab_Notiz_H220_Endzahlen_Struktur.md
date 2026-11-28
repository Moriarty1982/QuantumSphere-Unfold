# Vorab-Notiz H220 (k433): Endzahlen-Suche mit strukturellen Bausteinen und angepasster Dichte

Stand 28.11.2026, vor der Rechnung festgeschrieben. Der Autor hat am 28.11.2026 um 00:32 mit „ja“ eine zweite Endzahlen-Suche nach H219
freigegeben. Auslöser ist die Diagnose zu H219: Mit 5,8 Mio. Werten war die Suche für Ziele mit 3 bis 5 Stellen zu dicht, und sie nutzte
allgemeine Konstanten statt der Struktur des Modells.

## Frage

Treffen Ausdrücke aus **strukturellen** Bausteinen des Rahmens sehr genau gemessene Zahlen früher als gleich genaue Zufallszahlen? Die Größe
der Ausdrücke wird dabei so begrenzt, dass die Wertedichte zur Zielgenauigkeit passt. **Alle Treffer sind „angepasst“.**

## Bausteine (fest)

| Gruppe | Blätter |
|---|---|
| Cayley–Dickson-Dimensionen | 1, 2, 4, 8, 16 |
| Imaginärteile von ℍ und 𝕆 | 3, 7 |
| Spin bzw. Peirce-Wert; Koide-Form K | ½; ⅔ |
| Casimir-Flächen √(j(j+1)) für j = ½, 1, 3/2, 2 | √3/2, √2, √15/2, √6 |
| Zählregel r67 | γ_L = 1,8646997646 |

- **Operationen:** +, −, ×, ÷, √x, x², 1/x. Das 2^(−x) aus H219 entfällt, weil es in γ_L schon steckt.
- Ausdrücke mit gleichem Wert (relativ 10⁻¹¹) werden zusammengefasst, die kleinste Größe zählt.
- **Bewusst nicht als Blätter:**
  - die Vakuumwerte l_k, weil deren Phase δ an den Lepton-Massen angepasst ist und Lepton-Ziele sonst zirkulär wären;
  - β_sym, weil es aus γ_L folgt;
  - γ_M, γ_T, π und ln 2, weil sie allgemeine Konstanten sind (H219).
- Wertzahlen, gemessen vor dem Blick auf die Ziele (`bausteine_h220.py`):

  | Größe | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
  |---|---|---|---|---|---|---|---|
  | neue Werte | 14 | 29 | 318 | 1729 | 13 924 | 105 873 | 825 790 |
  | kumuliert | | | | | | | 947 677 |

## Größengrenze (Regel, fest)

S_max ist die **größte Größe ≤ 8**, bei der für das **breiteste** Zielfenster höchstens die Hälfte der Zufallskontrollen getroffen wird. Das
breiteste Fenster hat m_W/m_Z. Die Regel nutzt nur die Fensterbreiten und die Kontrollen, nicht die Treffer der echten Ziele. Für alle
schmaleren Ziele ist die Suche damit dünn genug, dass ein Zufallstreffer unwahrscheinlich ist.

## Ziele (fest, nur sehr genau bekannte Größen; Fenster 2σ)

| Ziel | Wert ± σ | rel. σ | Quelle |
|---|---|---|---|
| m_e/m_μ (Polmassen) | 0,51099895/105,6583755 | 2·10⁻⁸ | wie k427 |
| m_μ/m_τ | 0,059464 ± 0,000004 | 6,7·10⁻⁵ | wie k235 |
| sin²θ_W (MS-bar) | 0,23129 ± 0,00004 | 1,7·10⁻⁴ | wie k235 |
| α_em⁻¹(0) | 137,035999177 ± 0,000000021 | 1,5·10⁻¹⁰ | CODATA 2022 |
| m_W/m_Z | 80,3692/91,1880, σ aus σ(m_W) = 0,0133 | 1,7·10⁻⁴ | wie k235 |

**Nicht als Ziel:**

- Koide K = ⅔, weil es ein Blatt ist und im Rahmen gilt (H214);
- β_sym, weil γ_L ein Blatt ist und die Suche sonst zirkulär wäre.

**Nicht blind:** m_W/m_Z wird von γ_L/√(1 + γ_L²) = 0,88128 getroffen. Das ist die bekannte Lesart cot θ_W = γ_L (H15). Dieses Ziel wird
nur berichtet und zählt nicht für das Urteil. Gewertet werden die übrigen 4 Ziele.

## Messgrößen, Kontrollen, Kriterium

- Je Ziel werden s_min (kleinste Trefferbreite bis S_max) und N bestimmt. Kontrollen: 1000 Zufallswerte, log-gleichverteilt in [x/3, 3x],
  Startwert 220, mit gleicher relativer Fensterbreite. p = Anteil der Kontrollen mit s_min ≤ s_min(Ziel); ohne Treffer ist p = 1.
- **trägt:** mindestens eines der 4 gewerteten Ziele hat p < 0,05/4 = 0,0125;
- **trägt teilweise:** mindestens 2 der 4 haben p < 0,05. Das 95-%-Quantil von Bin(4; 0,05) liegt bei 1;
- **widerlegt:** sonst.

Ein Treffer bei m_e/m_μ oder α_em⁻¹ wäre wegen der winzigen Fenster stark. Erwartet wird aber, dass bei diesen Genauigkeiten gar nichts
getroffen wird (keine Rechnung). Erwartetes Urteil: widerlegt.

## Vorwissen geprüft

- H219: zu dicht, allgemeine Konstanten. k235: Zufallsabschätzung, Ziele und Werte.
- H15: cot θ_W = γ_L, nicht blind, siehe oben. H214: K = ⅔ im Polschema.
- H213/H214 und H168: Die Lepton-Massenverhältnisse folgen im Rahmen aus Brannen-Form plus Versatz x. Dort steckt δ als Eingabe drin. Diese
  Suche nutzt δ nicht.
- α_em kommt im Bestand nur als Eingabe oder als Kandidatengröße vor (H166, H167, k337), nie als Ziel einer Formel (Grep nach „137,0“).

## Prüfwege

Hauptrechnung in Python `k433_test_h220.py` mit Ausgabe `k433_out.txt`. Gegenprobe in Wolfram `k433b_gegenprobe.wl`: unabhängige Zählung
bis Größe 4 und Nachrechnung aller gemeldeten Treffer mit 30 Stellen.

Ordner: `notes/research/hilbert_shift_felder_2026_11_24/endzahlen_struktur_h220/`.
