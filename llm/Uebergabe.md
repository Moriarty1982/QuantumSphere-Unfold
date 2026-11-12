# Übergabe: Stand der letzten Sitzung

12. November 2026, ca. 20:15 (Claude). Wird pro Arbeitsblock überschrieben.

- Öffentliche Baseline v5.0.0 (DOI 10.5281/zenodo.24152615, Tag v5.0.0 auf 539b75b). PR #100, #101, #102 gemergt; main 1eed465; Läufe 43265308165 (Zwei-PDF) und 43265308144 (Wiki-Sync) erfolgreich. Keine weitere Veröffentlichung nötig.
- Lokaler Ordner des Autors (`Quantum Sphera`) stand noch auf dem 6.11. (93c3d21, r05) und wurde auf Autorenfreigabe per Fast-Forward auf 1eed465 gebracht. Der alte Stand ist als Tag `lokal-stand-2026-11-06` gesichert (dabei entfielen 58 verfolgte Dateien, u. a. `.claude/skills`, alte Zusammenfassungen; alle über den Tag erreichbar).
- Offener Zweig `research/v5-string-relaxation-rueckwaertssuche` mit PR (Nummer siehe GitHub): Rückwärtssuche zur Stringrelaxationsfrage, Notiz und Selbstprüfungsskript unter `notes/research/op3_string_relaxation_backward_2026_11_12.*`, Wiki (Forschungsstand, Wiki-Pflege). Merge nur nach „PR NN mergen“.
- Zuletzt vergebene Hypothese H98, letztes k219. In diesem Block keine neue H-/k-Nummer, kein MMA-Beleg.

## Inhaltlicher Stand

- Autorenentscheidung 12.11.: erst Rückwärtssuche, keine Netzsimulation.
- Ergebnis (analytisch, nicht blind): Bei fester Außenlänge und frei umverteilbaren Längen sind die Zugkräfte gleich. Konvexe Energie: Relaxationszeiten wählen nichts aus, gleiche Strings geben K=1/3. Reiner Maxwell-String: Endaufteilung r_i(0) plus Überschuss nach Fluidität, neutral und kraftfrei, kein Attraktor. Attraktor nur bei L proportional a (Anteile (1/eta_i+H/k_i)/Summe), im Widerspruch zur festen Außenlänge. Gleiche Strings: ungleiche Aufteilung nur mit nicht monotonem Kraftgesetz; ein Höcker gibt (lang, kurz, kurz), drei verschiedene Längen brauchen zwei Umkehrpunkte.
- Damit ist die v5-Frage für die Maxwell-Klasse bei fester Außenlänge negativ beantwortet; allgemein bleibt sie offen. Weder Lambda noch Koide 2/3 oder das Leptonspektrum folgen.
- Fehlende native Operation: nicht konvexe Energie des einzelnen Strings oder Herkunft ungleicher Moduln aus dem Companion.
- OP1–OP5/C5/C6/T2 unverändert. I3 durch den Lambda-Bezug berührt, nicht benutzt.

## Nächster Schritt (Autorentscheidung)

Einen der drei verbleibenden Wege wählen:
- W-a: native Herkunft ungleicher Gleichgewichtsmoduln suchen (Trialität spricht dagegen).
- W-b: im Companion nach einer Stringenergie mit zwei Umkehrpunkten und nach der Zahl L/ell_c suchen (Quellenauftrag, keine Simulation).
- W-c: Knotengeometrie mit festen Winkeln oder Wicklungen festlegen, in der die Kräfte nicht gleich sein müssen; gegen Torusgrenze K<=1/2 prüfen.

Danach erst, falls ein Weg eine native Größe liefert: vorab festgelegter Test (dann H99).

## Pflichten in jeder Sitzung

- `AGENTS.md`, `wiki/Gesamtbild.md` und die einschlägige Anleitung unter `notes/anleitungen/` lesen; Auslöser in `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` prüfen.
- Vorwissen-Pflicht, Vorab-Notizen, Suchrichtung prüfen. Merges nur nach ausdrücklicher Freigabe. Wiki im selben PR.
- `.codex/environments/` bleibt unversioniert.
