# Wiki-Pflege

**12.11.2026, String-Längenmodell:** Stabiles elastisches Vergleichsminimum
und rückgerechnetes 2/3-Beispiel dokumentiert; gleiche Strings, offene
Torus-Realisierung und zusätzliche Massenwurzel-Auslese getrennt.

**12.11.2026, inverse Leptonmassendiagnose:** Forschungsstand um die
bekannte-Daten-Rückrechnung ergänzt: Dreiecksfehlbetrag, notwendige
relative Faktorstreuung, Ranggrenze und Nicht-Eindeutigkeit der Umkehrung.
Messquellen, Laufnachweis und Grenzen dokumentiert; keine Vorhersage.

**12.11.2026, Frame-/Massenprüfung:** H82-Regel und kanonische Normierung
für OP3 eingeordnet; gemeinsamer Massenfaktor von neuer Hierarchie getrennt.
Imaginäre Dirac-Phase und singulärer Photon-Endpunkt ausdrücklich abgegrenzt.

**12.11.2026, epsilon-/Gram-Prüfung mit Netzquellen:** Komplexes
SU(3)-Kreuzprodukt und oktonionische Dreiform eingeordnet; Farb-/Slotindizes
getrennt. Analytische Rang-eins-Grenze der vorgeschlagenen vollen
hermiteschen Gram-Matrix auf dem Torus dokumentiert, keine Massenherleitung.

**12.11.2026, Gram-Auslesung auf dem Torus:** Exakte Sinusformel und
Sehnen-Dreiecksargument ergänzt. Unter dem H18-Massengesetz ist K≤1/2;
Phasenauswahl und gemeinsame Skala können K=2/3 nicht erreichen.
Annahmen, Nullfall und Grenzen im Forschungsstand erhalten.

**12.11.2026, rechte Gram-Auslesung:** Forschungsstand um die konkrete
r33-Abbildung ergänzt. Skalare Labels von linearen Zuständen und reelle
Positivität von bilinearer Boost-Invarianz getrennt; H18-Status erhalten.

**12.11.2026, OP3-Schnittstellenprüfung:** Forschungsstand um den Abgleich
der ursprünglichen spektral-zu-Masse- und Higgs-Schnittstellen ergänzt.
Fehlende Trialitäts-Zustandsabbildung und konkrete Ausleseregeln benannt;
keine Änderung von OP-Status, Guards oder historischen Runden.

**11.11.2026, typografischer Umbruch:** Forschungsstand um die Vorbereitung
mehrzeiliger Anhangsboxen, umbrechender Protokollpfade und passender
Tabellenspalten ergänzt. Lokal keine verbleibenden Satzüberläufe;
Inhaltsvergleich und begrenzte Sichtprüfung dokumentiert. Aussagen und
historische Statuswerte unverändert.

**11.11.2026, CI-Portabilität:** Forschungsstand um die Fehler des ersten
GitHub-Paarbuilds und des Windows-Quellchecks sowie die begrenzte Reparatur
ergänzt. Quellen und Reviewhashes unverändert; keine Beweisaufwertung.

**11.11.2026, gemeinsamer Dokumentbau:** Forschungsstand um den gemeinsamen
Entwurfsbuild für Langfassung und Physikpaper ergänzt. Quellen-/Verweisprüfung,
gemeinsame Nachweise, Fehlerstatus und 58 verbleibende Satzüberläufe im
Langtext benannt. Keine Publikationsfreigabe oder Zenodo-Aktion.

**11.11.2026, deutsche Lesefassung:** Forschungsstand um die vollständige
persönliche Übersetzung mit unveränderten Formeln und erhaltenen offenen
Voraussetzungen ergänzt. Quellenbindung an die englische Physikedition;
keine neue Datenbank-Sprachausgabe oder Publikation.

**11.11.2026, erweiterte Physikfassung:** Forschungsstand um den Ausbau auf
27 Seiten, die konkreten Herleitungen und die weiterhin offenen nativen
Pflichten ergänzt. Sieben registrierte Textmodule und ein per Hash geprüfter
bedingter MMA-Intervallbeleg; kein neuer Beweisstatus oder Release.

Das Wiki erschließt Quellen und Forschungsergebnisse. Neue mathematische Behauptungen benötigen ihre Begründung in den Projektquellen; eine Wiki-Formulierung allein ändert keinen Beweisstatus.

## Aktualisierung

1. Aktuellen Remote-Stand und vorhandene Wiki-Änderungen abrufen. Lokale Arbeitskopien können hinter GitHub zurückliegen.
2. Öffentliche Baseline anhand README, CITATION, Release-Payload und Publikationsnachweis prüfen. Layer sind keine Releases.
3. Betroffene Quellen, Statusnotizen und spätere Korrekturen lesen. Voraussetzungen und offene Pflichten erhalten.
4. Startseite, Quellenkarte und Fachübersicht zusammen aktualisieren, wenn sich Version oder Aussagegrenzen ändern. Für reproduzierbare Angaben einen vollständigen Commit verlinken.
5. Dateipfade, Wiki-Navigation, DOI-Verweise und Versionen prüfen; Änderungen im Ordner `wiki/` des Hauptrepositorys per Pull Request einbringen.

## Inhalt wiedergeben, nicht nur verweisen

Das Wiki soll den Inhalt des Companion selbst wiedergeben, nicht nur auf Quelldateien zeigen (Autorentscheidung, 2. November 2026). Wer eine Wiki-Seite liest, soll verstehen, **was** eine Quelle sagt, **unter welchen Voraussetzungen**, **wie weit** es trägt und **was offen** ist, ohne die TeX-Datei zu öffnen. Links auf Quelldateien und Labels dienen dem Nachprüfen und stehen hinter der inhaltlichen Aussage.

Konkret heißt das:
- Jeder Abschnitt, der auf einen Teil des Companion verweist, fasst dessen Kernaussagen in eigenen Worten zusammen, mit den wichtigsten Formeln und Zahlen.
- Ergebnisse neuer Runden kommen inhaltlich in [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie) und [Forschungsstand](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungsstand), neue Tests in [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests), Änderungen am Kern in [Was im Companion steht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) und dessen englische Fassung.
- Eine Liste von Links ohne Inhaltsangabe ist kein vollständiger Wiki-Eintrag.

## Formelsatz und gemeinsamer Leseweg

Mathematik mit GitHubs LaTeX-Darstellung setzen: kurze Ausdrücke zwischen `$…$`, eigenständige Gleichungen zwischen `$$` auf eigenen Zeilen. Dateinamen, Labels und Befehle bleiben Code. Formeln nicht als Bilder einfügen; ihr Markdown-Quelltext bleibt so auch für LLMs lesbar.

Der Fließtext erklärt die Inhalte für Menschen. Technische Extraktionshinweise und Satzlabels in eingerückten **Anmerkungen für LLMs und Quellenprüfung** sammeln. Voraussetzungen und fachliche Grenzen bleiben in der menschlichen Erklärung sichtbar. Englisch entsprechend **Note for LLMs and source checking**. Formeln nach Veröffentlichung auf GitHub visuell prüfen.

## Quellenpriorität

Deutsch ist die redaktionelle Hauptsprache. Der Dokumentführer und das Koide-Beispiel haben englische Begleitfassungen. Inhaltliche Änderungen zuerst in der deutschen Fassung klären und anschließend in der zugehörigen englischen Seite nachziehen. Fundstellen, Voraussetzungen, Statusgrenzen und Kontrollantworten müssen übereinstimmen. Die englische Einstiegsseite benennt den Übersetzungsumfang; sie darf keine vollständige Übersetzung des Manuskripts suggerieren.

Der Dokumentführer verwendet eine didaktische Reihenfolge. Beim Aktualisieren die tatsächliche Include-Reihenfolge und Abschnittstitel der Quellen prüfen; keine dauerhaften PDF-Seitenzahlen ohne Versionsbindung verwenden. Lehrbeispiele ausdrücklich von nativen Modellen und Messwerten unterscheiden.

Für eine Veröffentlichung gelten deren unveränderte Payloads und Metadaten. Für Forschung gelten die zum gewählten Commit gehörenden Quellen einschließlich Korrektur- und Statuslayern. Ältere Berichte bleiben Herkunftsnachweise; ihr damaliger Status ist nicht automatisch aktuell. Bei Widersprüchen den Konflikt offenlegen und neuere, spezifische Statusangaben mit Herkunft benennen.

Hypothesen, Fits, negative Kontrollen und offene Fragen behalten ihre Kennzeichnung. Issues verlinken, ihren fachlichen Status aber nur nach Prüfung der Belege zusammenfassen.

## Technischer Ort und Pflegeumfang

Quelle der Seiten ist der Ordner [`wiki/`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/main/wiki) im Hauptrepository. Der Workflow `.github/workflows/wiki-sync.yml` spiegelt ihn bei jedem Push auf `main`, der `wiki/` ändert, in das Wiki-Repository `https://github.com/Moriarty1982/QuantumSphere-Unfold.wiki.git`; er lässt sich auch von Hand starten. `_Sidebar.md` und `_Footer.md` liefern Navigation und Standhinweise.

**Nicht direkt im Wiki bearbeiten.** Änderungen über die Wiki-Oberfläche oder direkt im Wiki-Repository überschreibt der nächste Abgleich. Wiki-Änderungen gehören in denselben Pull Request wie die Repository-Änderung, die sie beschreiben.

Die Pflege erfolgt im Rahmen beauftragter Projektarbeiten. Eine zeitgesteuerte Hintergrundpflege ist durch diese Erstbefüllung nicht eingerichtet.

## Änderungsnachweis

- 11.11.2026: Forschungsstand – Physikfassung vom technischen Auszug zum wissenschaftlichen Haupttext mit Abstract, Literatur und Beweisanhang überarbeitet; Detailprovenienz im separaten Auditbericht erhalten.

- 11.11.2026: Forschungsstand – beide Datenbankeditionen, sieben Physikabschnitte, vollständigen Langquellbaum und sichtbar offene Kandidaten dokumentiert; keine Releasefreigabe.

- 11.11.2026: Forschungsstand – unbestätigten Themenvorschlag der Physikfassung entlang Träger, Methode, Teilchen, Massen und Geometrie eingeordnet; kein fertiges Ausgabeprofil.

- 11.11.2026: Forschungsstand – Plan für Langfassung und eigenständiges Physikpaper mit notwendiger QAM/MML/MMA-Einführung sowie gemeinsamer Zenodo-Ablage festgehalten; Scope und Zwei-PDF-Build offen.

- 11.11.2026: Forschungsstand – positive Spektralauswahl von Massenpositivität getrennt; explizites reguläres Zeta-Paket mit HC-Balance und endlichen Parameter-/Fourier-Streuungen dokumentiert.

- 11.11.2026: Forschungsstand – Basisrotationen der quadratischen Auslesung und scharfe 5/9-Grenze positiver antipodaler Zustandspaare eingeordnet; native Zweigauswahl offen.

- 11.11.2026: Forschungsstand – nach PR #93 HC-wechselnden Kopplungsblock von Closure-Leckage getrennt und die bedingte 5/9-Grenze der positiven quadratischen Zwei-Moden-Auslesung dokumentiert.

- 11.11.2026: Home, Gesamtbild, Versionen und Quellen, Forschungsstand – Entwicklungslinie 5.0.0-draft von öffentlicher 4.11.0 getrennt; arithmetischen HC-Partner und Grenze seiner Eigenzustandsauswahl dokumentiert.

- 11.11.2026: Forschungsstand – Zeta/HC/Unschärfe-Erkundung: Paritätsgrenze, antikommutierende Auslesungen, zusätzliche T-Auswahl und Impulsdomänengrenze dokumentiert.

- 11.11.2026: Forschungsstand – HC-Selbstprüfung und bedingten Anschluss an Koide mit Seed, Wurzelgesetz und offener Orthogonalitätsselektion dokumentiert; keine native Schließung.

- 9.11.2026: QAM – Erkundung aller 56 Fünferauswahlen benachbarter Ringkanten und Abgleich mit der Graphzählung.

- 9.11.2026: QAM – Folgeanfragen können mindestens einen Kandidaten bei einem Vorgänger voraussetzen.

- 9.11.2026: QAM – abhängige Stapelanfragen starten nach ihren eigenen Vorgängern, sobald ein Prozess frei ist.

- 9.11.2026: QAM – Integritätsprüfung gespeicherter Stapel samt Kontext, Einzelbelegen und blockierten Anfragen.

- 9.11.2026: QAM – direkter Vergleich zweier gespeicherter MMA-Stapelberichte nach Anfrage-ID.

- 9.11.2026: QAM – schreibgeschützter Replay gespeicherter MMA-Stapel mit Änderungen je Anfrage.

- 9.11.2026: QAM – Stapelberichte nach Anfrage-ID und MMA-Status filtern.

- 9.11.2026: QAM – jüngste verifizierte Stapelberichte mit Anfrage-IDs und Anzahlen je Status.

- 9.11.2026: QAM – gespeicherte MMA-Sammelberichte mit schreibgeschütztem Abruf per Hash.

- 9.11.2026: QAM – MML-Paarstapel direkt aus dem Chat über den lokalen MCP-Stapelserver.

- 9.11.2026: QAM – Abhängigkeiten für MMA-Stapel und Ausführung gespeicherter Stapel im vollständigen MCP-Server.

- 9.11.2026: QAM – parallele MMA-Ausführung unabhängiger MML-Paarabfragen mit gehashtem Sammelbericht.

- 9.11.2026: QAM – frei wählbare Paarbedingungen, exakte Kandidatenzahl und Konfliktbeleg mit MCP-Abruf.

- 8.11.2026: QAM – beidseitig indexierter Prämissengraph, Belegsuche, Korrekturverweise und Vorschläge für Regelketten.

- 8.11.2026: QAM – SQLite-Regelkatalog mit Pflichtanforderungen und optionalen Messungen für die Gram-Vorhersage.

- 8.11.2026: QAM – rekursive Prämissenauflösung in SQLite und Wiederverwendung der analytischen Gram-Intervallregel im MMA-Beleg.

- 8.11.2026: QAM – analytische Erkundung zum scharfen Gram-Zielbereich mit und ohne zusätzliche Intervallmessung.

- 7.11.2026: QAM – Beispiel für Horizontzugang, Punktzahl und Prüfung der Minimalspinmaske.

- 7.11.2026: QAM – bedingter Spektralabgleich zwischen HC-Boost und dem Flächenquantum aus r10.

- 7.11.2026: QAM – Schalenrest-Beispiel mit getrennten linearen und quadratischen Nullnachweisen.

- 7.11.2026: QAM – kompilierbares HC-Beispiel für gewichtete Rückwegwerte und Nullprüfungen.

- 7.11.2026: QAM – ausführbares r27-Beispiel für gemeinsame und unabhängige Zweikopienrotation.

- 7.11.2026: QAM – gerichtete r27-Rotationen mit getrenntem Port-Readout und nichtselektivem Messschritt.

- 7.11.2026: QAM – Quelle–Rückweg, gerichtete Rückwegwerte und Vergleich mit der historischen C5-Schwelle.

- 7.11.2026: QAM – Lorentz-Boost vor und nach Gram-Auslesung, mit rekonstruierbarer Darstellung auf dem Rang-zwei-Chart.

- 7.11.2026: QAM – Dorau–Much als Fallstudie zur Trennung von Beobachteruhr, Algebraeinschränkung und geometrischer Auslesung.

- **7.11.2026, QAM-Physikprofile umgesetzt:** QAM und Hinweise-fuer-LLMs erläutern das optionale TeX-Zusatzpaket, ART-/QM-Beispiele, Standardkontexte, explizite Konversion und Exporte. 34 Kompilier-/Fehlerfälle, zehn Exporte und Lean-Kompatibilität lokal geprüft; keine physikalischen Behauptungen oder nummerierten Forschungsschichten geändert.

- **6.11.2026, QAM-Standardkontext:** QAM-Seite und Schnittstellenentwurf erlauben auf Autorwunsch das Weglassen linker Rollen bei eindeutig deklariertem Standard-Frame/-Profil. Kontext bleibt bei Expansion und Export erhalten; abweichende Frames werden sichtbar markiert.

- **6.11.2026, QAM-Autorpräzisierung und Frame-Physikinterface-Entwurf:** QAM und Hinweise-fuer-LLMs trennen Frame-Schnittstellensprache, framegebundene Physikinterpretation und vorhandene Buchführungswerkzeuge. Kein universelles ART-Gesetz, keine automatische Invertierbarkeit und kein neuer physikalischer Beweis behauptet.

- **6.11.2026, Rückgang bis zur Grundidee (Arbeitsnotiz):** Gesamtbild und Offene-Probleme priorisieren die gemeinsame-Träger-/physikalische-Identifikationsfrage vor weiteren Spinmasken. Zehnstufige Rückwärtskette trennt Nullbegriffe, Projektor, Sektoren und ursprüngliche Einheitshypothese; kein neuer Gesamtabschluss.

- **6.11.2026, Projektor-/Spinbrücke (Erkundung):** Offene-Probleme trennt elektromagnetischen Reflektor, Dixon-Chiralität, P_C7 und Horizontmaske. Die vorhandene r51-Erhaltung ist kein neues Spin-Auswahlgesetz; „mod HC“ bleibt ohne konkrete Träger-/Zähldaten offen.

- **6.11.2026, gemeinsamer Zustand und Spinzugriff (Erkundung):** Offene-Probleme unterscheidet vollständige Frameumrechnung, eingeschränkten Zugriff und selektierten Zustand. Restbeiträge bleiben bilanziell relevant; keine physikalische Horizontabbildung wird durch das Vergleichsmodell behauptet.

- **6.11.2026, begrenzte Spinauswahlprüfung (nicht blind):** Offene-Probleme trennt Sättigung bei festem j, zusätzliche absolute Minimierung und vollständige Spinsektorzählung. Die feste-μ-Floorkinematik liefert keine j-Auswahl; bestehende Zählannahmen von H96 bleiben bestehen.

- **6.11.2026, analytische OP5-Auswahlerkundung (nicht blind):** Offene-Probleme beschreibt die explizite freie q-Familie bei festen lokalen Zusatzdaten und die getrennte Energiegewichtsabhängigkeit. Keine empirische Prüfung oder neue H-Nummer; zusätzliche native Auswahlgesetze bleiben außerhalb des begrenzten Gegenbeispiels.

- **6.11.2026, Zwischenabschluss OP5-Rückverfolgung:** Offene-Probleme und Hinweise-fuer-LLMs bündeln die sechs Arbeitsnotizen und benennen die verbleibende physikalische Zustands-/Messabbildung. Kein neuer Test, keine nummerierte Schicht und kein Abschlussstatus geändert.

- **6.11.2026, OP5-Nennerprüfung (Arbeitsnotiz):** Offene-Probleme trennt Eigenwertverhältnis, Übergangsfluss, Zählparameterkontrast und kosmologischen Dichteanteil. r31 als Stabilität einer eingesetzten Verzweigung präzisiert, nicht als Herleitung ihres Zahlenwerts.

- **6.11.2026, Frame-/Parameterprüfung (Arbeitsnotiz):** Offene-Probleme erläutert die bestehende R/P-Korrektur aus r24 und trennt Eigenwertverhältnis, Eigenanteil, Messport und kosmologischen Dichteanteil. H96 und Guards unverändert.

- **6.11.2026, OP5-Operations-Datenblatt (Arbeitsnotiz):** Offene-Probleme trennt Projektion, Referenz-/Basiswechsel, Dualität, Zeitumkehr und Beobachterboost. Feldrapidität und symmetrischer Frame-Versatz werden nicht gleichgesetzt; keine neue Evidenz oder Schicht.

- **6.11.2026, Feld-/Port-Datenblatt (Arbeitsnotiz):** Offene-Probleme erläutert die lokale Port-Auslesung, fehlende Skala/Orientierung des reduzierten Registers und die Trennung von nullartigem Feld, leerem Port und vollständigem Nullfeld. Keine neue Rechnung oder nummerierte Schicht.

- **6.11.2026, erstes OP5-Route-Datenblatt (Arbeitsnotiz):** Offene-Probleme und Hinweise-fuer-LLMs trennen das abstrakte Quelle–Rückweg-Schema von einer konkreten nativen Instanz und kennzeichnen Suchumfang sowie offene physikalische Brücke.

- **6.11.2026, Arbeitsnotiz nach r05 (keine neue Schicht):** Offene-Probleme, Gesamtbild und Hinweise-fuer-LLMs geben die beauftragte Aussetzung der historischen OP5-Auslöschungsgrundlage und die neue Messgrößen-/Auslesefrage wieder. Frühere Kriterien, Guards und Status von H96/H97 bleiben bestehen.

**6.11.2026, Anleitungen modellunabhängig:** Hinweise für LLMs um die Liste der Anleitungen in `notes/anleitungen/` ergänzt (Sitzungsstart und -übergabe, Hypothesentest, Runde, OP5, Wiki, `tools/qs.py`, Zenodo); sie gelten für Claude, ChatGPT und Codex gleich.

**2.11.2026, Layer r71:** Forschungsstand, Forschungslinie, Offene Probleme (OP5), Vorhersagen und Tests (H49, H50), Inhalt und Content overview um die Struktur des OP5-Vergleichssystems und die Polarwinkel-Eichsymmetrie ergänzt; Stand-Zeilen auf r71.

**2.11.2026, Layer r70 und Inhaltsseiten:** Neue Seiten [Was im Companion steht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) (mit englischer Fassung [Content overview](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Content-overview)), [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie), [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests) und [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme). Dokumentführer (DE/EN) in den Stationen 5–8 um Inhaltsangaben ergänzt. Forschungsstand um r70 ergänzt; der in r69 genannte Wert 1,689 korrigiert (richtig 1,686953). Regel „Inhalt wiedergeben, nicht nur verweisen“ aufgenommen.

**28.10.2026, Quelle ins Hauptrepository verlegt:** Seiten liegen jetzt unter `wiki/` und werden per Workflow ins Wiki gespiegelt, damit Wiki-Änderungen mit den Repository-Änderungen über Pull Requests laufen.

**28.10.2026, Layer r69:** Patches für r66–r68 eingespielt (lagen seit dem 25.10. lokal). Forschungsstand um einen OP5-Abschnitt zur Einbindung der Arbeitsserie vom 25.–27.10. ergänzt; Stand- und Layerangaben auf Commit b12adf5 und r69 gesetzt. Im r67-Eintrag den versehentlich ersetzten Commit wieder auf c4df998 gestellt.

**25.10.2026, Layer r68:** Forschungsstand um die unabhängige Nachrechnung ergänzt (U(1)- gegen SU(2)-Zählung); Stand- und Layerangaben auf Commit f2de387 und r68 gesetzt.

**25.10.2026, Layer r66:** Forschungsstand korrigiert: Der Widerspruch `thm:k-values` gegen `thm:frame-offset` stammt aus v4.9.0-r09 und ist dort aufgelöst; r66 holt die Zitierung nach. Hinweis zum lokalen Frame-Faktor ergänzt. Quellenstand: Merge von PR #43 (ce264ba).

**25.10.2026, Layer r67:** Forschungsstand um die Prüfung von `rem:einstein-blunder` ergänzt; Stand- und Layerangaben auf Commit c4df998 und r67 gesetzt. Fundstellen geprüft; keine mathematischen Manuskriptänderungen durch das Wiki.

**25.10.2026, Formelsatz und Lesefluss:** Deutscher und englischer Dokumentführer als gemeinsamer Weg für Menschen und LLMs überarbeitet; technische Hinweise als Anmerkungen markiert. Formeln in beiden Lesewegen, beiden Koide-Beispielen und im Forschungsstand auf LaTeX-Satz umgestellt. Mathematische Aussagen und Quellenstand beibehalten.

**25.10.2026, Leseweg-Erweiterung:** Acht Lernstationen mit Zielen, Erklärungen, Abschnittslinks und Kontrollfragen; Koide-Rechenbeispiel; englische Begleitfassungen und englischer Einstieg. Deutsch bleibt Hauptfassung. Quellenstand unverändert 64973ef. Quellenpfade und interne Verweise geprüft; Lehrrechnungen separat nachgerechnet. Keine mathematischen Manuskriptänderungen.

**25.10.2026:** Erstbefüllung mit Leseweg, Versions- und Quellenkarte, Forschungsstand, Begriffen und LLM-Hinweisen. Quellenbasis: Hauptrepository-Commit `64973efe8409cfd2ae985fbbd17b4ebc95845780`. Keine Release-Payloads oder mathematischen Quellen geändert; kein neuer Beweisaudit durchgeführt.

11.11.2026: Technischen Zwei-PDF-Build als abgeschlossen eingeordnet; offene fachliche Prüfung und Release-Schritte im Forschungsstand nachgezogen.

11.11.2026: Fachliche Selbstprüfung der vollständigen englischen Physikfassung dokumentiert, mit Quellen-/Prämissengrenzen und unveränderten Guards.

11.11.2026: v5-Entwurfsmetadaten und Änderungsübersicht ergänzt; lokalen Zwei-PDF-Trockenlauf und noch offene finale Payload-Schritte dokumentiert.

11.11.2026: Review-Präzisierungen in beiden Sprachen sowie erneute lokale Builds und Sichtprüfung dokumentiert.

11.11.2026: Englische Upload-Auswahl des Autors festgehalten; Quellen-/Datenbankpaket und vollständigen lokalen Trockenlauf dokumentiert.

11.11.2026: Inhaltliche Wiederaufnahme von OP3 dokumentiert; historische Koide-Frage, Hüllenverträglichkeit und heutige Operatorroute getrennt, keine Änderung eines Guards.

11.11.2026: Vier innere Operatorterme und die zusätzliche Invarianzpflicht des Drei-Seed-Raums dokumentiert; analytische Gegenprobe, kein Parameterfit oder OP-Abschluss.

12.11.2026: Farbtriplet-/Generationenprüfung mit direkter Kommutantenrechnung ergänzt; Grenzen der neutralen Closure und vorhandene alternative Sloträume dokumentiert.

12.11.2026: Vorhandene Trialitäts-/Hopfroute gegen den linearen Generationenraum abgeglichen; farbfesten Umgebungsraum und zweiphasigen Konfigurationsraum getrennt.

12.11.2026: Lambda-Längenvorgabe, dissipative Stringrelaxation und offene Anschlussfrage für Version 5 dokumentiert; kein OP-Abschluss.

12.11.2026: PR #100 integriert; v5-Reservierung und offene Frage in beiden englischen Ausgaben dokumentiert.

12.11.2026: Vom Autor veröffentlichte v5.0.0 öffentlich geprüft; Dateiintegrität und Vorschau bestätigt, ausstehende GitHub-Nacharbeiten benannt.

12.11.2026: Öffentliche Einstiegsseiten und Zitation auf v5.0.0 umgestellt; GitHub-Tag an den veröffentlichten Paketquellstand gebunden.

12.11.2026: Rückwärtssuche zur Stringrelaxationsfrage in Forschungsstand ergänzt (notwendige Bedingungen, Maxwell-Klasse bei fester Außenlänge ausgeschlossen, drei verbleibende Wege); Forschungsschicht nach v5.0.0, kein OP-Abschluss.

12.11.2026: Weg W-b in Forschungsstand ergänzt (Quellensuche negativ; kubisches Kraftgesetz gibt Brannen-Form mit freier Phase, Rückführung auf r44.1(e)); kein OP-Abschluss.

12.11.2026: Quellensuche zur Koide-Phase in Forschungsstand ergänzt (Phase als Verhältnis ρ-ungerade/ρ-gerade, ältere Bausteine ρ-symmetrisch, übersehenes Vorwissen zu W-b nachgetragen); kein OP-Abschluss.

13.11.2026: Erkundung zur ρ-ungeraden Platzkopplung aus der Trialitätsform in Forschungsstand ergänzt (Quarks: Brannen-Form mit freiem Winkel in der Ebene (1, e₇); Leptonen: keine Kopplung); Kandidat, kein OP-Abschluss.

13.11.2026: Erkundung zur Platzkopplung auf dem vollen Dixon-Raum in Forschungsstand ergänzt (Sektorformel für e, ν, u, d; zwei freie Winkel; Spiegelung Leptonen/Quarks; einfachste Form passt nicht zu r11); Kandidat, kein OP-Abschluss.

13.11.2026: Nachtrag zur Dixon-Platzkopplung in Forschungsstand (Verbinderblock r44.1(b) getroffen, Sektoren an Idempotenten, Hyperladung erlaubt nur einen Umlaufsinn, K ≤ 1/2); kein OP-Abschluss.

13.11.2026: Nachtrag 2 zur Dixon-Platzkopplung in Forschungsstand (Rückweg über Dixon-konjugiertes Element eichinvariant, Element trägt bei einem Dublett keine Phase; Phase = relative Phase zweier freier Kopplungskonstanten); kein OP-Abschluss.

13.11.2026: Weg C in Forschungsstand ergänzt (vier Generationenträger mit heutigem Stand; r33-Labels nicht ladungsinvariant; Modell I ohne Vorhersage; Korrektur: r53 als Vorbefund der Kopplungsabschnitte); kein OP-Abschluss.

13.11.2026: Erkundung zur Eigenwert-Auslesung der Platz-Gram-Matrix in Forschungsstand ergänzt (K = (1+2ρ²)/3, Bogen aus Positivität, Rang = Zahl der Massen, Torus-Mittel 2/3); Auslesung ist Annahme, kein OP-Abschluss.

13.11.2026: Nachtrag zur Eigenwert-Auslesung (Bedingung für Neutrinos durch H2 bereits beantwortet; in der Gram-Lesart mit bekannten Massendifferenzen nicht erfüllbar); keine neue H-Nummer.

13.11.2026: Indefinite Form im neutralen Sektor und Test H99 in Forschungsstand und Vorhersagen-und-Tests ergänzt (H99a verträglich, nicht blind; H99b nicht entscheidbar; Spannung mit JUNO nachträglich genannt); kein OP-Abschluss.

13.11.2026, nachmittags: H99b mit der NuFIT-6.1-Primärtabelle entschieden (verträglich, +1,80σ, nicht blind) in Forschungsstand und Vorhersagen-und-Tests nachgetragen; Ersatzrechnungen aus Sekundärwerten als überholt markiert; kein OP-Abschluss.

13.11.2026, abends: Erkundung zum Verlauf der NuFIT-Werte 2012–2025 mit Grafik in Forschungsstand ergänzt (R lag 2013/14 nur wegen des damals niedrigen Δm²₃₁ beim H99-Wert); kein Test, kein OP-Abschluss.

13.11.2026, abends: Erkundung der Varianten zu H99 (drei Ideen, 24-Varianten-Raster, nachträglicher Kandidat „H99 bei einer Skala M_Z“, +0,16σ) in Forschungsstand ergänzt; nicht blind, kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag zur Skalenfrage in Forschungsstand (M_Z nicht ausgezeichnet; Wahl Polmassen oder Kopplungen; Grund und Gegengrund); kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag Koide-Spannung (Pol-Koide als Zufall unwahrscheinlich; Sumino-Weg rechnet die Neutrinos an die Daten heran, nicht nativ) in Forschungsstand; kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag Exponent c (mit PMNS-Mittelung c ≈ 1,7–1,8; c = 1 +0,7σ) und Familiensymmetrie (keine native Eichsymmetrie; Platzindex-U(3) der Gram-Matrix als einziger stetiger Kandidat) in Forschungsstand; kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag c als Integral (c = 1,8 ± 1,0; c = 1 verträglich, bei Sumino c = 1) in Forschungsstand; kein Test.

13.11.2026, spät: Erkundung Eichung der Platzindex-U(3) in Forschungsstand (Bosonenmassen s_i und (s_i+s_j)/2; Auslesung A verlangt α_F = 8α, Auslesung B ist Sumino mit 4α); kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag Auslesung A oder B (Entscheidung A; Sumino-Bedingung hängt am Feldtyp) in Forschungsstand; kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag zwei Tripel und Zwei-Sonden-System (Ψ₁/Ψ₂ als L/R-Tripel, T₁₂ als Massenblock, α_F = 4α) in Forschungsstand; kein Test, kein OP-Abschluss.

13.11.2026, spät: Nachtrag Neutrino-Block L-L (Ω₁, c = 1, negative Wurzel bei Signatur (2,1); Seesaw und Tensorprodukt ausgeschlossen; offene Bedingung an η) in Forschungsstand; kein Test, kein OP-Abschluss.

13.11.2026, abends: H100 vorab in Vorhersagen-und-Tests und Forschungsstand eingetragen; Erkundung Form η (Brannen-Phase = Bargmann-Phase/3, H99 als Drehung um π/4, Ausschlüsse) in Forschungsstand; kein OP-Abschluss.

13.11.2026, abends: Nachtrag Paar-Phase (Fluss π/4 durch das Platzdreieck; native Phasen geben nur Vielfache von π/6; π/4 als Bargmann-Phase eines koplanaren Koide-Tripels) in Forschungsstand; Formulierung zur bilinearen Phase berichtigt; kein OP-Abschluss.

13.11.2026, abends: Nachtrag π/4 = (3/2)·π/6 in Forschungsstand (Lesart drei Kanten mal Spinor-Halbierung; 3ρ² und 1/K nur punktuell); kein OP-Abschluss.

13.11.2026, abends: Nachtrag Spinor-Transport (raumzeitlich ausgeschlossen; innerer Transport verlangt q_L − q_R = 1/2, nachträglich = Hyperladung des Higgs) in Forschungsstand; kein OP-Abschluss.

13.11.2026, abends: Nachtrag Dixon-Sektorphase (Struktur hyperladungsgebunden, Zahl mit nativen Phasen nicht erreichbar, Spiegelung widerspricht Quarks) in Forschungsstand; kein OP-Abschluss.

13.11.2026, abends: Nachtrag halbe Ladungsdifferenz (Verbinder-Hyperladung: Weinberg HH gegen H gibt π/12; Dirac H̃ gibt π/6 wie Dixon) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Nachtrag Mechanismus (Holonomie J^y; Rand-Tripel = Oktanten-Tripel dreier Qubits mit Phase π/4; Kandidat zusätzliches Higgs-Dublett, Hindernis r33) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Erkundung Oktanten-Tripel im Hopf-Träger von r15 in Forschungsstand (symmetrischer Punkt als Q_em-verträglicher Transport, magischer Winkel gibt Rand-Tripel; r33-Hindernis entfällt); kein OP-Abschluss.

13.11.2026, spät: Nachtrag magischer Winkel (gleichwertig mit orthonormalen Platzrichtungen; Farb- bzw. Ladungsanteile; neutraler Teil mit Signatur (2,1) ohne exakten Oktanten) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Nachtrag Lorentz-Fassung (Lorentz-Qubit ohne Koide-Tripel; in (2,1) keine native Zeitachse) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Erkundung neutrale SU(2) (Suminos SO(3)-Vektorindex trägt die Generationen auf orthogonalen Achsen; nur Spin 1/2 gibt Koide und π/4) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Nachtrag neutrale SU(2) gesucht (Schur: nur Familien-Symmetrie; in U(3) kein Vektor-mit-Spinor; zweite Familien-SU(2) nötig) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Nachtrag Feldsuche (Dixon-Raum ohne neutrale SU(2); ν^c-Kondensat gibt kein Koide; Erweiterung nötig) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Prüfung der Feldsuche (stetige SU(2) nicht nötig; Hurwitz-Einheit, 2T, A4; Sedenion-Ebene (e7, e15) als neutrales Dublett, Bezugszustand fehlt) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Erkundung Bezugszustand in den Sedenionen (farbneutrale Quaternionen span(1,e7,e8,e15), Raumdiagonale gibt Oktant; Ladung als Hindernis) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Nachtrag Ladung auf die Sedenionen fortgesetzt (keine ψ-verträgliche Fortsetzung; Drehung um e7 kein Automorphismus, e8/e15 geladen) in Forschungsstand; kein OP-Abschluss.

13.11.2026, abends: Erkundung Ladung über e8 (ψ- und farbverträgliche Ladung bis auf Vorzeichen eindeutig; farb- und ladungsneutrales Qubit span(1+ie8, e7−ie15); Bezug unter dem magischen Winkel nicht nativ) in Forschungsstand; kein OP-Abschluss.

14.11.2026: H103 (widerlegt) und Nachtrag R_f (Rechtsmodul, Pauli-Tripel, Treffer analytisch erzwungen) in Forschungsstand und Vorhersagen-und-Tests; kein OP-Abschluss.

14.11.2026: Erkundung Generationen unter Q_* (zwei vollständige Generationen; ψ-Sektoren keine Generationen; ψ als Phase innerhalb der Generationen; N = Raum zweier Neutrino-Flavours) in Forschungsstand; kein OP-Abschluss.

14.11.2026: Regel „gemergte Zweige löschen“ (AGENTS.md) in Hinweise-fuer-LLMs.

14.11.2026: Erkundung Hurwitz-Einheiten auf N (2T-Dublett nativ; Bezug = Eigenzustand einer Hurwitz-Einheit der Ordnung 3; ψ normalisiert 2T nicht) in Forschungsstand; kein OP-Abschluss.

14.11.2026: Platzhalter-Methode an CT-001 (Einheit bei γ/2: κs = 1/2 aus minimaler Dirac-Phase; Rest: Raumwinkel = γ_M) in Forschungsstand; kein OP-Abschluss.

14.11.2026: CT-001 Schritt 2 (Sektor: Fläche gegen Winkel; drei Konventionen = drei Messweisen eines Sektors; ½ aus A = r²θ/2) in Forschungsstand; kein OP-Abschluss.

14.11.2026: CT-001 Schritt 3 (γ_M als Winkel: Wert aus der Zählregel, Bedeutung aus dem Unruh-Bild r10.1; offen: Kopplung an einen Radianten) in Forschungsstand; kein OP-Abschluss.

14.11.2026: I1 verfolgt (String-Brücke zur Punktierung; eine Lichtquerung gibt γ_M/2) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Runde v4.10.0-r12 (Statusvermerke) in Forschungslinie, Inhalt, Content-overview, Offene-Probleme und Forschungsstand; Fäden Potential und T₁₂ in Forschungsstand.

13.11.2026, spät: Nachtrag Auswahlprinzip (Koide als qubitartige Treue; Mittelwert erklärt die Genauigkeit nicht) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Rückwärtssuche Auswahlprinzip (Elektronmasse = Abstand vom Qubit-Oktanten; zwei Zahlen festzulegen) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Herleitungsversuch (K = (1 + cos²β)/2; in A4 einziger Wert 2/3; Elektronmasse als A4-Bruch) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: H101 (Maske hebt Elektron) in Vorhersagen-und-Tests und Forschungsstand eingetragen (widerlegt, Sylvester; Nebenrechnung lineare Form); kein OP-Abschluss.

13.11.2026, spät: Nachtrag andere Anhebung (nur Fluss erhält Koide; nötiger Fluss 2/3 rad; Kreis zum historischen OP3) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Erkundung Fluss 2/3 rad (kein Mechanismus; Scan-Treffer ΔΦ = γ_BI/2, nachträglich, verlangt m_τ = 1777,13 MeV) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: Nachtrag Mechanismus-Suche für ΔΦ = γ/2 (γ_M nativ; Literatur-Lesarten mit unbegründeter Einheit) in Forschungsstand; kein OP-Abschluss.

13.11.2026, spät: H102 vorab (m_τ = 1777,134 MeV) in Vorhersagen-und-Tests und Forschungsstand eingetragen.

13.11.2026, spät: Nachtrag Holonomie-Fluss-Paarung (γ m als Fläche und Phase; γ/2 nur mit Einheit 8πGħ und |m|) in Forschungsstand.
