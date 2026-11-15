# OP1 mit I1: Zählt der Tachyon-Frame nur Endpunkte fundamentaler Strings?

15. November 2026, Claude Opus. **Erkundung, nicht blind** (Rückwärtssuche): Das Ziel, M zählt alle Spins und T nur
j = ½, ist bekannt und durch H98 an die Daten gebunden. Auftrag des Autors: „OP1 mit I1 angehen“. Zurückgestellte Idee
I1 (mehrere LQG-Systeme, verbunden durch einen String) wird auf Autorentscheidung verfolgt; Auslöser 3 (β_sym als
γ_BI/γ_string) ist getroffen. Keine H-Nummer, kein CT-Eintrag, Guards unverändert. Einordnung T6, T11, OP1.

## Ziel und notwendige Bedingungen
Gesucht ist ein Grund für die Zählregel je Frame (r09, r10.3): Materie-Frame M alle Spins mit Gewicht 2
(γ_M = 0,237533), Tachyon-Frame T nur j = ½ mit Gewicht 2 (γ_T = ln 2/(π√3) = 0,127384), Verhältnis γ_L = 1,8647.
- **N1:** Eine native Unterscheidung zwischen den beiden Frames.
- **N2:** In T genau j = ½. Nicht „alle halbzahligen“ und nicht „kleinste Fläche“ ohne Grund.
- **N3:** In M alle Spins mit Gewicht 2.

## Vorwissen geprüft
- **v4.9.0-r63:** γ_string ist die ABCK-Zählung (nur j = ½), γ_BI die DL/Meissner-Zählung (alle Spins, g = 2).
  Exakt: Robertson-Sättigung genau für m = ±j (r63.2), Tachyon-Boden (r63.3).
- **v4.10.0-r09** (`v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md`): Prinzip P. P1 heißt „nur sättigende Zustände“ und
  gibt Gewicht 2, P2 heißt „M alle Stufen, T nur die kleinste Fläche“. H98: Im Regelraum (alle, halbzahlig, ganzzahlig,
  nur ½, nur 1; Gewichte 2 und 2j + 1) trifft nur das gewählte Paar alle drei Fenster.
- **v4.10.0-r10:** Die Energiebrücke von P2 trägt nicht. Die Zählgleichung ist eine Unruh-Statistik, der Abstand des
  Beobachters fällt heraus, und T sieht dieselbe Statistik. Übrig bleibt ein frame-abhängiges Flächenquant.
- **H104:** Bei freiem Flächenspektrum trifft ein zweites Paar; die Sonderstellung hängt am festen Spektrum.
- **T11** (`thm:string-lqg-duality`, v470/10): String- und LQG-Sektor als die zwei Kompensator-Sektoren. Die
  Äquivalenz stützte sich auf Stone–von Neumann aus der Riemann-Arbeit und ist seit r04 offen. Nomenklatur (v470/08):
  γ_string heißt „string coupling“.
- **I1** (`v4_10_0_w1/Zurueckgestellte_Ideen.md`) und `../op3_i1_string_bridge_2026_11_14.md`: String zur
  Horizont-Punktierung, „eine Querung“ (CT-002).
- **OP3-Befunde vom 15.11.** (`../op3_guarded_core_flux_2026_11_15/`): genau ein Kern; Umkehrwalze antilinear mit
  Θ² = −1.
- Volltextsuche nach Chan–Paton: keine Fundstelle im Repo.

## Kandidaten

| Kandidat | Regel für T | N1 | N2 | N3 | Stand |
|---|---|---|---|---|---|
| C1 Energie-Boden (r09, P2) | kleinste Fläche | Tachyon-Boden | ja | ja | Brücke trägt nicht (r10) |
| C2 Kramers über die Umkehrwalze | Θ² = (−1)^{2j} = −1, also alle halbzahligen Spins | antilineare Umkehrwalze | **nein** | ja | ausgeschlossen, siehe unten |
| C3 Stringendpunkte (I1) | nur j = ½, Gewicht 2 | T = String-Sektor (T11, Nomenklatur) | ja | ja | Lesart, siehe unten |

**C2 nachgerechnet:** Für „alle halbzahligen Spins, Gewicht 2“ ist γ = 0,189138. Das Paar mit M gibt γ_L = 1,255868
und β = 0,336784, weit außerhalb des Fensters [0,545; 0,570]. Das deckt sich mit H98. Die Fixpunktfreiheit der
Umkehrwalze wählt also zu viel aus.

**C3, die Lesart über I1:**
- T ist der String-Sektor (T11; γ_string heißt im Companion „string coupling“), M der LQG-Sektor.
- Im String-Sektor sind die Punktierungen eines Horizonts **Endpunkte offener Strings**, also Stellen, an denen der
  String aus I1 auf das andere System trifft.
- Ein Endpunkt eines einzelnen offenen Strings trägt die **Fundamentaldarstellung** der Eichgruppe. Das ist der
  Chan–Paton-Faktor der Stringtheorie (Literatur, aus Vorwissen, hier nicht nachgeprüft). Für SU(2) ist das j = ½ mit
  der Dimension 2, also genau Gewicht 2.
- Der LQG-Sektor zählt dagegen Kanten eines Spin-Netzwerks mit beliebigem j. Nach P1 (Sättigung, m = ±j) hat jede
  Kante Gewicht 2.

C3 erfüllt N2 ohne die Energiebrücke, die r10 verworfen hat: Ein *einzelner* String endet in der Fundamentaldarstellung,
höhere j bräuchten mehrere Strings an einem Punkt. Damit fallen drei bisher getrennte Platzhalter auf eine Aussage
zusammen:
- die „eine Querung“ von CT-002 (ein String);
- der eine Kern aus der Topologie (genau eine Punktierung bricht ohne freien Parameter);
- die Zählung j = ½ in T (Endpunkt in der Fundamentaldarstellung).

Auch das Gewicht passt in beiden Lesarten, denn bei j = ½ ist 2j + 1 = 2.

## Grenzen
- **Lesart, keine Herleitung.**
  - Chan–Paton gilt für offene Strings, die auf D-Branen enden. Den Horizont als Brane zu lesen, ist eine Analogie;
    ABK nennen ihn selbst eine „gravitational 2-brane“ (arXiv:gr-qc/0005126, S. 60), betonen aber die Unterschiede.
  - Dass die Eichgruppe an diesen Endpunkten SU(2) mit Fundamentaldarstellung ist, ist gesetzt.
- **Vertauschte Statistik:** T11 nennt den String-Sektor bosonisch (symmetrisch) und den LQG-Sektor fermionisch. C3
  lässt den String-Sektor aber den fermionischen Spin ½ zählen. Ein Endpunkt kann Spin ½ tragen, auch wenn der String
  selbst bosonisch ist; die Zuordnung in T11 ist aber eine geerbte Lesart mit offenem Äquivalenzschritt (r04).
- **Kein blinder Test.** C3 reproduziert das Paar, das H98 schon ausgewählt hat. Eine neue Zahl folgt nicht. Ein
  echter Test bräuchte eine dritte Größe, die von der String-Lesart abhängt und noch nicht gemessen ist.
- H104 bleibt bestehen: Die Sonderstellung des Paares hängt am festen Flächenspektrum a(j) = √(j(j+1)).

## Befund
Die Zählregel je Frame lässt sich mit I1 als **„T zählt Endpunkte einzelner offener Strings, M zählt Kanten des
Spin-Netzwerks“** lesen. Das ersetzt die gescheiterte Energiebrücke von r09/r10 durch ein Argument aus der
Darstellungstheorie und bindet drei Platzhalter (CT-002, genau ein Kern, Zählung in T) an dieselbe Stelle. Die
Kramers-Regel über die Umkehrwalze ist ausgeschlossen (C2). OP1 ist damit nicht geschlossen: Die Gleichsetzung
T = String-Sektor und der Chan–Paton-Schritt sind Annahmen. Sie wären als ein Platzhalter (etwa CT-004) zu führen,
falls der Autor das will.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
