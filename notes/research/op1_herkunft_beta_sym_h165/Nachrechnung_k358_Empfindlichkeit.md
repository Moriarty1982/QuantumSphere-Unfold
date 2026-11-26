# Nachrechnung k358: Wie reagieren die einzelnen Stellen auf den exakten Wert von β_sym?

Stand 26.11.2026. **Erkundung, kein Test** (keine Vorab-Notiz, kein Entscheidungskriterium). Frage des Autors nach der Annahme des
Zählpostulats (r67): „Müssen wir nicht trotzdem nochmal nachrechnen, um zu sehen, wie die einzelnen Stellen darauf reagieren?“

**Kurz:** Kein Urteil kippt. Zwei Stellen reagieren spürbar: die m_W-Beziehung (schärfste Stelle, Fenster in β nur ±6 Schritte breit) und
m_τ aus H102 (hängt an γ_M; der exakte Wert liegt 0,9σ weiter von der Messung als der gerundete). Die Trefferzahl der Maskenrechnung
(H45/H46) ändert sich deutlich, das Fenster der Vorhersage kaum.

## Verglichene Werte

| Kürzel | β_sym | γ_L | Herkunft |
|---|---|---|---|
| alt4 | 0,5493 | 1,864224 | vierstellig, in vielen älteren Skripten (k100, k263, k181 und andere) |
| alt7 | 0,5493482 | 1,864441 | im Bestand geführt, aus gerundeten Eingaben |
| exakt | 0,5494056410 | 1,8646997646 | Wurzel der Zählgleichung, Postulat r67.P |

Ein „Schritt“ ist unten die Änderung exakt − alt7 = 5,74·10⁻⁵ in β (relativ 1,05·10⁻⁴).

## Werkzeuge und Prüfungen

- `k358_empfindlichkeit.py` (mpmath, 30 Stellen; H102 mit den Funktionen aus `predictions/k224_test_h102.py`), Ausgabe `k358_out.txt`.
- `k358d_gegenprobe.wl` (Wolfram Language, unabhängig; Empfindlichkeiten symbolisch), Ausgabe `k358d_out.txt`. Übereinstimmung in
  γ_L, β, γ_L⁵, m_W, β² und den Empfindlichkeiten auf alle gezeigten Stellen. Eine Warnung des Vorab-Prüfers ist in der Ausgabe vermerkt.
- `k358b_maske_h46.py` und `k358c_maske_h134.py` führen den unveränderten Code von k105 und k263 mit ausgetauschtem ε aus
  (Ausgaben `k358b_out.txt`, `k358c_out.txt`).
- Qiskit passt hier nicht: Es gibt keine Schaltung und keine Messsimulation, nur Zahlen aus geschlossenen Formeln und zwei Matrixscans.
- Grenzen: Die Messwerte sind die im Bestand geführten; keiner ist neu, keiner zählt als Prüfung einer Vorhersage. Die σ-Abstände
  sind Lagebeschreibungen. Skripte, die 0,5493 nur für Anschauungszahlen benutzen (etwa k181, k297, k298, k352), sind nicht einzeln neu
  gelaufen; ihre β-abhängigen Formeln stehen in Tabelle 1.

## 1. Abgeleitete Zahlen

Empfindlichkeit = d ln X / d ln β beim exakten Wert. Eine Zahl mit Empfindlichkeit s ändert sich relativ um s · 1,05·10⁻⁴.

| Größe | Stelle | alt7 | exakt | Differenz | relativ | Empfindlichkeit |
|---|---|---|---|---|---|---|
| β_sym | OP2-Versatz, r66 | 0,5493482 | 0,5494056 | +5,7·10⁻⁵ | +1,05·10⁻⁴ | 1,00 |
| β² = Ω_M = \|U_e2\|² | H96, H9, H112, OP4, OP5 | 0,301783 | 0,301847 | +6,3·10⁻⁵ | +2,1·10⁻⁴ | 2,00 |
| 1 − β² = Ω_Λ | r05 | 0,698217 | 0,698153 | −6,3·10⁻⁵ | −9,0·10⁻⁵ | −0,86 |
| Ω_Λ/Ω_M | r05 | 2,31363 | 2,31294 | −6,9·10⁻⁴ | −3,0·10⁻⁴ | −2,87 |
| γ_L = cot θ_W | H15, r61 | 1,864441 | 1,864700 | +2,6·10⁻⁴ | +1,4·10⁻⁴ | 1,33 |
| γ_L² | Frame-Potenzen | 3,47614 | 3,47711 | +9,7·10⁻⁴ | +2,8·10⁻⁴ | 2,66 |
| γ_L³ | Frame-Potenzen | 6,48106 | 6,48376 | +2,7·10⁻³ | +4,2·10⁻⁴ | 3,99 |
| **γ_L⁵** (Vakuumquotient) | H159, v4.9.0-r69.3 | 22,5291 | 22,5447 | +0,0156 | +7,0·10⁻⁴ | **6,64** |
| γ_L^(−3/2) | Photon-Planck (alt) | 0,392805 | 0,392723 | −8,2·10⁻⁵ | −2,1·10⁻⁴ | −1,99 |
| ε = η = artanh β | Maske, H45, H46, H134 | 0,617447 | 0,617530 | +8,2·10⁻⁵ | +1,3·10⁻⁴ | 1,27 |
| tanh 2η | r63 | 0,843993 | 0,844041 | +4,7·10⁻⁵ | +5,6·10⁻⁵ | 0,54 |
| 1/β (Tachyon) | v4.9.0-r24.2 | 1,820339 | 1,820149 | −1,9·10⁻⁴ | −1,05·10⁻⁴ | −1,00 |
| θ_H | r61, r66 | 66,6446° | 66,6525° | +0,0079° | +1,2·10⁻⁴ | 1,13 |
| π − θ_H | H164 | 113,3554° | 113,3475° | −0,0079° | −7,0·10⁻⁵ | −0,66 |
| 2α = 2 arctan β | r66 | 57,5642° | 57,5693° | +0,0051° | +8,8·10⁻⁵ | 0,84 |
| Besetzungen 1/(1+β²), β²/(1+β²) | r66, H73 | 0,768177 / 0,231823 | 0,768140 / 0,231860 | ∓3,7·10⁻⁵ | −4,9·10⁻⁵ / +1,6·10⁻⁴ | −0,46 / 1,54 |
| w = −β²/3 | H73 | −0,100594 | −0,100616 | −2,1·10⁻⁵ | +2,1·10⁻⁴ | 2,00 |
| τ*/δ = β/(1+β) | H81 | 0,354567 | 0,354591 | +2,4·10⁻⁵ | +6,8·10⁻⁵ | 0,65 |
| HC-Winkel arctan β² | k297, k298 | 16,7929° | 16,7963° | +0,0033° | +2,0·10⁻⁴ | 1,89 |
| K = (1+β⁴)/3 | r63, H155 | 0,363691 | 0,363704 | +1,3·10⁻⁵ | +3,5·10⁻⁵ | 0,33 |
| κ = (γ_L + 1/γ_L)/2 | r64.4 | 1,200397 | 1,200490 | +9,2·10⁻⁵ | +7,7·10⁻⁵ | 0,74 |
| 2^(1−γ_L) | H165 | 0,549259 | 0,549161 | −9,9·10⁻⁵ | −1,8·10⁻⁴ | −1,72 |
| **Hopf-Lücke** in β | r61 | 5,097 % | 5,086 % | −0,011 Punkte | −2,2·10⁻³ | **−20,7** |
| **Hopf-Lücke** in γ_L | r61 | 7,271 % | 7,256 % | −0,015 Punkte | −2,0·10⁻³ | **−19,6** |
| sin²θ_W = 1/(1+γ_L²) | H15 | 0,223407 | 0,223359 | −4,8·10⁻⁵ | −2,2·10⁻⁴ | −2,06 |
| **m_W** = m_Z γ_L/√(1+γ_L²) | H15 | 80,3590 GeV | 80,3615 GeV | +2,5 MeV | +3,1·10⁻⁵ | 0,30 |
| sin²θ₁₂ = β²/(1 − s₁₃), s₁₃ = 0,02215 | H9 | 0,308619 | 0,308684 | +6,5·10⁻⁵ | +2,1·10⁻⁴ | 2,00 |

Stark reagieren also: die Hopf-Lücke (kleine Differenz zweier fast gleicher Zahlen, Faktor 20) und hohe Potenzen von γ_L (γ_L⁵, Faktor 6,6).
Beide sind im Bestand keine Größen mit Datenvergleich: Die Hopf-Lücke ist eine Kennzahl, γ_L⁵ wird nach H159 von keiner Rechnung gestützt.
m_W reagiert relativ schwach (0,30), ist aber so genau gemessen, dass es trotzdem die schärfste Stelle ist (Abschnitt 2).

## 2. Abstand zur Messung

| Vorhersage | Messung | alt7 | exakt | z alt7 | z exakt | Änderung | Urteil |
|---|---|---|---|---|---|---|---|
| H96 Ω_M = β² | DESI DR2 BAO 0,2975 ± 0,0086 | 0,30178 | 0,30185 | +0,50σ | +0,51σ | +0,007σ | unverändert offen (registriert mit 0,30185) |
| H96 Ω_M = β² | Planck 2018 0,315 ± 0,007 | 0,30178 | 0,30185 | −1,89σ | −1,88σ | +0,009σ | unverändert |
| **H15 m_W** | PDG 2024 80,3692 ± 0,0133 GeV | 80,3590 | 80,3615 | −0,76σ | −0,58σ | **+0,19σ** | unverändert offen (registriert mit 80,3615) |
| **H15 m_W** | PDG 2026 80,3625 ± 0,0077 GeV | 80,3590 | 80,3615 | −0,44σ | −0,13σ | **+0,32σ** | unverändert offen |
| H9 sin²θ₁₂ (s₁₃ = 0,02215) | JUNO 2026 0,3036 ± 0,0064 | 0,30862 | 0,30868 | +0,78σ | +0,79σ | +0,01σ | unverändert offen |
| H9 sin²θ₁₂ (s₁₃ = 0,02248) | NuFIT 6.1 0,3088 ± 0,0067 | 0,30872 | 0,30879 | −0,01σ | −0,00σ | +0,01σ | unverändert |
| **H102 m_τ** (über γ_M) | PDG 1776,93 ± 0,09 MeV | 1777,055 (γ_M = 0,2375) | 1777,134 (γ_M exakt) | +1,39σ | +2,27σ | **+0,88σ** | unverändert offen; registriert mit dem exakten Wert |

Bei m_W ist die Unsicherheit der Vorhersage aus m_Z (1,8 MeV) eingerechnet.

**H9:** Registriert ist 0,30862 ± 0,00018 (v4.8.0, mit β aus gerundeten Eingaben). Mit dem exakten Wert sind es 0,30868. Der Unterschied
(6·10⁻⁵) liegt in der dort angegebenen Unsicherheit und ist 1 % der JUNO-Unsicherheit. Die registrierte Zahl bleibt stehen.

**H102:** Diese Stelle hängt nicht an β_sym, sondern an γ_M allein, und sie reagiert stark: d m_τ / d γ_M = 2396 MeV. Die Rundung
0,2375 → 0,237533 verschiebt m_τ um 0,079 MeV, fast eine Messunsicherheit. H102 ist am 13.11.2026 mit γ_M = 0,237533 festgeschrieben
(1777,134 MeV), das Postulat ändert daran nichts. Zur Einordnung: Die Messung träfe γ_M = 0,237448, exaktes Koide γ_M = 0,237464
(linear gerechnet). Der gerundete Wert läge näher an der Messung als der exakte; das ist kein Grund, ihn zu nehmen, weil er aus keiner
Regel folgt. H102 steht damit wie bisher bei +2,3σ gegen PDG und wird an der nächsten PDG-Ausgabe entschieden.

## 3. Schwellen: wie weit dürfte β wandern?

| Schwelle | β an der Schwelle | Abstand vom exakten Wert | in Schritten |
|---|---|---|---|
| m_W, 2σ unten (PDG 2026) | 0,549074 | −0,00033 | **−5,8** |
| m_W, 2σ oben (PDG 2026) | 0,549784 | +0,00038 | **+6,6** |
| Leptonfenster unten (0,545) | 0,545 | −0,0044 | −77 |
| Maske, unterer Rand η = 0,611 (r61) | 0,544831 | −0,0046 | −80 |
| H9, JUNO 2σ oben | 0,556136 | +0,0067 | +117 |
| Ω_M, DESI 2σ oben | 0,560981 | +0,0116 | +202 |
| Maske, oberer Rand η = 0,647 | 0,569647 | +0,0202 | +352 |
| Leptonfenster oben (0,570) | 0,570 | +0,0206 | +359 |

Die drei Fenster von H98 (Leptonfenster, m_W, Ω_M) enthalten alt4, alt7 und den exakten Wert. Die Änderung ist gegen alle Schwellen
klein, außer gegen m_W: Dort entspricht das 2σ-Fenster einem β zwischen 0,54907 und 0,54978. Beide Werte liegen drin, der exakte näher
an der Mitte. Der Hopf-Wert 1/√3 = 0,57735 gäbe m_W = 81,56 GeV und liegt weit draußen.

## 4. Maskenrechnungen (Mischung)

Beide Rechnungen sind Rasterscans mit ε = artanh β_sym als Maske; der Code ist unverändert, nur ε ist getauscht.

**H45/H46 (k105 neu als k358b, Raster 2°):**

| ε | Treffer A | Treffer B | sin²θ₂₃ der Treffer | \|sin δ\| |
|---|---|---|---|---|
| artanh(0,5493) = 0,61738 | 120 | 1104 | [0,4913; 0,4975] | [0,169; 0,998] |
| artanh(0,5493482) = 0,61745 | 120 | 1104 | [0,4913; 0,4975] | [0,169; 0,998] |
| artanh(0,5494056410) = 0,61753 | **168** | **1552** | [0,4908; 0,4975] | [0,169; 0,998] |

Die Trefferzahl springt zwischen alt7 und dem exakten Wert um 40 %, das Intervall für sin²θ₂₃ wird unten um 0,0005 breiter. Der Sprung ist
eine Rasterwirkung: Bei festem Raster in φ rückt eine weitere Gruppe von Rasterpunkten in die Messfenster. Er war schon aus der
Nachrechnung vom 25.10.2026 bekannt (`v4_10_0_r63_r64/llm/Nachrechnung_r63_r67.md`, Punkt 6); neu ist, dass er genau zwischen 0,5493482
und dem exakten Wert liegt. Die registrierte Vorhersage H46, sin²θ₂₃ ∈ [0,49; 0,50], enthält beide Intervalle und bleibt unverändert.
Trefferzahlen aus diesem Scan eignen sich nicht als Maß. Die drei letzten Zeilen von `k358b_out.txt` („H45a … widerlegt“) sind ein Rest
des Codes von k105, der dort nach einem Namen sucht, den es in der Kandidatenliste nicht gibt; sie sind kein Befund.

**H134 (k263 neu als k358c, Raster 2°), Klasse TM1, Variante B:**

| | ε = artanh(0,5493) (k263) | ε = artanh(0,5494056410) (k358c) |
|---|---|---|
| θ₁₃ in 3σ | 24568 | 25128 |
| Treffer (JUNO 2σ) / davon 1σ | 56 / 32 | 56 / 32 |
| sin²θ₁₂ der Treffer | [0,2920; 0,3139] | [0,2919; 0,3139] |
| sin²θ₂₃ der Treffer | [0,5403; 0,5634] | [0,5402; 0,5633] |
| \|sin δ\| der Treffer | [0,523; 0,705] | [0,523; 0,705] |
| Variante A, nächster Wert zu 0,3036 | 0,3480 | 0,3459 |
| H134a / b / c | bestätigt / widerlegt / bestätigt | bestätigt / widerlegt / bestätigt |

H134 reagiert in der vierten Stelle; alle drei Teilurteile bleiben.

## 5. Was sich an den Texten ändert

- Die Runden bleiben, wie sie sind (append-only). Der Bezugswert steht seit r67.2 im Companion.
- Physik-Artikel und Preprint nennen β_sym = 0,549406, m_W = 80,3615 GeV, Ω_M = 0,30185 und m_τ = 1777,134 MeV schon mit dem exakten Wert.
  Die Zahl 0,3086 bei H9 ist die registrierte; exakt gerundet wären es 0,3087.
- Kein Status in der Liste der Vorhersagen ändert sich. OP1 bis OP5 bleiben offen.

## Vergeben

k358, k358b, k358c, k358d. Nächste freie Nummern: H166, k359, Runde r68.
