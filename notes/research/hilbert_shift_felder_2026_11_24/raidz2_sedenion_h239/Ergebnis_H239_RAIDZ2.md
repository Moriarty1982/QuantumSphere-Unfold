# Ergebnis H239 (k455): Ist die Struktur von 𝕊 zweimal RAIDZ2?

**Datum:** 2026-11-28. **Vorab:** `Vorab_H239_RAIDZ2.md`, Commit d620653, vor der Rechnung. **Rechnung:** `k455_test_h239.py` → `k455_out.txt`;
Gegenprobe `k455b_gegenprobe.wl` → `k455b_out.txt` (exakt); Nachtrag `k455c_profil.py` → `k455c_out.txt` (nachträglich, nur Bericht).
**Urteil nach dem Wortlaut der Vorab-Notiz: trägt teilweise. Inhaltlich stimmt nur die Kapazität 12/16; die Paritätseigenschaft von RAIDZ2 fehlt.**

## Übersetzung (gesetzt)
Zweimal RAIDZ2 = ein [16, 12]-Code, der in zwei unabhängige Gruppen zu je 8 Koordinaten mit je 6 Daten und 2 Parität zerfällt; jede Gruppe verkraftet
zwei beliebige Ausfälle. In 𝕊 ist der Code eines Nullteilers x das Bild C_x = Bild(L_x) (was beim Multiplizieren erhalten bleibt), die Ausfallrichtungen
sind der Kern. Koordinaten sind die Basiseinheiten, die natürliche Gruppengrenze ist die Wand e₈.

## Befunde
- **D1 (nicht blind) erfüllt:** Rang L_x = 12 für alle 84 Basis-Diagonalen (e_i ± e_j)/√2 und alle 200 allgemeinen Nullteiler (a, b)/√2 (Python;
  Wolfram exakt). Die Kapazität 12/16 = 6/8 passt also zu zweimal RAIDZ2.
- **D2 (blind) an der Wand verfehlt:** dim(C_x ∩ unten) = dim(C_x ∩ oben) = 4, nicht 6. Das ist genau die generische Lage (12 + 8 − 16 = 4): Der Code
  spaltet an der Wand nicht. Der Kern ist ebenfalls nicht gespalten (Projektionen 4 und 4).
- **Andere Aufteilungen:** Basis-Diagonalen spalten an 210 von 6435 Aufteilungen 6 + 6, aber nur trivial (siehe unten). Allgemeine Nullteiler spalten
  an keiner der 6435 Aufteilungen (5 Stichproben).
- **D3 (blind) verfehlt:** An keiner gefundenen Spaltung ist auch nur ein einzelner Ausfall in jeder Gruppe rekonstruierbar. Zufällige [8, 6]-Codes
  verkraften dagegen genau 2 Ausfälle und nicht 3, also das RAIDZ2-Profil.
- **Zufallskontrolle:** 0 von 2000 zufälligen 12-dim. Unterräumen und 0 von 2000 zufälligen Rang-12-Bildern spalten an der Wand.

## Nachträglich (k455c, nur Bericht): wie der Nullteiler-Code wirklich aussieht
- **Basis-Diagonalen:** L_x bildet jede Basiseinheit auf eine Summe zweier Basiseinheiten ab. Der Code zerfällt in 8 Koordinatenpaare: 4 Paare sind
  Klartext (Rang 2, ungeschützt), 4 Paare sind Spiegel (Rang 1, Wiederholungscode, also RAID1). Das ist eher „halb gespiegelt, halb ungeschützt“ als RAIDZ2.
- **Allgemeine Nullteiler:** Die Koordinaten e₀ und e₈ sind ungeschützt (die Paritätsprüfung sieht sie nicht; Wolfram exakt). Das ist derselbe Raum
  span{1, e₈}, der in H237 als gemeinsamer Kern aller 15 Richtungen auftrat.
- **Ausfallprofil des ganzen [16, 12]-Codes** (nicht rekonstruierbare Ausfallmengen der Größe 1, 2, 3, 4; dazu Muster „2 unten + 2 oben“ von 784):
  Basis-Diagonalen 8, 96, 528, 1804; 778. Allgemeine Nullteiler 2, 29, 196, 819; 343. Zufällige Codes 0, 0, 0, 0; 0.
  Der Nullteiler-Code ist also deutlich schwächer als ein zufälliger Code gleicher Größe und weit von RAIDZ2 entfernt.

## Lesart
Die Zahl stimmt: Ein Nullteiler verliert 4 von 16 Richtungen, so viel wie zweimal RAIDZ2 an Parität braucht. Die Struktur stimmt nicht: Die 4 verlorenen
Richtungen sind keine verteilte Parität, die zwei Ausfälle je Gruppe auffängt, sondern liegen quer über die Wand e₈, und 1 und e₈ bleiben ganz ungeschützt.
Die Wand e₈ ist in 𝕊 also keine Grenze zwischen zwei unabhängigen Paritätsgruppen.

## Hergeleitet, gesetzt, offen
- **Hergeleitet:** Rang 12, Lage an der Wand (4, 4), keine 6+6-Spaltung für allgemeine Nullteiler, Ausfallprofile, Spiegelpaare der Basis-Diagonalen.
- **Gesetzt:** die Übersetzung (Code = Bild der Linksmultiplikation, Koordinaten = Basiseinheiten, Ausfall = Löschung einer Koordinate). Andere
  Übersetzungen, etwa über die Rechtsmultiplikation oder über G₂-invariante statt Basis-Koordinaten, wurden nicht geprüft.
- **Offen:** ob eine andere Übersetzung eine echte Paritätsstruktur zeigt. Die Basis-Koordinaten sind nicht G₂-invariant; die ungeschützten Richtungen
  1 und e₈ sind es.

## Werkzeuge und Grenzen
Python (Stichproben, Suche über alle 8+8-Aufteilungen, Zufallskontrolle) und Wolfram (exakt: Ränge, Wandlage, ungeschützte Koordinaten). Qiskit nicht
einschlägig. Die Suche über alle Aufteilungen lief für allgemeine Nullteiler nur auf 5 Stichproben.
