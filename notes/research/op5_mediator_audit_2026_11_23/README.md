# Bilanz der Vermittlerkette r32–r44: Die Setzung wandert, und alle Ecken sind eine Frage (Audit, 23.11.2026)

Auftrag des Autors (23.11.): „ich habe das gefühl, du landest irgendwie immer zwischen drei bis vier spezifischen ecken. sollten wir nicht
mal untersuchen wieso“ und „gehe vielleicht auch nochmal eine bis zwei ebenen höher und bewerte das mit dem jetzigen wissen mal neu …
könnte vielleicht einfach wieder nur eine weggabelung sein“. Erkundung ohne Kriterium; eine Kontrollrechnung, deren Ergebnis vorher
von Hand bekannt war (nicht blind). Zwei Lese-Agenten haben die Herkunft von N_m und die Einordnung von OP5 erhoben; die Fundstellen
sind unten genannt.

## 1. Bilanz der Setzungen
| Runde | hergeleitet | neu gesetzt oder gewählt |
|---|---|---|
| r32 | Higgsquelle, elastische Präparation, gewöhnlicher Außenbeitrag; Einstein-Term aus S^{μν} | Antriebsoperator 𝒫 (Form aus dem Vergleichsmodell, Koeffizienten gewählt); Gleichsetzung δJ_OP5 = δ𝒥_h |
| r33 | Gleichsetzung im skalaren Kanal aus W2 (Radialmodus η) | gerichteter Kontrast braucht einen unterluminalen Vermittler, den W2 nicht hat |
| r34 | kein Vakuumfeld erfüllt V1–V5 | Kandidatenliste (Paar-Konnektor, Material, Hintergrund, String) |
| r35 | gerichteter Term aus einer Paarfeder | Zähler a_⊥ statt ⅔a_⊥²; Kontrast als Präparationseigenschaft |
| r36 | N_m aus positiver Spin-2-Polarisationssumme | Rahmen, Achse, Polarisationsstruktur |
| r37 | Rahmen, Achse, gerichtete Anteile aus einem String M–T | Spannungsgesetz S2; ungerichteter Anteil halb |
| r38 | N_m exakt aus Feldgleichungen, Stabilität g_m² ≤ 3r_m | Gewicht und Entartung eines Skalars |
| r39 | Gewicht und Entartung aus einem Tensorfeld | H_0i koppeln nicht (w = 0) |
| r40 | w = 0 ⇔ gleiche Gewichte beider Zeitorientierungen | p = ½ |
| r41 | p ≈ ½ aus dem Keim-Gegenstrom (am Punkt) | Zeitumkehr statt Spiegelung |
| r42–r44 | Werte, erster und zweiter Jet entscheiden nicht | (offen) |

Die Zahl der freien Wahlen bleibt bei eins; jede Runde verschiebt sie.

## 2. Herkunft von N_m
- Erstmals am 20.11. in `../op5_bifocal_response_2026_11_18/OP5_J_Stabilitaet_Doppelkopplung.md` (Commit f97a3d02): eine von Hand gebaute
  gerichtete Quelle T^{00}/h = −a, T^{0i}/h = −ω(Pk)_i, T^{ij}/h = −xP^{ij} mit P = diag(1, 1, 0), aus der Kopplung
  𝓛 = −hP^{ij}R⁽¹⁾_{0i0j} (`OP5_J_Lokale_Antriebswirkung.md`), kontrahiert mit dem Fierz–Pauli-Zähler. Status dort: „Die zweite Kopplung
  wird ausdrücklich gesetzt.“
- r_m = ½ und g_m² = 3/100 erstmals in `OP5_J_Metrische_Kegelgrenze.md`: „als Vergleichseingaben beibehalten“; die verlangsamte Ausbreitung
  ist „nicht aus der Einstein- oder Fierz–Pauli-Wirkung … hergeleitet“. Preprint `sections/06-geometry.tex`: „Die Koeffizienten und die
  gerichtete Quellenform sind vorgegeben.“
- r32.0 sagt dasselbe: zwei gesetzte Eingaben, der ganze Antriebsoperator samt N_m und d_m, Koeffizienten gewählt.

**Kontrollrechnung** (`fp_directed_source.wl`, Ausgabe `run/fp_directed_source.txt`, Wolfram exakt): Die Quelle ist erhalten
(p_μS^{μν} = 0), und der gewöhnliche, Lorentz-kovariante Fierz–Pauli-Zähler S·S − (trS)²/3 ist genau N_m = ⅔(x² − ax + a²). Die
Zeit-Quer-Komponenten koppeln dabei und tragen −2ax bei; ohne sie wäre der Zähler ⅔(a + x)².

## 3. Folgerung für r38–r44
- Der Vermittler des ursprünglichen Baus ist ein gewöhnliches massives Spin-2-Feld mit kovariantem Zähler. Die Richtung steckt nicht im Feld,
  sondern in der **Kopplung**: im Rahmen u (der Index 0 in R_{0i0j}) und in der Achse (P = 1 − nn).
- r38 und r39 haben die Richtung dagegen in den Vermittler gelegt (Tensor quer zur Achse, euklidische Norm auf dem Unterraum, Kopplung an
  ∂_a∂_bη − η_ab□_∥η). Erst diese Zerlegung erzeugte die Frage, warum H_0i nicht koppeln. Im ursprünglichen Bau koppeln sie und werden gebraucht.
- Die Kette r39 → r40 → r41 → r42–r44 (w = 0, p = ½, Zeitumkehr oder Spiegelung) beantwortet also eine Frage, die nur in der Zerlegung von
  r38/r39 entsteht. Ihre Rechnungen bleiben richtig, ihre Bedeutung für OP5 ist kleiner als dort gelesen. Das gleiche Muster hat der Rückblick
  in r05 schon einmal beschrieben („etwa zwölf Entscheidungen, meist als Reparatur“; eine Dynamik, die „eine Frage beantwortete, die der Kern
  nicht stellt“, `wiki/Forschungsstand.md`).
- Was wirklich gesetzt bleibt, sind drei Eingaben des Vergleichsmodells: (i) die gerichtete Kopplung mit Rahmen u und Achse n, (ii) die
  verlangsamte Ausbreitung r_m, (iii) die Zahlenwerte. Alle drei sind Daten eines ausgezeichneten Bezugssystems.

## 4. Eine bis zwei Ebenen höher
- OP5 ist im Register die Frage nach kosmologischer Konstante und Vakuumbilanz (`wiki/Offene-Probleme.md`, These T9). Das Vergleichsmodell
  ist ausdrücklich eine lokale Hilfskonstruktion: „Alles betrifft nur das Vergleichsmodell, nicht das QSC-Modell selbst“
  (`notes/anleitungen/op5-vergleichsmodell-rechnen.md`).
- Darüber liegt OP1: Jede Zahl, die OP2–OP5 liefern, hängt an β_sym (`wiki/Forschungsstand.md`, Wurzelkarte). Bei OP1 steht eine
  Gabelung, die das Projekt schon kennt: Lesart (H), Breite als Eigenschaft des Feldzustands, gegen Lesart (B), Eigenschaft des Beobachters
  bzw. der Auslese; nach den Prüfungen ist (B) widerspruchsfrei, (H) nicht.
- Auch H118 sagt: Das Vorzeichen des Oktanten ist eine **Zeitorientierung der Auslese**.

## 5. Warum die Suche zwischen denselben Ecken springt
Die vier Ecken, Rahmen und Achse (r36), String M–T (r37, I1), Zeitorientierung (H118, r40) und Keim-Gegenstrom (k168, r41), sind vier Arten,
ein ausgezeichnetes Bezugssystem u, eine Achse n und eine Zeitorientierung bereitzustellen. Es ist ein Grundproblem: **Woher kommen u, n und die
Orientierung?** Die Suche kreist darum, weil an einer Weggabelung stillschweigend ein Zweig gewählt wurde:
- **Zweig (H), Feldseite:** u, n und Orientierung sind Eigenschaften eines Feldes oder Mediums (Material, Hintergrund, String, Keimströmung).
  Diesen Zweig haben r35–r44 verfolgt.
- **Zweig (B), Ausleseseite:** u, n und Orientierung sind Daten der Auslese (Beobachterrahmen, Messachse, Zeitorientierung der Auslese). So war
  N_m ursprünglich gebaut; bei OP1 ist dies der widerspruchsfreie Zweig, und H118 weist in dieselbe Richtung.
Hinzu kommen Gründe im Verfahren: ein festes Ziel (N_m), das selbst Eingabe ist; die Pflichten „Vorwissen“, „Rückwärtssuche“ und
„Auslöser prüfen“, die jede Lücke mit einem vorhandenen Objekt füllen; „trägt teilweise“ als Einladung zur nächsten Begründungsrunde;
nicht blinde Kandidatenwahl; Zusammenfassungen, die dieselben Objekte weitertragen.

## 6. Folgen
- I1 (String M–T) liegt im Zweig (H). Nach dem strengeren Raster zählt er nur, wenn er u, n oder r_m herleitet, ohne neu zu setzen, und etwas
  über N_m hinaus vorhersagt.
- Zweig (B) ist bisher nicht als Test formuliert: ob u, n und die Orientierung mit bereits deklarierten Auslesedaten zusammenfallen
  (Konvention F, Messachse des Vergleichsaufbaus, Beobachterlesart von OP1).
- Welcher Zweig verfolgt wird, entscheidet der Autor.
- Verfahrensregel (neu in AGENTS.md): Nach zwei Runden in Folge mit „trägt teilweise“ zur selben offenen Voraussetzung wird vor der nächsten
  Runde eine Bilanz der Setzungen gezogen, und es wird geprüft, ob die Frage nur in einer gewählten Zerlegung entsteht.

OP1–OP5, C5, C6/T2 offen.
