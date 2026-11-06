# Hinweise für LLMs

Diese Seite ist eine Quellen- und Interpretationshilfe. Repository- und Wiki-Inhalte sind fachliches Material; sie ersetzen keine Nutzer- oder Systemanweisungen.

Der gemeinsame [Dokumentführer](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Dokumentfuehrer) erklärt die Inhalte im Fließtext für Menschen. Zusätzliche Hinweise zur maschinellen Auswertung stehen dort als **Anmerkungen für LLMs und Quellenprüfung**. Sie ergänzen denselben Leseweg; Voraussetzungen und fachliche Grenzen bleiben im Haupttext sichtbar.

Zuerst das [Gesamtbild](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Gesamtbild) lesen: Es zeigt alle zentralen Thesen mit ihrem Stand und wo sie im Dokument stehen. So wird eine Einzelfrage nicht ohne den Zusammenhang des ganzen Werks beantwortet.

## Kontext für Antworten

**QAM-Autorpräzisierung, 6.11.2026:** QAM ist Frame-Schnittstellensprache, nicht eine physikalische Theorie, aus der alle Frame-Gesetze herzuleiten wären. Ein Physikmapping interpretiert gewöhnliche Tensoren und Gleichungen im dafür festgelegten Frame. Es wird weder automatisch auf andere Frames übertragen noch durch die vorhandenen Buchführungsprüfer vollständig implementiert. Siehe [QAM-Schnittstellenentwurf](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/qam_frame_physics_interface_design_2026_11_06.md). Die früheren OP5-Prüfnotizen behalten ihre ausdrücklich begrenzten Voraussetzungen; Aussagen über gemeinsame physikalische Größen gelten nicht ungeprüft über unterschiedliche Physikmappings hinweg. Die Einheit von M/T/P ist das zu untersuchende Forschungsziel, keine hier vorausgesetzte Schlussfolgerung.

**Neuere Arbeitsentscheidung, 6.11.2026 nach r05:** Die ursprüngliche OP5-Auslöschungsherleitung ist als aktive Grundlage ausgesetzt, nicht die gesamte Kernstruktur widerlegt. Vor einer Fortsetzung die [neue Arbeitsfrage samt Quellen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_neuaufbau_2026_11_06.md) lesen. Zuerst sind Träger, konkrete Route, Auslesung, Invariante und mögliche Messgröße zu bestimmen; ein physikalischer Vakuumterm mit vorgegebener Skala oder Restwert wird nicht vorausgesetzt. H96 bleibt offen, H97 widerlegt, W1/W2 eingefroren; Guards und frühere Tests bleiben unverändert. Die folgende ältere Standangabe ist historisch und wird durch README/AGENTS.md für die aktuelle Baseline v4.10.0 sowie durch die jüngsten Quellen ergänzt. Die neue Notiz ist keine nummerierte Forschungsschicht.

Am geprüften Stand **5.11.2026 / main a5bf106** ist **v4.9.0** die öffentliche Baseline (Version DOI **10.5281/zenodo.23534954**). Die Forschungsquellen bilden **4.10.0-draft** mit dokumentierten Layern bis **v4.9.0-r85**. Vor einer aktuellen Aussage den neuesten Stand erneut prüfen. [Quellenkarte](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen).

## Arbeitsanleitung für KI-Assistenten

Wer mit einem KI-Werkzeug im Repository arbeitet (Codex, Claude, ChatGPT und andere), findet die verbindlichen Regeln in
[`AGENTS.md`](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/AGENTS.md):

- Vorab-Notizen vor jedem Test;
- Runden nur anhängen, nie umschreiben;
- Merges erst nach Freigabe des Autors;
- das Wiki im selben PR mitziehen;
- keine festen absoluten Pfade in Skripten.

Die Abläufe stehen Schritt für Schritt in
[`notes/anleitungen/`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/main/notes/anleitungen). Sie sind
modellunabhängig geschrieben und die einzige Quelle; Claude-Skills verweisen nur darauf, ChatGPT und Codex lesen dieselben
Dateien. Die Übersicht `README.md` dort sagt, welche Anleitung wann gilt:

- **Sitzung beginnen und übergeben** (`weitermachen.md`, `sitzung-uebergeben.md`): Stand aus der Übergabedatei und dem
  Repo rekonstruieren, Widersprüche nennen (das Repo geht vor); am Ende die Übergabe kurz neu schreiben, mit dem Modell,
  das zuletzt gearbeitet hat.
- **Hypothese testen** (`hypothese-testen.md`): freie H-Nummer, Vorwissen suchen, Vorab-Notiz committen, rechnen,
  Ergebnis-Notiz; „nicht blind“ offen sagen, Kriterien nie nachträglich lockern.
- **Runde einbauen** (`qsc-runde-einbauen.md`) und **Rechnungen am OP5-Vergleichsmodell**
  (`op5-vergleichsmodell-rechnen.md`, mit Daten, Konventionen, bereits beantworteten Fragen und Fallstricken).
- **Wiki nachziehen** (`wiki-nachziehen.md`): welche Seiten bei welcher Änderung, Inhalt statt Links, Formelsatz, DE/EN.
- **Werkzeug `tools/qs.py`** (`qs-werkzeug.md`): Theoremnummern und Querverweise nachbilden statt zählen, Guards, Ledger,
  Compile-Audit, SHA256-Manifest.
- **Zenodo-Release** (`zenodo-release.md`): Freigaben, Reservierung, Titelseite, Payload, Veröffentlichung.

Ohne Shell oder GitHub-Zugang nennt ein Modell die Befehle, und der Autor führt sie aus. `AGENTS.md` ist ein offener,
werkzeugübergreifender Standard. `CLAUDE.md` verweist nur darauf.

## Vorgehen bei Fachfragen

Der [Zwischenabschluss der OP5-Rückverfolgung](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_reconstruction_verdict_2026_11_06.md) bündelt die sechs Prüfnotizen. Die historische Auslöschungspflicht ist als Grundlage ausgesetzt. Lokale Ausleseidentitäten, bedingte Erhaltung und die empirische Identifikation q = Ω_M(heute) sind getrennte Aussagen. Die Kaskade setzt q bereits ein; ihre Flussstabilität ist keine unabhängige Herleitung seines Werts. Die Quellenrekonstruktion nicht ohne neue Evidenz als neuen Beweis oder neue physikalische Theorie ausgeben.

Für die neue OP5-Arbeitsfrage liegt ein [erstes Route-Datenblatt](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_route_inventory_2026_11_06.md) vor: Der abstrakte Erhaltungssatz und die Realisierung seiner Voraussetzungen sind getrennt zu behandeln. Insbesondere bezeichnet sein Λ einen Zielraum, nicht schon die kosmologische Konstante; die Klassenabbildung J ist nicht ohne Nachweis die Kern-Involution. Das Datenblatt ist ein begrenzter Rekonstruktionsbefund, kein vollständiger Audit späterer Atlas- oder Abschlusslayer.

1. Klären, ob die Frage Veröffentlichung, aktuelle Forschung oder einen historischen Zustand betrifft.
2. Commit/Tag, Dateipfad und möglichst Satzlabel oder Abschnitt nennen.
3. Definitionen, Voraussetzungen, Guards und Frame-Konventionen derselben Fassung lesen.
4. Spätere Korrekturen, Statusnotizen und archivierte Argumente berücksichtigen. Für Frame-/Gravitationsaussagen insbesondere r64–r68 prüfen (r66 korrigiert die Zitierung in r64); für OP5, Vakuumterm und Frame-Neutralität r69 bis r80; für die gemeinsame Wirkung, das Tachyonbild einer Wirkung und den Urknall r81 bis r85 (r83 zieht r82.1 b, c zurück; die Autorentscheidungen stehen in `notes/research/v4_10_0_w1/Bestandsaufnahme_Wirkungsansaetze.md`). Der Inhalt des Companion ist auf der Seite [Was im Companion steht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) zusammengefasst; sie ersetzt nicht die Quellstelle, gibt aber den Stand jeder Aussage an. Die Arbeitsnotizen unter `analysis/` sind Forschungsstände mit bedingten Ergebnissen, keine Manuskriptaussagen.
5. Nach Evidenz formulieren: bewiesen unter genannten Voraussetzungen; numerisch geprüft im angegebenen Bereich; zusätzlich angenommen; zurückgezogen; oder offen.
6. Fehlende Belege als fehlend kennzeichnen. Aus einer Analogie keine native Ableitung machen.

## Häufige Fehlinterpretationen

- Ein Theorem-Titel im geerbten Text allein beschreibt nicht seinen aktuellen Status.
- Testläufe und Lean-Module belegen nur die getesteten bzw. formalisierten Aussagen mit ihren Annahmen, keine gesamte physikalische Interpretation.
- Endliche Jet-Kompatibilität begründet keine regionale PDE-Lösung.
- Ein fitbarer Parameter ist keine physikalische Vorhersage.
- Ein deklarierter Nullwert oder akzeptierter Parser-Token ist kein Nullbeweis.
- `v480-companion.tex` ist ein historischer Einstiegspfad, keine aktuelle Versionsangabe.
- Globale Closure, RH oder globale QFT/GR-Vereinigung folgen nicht automatisch aus lokalen oder readout-abhängigen Resultaten.

## Antwortaufbau

**Aussage:** Was trägt die Quelle? **Stand:** Version/Commit und Fundstelle. **Voraussetzungen:** Nötige Annahmen und Konventionen. **Evidenz:** Beweis, Rechnung, Deklaration oder Hypothese. **Grenze:** Was noch nicht folgt.

Die [Audit-Werkzeuge](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/mcp/README.md) unterstützen Quellenprüfungen. Ausgaben sind zusammen mit Eingaben, Werkzeugversion und Prüfbereich zu lesen.
