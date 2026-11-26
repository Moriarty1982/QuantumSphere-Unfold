# v4.10.0-r64 und Berichtigung des Physik-Artikels „One Object, Three Frames“ (26.11.2026)

Auftrag des Autors vom 26.11.2026: den veröffentlichten Artikel 1.0.0 (doi:10.5281/zenodo.24539644) auf Richtigkeit prüfen und berichtigen.
Geprüft wurde jeder Satz, jede Zahl, jede Formel und jede Belegstelle in `paper/physics-standalone/` gegen den Companion (Runden bis r63),
das Testregister (`wiki/Vorhersagen-und-Tests.md`) und die Ergebnis-Notizen H128–H156. Vier unabhängige Prüfungen je Abschnittsgruppe,
danach Zusammenführung und Gegenprüfung der Belegstellen. Zahlen sind mit Python nachgerechnet; die Skripte der Abbildungen wurden neu
ausgeführt und geben dieselben Werte.

**Die Zenodo-Fassung 1.0.0 ist unverändert.** `release-info.tex` und `article.pdf` im Repo bleiben auf dem Stand 1.0.0; eine neue Fassung
entsteht nur mit Freigabe des Autors. Der berichtigte Text hat 50 Seiten, keine offenen Verweise, keine Overfull-Boxen.

Weil der berichtigte Artikel auf Befunde verweist, die in keiner Runde standen, gibt es die Sammelrunde **v4.10.0-r64**
(`rounds/v4100_r64_round.tex`, angehängt an `sources/research/parts/v4100-post-release-layers.tex`). Sie rechnet nichts neu.
H138–H156 stehen in r62 und r63 (PR #329).

## Runde r64

| Eintrag | Inhalt | Test, Skript |
|---|---|---|
| r64.1 | dim Der(H₃(𝕊)) = 22 = g₂ ⊕ su(3); r(u) = 1 − (1 − u₈²)/10: 9/10 für e₇, 1 für e₈; Vorzeichen offen | H128 (a widerlegt, b für e₇ bestätigt, für e₈ widerlegt), k283 |
| r64.2 | Oktonionische, farbstabile Träger nur bei u₈ = 0; bei u = e₈ nicht alternativ. CT-003 wird nicht gestützt, bleibt Platzhalter | H130 (a, b bestätigt), k258 |
| r64.3 | Mischung: eine Klasse (TM2, δ = 0/180°); Frame-Regel für Datenvergleiche; TM1 mit Maske verträglich, keine Vorhersage | H131, H134, k260–k263 |
| r64.4 | Rekursive Feldgleichung auf dem Turm legt keine Skala fest; Zahlentreffer κ = 1,2004 kein Beleg | H129, H133 nicht bestätigt; H132, H135, H136 widerlegt; k290–k305 |
| r64.5 | H105 ist vergeben und offen (Frist 31.12.2028); „H105 bleibt frei“ (r18) überholt | H105, k227 |
| r64.6 | Zahlen: m_W (SU(2)-Zählung) 82,69 statt 82,68 GeV (r08.3); γ_L = 1,86444/1,8645 ist der Wert zur gerundeten Eingabe; Koide 0,43σ; H102 mit ρ² = 0,500014 | – |
| r64.7 | r29.4 ist mit D: z ↦ iz zu lesen; der Tausch J aus r63 ist antilinear (J_B-Typ), nicht D; Fixpunkt ist Re Ψ² = 0, nicht P | – |
| r64.8 | Geltungsbereich: Dorau–Much (Skalarfeld), prop:compensator („erzeugt das Photon“ überholt), r30.6 („alle“ Zahlen), r19.4 (Formeln bestätigt), zwei Türme HS(n) | – |

Guards unverändert: Γ_guard = (1,1,1,1,1), R_glob = (0,1,1,1,1), β₄ = 1/256. OP1–OP5, C5, C6/T2 offen.

## Änderungen im Artikel

Art: **F** Fehler, **Ü** zu starke Aussage, **V** veraltet seit H128–H156, **B** Belegstelle, **K** Konsistenz. Zeilen nach der Fassung 1.0.0.

### Zusammenfassung und Einleitung (`00-abstract.tex`, `01-introduction.tex`)
| Art | Stelle | vorher | jetzt | Quelle |
|---|---|---|---|---|
| Ü | Abstract Z. 11 | sin δ_PMNS < 0 als direkte Folge der Platzhalter-Achse | braucht eine weitere Setzung (S1) | r59 |
| Ü | Abstract Z. 12 | „Koide ist äquivalent zu mittlerem Überlapp ½“ | nur in der Gram-Lesart; mittlerer quadratischer Überlapp | r12.2 |
| V | Abstract, Einl. Z. 57 | „Überlapp ist Eingabe“ | dazu: zurückgeführt auf ein Postulat (Tausch von Materie- und Tachyon-Frame), δ = 2/9 Fit, Generationszahl Eingabe | H140, H149, H155, H156; r62, r63 |
| Ü | Abstract Z. 14 | „alle bedingten Zahlen ruhen auf β_sym“ | die Werte für OP2–OP5, je über eine eigene Setzung | r30.6, r55.1, r64.8 |
| Ü | Abstract Z. 15 | gemeinsame Wirkung ohne Bedingung | „durch Entscheidungen des Autors aufgestellt“ | v4.9.0-r81 |
| K | Einl. Z. 22, 30, 63 | – | „des freien Trägers“; Hinweis auf r62–r64; Stand der Testzählung 6.11. | r16.6, r05.2 |

### Träger und Frames (`02-carrier.tex`, `03-frames.tex`, F1)
| Art | Stelle | vorher | jetzt | Quelle |
|---|---|---|---|---|
| B | 02 Z. 97 | Projektions-Aussage mit `prop:compensator` belegt | Label entfernt (ist eine andere Aussage); Quelle v4.8.0-r04.2 | Haupttext |
| F | 02 Z. 112, 215 | „der Companion hat die Aussage ‚erzeugt das Photon‘ korrigiert“ | korrigiert ist nur die Orthogonalität (r03.4); der Satz ist durch r23.2 überholt | r64.8 |
| Ü | 02 Z. 230 | Generationszahl „erfordert die größere Algebra“ | wird auch dort nicht hergeleitet, ist Eingabe | H138, H140 |
| Ü | 03 Z. 38 | „jede Aussage des Companion trägt ihren Frame“ | ab v4.9.0-r22 verlangt | Konvention F |
| Ü | 03 Z. 59, 99, Tab. | Ladungen in M und T gleich: gesichert | gesichert als Algebra, unter der Lesart „ℂ-Faktor = Amplitudenebene“ | v4.9.0-r33, r51 |
| B | 03 Z. 74 | Teil (b) ohne Quelle | v4.8.0-r20.1 ergänzt | – |
| K | 03 Z. 143 | φ = sech 2η_R ohne Herleitung | einzeilige Herleitung ergänzt | r21.8 |
| Ü | 03 Z. 178, Tab. | Dorau–Much „hergeleitet“; Kette in M stillschweigend | „Argumente“, reelles Skalarfeld, führende Ordnung; Kette in M als Annahme | r06.1, r64.8 |
| B | 03 Z. 209 | r07.4 | r07.4 mit r61.2 | r61 |
| V | 03 §3.6, Tab. | „Frame-Abbildungen geben Gleichungen, keine Werte“ | Ausnahme: Fixpunkt einer Tauschabbildung (K = ⅔ bei π/4 unter Postulat); J ist J_B-Typ, nicht D | r63, r64.7 |
| K | F1 | Feldklassen nur aus dem Kompensator | Kante Kern → Klassen | r21.8 |

### Teilchen und Koide (`04-particles.tex`, `05-koide.tex`, F4)
| Art | Stelle | vorher | jetzt | Quelle |
|---|---|---|---|---|
| V | 04 Z. 179, 277, F4 | Weg A: zwei Generationen, kein Wort zu den Kopien | drei Oktonion-Kopien = drei Lesarten einer Generation | r59.9, r62 (H138, H140) |
| V | 04 Z. 176 | CT-003 ohne Einschränkung | H130 stützt die Achse e₈ nicht | r64.2 |
| Ü | 04 Z. 86 | „übrig bleibt das Standardmodell“ | Ladungszuordnung einer Generation, unter der Setzung | v4.9.0-r43 |
| V | 05 Z. 11 | K = ⅔ „besser als 0,005 %“ | K = 0,6666645 ± 0,0000051, 0,43σ unter ⅔ | H154, r63.5 |
| V | 05 Z. 17, 310 | nichts zur Mischwinkel-Form | K = 1/(3cos²θ), π/4 Fixpunkt von J; Symmetrie-Argument unter Postulat; Schleife {1,U} Setzung; δ Fit | r63 (H148–H156) |
| K | 05 Z. 139, Tab. | H102: m_τ = 1777,134 MeV | mit ρ² = 0,500014 aus m_e/m_μ, nicht ½ | Vorab-Notiz H102 |

### Frame-Versatz, Λ und OP5 (`06-beta.tex`, `08-lambda-op5.tex`)
| Art | Stelle | vorher | jetzt | Quelle |
|---|---|---|---|---|
| F | 06 Z. 115 | m_W = 82,68 GeV (SU(2)-Zählung) | 82,69 GeV | k218-Ausgabe, r64.6 |
| Ü | 06 Z. 5 | „jeder Zahlenwert außerhalb der reinen Algebra“ | die Werte für OP2–OP5 | r30.6 |
| F | 06 Z. 7 | β_sym „ist das Verhältnis“ | „ist durch das Verhältnis festgelegt“ | Definition |
| K | 06 Z. 41, 44 | γ_L als Faktor zwischen M und T; „T ist das J_B-Bild“ | zwischen den reellen Projektionen; Abbildung nach T kehrt Re s um (mit D gelesen) | v4.9.0-r61.1(c), r64.7 |
| K | 06 Z. 70 | „Leptonfenster enthält nur das U(1)-Paar“ | „von diesen dreien“ (H98: zwei Paare) | r09 |
| V | 06 Z. 100, 117 | „die vier offenen Vorhersagen“ | „die damals vier offenen“; heutiger Stand ergänzt | Wiki |
| Ü | 06 Z. 196 | Querungs-Lesart „im Companion gestützt“ | verweist auf einen erzählenden Satz und eine Typisierung | r24.4 |
| Ü | 06 Z. 221 | LQG-verträglich nur bei nicht unitärer Abbildung | zweite Option (γ_T als Mittelwert) ergänzt | r30.1 |
| K | 06 Z. 322 | Widerlegt-Liste ohne H123b | ergänzt | Wiki |
| Ü | 08 Z. 36 | Λ-Auslesung „ohne freien Parameter“ | „sobald das Paar der Zählregeln gewählt ist“ | v4.9.0-r63 |
| Ü | 08 Z. 56 | „jeder Schritt exakt in Wolfram geprüft“ | die algebraischen Schritte 32.2, 32.4–32.6 | r32 |
| K | 08 Z. 130 | „relative Größe β²“ (Detektorgeschwindigkeit) | v²/c² | r46.3 |
| K | 08 Z. 131–157 | j₀, j_m, r₀, α undefiniert; Schranke ohne Bedingung | Definitionen; „für Z = 1, g₀ = g_m“; „nahe dem Gleichgewicht“ | r47, r50.3, H120b |
| K | Skripte F7, F10 | absolute Pfade in der Ausgabe | relative Pfade; Zahlen identisch | – |

### Wirkung, offene Probleme, Schluss, Anhänge (`07`, `09`, `10`, `A-ledger`, `B-reproduction`, F8)
| Art | Stelle | vorher | jetzt | Quelle |
|---|---|---|---|---|
| F | 07 Z. 222 | γ_L = 1,8645 | 1,8647 (wie Abschnitt 9) | r64.6 |
| K | 07 Z. 125 | Prüfungen und Fehleroffenlegung einer Runde zugeschrieben | je der richtigen Runde (r01, v4.9.0-r86) | r01.1, r86.3 |
| Ü | 07 Tab. | H88, H90 „gesichert“ | dazu „nicht blind“; H90 numerisch an generischen Punkten | Wiki |
| Ü | 07 Z. 286 | Beimischung exponentiell abgeschnitten (H86) | H86 nicht blind, nach H85 aufgestellt; H87b widerlegt | r85.6, r86.1, r02.3 |
| Ü | 07 Z. 304 | „offenes Problem für ΔN_eff“ | ΔN_eff ≈ 3,6 bzw. ≈ 2,6 gegen Schranke ≈ 0,3 | r05.1 |
| V | 07 §7.6 | – | späterer Schleifen-Ansatz auf dem Turm legt ebenfalls keine Skala fest | r64.4 |
| Ü | F8 | Maxwell-Pfeil als „hergeleitet und geprüft“ | Maxwell-Gleichung war vorausgesetzt | r01.1 |
| V | 09 OP3 | „OP3 ruht“ | seit 25.11. wieder aufgenommen: Kopien, π/4, Postulat, δ Fit | r62, r63 |
| Ü | 09 OP4 | „ein Vorzeichen ist von der Struktur festgelegt“ | nur unter CT-003; S1 weitere Setzung | r59.6 |
| K | 09 Tab. | H105 fehlte; H125 ohne NuFIT-Hinweis; H102 ohne Vergleich | H105 genannt; NuFIT neigt schon zu sin δ < 0; exaktes Koide bei +0,4σ | Wiki, r64.5 |
| F | 10 | „H42, H112, H125“ hängen nicht an β_sym | auch H100 | r12.5 |
| Ü | 10 | „jede bedingte Zahl geht auf β_sym zurück“ | die Zahlen in OP2–OP5 | r30.6 |
| K | A-ledger | H98 „bestätigt“; H123d „widerlegt“; Albert „gesichert“ | „nur bei festem Spektrum (H104)“; „trägt nicht“; „gesichert als Algebra“ | r14.1, r58.3, r60 |
| F | B Z. 17 | „jede Runde endet mit ‚Proof and measurement sources‘“ | nur ein Teil der Runden; jede nennt Notizen oder Skripte | Zählung |
| F | B Z. 25 | „alle Test-Notizen in `predictions/`“ | Ablageorte je Nummernbereich | git ls-files |

## Geprüft und unverändert (Auswahl)
Alle übrigen Rundenverweise wurden geöffnet und enthalten die Aussage. Nachgerechnet: β_sym = 0,549406, γ_L = 1,864700, γ_BI, γ_SU(2),
die Zählpaare (H98), die Koide-Zahlen (Wurzelverhältnisse, det G, Phasen), die Attraktor-Zahlen (χ² = 18,42, Δχ² = 7,87), Λℓ_P² = 2,85·10⁻¹²²,
die OP5-Schranken. r56/r61: Der Artikel benutzte bereits ρ_Λ = Λ/κ und die Wurzel in β_sym. Alle Teststatus der Tabellen stimmen mit dem Wiki.
Tachyon-Abbildung und Zeitumkehr sind im Artikel durchgehend getrennt. Literaturangaben stimmen (eine Ausnahme offen: Titel der Zeitschriftenfassung von Ghosh–Mitra nicht online prüfbar).

## Offen gelassen
- Ob Weg A (r13) und das CP-Vorzeichen (r59.6) auf der Ladungsrichtung e₇ bestehen, ist nicht gerechnet (r64.2).
- „Brannens δ = 2/9“: Brannen selbst schreibt die Formel G. Rosen zu; im Artikel unverändert, in r64.8 vermerkt.
- Das Physik-Paper der v5.4.0 (`qam/editions/`) und der deutsche Preprint sind nicht Teil dieser Prüfung.
