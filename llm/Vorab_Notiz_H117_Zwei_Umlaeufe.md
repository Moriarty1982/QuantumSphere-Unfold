# Vorab-Notiz H117: Zwei Umläufe und die Wahl der Oktant-Orientierung

22. November 2026. Nicht blind. Der Autor fragt, ob eine erst beim zweiten Umlauf fallende Wegwahl trägt. Getestet werden die logische Vereinbarkeit mit einer Rückkehrbedingung und die native Quellenlage. Die Testmaschine ist ein endlicher Vergleich.

## Vorwissen geprüft

- [H116](Ergebnis_H116_Spinorband_Phasenquelle.md) unterscheidet bei gleichen Start-/Endstrahlen zwei geordnete Oktantrückwege mit +45 bzw. −45 Grad.
- [Abschnitt 19](../sources/research/parts/v470/19_local_op_entry.tex), Zweischritt-Persistenz: ein kurzer guter erster Schritt genügt nicht. [HC-Reparatur](../sources/research/parts/v470/15_hc_repair_and_transport.tex) kennt einen bedingten zweiten Einfangschritt und eine Rangfolge lokaler Endpunkte.
- [19Q](../sources/research/parts/v470/24_computational_specification.tex) fordert beim tatsächlichen Rückkehrtrigger einen eindeutigen zulässigen Nachfolger. [QAM-Hilbert-Shift](../sources/research/parts/v470/07_qam_infrastructure.tex) und [Atlas](../sources/research/parts/v470/32_atlas_and_op_promotion.tex) definieren die Shift-Clocks als Index-/Maskenstruktur. In den geprüften Vorarbeiten ist ihre Identifikation mit physischen Oktant-Umläufen offen. Einordnung T2/T5, siehe [Gesamtbild](../wiki/Gesamtbild.md).

## Kriterien

- **H117a, bedingtes Vergleichsmodell:** Für jede Orientierung d∈{+,−} liegen Indikatoren a_d (erster Schritt) und b_d (zweiter Schritt) vor. Erste Rückkehr besteht aus genau einem Zwischenzustand, der die Kandidaten a festhält und keinen Phasenschritt ausgibt. Zweite Rückkehr übernimmt nur durchgängig zulässige Kandidaten s_d=a_d b_d. Genau ein Überlebender gibt den zugehörigen signierten Phasenschritt aus. Kein Überlebender sperrt, zwei bleiben mehrdeutig. Bei a=(1,1) müssen die späteren Eingaben b=(1,0) und b=(0,1) aus derselben ersten logischen Stufe entgegengesetzte Schritte erzeugen. Alle 16 Maskenpaare prüfen; ein zuerst ausgeschiedener Kandidat darf nicht wieder eintreten.
- **H117b, Symmetrie- und Nativprüfung:** Zwei gleich behandelte Kandidaten dürfen alleine durch Zweischritt-Persistenz keinen unterschiedlichen Ausgang bekommen. Ein nativer Nachweis bräuchte einen physisch definierten ersten und zweiten Umlauf und einen Closure-/Routingwert, der bei sonst gleichem ersten Fenster die Orientierungen trennt. Fehlende Spezifikation wird als offen protokolliert.
- **Unabhängige Kontrolle:** Wolfram für die exakte Auswahltabelle, dazu eigene MMA-/SystemVerilog-Fälle im unveränderten 209-Fälle-Vergleichsrahmen. Für jede einzelne Orientierung wird derselbe Zweischritt-Test mit erstem und zweitem Guard als Tape-Eingabe kodiert. Es werden MMA und beide HDL-Kerne verglichen und die Ergebnisse zu den 16 Maskenpaaren zusammengesetzt. Die vorab geladenen zweiten Guard-Bits werden erst im zweiten Maschinenversuch gelesen. Das stellt verzögerten Zugriff dar, ohne einen physikalischen Eingriff zwischen zwei Umläufen zu behaupten.

Eine Quantenschaltung ist nicht vorgegeben. Der Zwischenzustand ist ein logischer Kandidatensatz; Kohärenz und echte Zeitentwicklung sind nicht Teil dieses Vergleichs.
