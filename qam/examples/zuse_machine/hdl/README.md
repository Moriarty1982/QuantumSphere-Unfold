# Die Bandmaschine in SystemVerilog

[`tape_core.sv`](tape_core.sv) implementiert das feste und das nach rechts
wachsende Band aus `RUN_TAPE`. Die Beispielinstanz hat acht physische Zellen
und sechs Tabellenadressen für drei Zustände und zwei Lesebits. Der
Tabelleninhalt ist ladbar. Der Aufrufer lädt alle Einträge bei gestopptem Kern,
einschließlich ungültiger Einträge für fehlende Regeln. MMA validiert beim
Vergleich Programm, Startzustand und Grenzen.

Mit `SCAN=0` adressieren Zustand und Lesebit den passenden Eintrag direkt.
Mit `SCAN=1` liest der Kern bei jedem Maschinenversuch die ganze Tabelle
zyklisch, merkt sich den passenden Eintrag und übernimmt dessen Wirkung nach
dem letzten Slot. Der Kern verwendet in beiden Fällen dieselbe Logik für
Schreiben, Kopfbewegung, Bandwachstum und Stopmeldungen. Beim Wachstum gibt
er die nächste physische Zelle frei und setzt sie auf null.

## Simulation und Bericht

Die Simulation braucht Python, `iverilog` und `vvp` im Suchpfad.
Vom Stammverzeichnis des Repositorys aus kannst du den Vergleich so starten.

```sh
python -m qam.examples.zuse_machine.hdl.check --report build/hdl-comparison.md --wave build/hdl-comparison.vcd
```

`--yosys` ergänzt die generischen Zellzahlen, wenn Yosys installiert ist.
`--iverilog`, `--vvp` und `--yosys PFAD` erlauben lokale Werkzeugpfade.
Die VCD-Datei zeigt beide Kerne samt ihren Takten, Zuständen, aktiven
Bandlängen und dem Slotzähler der zyklischen Variante. [Icarus-Dokumentation](https://steveicarus.github.io/iverilog/) · [Yosys-Dokumentation](https://yosyshq.readthedocs.io/)

Der Treiber holt die Referenzspuren über den regulären MMA-Aufruf im
Python-Adapter. Der Testbench speist beide Schaltungen mit denselben
Eingaben. Der Python-Vergleich meldet bei einer Abweichung den Startfall und
den ersten abweichenden Spureintrag. Unter Linux läuft der Vergleich
außerdem im bestehenden GitHub-Workflow für QAM.

In Codex führt das Werkzeug `run_qam_hdl_check` auf `qsc-qam-batch`
dasselbe Prüfprogramm aus und liefert die Ergebnisse als strukturierte
Daten. [MCP-Aufruf und Voraussetzungen](../../../../mcp/README.md#hdl-and-mma-comparison-in-codex)

Der Vergleich erfasst das Startband und jeden sichtbaren Maschinenversuch.
Ein Schritt über eine feste Grenze zählt in MMA als Versuch mit
`boundary`. Beim `cell_limit` verbraucht der Versuch Takte und lässt Band,
Kopf und Schrittzähler unverändert. Die Taktmessung beginnt nach der
Startflanke. Laden der Regeln und Einlesen der Ergebnisse liegen außerhalb
der Messung. Yosys zählt generische Zellen vor dem Mapping auf ein FPGA.

## Streaming-Guard für zwei Prüfschritte

Der [Streaming-Guard](guard_stream.sv) prüft beide Zulässigkeitsmasken je
Kandidat und gibt nur eindeutige Orientierungen aus. Bei freiem Empfänger
nimmt er einen Kandidaten pro Takt an. Bei Rückstau hält der registrierte
Ausgabeslot den ausstehenden Treffer stabil.

~~~sh
python -m qam.examples.zuse_machine.hdl.guard_stream_check --rows 65536
~~~

Der [Laufbericht](guard-stream-verification.md) dokumentiert den Vergleich
mit MMA, die Takte, die logische Nutzlast und die generische Synthese.

## Verwendung im Companion

Der [Laufbericht](verification.md) liefert eine reproduzierbare Tabelle
für den Abschnitt zur Maschinenbeschreibung 19K–19L. Die Aussage über
Takte bezieht sich auf die beiden konkreten Steuerungen und ihre sechs
Tabellenadressen.

> In a bounded SystemVerilog reference implementation with eight physical tape cells and six transition-table slots, direct lookup and a cyclic scan produced the same configuration traces and stop reasons as MMA on all 209 tested inputs. The binary increment from seven to eight took four machine steps. It used four clock cycles with direct lookup and twenty-four with the cyclic scan, measured after loading the initial configuration.

Für 19AF–19AH bleiben die Identifikation des spinoriellen Bands und der
HC-Rückkehr sowie die unbeschränkte Erweiterbarkeit mit stabiler
Dekodierung Voraussetzungen. Die geprüften Spuren konkretisieren das
Verhalten einer endlichen Referenzmaschine.
