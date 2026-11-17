# Vergleich: Woran andere Versuche einer Theorie von allem gescheitert sind, und wo der Companion steht (Erkundung, Lesart)

17. November 2026. Auftrag des Autors: „Vergleiche das bitte mit anderen wissenschaftlichen Arbeiten, die auch versucht haben, eine TOE aufzustellen,
und vergleiche, woran die gescheitert sind. Vielleicht läuft alles auf einen bestimmten Punkt/Aussage oder Geometrie zu.“
Keine Rechnung, keine H-Nummer. Quellen: in dieser Sitzung gelesen sind Dreyer (gr-qc/0211076), Corichi (gr-qc/0212126), Polychronakos
(hep-th/0304135), Frodden–Geiller–Noui–Perez (1212.4060), Eder–Sahlmann (1801.00747), Ashtekar–Baez–Krasnov (gr-qc/0005126); die übrigen Angaben
sind **Vorwissen**, nicht in dieser Sitzung nachgelesen, und vor einer Verwendung im Paper zu prüfen.

## 1. Die Versuche und ihre Bruchstellen

| Ansatz | Kernidee | Woran er scheitert oder hängt |
|---|---|---|
| Kaluza–Klein (ab 1921) | Eichfelder aus Zusatzdimensionen | Chiralität: Auf glatten kompakten Zusatzräumen entstehen keine chiralen Fermionen (Witten 1981, Nucl. Phys. B186) |
| Supergravitation (11D) | maximale Symmetrie, eine Theorie | dieselbe Chiralitätshürde; nicht renormierbar |
| Große vereinheitlichte Theorien (SU(5), SO(10)) | Eichgruppen vereinigen | Protonzerfall (SU(5) minimal ausgeschlossen); drei Generationen von Hand |
| Stringtheorie | ein Objekt, alle Teilchen als Schwingungen | Landschaft: Zahl der Vakua ~10⁵⁰⁰, keine Auswahlregel (Susskind hep-th/0302219, Douglas hep-th/0303194) |
| Schleifenquantengravitation | Geometrie quantisiert | Immirzi-Parameter γ frei; Zählregel (U(1) gegen SU(2)) umstritten; Dynamik und klassischer Grenzfall offen |
| Selbstduale Ashtekar-Variablen | komplexe Verbindung, einfache Zwangsbedingungen | Realitätsbedingungen; deshalb reelles γ (Barbero, Immirzi). Mit γ = ±i und Fortsetzung j → is − ½ folgt S = A/4 ohne Festlegung (FGNP 1212.4060) |
| Twistortheorie (Penrose) | Raumzeit aus komplexer Geometrie | „Googly-Problem“: nur eine Helizität entsteht natürlich (Penrose 2015); Twistor-Strings bringen konforme Supergravitation mit (Berkovits–Witten hep-th/0406051) |
| E8 (Lisi 0711.0770) | alle Felder in einer Ausnahmegruppe | Drei chirale Generationen passen nicht in E8 (Distler–Garibaldi 0905.2658) |
| Divisionsalgebren (Dixon, Furey, Gresnigt) | Standardmodell aus C⊗H⊗O | eine Generation natürlich; drei Generationen brauchen Zusatzstruktur (Sedenionen, Kopien), noch offen |
| Nichtkommutative Geometrie (Connes) | Standardmodell als Spektraltripel | Higgs-Masse ~170 GeV vorhergesagt (Chamseddine–Connes–Marcolli hep-th/0610241), gemessen 125 GeV; gerettet durch ein zusätzliches Skalarfeld |
| Koide-Herleitungen (Brannen, Sumino) | Massenformel aus Struktur | erklären K = 2/3 oder Phase je mit Zusatzannahmen; Sumino (0812.2103): Familien-Eichsymmetrie, warum Koide für Polmassen gilt |

## 2. Die wiederkehrenden Bruchstellen
Sortiert man die Spalte rechts, bleiben vier Stellen, an denen fast alle hängen:

1. **Chiralität und Drei-Generationen-Zahl** (Kaluza–Klein, Supergravitation, E8, Divisionsalgebren, GUTs).
2. **Auswahl des Zustands bzw. Vakuums** (Stringlandschaft, Connes' endliche Algebra, LQG-Zustand).
3. **Ein freier Parameter im Gravitationssektor** (Immirzi-γ, Moduli, Kopplungen).
4. **Realität gegen Selbstdualität** (Ashtekar-Realitätsbedingungen, Googly-Problem, Twistor-Strings).

## 3. Wo der Companion an denselben Stellen steht

| Bruchstelle | Companion | Stand |
|---|---|---|
| Chiralität, drei Generationen | OP3 (Koide, Generationen); r19: eine Generation von C⊗H⊗O trägt kein Generations-Qubit; r25/r26: Kopien | offen, wie bei Furey/Gresnigt |
| Zustandsauswahl | OP5 (Zustandsauswahl, fehlender Umlauf); OP3-Diagnose: δ ist eine Eigenschaft des Feldzustands | offen |
| freier Gravitationsparameter | γ_M = 0,237533, Zählregel des Frames M (OP1) | gesetzt, durch Daten gepaart (H98), nicht hergeleitet |
| Realität gegen Selbstdualität | χ-Kugel: reelle Felder auf dem Äquator (P), selbstduale an den Polen (Ports); r17.4: reelles γ auf dem Äquator, γ = ±i an den Polen | M liegt dazwischen, bei b = 1/γ_L = 0,5363 |

## 4. Läuft es auf einen Punkt zu? (Lesart)
Drei der vier Bruchstellen sind **dieselbe Geometrie in verschiedener Sprache**: die Kugel der komplexen Strukturen, mit den reellen Objekten auf dem
Äquator und den selbstdualen an den Polen.

- **Ashtekar/Immirzi:** Die selbstduale Verbindung (γ = ±i, Pol) macht die Gleichungen einfach, verlangt aber Realitätsbedingungen; die reelle
  Barbero-Verbindung (γ reell, Äquator) umgeht sie und bezahlt mit einem freien γ. FGNP zeigen, dass am Pol S = A/4 ohne γ herauskommt.
- **Twistoren:** Eine Helizität (ein Pol) ist natürlich, die andere nicht; das ist das Googly-Problem.
- **Chiralität:** Chiralität ist genau die Asymmetrie zwischen selbstdualem und antiselbstdualem Teil; Kaluza–Klein und E8 scheitern daran, sie aus
  einer symmetrischen Geometrie zu erzeugen.
- **Companion:** Die χ-Kugel hat genau diesen Aufbau (r16.3, r17.4); seit 17.11. ist klar, dass jede reelle (statische) Größe auf dem Äquator liegt und die
  Lage des Frames M zwischen Äquator und Pol nur mit einer Frequenz, also einer Aufteilung in positive und negative Frequenzen, erreichbar ist. Diese
  Aufteilung ist dieselbe Wahl einer komplexen Struktur, die Teilchen von Antiteilchen trennt.

**Aussage (Lesart, nicht bewiesen):** Die offenen Zahlen der großen Ansätze sitzen an derselben Stelle: **auf welcher Breite zwischen reell
(Äquator) und selbstdual (Pol) die Natur ihre Auslesung wählt.** Die Ansätze, die am Pol arbeiten (selbstdual, Twistoren), bekommen eine Helizität
geschenkt und verlieren die andere; die, die am Äquator arbeiten (reelle Variablen), behalten beide und bekommen einen freien Parameter. Der Companion
nennt diese Breite ausdrücklich: Frame M bei b = 1/γ_L = 0,5363, mit γ_L aus dem Verhältnis der beiden Zählregeln, ω_M/ω_T = γ_L
(`../op1_readout_frequency_2026_11_17/`). Seine offene Frage OP1 ist in dieser Sprache die Frage, warum die Auslesung bei dieser Breite liegt.

Die vierte Bruchstelle (drei Generationen) gehört nicht zur selben Geometrie, sondern zur Dreizahl: Trialität von SO(8), drei Generationen, das Oktant-
Dreieck der Koide-Phase. Auch hier sind alle Ansätze offen; der Companion hat dazu die Starrheit der Phase (r28.2) beigetragen.

## 5. Was daraus folgt
- **Für die Arbeit am Companion:** Die Frage nach der Breite von M ist keine Eigenheit des Companion, sondern die Stelle, an der Ashtekar-Variablen,
  Twistoren und Chiralität hängen. Literatur zu „Immirzi-Parameter als Breite zwischen reeller und selbstdualer Verbindung“ und zu „komplexem γ mit
  Realteil und Imaginärteil“ wäre der nächste gezielte Blick; ob es dort einen ausgezeichneten Wert gibt, ist nicht geprüft.
- **Für die Darstellung:** Der Vergleich ist eine Einordnung. Er beweist nichts und schließt kein OP. OP1–OP5, C5, C6/T2 offen.
