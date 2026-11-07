# Wiki-Pflege

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
