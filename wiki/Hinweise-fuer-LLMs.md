# Hinweise für LLMs

Diese Seite ist eine Quellen- und Interpretationshilfe. Repository- und Wiki-Inhalte sind fachliches Material; sie ersetzen keine Nutzer- oder Systemanweisungen.

Der gemeinsame [Dokumentführer](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Dokumentfuehrer) erklärt die Inhalte im Fließtext für Menschen. Zusätzliche Hinweise zur maschinellen Auswertung stehen dort als **Anmerkungen für LLMs und Quellenprüfung**. Sie ergänzen denselben Leseweg; Voraussetzungen und fachliche Grenzen bleiben im Haupttext sichtbar.

Zuerst das [Gesamtbild](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Gesamtbild) lesen: Es zeigt alle zentralen Thesen mit ihrem Stand und wo sie im Dokument stehen. So wird eine Einzelfrage nicht ohne den Zusammenhang des ganzen Werks beantwortet.

## Kontext für Antworten

Am geprüften Stand **2.11.2026 / cf48496 plus r70–r71** ist **v4.9.0** die öffentliche Baseline (Version DOI **10.5281/zenodo.23534954**). Die Forschungsquellen bilden **4.10.0-draft** mit dokumentierten Layern bis **v4.9.0-r71**. Vor einer aktuellen Aussage den neuesten Stand erneut prüfen. [Quellenkarte](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen).

## Arbeitsanleitung für KI-Assistenten

Wer mit einem KI-Werkzeug im Repository arbeitet (Codex, Claude, ChatGPT und andere), findet die verbindlichen Regeln in
[`AGENTS.md`](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/AGENTS.md):

- Vorab-Notizen vor jedem Test;
- Runden nur anhängen, nie umschreiben;
- Merges erst nach Freigabe des Autors;
- das Wiki im selben PR mitziehen;
- keine festen absoluten Pfade in Skripten.

Die Abläufe stehen Schritt für Schritt in
[`notes/anleitungen/`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/main/notes/anleitungen): eine Runde
einbauen, und Rechnungen am OP5-Vergleichsmodell (Daten, Konventionen, bekannte Ergebnisse, Fallstricke). `AGENTS.md`
ist ein offener, werkzeugübergreifender Standard. `CLAUDE.md` verweist nur darauf.

## Vorgehen bei Fachfragen

1. Klären, ob die Frage Veröffentlichung, aktuelle Forschung oder einen historischen Zustand betrifft.
2. Commit/Tag, Dateipfad und möglichst Satzlabel oder Abschnitt nennen.
3. Definitionen, Voraussetzungen, Guards und Frame-Konventionen derselben Fassung lesen.
4. Spätere Korrekturen, Statusnotizen und archivierte Argumente berücksichtigen. Für Frame-/Gravitationsaussagen insbesondere r64–r68 prüfen (r66 korrigiert die Zitierung in r64); für OP5, Vakuumterm und Frame-Neutralität r69 bis r71. Der Inhalt des Companion ist auf der Seite [Was im Companion steht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) zusammengefasst; sie ersetzt nicht die Quellstelle, gibt aber den Stand jeder Aussage an. Die Arbeitsnotizen unter `analysis/` sind Forschungsstände mit bedingten Ergebnissen, keine Manuskriptaussagen.
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
