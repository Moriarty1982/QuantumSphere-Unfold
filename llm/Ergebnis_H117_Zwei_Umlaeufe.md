# H117: Zwei Umläufe und die Wahl der Oktant-Orientierung

22. November 2026. Nicht blind nach [Vorab-Notiz](Vorab_Notiz_H117_Zwei_Umlaeufe.md), Commit 29094b7564d0c5fb4ac471f3f862370afab9066e. [Wolfram-Skript](h117_two_returns.wl), [MMA-/HDL-Vergleich](h117_two_returns_hdl.py) und [Laufprotokoll](h117_two_returns.txt).

## Der erste Umlauf kann einen eindeutigen Zwischenzustand liefern

Der erste Schritt speichert die zulässigen Orientierungen als Maske \(a=(a_+,a_-)\) in einem einzigen vorläufigen Zustand. Die zwei Einträge sind Möglichkeiten innerhalb dieses Zustands. Zu diesem Zeitpunkt wird kein Vorzeichen ausgegeben. Der zweite Schritt prüft dieselben Kandidaten mit einer Maske \(b\). Es gilt
\[
s_d=a_d b_d,\qquad d\in\{+,-\}.
\]
Ein Kandidat muss somit beide Fenster überstehen. Bei genau einem verbleibenden Kandidaten ergibt sich im Oktantvergleich der Phasenschritt gemäß [H116](Ergebnis_H116_Spinorband_Phasenquelle.md).

| Erste Maske | Zweite Maske | Ausgang |
|---|---|---|
| beide | nur + | \(+45^\circ\) |
| beide | nur − | \(-45^\circ\) |
| beide | beide | mehrdeutig, kein Phasenschritt |
| beide | keine | gesperrt |

Der Zeitpunkt der Auswahl liegt damit im zweiten Fenster, sofern die erste Stufe als vorläufiger Zustand gewertet wird. Unter allen 16 Maskenkombinationen gibt es dreimal \(+45^\circ\), dreimal \(-45^\circ\), neun Sperren und einen mehrdeutigen Fall. Ein im ersten Fenster entfallener Weg kann nicht zurückkehren. Die Häufigkeiten gelten für vollständiges Abzählen der binären Vergleichsmasken, ohne probabilistisches Modell.

## Was der Companion schon trägt

Die [Zweischritt-Persistenz](../sources/research/parts/v470/19_local_op_entry.tex) verwirft kurzzeitig passende Kandidaten. [19Q](../sources/research/parts/v470/24_computational_specification.tex) fordert beim eigentlichen Rückkehrereignis genau einen zulässigen Nachfolger. Beides ist mit der Tabelle vereinbar, wenn der erste Schritt den einen vorläufigen Zustand herstellt und das Rückkehrereignis erst beim zweiten, eindeutigen Ausgang ausgelöst wird. Wenn beide Wege gültig bleiben, muss der Trigger ausgesetzt werden oder es braucht eine belegte zusätzliche Auswahlregel.

Die [HC-Reparatur](../sources/research/parts/v470/15_hc_repair_and_transport.tex) hat bereits eine bedingte Einfangregel im zweiten Schritt. Sie setzt einen zulässigen lokalen Korridor und einen verschwindenden Phasenfehler voraus. Sie behält auch gekoppelte Residualzweige bei, wenn die lokalen Rangkriterien sie nicht unterscheiden. Diese Vorschriften liefern für den Oktanten keine konkrete Größe, die beim zweiten Umlauf zwischen \(+45^\circ\) und \(-45^\circ\) entscheidet. Eine [OP3-Erkundung](../notes/research/op3_repair_connected_family_2026_11_10.md) hat ein mitgeführtes Phasenregister als Vergleich, dessen native Vorbereitung und Kopplung offen sind. Der [doppelte Hilbert-Shift](../sources/research/parts/v470/07_qam_infrastructure.tex) ist im vorliegenden Aufbau eine Index- und Maskenkodierung. Eine Zuordnung dieser Clocks zu den beiden physikalischen Umläufen wurde nicht gefunden.

**H117a trägt im endlichen Vergleich.** Die Symmetriekontrolle zu H117b zeigt exakt, dass bei gleich behandelten Orientierungen keine eindeutige Wahl entsteht. Die fehlende Ableitung ist ein nativer, vorzeichenempfindlicher Routing- oder Closure-Wert im zweiten Fenster. Die erste Vormerkung allein verschafft dem Modell weder Zufall noch ein nachgewiesenes kohärentes Gedächtnis.

## Unabhängige Kontrolle

Wolfram prüfte alle 16 Tabellenzeilen exakt. Die Referenzmaschine prüft die vier Eingabepaare einer einzelnen Orientierung. Nach einem negativen ersten Guard hält sie an, sonst liest sie den zweiten Guard erst im zweiten Maschinenversuch. Die Eingaben waren vorab geladen. Aus den entsprechenden MMA-Endzuständen ergeben sich dieselben 16 Zeilen. Die direkte und die zyklische SystemVerilog-Steuerung stimmen für alle vier Zusatzfälle einschließlich Spuren und Stopmeldungen mit MMA überein. Der unveränderte MCP-Grundtest mit 209 Fällen bestand ebenfalls. Für die lokale Zusatzsimulation wurde Icarus 10.3 aus einem temporär entpackten Ubuntu-Paket mit expliziten Modulpfaden in WSL verwendet. Die erste Simulationsaufnahme scheiterte an der lokalen Werkzeugsuche, und der erste Lauf mit entpacktem Paket brauchte den Modulpfad für die Laufzeit. Die gespeicherte Ausgabe stammt aus dem anschließenden erfolgreichen Lauf.

Eine Quantenschaltung war nicht vorgegeben. Die Tests verifizieren die konkrete diskrete Vergleichsregel, einschließlich des verzögerten Zugriffs. Sie weisen keinen physischen Phasenschritt des Spinorbands nach.
