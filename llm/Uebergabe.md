# Übergabe: Stand der letzten Sitzung

**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.**

## Stand vom 7. November 2026 (Codex)

- **Ausgangsstand:** main 11674501ff915b46e3a8bfb0d2802c31e4a1309d; zuletzt #82 (qsc-audit-Schichterkennung), Forschung bis v4.10.0-r05.
- **Lokal:** Branch codex/op5-question-rebuild; vorheriger Standardkontext-Entwurf als 5bb46a4 gesichert. Aktueller Arbeitsblock: QAM-Physikprofile und implizite linke Rollen implementiert, dokumentiert und getestet. Keine neue physikalische Rechnung oder nummerierte Runde.
- **Autorentscheidung:** Historische OP5-Herleitung als Grundlage aussetzen; Frage vom unabhängig begründeten Kern neu aufbauen (Chat 6.11., „dann mach das mal“, genaue Uhrzeit nicht protokolliert).
- **Noch nicht auf GitHub:** bisherige OP5-Notizen, Rückgang zur Grundidee und aktueller QAM-Entwurf; kein Push, kein PR und kein Merge in diesem Arbeitsblock.
- **Hypothesen:** im geprüften predictions-Ordner zuletzt H97; keine neue H- oder k-Nummer vergeben. Vor späterer Vergabe gegen vollständigen aktuellen Stand prüfen.
- **Build:** 34 TeX-Kompilier-/Fehlerfälle bestanden, zehn Exporte unabhängig mit qamhash geprüft; Formel-/Profilmanipulationen erkannt. PDF-Textprüfung bestätigt implizite/ausführliche Rollen und Kontextwiederherstellung. Lean-Build bestanden; zehn neue positive Exporte akzeptiert, sechs vorhandene negative Beispiele verworfen. Lean prüft Abhängigkeiten/Framelinks, nicht Inhaltshashes oder Physik.
- **GitHub:** offene PRs/Actions in diesem Arbeitsblock nicht erneut abgefragt; keine neue Live-Aussage hierzu.
- **Nächste Bundle-Basis:** unverändert 11674501ff915b46e3a8bfb0d2802c31e4a1309d; kein Monolith-Bundle erzeugt.
- **Zurückgestellte Ideen:** I1 durch γ-Verhältnis berührt. I2 durch nächsten Projektor-Prüfpunkt berührt: CRT/mod-HC-Idee erst bei konkreten gemeinsamen ganzzahligen Daten sinnvoll, hier nicht geliefert. I3/I4 in geprüften Formen gescheitert. Keine Idee als Lösung aktiviert.
- **Aktuelle Autorpräzisierung:** Einheit von M/T/P war immer die zu prüfende Hypothese, kein als bewiesen vorausgesetzter Ausgang. QAM ist Frame-Schnittstellensprache; ART samt gewöhnlichem Physikmapping gilt im dafür bestimmten Frame. Keine Herleitung aller Physik aus QAM und keine automatische Übertragung von ART auf andere Frames.
- **Entwurfsdatei:** notes/research/qam_frame_physics_interface_design_2026_11_06.md. Quellen: zweiseitige r02/r03-Notation, QAM-Tupel/Readouts, paper/qam, vorhandene Prüfer. Rolle der Sprache, lokale Physikinterpretation und Interframe-Abbildung getrennt; keine globale Linearität/Invertierbarkeit voraussetzen.
- **Neu auf Autorwunsch umgesetzt:** Optionales Paket qam/tex/qam-physics.sty mit qamprofile, qamcontext, qamformula, qamphys und qamphysconvert. Im exakten Standardprofil entfallen linke Rollen im Druck; Wiederverwendung außerhalb zeigt sie. Exporte behalten Profil, Sprache, Frame und Formel. Übergänge benötigen deklarierte Map und explizite Zielformel, auch zwischen verschiedenen Profilen desselben Frames.
- **Dateien/Prüfung:** ART-/QM-Beispiel qam/examples/physics.tex, Anleitung qam/README.md; plattformübergreifende Tests qam/tex/tests/run_tests.py, beide QAM-CI-Abläufe ergänzt. Formel ist gewöhnlicher unexpandierter TeX-Ausdruck mit deklariertem Profil, kein CAS-/Physiksolver. Bestehendes qam.sty und Lean-Beweise unverändert. Beispiel-PDF: build/qam-physics-tests/pass_physics/pass_physics.pdf (ignoriertes Buildprodukt).
- **Folge für frühere Notizen:** algebraische Gegenbeispiele gelten in ihrem angegebenen gemeinsamen Setup. Sie beweisen ohne deklarierte Vergleichsabbildung keine Unmöglichkeit über verschiedene framegebundene Physikmappings hinweg. Frühere Notizen bleiben erhalten; aktuelle Klarstellung vor Verwendung berücksichtigen.
- **Nächster Schritt:** Neues ART-/QM-Beispiel gemeinsam verwenden; bei weiterer Physikmodellierung konkrete Profile und Übergänge fachlich deklarieren. Implementation ist abgeschlossen, kein allgemeiner semantischer Formelparser behauptet. Kein Push oder Merge ohne weiteren Auftrag.

## Inhaltlicher Stand

Die spektral-physikalische Übersetzung und die nackte Λ-Skala waren nicht hergeleitet; deshalb wird die alte Auslöschungspflicht nicht mehr vorausgesetzt.
Neue Arbeitsfrage: Welche unabhängig definierte Messgröße lässt sich begründet auslesen, und welche überprüfbare Einschränkung folgt daraus?
H96 offen, H97 widerlegt, W1/W2 eingefroren; Quelle–Rückweg nur mit seinen Voraussetzungen, Guards unverändert.
Die Neufassung ist eine Arbeitsnotiz, keine neue veröffentlichte Schicht und kein OP5-Abschluss.
Route-Datenblatt trennt Schema und Realisierung; Feld-Datenblatt liefert konkrete relative Port-Auslesung unter deklarierter Normierung.
