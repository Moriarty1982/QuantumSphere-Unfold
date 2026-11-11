# Quellenprüfung, 11. November 2026

Keine neue Literatur- oder Neuheitssuche; keine Volltextkopien archiviert.
Vor der Abfrage wurden die lokalen Notiz-/Analysepfade nach passenden
DLMF-/Robertson-/Literaturdateinamen durchsucht; kein Treffer. Der
vorhandene redaktionelle Prüfbericht wurde als Vorbefund gelesen.

## DLMF

- NIST DLMF, §27.4, Gleichung 27.4.12; Version 1.2.8, 15.09.2026.
- Primärquelle: https://dlmf.nist.gov/27.4.E12
- Status: Formel angegeben, Re(s)>1 ausdrücklich vorhanden.
- Übersetzung: s=sigma+it; Im des negierten Dirichlet-Ausdrucks ergibt
  das positive Vorzeichen der Sinusreihe im Manuskript.
- Implikation: verified für die verwendete Reihenformel bei sigma>1.
- Gleichmäßigkeit der Ableitungen und Operatorfolgen wurden unmittelbar
  aus den im Manuskript genannten Majoranten rekonstruiert, nicht der
  DLMF als zusätzlicher Satz zugeschrieben.
- Keine Aussage über sigma=1/2; keine Neuheitsbewertung.

## Robertson

- H. P. Robertson, The Uncertainty Principle, Physical Review 34 (1929),
  163–164, DOI 10.1103/PhysRev.34.163.
- Primärseite: https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163
- Authentifiziert: Autor, Titel, Band, Anfangsseite, DOI und Publikationsdatum.
- Originalvolltext: zugangsbeschränkt, nicht gelesen; dessen genaue
  historische Formulierung bleibt unverified, kein zitierter Theoremsatz.
- Anwendung stattdessen direkt geprüft: Für zentrierte selbstadjungierte
  Operatoren liefert Cauchy-Schwarz Delta(X)Delta(Y) mindestens den Betrag
  des Imaginärteils ihres gemischten Skalarprodukts. Bei vorhandenen
  Produktdomänen ist dieser die halbe Kommutatorerwartung. R/A sind
  beschränkt; beim Q/P-Packet wurden die Produktdomänen im Text geprüft.
- Keine erfundene Quellenversion, kein gespeicherter Originalvolltext.

## Baez

- John C. Baez, The Octonions, Bull. Amer. Math. Soc. 39 (2002), 145–205;
  Autorenseite nennt auch Errata 42 (2005), 213.
- https://math.ucr.edu/home/baez/octonions/ und dortiger Abschnitt G2.
- Als Überblick über den algebraischen Kontext authentifiziert; keine
  spezifische physikalische Ableitung oder native CAR-Darstellung daraus
  als verifiziert übernommen. Keine versionierte Volltextbegutachtung.

## Bindung an die Arbeitskopie

Der gelesene exportierte Quelltext stimmt bytegenau mit der im
Vorbereitungsmanifest genannten Datei überein. Die neun aktuellen
Erklärungs-/Literaturquellen unter qam/editions/v5_*.tex stimmen nach
CRLF-zu-LF-Normalisierung mit den Container-Quellhashes überein.
Ein erster roher Bytevergleich scheiterte an Windows-Zeilenenden;
er wurde nicht als Inhaltsabweichung oder erfolgreicher Bytevergleich
ausgegeben. Die Manuskriptdateien wurden nicht verändert.
