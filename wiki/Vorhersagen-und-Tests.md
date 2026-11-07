# Vorhersagen und Tests

**Stand: 7. November 2026.** Die Runden v4.10.0-r06 (Literaturbezug Dorau–Much) und r07 (die Kette im Tachyon-Frame) enthalten keinen Test und keine neue Vorhersage; ein geplanter Test zu r07 wurde nicht vergeben, weil das Ergebnis analytisch feststand. Seit v4.8.0 gilt eine feste Regel: Eine neue Vorhersage oder ein Test wird **vor** der Rechnung als Vorab-Notiz festgeschrieben (Hypothese, Daten, Entscheidungskriterium) und committet. Erst dann wird gerechnet. So lässt sich später prüfen, dass nichts nachträglich angepasst wurde. Diese Seite listet alle Tests mit ihrem Ergebnis. [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie) · [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt)

## Offene Vorhersagen (warten auf neue Daten)

**Abhängigkeit (v4.10.0-r08, präzisiert in r10):** H15, H46 und H96 ruhen auf demselben Kern (γ_BI, γ_string und die Zuordnung der Zählregeln zu den Frames, U(1) statt SU(2)); H42 ist davon unabhängig. Die vier sind also zwei unabhängige Prüfungen. Wird eine der drei Kern-Vorhersagen widerlegt, steht zuerst die Zählregel unter Verdacht. Alle vier haben in der QAM-Buchführung den Status einer Lesart.
Nach v4.10.0-r10 ist der gemeinsame Kern gleichwertig mit einem frame-abhängigen Flächenquantum (γ_M/γ_T = γ_L); eine Begründung dafür fehlt.
Nach v4.10.0-r11 (Einordnung der OP5-Rekonstruktion) ist Ω_M = β² ausdrücklich eine zusätzliche Gleichsetzung von Registerverhältnis und Dichteanteil; H96 bleibt unverändert offen, ohne neuen Beleg und ohne Änderung des Kriteriums.

| Nr. | Vorhersage | Prüfdaten | widerlegt, wenn |
|---|---|---|---|
| **H9** | $\sin^2\theta_{12} = \beta_{\mathrm{sym}}^2/\cos^2\theta_{13} = 0{,}3086$ | künftige JUNO-Daten | Kriterium in der Vorab-Notiz; nachträglich gefunden, also nicht blind gewählt |
| **H15** | W-Masse $m_W = 80{,}3615 \pm 0{,}0018$ GeV | erste Weltmittelung nach dem 21.10.2026 | Kriterium in der Vorab-Notiz; noch offen. PDG 2026 (Mai 2026, vor H15) 80,3625 ± 0,0077 GeV, kein Test (v4.10.0-r04) |
| **H42** | $\sin^2\theta_{23} \le 0{,}54$ (normale Ordnung) | erste globale Auswertung oder DUNE/Hyper-K-Messung nach dem 24.10.2026 | das 2σ-Intervall liegt ganz oberhalb 0,54 |
| **H46** | $\sin^2\theta_{23} \in [0{,}49;\,0{,}50]$ unter der Lesart $\varepsilon = \eta$ (schärfer als H42) | dieselben Daten | das 2σ-Intervall berührt [0,49; 0,50] nicht |
| **H96** | $\Omega_M = \beta_{\mathrm{sym}}^2 = 0{,}30185$ heute (Λ-Auslesung, kein freier Parameter) | erstes flaches-ΛCDM-$\Omega_m$ aus DESI DR3 (BAO allein) oder Euclid nach dem 6.11.2026 | Abweichung größer als 2σ |

Zu H46: Eine Bestätigung würde die Kette r55–r60 prüfen, nicht die Lesart allein; auch andere Modelle sagen $\theta_{23}$ nahe 45° voraus. Heutige Daten (NuFIT 6.0) entscheiden nicht: 0,561 ohne und 0,470 mit atmosphärischen Super-K-Daten.

## Abgeschlossene Tests

| Nr. | Hypothese | Ergebnis |
|---|---|---|
| H1 | Koide-Phase $\delta = K/3$ | widerlegt für Quarks und laufende Leptonmassen |
| H2 | Neutrinos als lichtartige Triole | verträglich; sagt normale Ordnung und $\sum m_\nu = 0{,}0592$ eV voraus; normale Ordnung von JUNO gestützt |
| H3 | Vorzeichen als Majorana-CP-Parität | verträglich, derzeit nicht prüfbar ($m_{\beta\beta} \le 3{,}5$ meV) |
| H4 | TM1 gegen TM2 | TM1 zunächst bevorzugt, nach JUNO disfavorisiert |
| H5 | Hopf-Winkel als Mischwinkel | gescheitert |
| H6, H7 | Kriterien, die den TM1-Lift auswählen | weder Minimalität noch Kaskade noch Kompensator wählen ihn |
| H8 | Cayley–Dickson-Involution als CP-Symmetrie | nach JUNO disfavorisiert |
| H10 | Assoziator als Auswahlkriterium | kein Auswahlgrund |
| H11 | Massen aus invarianten Funktionen auf dem Tripel-Raum (bis Grad 4) | widerlegt: höchstens zwei verschiedene Massen |
| H12 | Zuordnung des Versatzes zu Kreuztermen | gegen H9 nicht trennbar; Grenze setzt $\Omega_M$ |
| H13 | Wigner-Holonomie als Auslesefaktor | widerlegt ($z = -7{,}9$) |
| H14 | Kegelwinkel = $2\theta_W$ | widerlegt ($z = +8{,}2$) |
| H16, H17 | Massenpotentiale bis Grad 6, Realteil-Invarianten | widerlegt: nur Sattelpunkte |
| H18 | Massen aus links-invarianten Etiketten | widerlegt |
| H19–H21 | Ladungen in der Dixon-Ablage, innere gegen äußere Einheit, Herkunft der Doppelbelegung | Ladungsmuster einer Generation reproduziert (keine Vorhersage); wörtliche alte Zuordnung widerlegt; Farbe und Generation im alten Text dasselbe Objekt |
| H22–H24 | Triality als Selbstdurchwanderung, Frame-Triole, Zoom | strukturelle Befunde (Generation = Bahn, Farbe = Fixgruppe, Photon = Vektor-Platz) |
| H25–H28 | Kontraktion über Frames, Verteilung der Quaternion-Rollen, Kompensator als Chiralität, Wahl des Projektors | volle Generation mit Neutrino unter Wahlen; Anomaliefreiheit wählt den Projektor |
| H29–H32 | Massenterme, Brechungen, Masken | strukturelle Befunde; Linearitätsannahme H32c in 4 von 200 Fällen widerlegt |
| H33–H36 | $e_7$-Achse, Mischung aus der Maske, $e_7$ und die Frames, exakte Kopplungsformen | $e_7$ trägt $B-L$; Maske erklärt CKM nicht (auf ±20 % in keiner Kombination) |
| H37 | Kopplungen aus der Triality-Form | widerlegt; für Dirac-Neutrinos $\sum m = 0{,}115$ eV, über der DESI-Grenze |
| H38 | ein $\varepsilon$ je Sektor | trifft CKM und PMNS, aber als Anpassung |
| H39 | Lesart je Teilchenart | TM2 mit $\sin^2\theta_{12} \approx 0{,}341$, 3,6σ über JUNO 2025 |
| H40 | Kalibrierung der Ausleseschicht | 16 Einstellungen für 17 Größen; Korpus-Kandidaten treffen nicht mehr als Zufall |
| H41 | TM2 mit Maskenkorrektur | trifft alle drei Winkel; $\theta_{23}$ nicht festgelegt |
| H43 | CP-Phase aus TM2 | nicht festgelegt |
| H44 | $\varepsilon$ aus einem Strukturwert | kein Treffer |
| H45 | $\varepsilon$ als Rapidität des Materie-Frames (nicht blind) | trifft; daraus H46 |
| H47 | $\beta_{\mathrm{sym}}$ als Verhältnis zweier Horizontzählungen (nicht blind) | Domagała–Lewandowski/Meissner im Fenster, Ghosh–Mitra nicht; bestätigt in r68, aber nur mit U(1)-Zählung |
| H48 | $\beta_{\mathrm{sym}}$ als eingefrorene Länge des Materie/Tachyon-Zustands | widerlegt: hängt an der Expansionsgeschichte; Einstein–Cartan-Term wirkungslos |
| H49 | OP5-Vergleichssystem: abseits des Äquators tritt schon bei den zweiten Ableitungen eine versteckte Bedingung auf | widerlegt: Verträglichkeit überall auf Rauschniveau ($10^{-10}$); die Prämisse eines Symmetriebruchs war falsch (r71) |
| H50 | $\Omega$ wirkt über die $\vartheta$-Richtung auf $\Psi$ zurück (Frage des Autors) | widerlegt: $\Omega$ ist eichinvariant, Änderung höchstens $1{,}5 \cdot 10^{-10}$ gegen 0,04 bis 0,11 in Kontrollrichtungen (r71) |
| H51 | Das $\vartheta$-geeichte OP5-Symbol besteht den Cartan-Test erstmals bei Ordnung 6 | bestätigt: nicht involutiv bei 4 und 5, involutiv bei 6 und 7, in drei Koordinatensystemen (r72) |
| H52 | Das geeichte System ist ab Ordnung 6 formal integrabel (fester Keim bis Ordnung 5) | ungültig: Ränge ohne saubere Lücke; die gespeicherte fünfte Ordnung ist nicht fortsetzbar (Planungsfehler) (r72) |
| H53 | Wie H52, aber nur Ordnung 4 fest und exakte Linearisierung | ungültig: ein Rang ohne saubere Lücke; bis Grad 6 alles wie vorhergesagt, mit Grad 7 vier zusätzliche Bedingungen an 6-Jets (r72) |
| H54 | Es gibt genau vier versteckte Bedingungen an 6-Jets | ungültig: Lückenforderung an absichtlich gestörten Varianten war unerfüllbar; die Fehlerschranke spricht inhaltlich für genau vier (r72) |
| H55 | Die vier versteckten Bedingungen treten auch an einem zweiten Ausgangspunkt auf | bestätigt: wieder 852 und 848 Freiheitsgrade, Fehlerschranken 710- und 1390-fach (r73) |
| H56 | Das um die vier Bedingungen erweiterte Symbol wird bis Ordnung 8 involutiv | ungültig: ab Ordnung 8 Ränge ohne saubere Lücke; bei 6 nicht involutiv (r73) |
| H57 | Wie H56 mit projizierten Bedingungen (nicht blind) | ungültig: bei Ordnung 8 nicht entscheidbar (723 oder 724); Genauigkeit reicht nicht (r73) |
| H58 | Wie H56 mit konsistenten Daten am reparierten Keim (nicht blind) | ungültig: fünf Ränge knapp unter der Schwelle; Zahlen wie vorhergesagt, erstmals bei Ordnung 8 involutiv (r74) |
| H59 | Keine weiteren versteckten Bedingungen auf 7- und 8-Jets (Fasern 594 und 723) | bestätigt: 594 und 723, Gegenprobe 477, Lücken ≥ 4·10⁵⁶, parallel auf GitHub-Runnern (r77) |
| H60 | 6 reelle Polarisationen je Lichtrichtung im involutiven Symbol | bestätigt: 6 in allen 200 Richtungen bei Ordnung 6 bis 9, außerhalb des Kegels 0 (r77) |
| H61 | Die 6 Moden sind Weyl-Moden gleicher Chiralität (naive Spin-Zuordnung) | widerlegt: weder unter i noch unter γ₅ noch unter der Helizität invariant (r77) |
| H62 | Die Symmetrie-Algebra des Symbols enthält eine Lorentz-Algebra | widerlegt: nur Skalierung; bei festem Hintergrund strukturell erwartet (r77) |
| H63 | Der dynamische Teil F ist lorentzsymmetrisch, die Brechung sitzt in G | widerlegt: schon F nicht (7 Raumzeit-Symmetrien, keine Lorentz-Algebra); mit G bleibt nur die Skalierung (r77) |
| H64 | Die Konstruktion R ist koordinaten- und intern lorentzkovariant | bestätigt (zweiter Lauf, nicht blind): Residuen ≤ 4·10⁻¹⁰, Gegenprobe ohne Hintergrund-Transformation 0,26 (r77) |
| H65 | R ist auf Werteebene kovariant; die Eichung wird genau von so(1,2) erhalten | ungültig: (b) wie vorhergesagt, (a) Kontrollschranke 10⁻¹² zu streng gewählt (r78) |
| H66 | R ist auf Werteebene kovariant (Kontrollschranke 10⁻⁹, nicht blind) | bestätigt: Residuen ≤ 2·10⁻¹¹, Gegenprobe ohne Hintergrund-Transformation 57 bzw. 1200 (r78) |
| H67 | Zahl und Lage der vier versteckten Bedingungen sind eichunabhängig | bestätigt: in fünf Eichungen (darunter Ψ̄Ψ) jeweils 477 und 6 Polarisationen (r79) |
| H68 | Der Hintergrund A, h erfüllt Yang–Mills (auf span(λ₂, λ₄, λ₆)) und Klein–Gordon mit den Spinorblöcken als Quelle, je mit einer Kopplung | widerlegt: Residuen 0,955 / 0,995 / 0,826 in der Koframe-Metrik, Quellen rund 10³ zu klein (r80) |
| H69 | Ein um δ versetztes Paar aus Materie und Tachyonbild (Konvention F) hat keinen Nettostrom (genau bei Δω·δ = π mod 2π) und keinen Nettoenergie-Impuls | bestätigt: Residuen 5e-15 und 1e-15, Kreuzterme eingeschlossen; klassisch, Vorzeichen des Tachyon-Anteils als Eingabe (Notizen zu W1) |
| H70 | Nur ein mitbewegt fester Versatz erhält das Paar auf FRW (a); falsche Kopplungen erzeugen keinen homogenen Rest (b) | a bestätigt (δ = 1/H und die Form aus thm:expansion scheitern); b widerlegt: homogener Rest, aber nicht Λ-artig, Folge verletzter Feldgleichungen |
| H71 | Massiver Partner: Antiteilchen/Spiegelpartner normal massiv, Tachyonbild tachyonisch (a, b); das Tachyonbild erfüllt die Strombilanz der komplexen Lesart (c) | a, b bestätigt (ω² = k² − m² mit negativer Norm); c widerlegt: raumartiger Strom, keine Variante mit Masse erfüllt die Bilanz |
| H72 | Ein Gas tachyonischer Moden kann einen Λ-artigen Term erzeugen (a); seine Höhe ist frei (b); die Frame-Gewichte legen ihn bei einem Impuls fest (c) | a, b bestätigt (p = −ρ isotrop aus Moden beider Normvorzeichen auf zwei Impulsschalen); c widerlegt |
| H73 | Bezugszustände der Frames (Materie in Ruhe, Tachyon an der Schwelle) mit den Gewichten des Materie-Frames geben w ≈ −1 | widerlegt: w = −β_sym²/3 = −0,10, ohne freie Parameter; nachträglich im Tachyon-Frame −1,105 (nicht vorregistriert) |
| H74 | Direkte Kopplung εφχ zwischen Materie- und Tachyonsektor: gleiche Spektren instabil für jedes ε > 0, verstimmte beschränkt unterhalb einer Schwelle (nicht blind) | bestätigt: Rate ε/2ω (gemessen 5,011·10⁻⁴, 4,985·10⁻³, 0,0498); verstimmt Schwelle |ω₁²−ω₂²|/2; Lauf 1 zu kurz geplant, Lauf 2 offengelegt (r82) |
| H75 | Gravitation als einzige Kopplung: bei Photon-Gewichten keine exponentielle Instabilität (a), Jeans-Rate bei Materie-Gewichten (b), Bondi-Durchgehen (c) (nicht blind) | b, c bestätigt; a ohne exponentielles Wachstum, aber der Gleichtakt wächst wie t², die Schranke „höchstens linear“ war im Grad falsch (r82) |
| H76 | Vakuumzerfall 0 → φφχχ über das Graviton: Lorentz-invariant unbeschränkt (a); mit Rahmen-Cutoff Γ/V = c·Λ⁸/M_P⁴ (b); Schranke weit unter der Higgs-Skala (c) (nicht blind) | a, b, c bestätigt: Verhältnisse gegen 4 (Γ ∝ L²); c = 2,25·10⁻⁵, Exponent 8,000; Λ ≲ 14 MeV (grob); Lauf 2 nicht konvergiert, Lauf 3 halbanalytisch (r83) |
| H77 | Nur die Lesart „Kinematik fortgesetzt“ (B) des Tachyonbilds einer Wirkung ist mit r07, r20, H71, r81 und F3 verträglich (nicht blind) | bestätigt: A gibt normale Dispersion (Geist), B′ verletzt r81 und F3; Folge: r82.1(b), (c) zurückgezogen (r83) |
| H78 | T als zweite Lesart in der Form von k174 (Spinor gedreht, Argument verschoben): Skalar stabil (a), Weyl anisotrop mit Faktor (a+b)/(a−b) quer zu n (b), keine eigenen T-Quanten (c) (nicht blind) | a, b, c bestätigt; Faktor γ = 1,86 für Fermionen → durch Laborgrenzen ausgeschlossen; δ-Probe Lauf 1 mit nicht periodischem Testfeld offengelegt (r84) |
| H79 | Vollständiger komplexer Boost: holomorphe Adjungierte gibt (a−b)S_M isotrop mit entgegengesetzter Energie (a), hermitesche (a+b)S_M (b), Skalar unverändert (c) (nicht blind) | a, b, c bestätigt; Autor legt holomorph fest (r84) |
| H80 | Spiegelung um den Urknall (δ = 0): Modengleichung exakt die des Materie-Skalars mit m² ↦ γm² (nicht blind) | bestätigt, für Strahlung, Materie und beide Fortsetzungen (r84) |
| H81 | Versatz δ ≠ 0: Kinetik verschwindet bei τ* = β_sym δ/(1+β_sym) (a), regulär singulärer Punkt mit Modenauswahl (b), tachyonisches Wachstum davor über Faktor 10 (c) (nicht blind) | a, b bestätigt; c quantitativ widerlegt (Faktor 1,57 bei mδ = 3); Wahl k = m = 1 in b offengelegt (r84) |
| H82 | Massen und Kopplungen unter der zweiten Lesart: Faktoren nach Ableitungszahl (a); Übereinstimmung mit den r19-Gewichten (b) (nicht blind) | a bestätigt; b widerlegt: α, α_s, θ_W passen, G (1 statt 2) und ℓ_P (½ statt 3/2) nicht (r85) |
| H83 | Eine von drei Regeln (R1; g ↦ −g; Metrik c·g) trifft k(α) = 1 und k(G) = 2 zugleich (nicht blind) | widerlegt: G immer γ¹; aus g ↦ −g folgt für Spinoren −i (r85) |
| H84 | Quantenmoden sind an der Epoche τ* singulär, Energiedichte ∝ 1/|τ − τ*| mit Vorzeichenwechsel (nicht blind) | bestätigt (E·|τ − τ*| → −0,150 / +0,149) (r85) |
| H85 | Weicher komplexer Übergang am Urknall: Grenzfall langer Wellen (a), Mischung verschwindet bei kurzen Wellen (b) (teilweise nicht blind) | a, b verfehlt (Rollen von C und D vertauscht, Konvergenz linear); nachträglich CPT-Zuordnung bemerkt (r85) |
| H86 | CPT-Zuordnung, exponentieller Abfall der Beimischung, Grenzfall langer Wellen, Asymmetrie der Drehsinne, an neuen Einstellungen (nicht blind, nachträglich motiviert) | bestätigt; Abfall-Steigung 2,67 statt π, knapp im Kriterium (r85) |
| H87 | Wolfram-Gegenprobe zu H86: Werte auf 10⁻⁵ (a), Steigung des Abfalls bei kΔ = 20–30 innerhalb 3 % von π (b), Formeln des scharfen Übergangs symbolisch (c) (nicht blind) | a, c bestätigt; b widerlegt wie formuliert (2,956, 5,9 % unter π); nachträglich Fit mit Potenzvorfaktor s ≈ π (r86) |
| H88 | Unabhängige Herleitung der W1-Feldgleichungen: Erzeuger, Torsion −(3/16)κ j², Weyl-Gleichung, Ward-Identität (nicht blind) | bestätigt, keine Abweichung (r86) |
| H89 | Energie-Impuls-Tensor von W1: Vier-Fermionen-Anteil, homogener Zustand, Belinfante aus der Vierbein-Variation (nicht blind) | bestätigt: T^(4f) in Λ-Form, homogen ρ = p > 0, erste Ordnung = −Belinfante; zwei Fehler im Prüfcode offengelegt (r86) |
| H90 | Volle Einstein–Cartan-Gleichung von W1: Cartan-Lösung, Einstein-Gleichung mit T^eff, Bianchi-Verträglichkeit, Vorzeichen der Gravitationswirkung (nicht blind) | bestätigt; W1 wie notiert stößt ab (G̃ = −κT), korrigiert auf −R/2κ (Autorentscheidung); Vorzeichen aus H88, H89 und r82.4 umgekehrt (v4.10.0-r01) |
| H91 | Abfall der Beimischung bis kΔ = 60: Exponent π (Fit mit √x), Wurzelterm nötig, Steigung 50–60 innerhalb 3 % von π (teilweise nicht blind) | ungültig nach Kriterium a (Planungsfehler: H87 nur vierstellig); b–d wie formuliert verfehlt (v4.10.0-r02) |
| H92 | Vorfaktor = Stokes-Funktion r(λ) des lokalen Problems, λ = L kΔ/2: Universalität, Wellen, Drehsinne, Born-Grenzfall (teilweise nicht blind) | b, c, d bestätigt; a verfehlt (fester Faktor ≈ 0,54) (v4.10.0-r02) |
| H93 | Hergeleitete Asymptotik `ln\|C\| = −πkΔ + c√(kΔ) − ½ln(a/b)`, c = 2√π Γ(3/4)/Γ(1/4)·Re√L = 1,809205 (teilweise nicht blind) | Zahlen getroffen (c auf 0,013 %, Konstante ≤ 0,006, volles Problem ≤ 0,009); formal ungültig (Genauigkeitskontrolle Drehsinn +, kΔ = 600); Drehsinn − bestätigt (v4.10.0-r02) |
| H94 | Gewichtete Norm am Urknall-Übergang: Bosonen +1 → −1 mit genau einer Nullstelle, dazwischen nicht normerhaltend; Fermionen exakt −1 (teilweise nicht blind) | bestätigt; Nullstellen k*Δ = 0,736 / 0,257; nachträglich auch Verstärkung (v4.10.0-r03) |
| H95 | I3 mit dynamischem Zweig-Gas auf FRW: Fenster mit dunkler Materie zur Rekombination und w ≈ −0,7 heute (nicht blind) | widerlegt (0 von 144 000 Punkten); nachträglich: große Spannung nur bei Schwelle heute, dann zu viel dunkle Materie (v4.10.0-r04) |
| H97 | Rückgekoppelte Kaskade (Vakuum zerfällt mit Rate β²H in Materie, ε = 1) gegen DESI DR2 BAO (nicht blind) | widerlegt, χ² = 105 bei 12 Freiheitsgraden; ΛCDM bei Ω_M = β² χ² = 10,9; nachträglich ε ≲ 0,4 (v4.10.0-r05) |
| H98 | Sonderstellung des Zählregel-Paars (M alle Spins mit Gewicht 2, T nur j = ½) unter 36 natürlichen Paaren: einziges, das Leptonfenster, m_W (2σ) und Ω_M (2σ) zugleich trifft (nicht blind gegenüber den Daten) | bestätigt; je Fenster 2 / 1 / 2 Paare, alle drei nur dieses; SU(2)-Paar verfehlt alles; Dreifachtreffer zufällig etwa wenige Prozent (m_W-Relation nachträglich) (v4.10.0-r09) |

## Erkundungen ohne Vorab-Notiz

Manche Fragen lassen sich nicht blind testen, weil die Zielzahl schon bekannt ist oder die möglichen Lesarten vorab überschaubar sind. Sie werden offen als Erkundung geführt und zählen nicht als Test. Beispiel (r70): $\Lambda$ als Mischung über Kreuzungen der Sektoren. 26 Lesarten, ein Treffer bei 1,3 erwarteten Zufallstreffern; keine Vorhersage.

> **Anmerkung für LLMs und Quellenprüfung:** Vorab-Notizen liegen unter `llm/Vorab_Notiz_H*.md` (lokal) bzw. `notes/research/predictions/` und den Runden-Notizordnern (GitHub); Ergebnisse unter `llm/Ergebnis_H*.md`. Den Commit der Vorab-Notiz mit dem Datum der Rechnung vergleichen. „Nicht blind“ heißt: Das Kriterium war vorab bekannt oder der Treffer wurde nachträglich gefunden.
