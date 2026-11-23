# Sichtung des OpenAI-Mathematikpakets für die offenen Probleme (Erkundung, Literatur, 23.11.2026)

**Ergebnis in einem Satz:** Von 721 Manuskripten in 373 Familien ist für unsere offenen Probleme ein Satz direkt verwendbar (Quasi-RH, nur
für das RH-Paper des Autors), fünf liefern übertragbare Methoden (148 → OP1, 149 → C5/C6, 104 → C6/T2, 334 → OP5(b) als Warnung,
376 → C6/T2 als No-go-Vorlage); für OP2, OP4, Q1 und Q2 gibt es keinen Treffer. Kein Ergebnis schließt ein OP, keines ist begutachtet.

Auftrag des Autors (Chat 23.11.2026): „OpenAI hat eine Arbeit zu Riemann veröffentlicht, vielleicht kannst Du da was raus ziehen?“, „ließ
dazu nochmal mein eigenes riemann paper“, „lade die arbeit über die verlinkte doi im hauptpaper“, „jetzt schaust du bitte nach, was du von
den openai papern für die aktuellen probleme benutzen könntest und ich meine alle davon“, „Erst festhalten“. Keine Rechnung, keine H-Nummer.

## Quelle und Stand
- Repository github.com/openai/math, Stand Commit `4eaee87548250b2682affda7d05d947c05554bae` (30.10.2026). Verzeichnis `CONTENTS.md`
  (SHA-256 `080badcb…be175`) mit 721 Manuskripten und Abstracts in 373 Familien; Änderungshistorie `history.md` (SHA-256 `f065ee13…d4484`).
- Laut Repository sind rund 42 % der Hauptergebnisse in Lean formalisiert; die Manuskripte gelten dort selbst als „raw research data“.
- **Rückzüge (7.10.):** Ein Vorzeichenfehler in „Algebraicity of Weil classes on split abelian eightfolds“ entwertete diese und zwei
  abhängige Arbeiten (Kuga–Satake für K3, rationale Hodge-Vermutung für Produkte von K3-Flächen); 14 weitere Arbeiten wurden repariert.
  Keiner der Treffer unten ist davon betroffen. Für Quasi-RH ist kein Fehler gemeldet (Quanta, 19.10.: Experten halten die 11/12-Fassung
  weitgehend für richtig; nicht begutachtet).

## Verfahren
1. `parse_contents.py <ordner> 5` zerlegt `CONTENTS.md` in Familien und fünf Teile (001–078, 079–154, 155–230, 231–305, 306–378).
2. `problem_profile.md`: Suchprofil der offenen Probleme (OP1–OP5, C5, C6/T2, Q1, Q2 aus `../op_cross_map_2026_11_23/`, RH-Paper, Werkzeuge).
3. Fünf Subagenten lasen je einen Teil vollständig (Familientext und alle Abstracts) gegen das Profil; Stufen A (Satz direkt anwendbar),
   B (Methode übertragbar), C (lose). Gelesen wurden Abstracts, keine Volltexte.
4. Gegenkontrolle: `keyword_screen.py <ordner>` (Stichwortsuche über alle Abstracts), Ausgabe `keyword_hits.txt`. Die Stichwortsuche ergab
   keinen zusätzlichen Treffer (352, Calabi-Fluss, nur per Stichwort „finite time“: Blowup, keine Auslöschung, wie 351); die Stichwortliste
   ist wegen kurzer Muster wie „sic“ verrauscht. Umgekehrt fand die Lesesichtung 104 und 334, die keine Stichwörter trafen. Nachträglich ergänzt: 029 (Begleitsatz zu 142), in Teil 1 nicht genannt.
5. Die Verzeichnisdateien selbst sind nicht abgelegt (fremder Text); Pfade und Prüfsummen oben genügen zur Wiederholung.

## Stufe A
| Fam. | Ergebnis (laut Abstract) | Problem | Nutzung | Vorbehalt |
|---|---|---|---|---|
| 003 | ζ, alle Dirichlet-L-Funktionen und Hecke-L-Funktionen endlicher Ordnung über ℚ(√−3) ohne Nullstellen in Re s > 7/8 (30.9.) bzw. > 11/12 (5.10.); keine Landau–Siegel-Nullstellen | RH-Paper des Autors | unbedingte Eingabe; mit Nullstellen ½ + iE gilt \|Im E\| < 3/8: Schranke für den nicht-selbstadjungierten Anteil jedes Hilbert–Pólya-Kandidaten; dritter Prüfstein (siehe unten) | unbegutachtet; nach r04 keine Beweisquelle für den Companion |

Abhängige Familien: 182 (Potenzersparnis an Primzahlargumenten) benutzt den „companion zero-free half-plane theorem“; 142 (deterministische
Faktorisierung über 𝔽_p) benutzt den „uniform Hecke zero-free theorem“ aus 029 (unendlicher Teil der Artin-Vermutung).

## Stufe B
| Fam. | Ergebnis (laut Abstract) | Problem | Übertragbar als | Vorbehalt |
|---|---|---|---|---|
| 148 | Für jedes endliche reelle selbstähnliche Maß: dim_H μ = min{1, h_RW/χ} (Entropierate der Zufallsirrfahrt durch Lyapunov-Exponent), auch bei exakten Überlappungen | OP1, Moran-Lesart (`../op1_moran_geometry_2026_11_17/`) | Prüffrage: Sind die beiden Extremzustände \|j, ±j⟩ der M-Zählung zwei verschiedene Abbildungen oder überlappen sie exakt? Nur im ersten Fall ist „Gewicht 2“ eine echte Verdopplung; sonst liegt die Dimension unter der Moran-Lösung, und γ_M/γ_T würde zu einem Quotienten von Entropieraten | auf der Geraden, endlich viele Abbildungen (unsere Spinsumme ist abzählbar unendlich, die Moran-Lesart flächig); begründet die Zählregel nicht (U2 bleibt offen) |
| 149 | Endliche schwach reversible Massenwirkungssysteme mit positiven Raten: beschränkt, persistent, permanent; jede Kompatibilitätsklasse hat eine kompakte absorbierende Menge mit positiver unterer Schranke | C5, C6/T2 | No-go für eine Zeugenklasse von Form (iii): Ein Zeuge in dieser Form erreicht null weder endlich noch asymptotisch; die absorbierende Menge wäre eine „benannte bleibende Obstruktion“ | ob unsere Zeugen diese Form haben, ist ungeprüft. Eine Attraktor-Lesart für Ω_M (OP5) steht nicht im Abstract; ihr Zielwert wäre eine gesetzte Eingabe |
| 104 | Mean-Payoff-Spiele (auch stochastisch, mit Parität) deterministisch quasipolynomial lösbar, mit zertifizierbaren Gewinnregionen und Strategien | C6/T2; QAM/HDL | Ist die Auslesungsklasse ein endlicher Spielgraph (Gegner wählt Auslesung, Gewichte log-Normänderungen), wird „für alle Auslesungen“ exakt entscheidbar: negativer Wert = Abstiegszeuge, Gegnerstrategie mit Wert ≥ 0 = bleibende Obstruktion | nur für endliche, explizit kodierte Klassen; misst Durchschnitt, nicht Abstieg je Schritt |
| 334 | Glatte Flächenmetrik, im Ursprung in jeder Ordnung euklidisch, ohne lokale isometrische Immersion in ℝ³ | OP5(b), Vergleichsmodell | Warnung: Formale Lösbarkeit in allen Jet-Ordnungen an einem Punkt (Keim bei (1, 3/5, 0, 0); r43, r44, r77) trägt im glatten Fall keine lokale Lösung; Cartan–Kähler braucht Analytizität | anderes Gleichungssystem; stützt die bestehende Vorsicht („keine Lösung auf einem Gebiet“), ändert keinen Befund |
| 376 | Erzwungene viskose Strömung: Ob ein festes Teilchen einen festen Bereich erreicht, ist unentscheidbar (Einbettung von Turingmaschinen) | C6/T2 | No-go-Vorlage: Lassen sich Bandmaschinen in die Auslesungsklasse einbetten, gibt es keinen einheitlichen Rückgabevertrag; zu prüfen, ob unsere Klasse das zulässt | braucht eine frei programmierbare, unendlich reiche Eingabeklasse |

## Stufe C (lose)
- OP3: 266 (in ℂ⁶ = ℂ² ⊗ ℂ³ höchstens drei gegenseitig unverzerrte Basen; computergestützt), 096 (Optimum bei drei 120°-Sektoren, ℤ₃-Muster),
  204 (Sättigung für Spin(2n), Kontrolle von Kopplungsauswahlregeln).
- OP1: 251 (Unitarisierbarkeit ⇔ Amenabilität; Ähnlichkeit lässt Spektren ohnehin fest), 230 (exaktes Hausdorff-Maß für SLE), 153
  (Bernoulli-Faltungen; ABCK-Gleichung formal eine Faltung mit λ = e^{−π√3}, trivial separiert).
- C6/T2: 004 (Hilberts zehntes Problem über ℚ), 242 (eindeutig-diophantische Darstellungen), 206 (Unentscheidbarkeit bei endlichen Verbänden),
  235 (zweiseitige Zertifikatssuche ohne Ratenkenntnis), 245 (schwache ⇒ starke Normalisierung), 056 (Terminierung über wohlgeordnete
  Invariante), 141 (∃∀-Sätze über ℝ in der Zählhierarchie).
- Q2/Skala: 282 (Skalen- ⇒ lokale konforme Symmetrie in 4D, unter starken Annahmen), 215 (exakte Massenlücke im 2D-O(4)-Modell).
- OP5(c): 095 (Hyperbolizitätskegel ohne semidefiniten Lift; für zwei Lorentzkegel nicht einschlägig). Q2: 341 (hypersymplektische Tripel).
- RH-Spielzeug: 178 (Ramanujan-Graphen), 219 (GOE-Universalität); Werkzeug-Muster: 189, 222, 229 (Zertifikate, Doppelimplementierung), 378 (#SAT).

## Kein Treffer
OP2 (selbstadjungierte Erweiterungen, xp-Spektren), OP4 (Mischung, ℤ₂, δ_CP, CKM), Q1 (Auslese), Q2 (gemeinsame Wirkung), OP5(a) (Λ-No-go),
OP5(c) (massiver Spin-2, Kausalität) im engeren Sinn.

## Das RH-Paper des Autors und Quasi-RH
- Geladen über die Concept-DOI 10.5281/zenodo.19157158 (→ v4.15, Record 19157897, 22.03.2026; MD5 von PDF und TeX gleich Zenodo). Die
  Prüfung vom 19.10. (`../v4_8_0_r03_r12/llm/Pruefung_Riemann_Paper_v4_15.md`, B1–B8) gilt unverändert.
- **B8 bestätigt:** Die Prüfung forderte, dass ein Beweis ζ von L(s, χ) unterscheidet und an der Davenport–Heilbronn-Funktion scheitert, also
  das Euler-Produkt benutzt. Quasi-RH tut das (Möbius-Summen μ(n) über Ideale von ℤ[ω], Mittelquadrat über eine Familie sextischer Twists,
  Poisson-Summation zu kubischen Gauß-Summen = Koeffizienten von Kubotas kubischer Thetafunktion, deren Automorphie, großes Sieb). Die
  J-Symmetrie s ↦ 1 − s̄, das Zentrum des RH-Papers, trägt dort im entscheidenden Schritt nicht.
- **Sektorsprache:** Mit Re ρ = ½ + γ⁻ ist Quasi-RH die Schranke \|γ⁻\| < 3/8 (bzw. 5/12) für den kontravarianten Anteil. Umformulierung,
  kein Beweisschritt; sie gibt dem Programm einen **dritten Prüfstein**: Ein Ansatz, der RH beansprucht, muss mindestens eine bekannte
  nullstellenfreie Region reproduzieren.
- **Mengen-Argument (B8):** Soll der Beweis „aus der Menge“ kommen, muss die Menge eine Familie von Twists und eine automorphe Symmetrie tragen,
  nicht nur (ℙ, log p).
- Lesart, ohne Gewicht: Die Einheiten von ℚ(√−3) (sechste Einheitswurzeln) liegen in der Hurwitz-Gruppe 2T, die der Companion auf dem
  neutralen Qubit nutzt. Gemeinsame Symmetrie, keine Herleitung.

## Ehrliche Buchführung
- Literatursichtung, keine Rechnung, keine neue Aussage über ein Problem. OP1–OP5, C5, C6/T2 offen; kein Guard (auch nicht RH) und keine
  Vorhersage berührt. Companion, Physik-Paper und Preprint unverändert.
- Alle Einstufungen beruhen auf Abstracts. Vor jeder Übernahme ist der Volltext zu prüfen; am meisten versprechen 148 (an der Moran-Gleichung
  von OP1, mit Wolfram) und 149 (Abgleich mit der C5-Rekursion).
