# OP1: Die Frame-Abbildungen wirken nur bei j = ½ irreduzibel

15. November 2026, Claude Opus. **Erkundung, nicht blind**: Das Paar aus H98 (M alle Spins mit Gewicht 2, T nur j = ½) und
seine Werte waren bekannt; die Bedingungen sind danach formuliert. Auftrag des Autors: „OP1 angehen“, dann „Ja, als
Erkundung“. Keine H-Nummer, kein CT-Eintrag, Guards unverändert. Skript `frame_irreducibility.py`, Ausgabe
`run/frame_irreducibility_stdout.txt`.

## Vorwissen geprüft
- **H98 (v4.10.0-r09.1):** Im Regelraum (9 Regeln, 36 Paare) trifft nur das Paar „M alle Spins, Gewicht 2; T nur j = ½“ alle
  drei Datenfenster. **H104 (r14.1):** Mit freiem Flächenspektrum gibt es ein zweites Paar; die Sonderstellung hängt am
  festgehaltenen Spektrum.
- **Prinzip P (r09.2):** P1 (Unschärfe-Sättigung) gibt das Gewicht 2; P2 (Energie) sollte T auf j = ½ beschränken.
  **r10.2:** P2 trägt nicht (M und T sehen dieselbe Unruh-Statistik). **r10.4(a):** Sättigung allein wählt j = ½ nicht aus.
  **r10.4(c):** Eine umkehrbare Umbeschreibung entfernt keine Spinsektoren; eine T-Regel muss eine eingeschränkte
  Auslesung sein. **r10.3:** Die Regel ist gleichwertig zu einem frame-abhängigen Flächenquant.
- **r16.6 (k220):** Die Zählregel kommt nicht aus SO(3, ℂ) × Dualität.
- **r16.7:** Die Frame-Abbildungen wirken auf dem Dublett χ als halbe Drehungen um drei senkrechte Achsen.
- **I1, CT-004** (`../op1_i1_string_endpoints_2026_11_15/README.md`): T zählt Endpunkte offener Strings (Chan–Paton,
  j = ½); Guard 1 („T = String-Sektor“) ohne Stütze. **Kramers-Regel** (alle halbzahligen j) ausgeschlossen (β = 0,337).
- Zurückgestellte Ideen: Auslöser 3 von I1 ist berührt (OP1), die Idee wird über CT-004 schon verfolgt.

## Annahme (A)
Die Frame-Abbildungen wirken auf einer Horizont-Punktierung mit Spin j über dieselbe SU(2) wie auf χ, also als
exp(−iπJ_k) für drei senkrechte Achsen. Das ist eine **Brücke vom Feld-Dublett zur Punktierung**; sie ist nicht hergeleitet
und trägt alles Folgende.

## Ergebnisse
1. **Irreduzibel nur bei j = ½** (geprüft für j = ½ bis 20):
   - bei halbzahligem j antikommutieren die Abbildungen; der Raum zerfällt in (2j + 1)/2 Kopien der 2-dimensionalen
     Darstellung, irreduzibel nur bei j = ½;
   - bei ganzzahligem j kommutieren sie; der Raum zerfällt in eindimensionale Charaktere.
2. **Das Extremdublett |j, ±j⟩ ist bei jedem j invariant.** Invariant sind aber auch alle Paare |j, ±m⟩; zählt man sie alle,
   entsteht das SU(2)-Gewicht 2j + 1.
3. **Regeln und γ:**

   | Regel M | Regel T | γ_M | γ_T | γ_L | β_sym |
   |---|---|---|---|---|---|
   | invariantes Extremdublett je j (Gewicht 2) | irreduzibel (j = ½) | 0,237533 | 0,127384 | **1,864700** | **0,54941** |
   | invariantes Extremdublett je j | antikommutierend (Kramers) | 0,237533 | 0,189138 | 1,2559 | 0,337 |
   | alle invarianten Paare (2j + 1) | irreduzibel | 0,274067 | 0,127384 | 2,1515 | 0,604 |
   | irreduzibel | irreduzibel | 0,127384 | 0,127384 | 1 | 0 |

   Die Bedingung „irreduzibel“ für T und „invariantes Extremdublett“ für M geben genau das Paar aus H98.

## Lesart
- **T:** Eine Punktierung zählt im Tachyon-Frame nur, wenn die Frame-Abbildungen auf ihr irreduzibel wirken. Dann trägt sie
  kein Merkmal, das die Frame-Abbildungen nicht sehen (Schur: Kommutant = Skalare). Das ist genau j = ½ mit Gewicht 2. Es
  ersetzt die Energiebedingung P2, die in r10.2 gescheitert ist, durch eine gruppentheoretische Bedingung, und es ist eine
  eingeschränkte Auslesung im Sinn von r10.4(c). Die Kramers-Regel unterscheidet sich davon: Bei j = 3/2, 5/2, …
  antikommutieren die Abbildungen, wirken aber reduzibel.
- **M:** Eine Punktierung zählt mit ihrem unter den Frame-Abbildungen invarianten Extremdublett; „extremal“ bleibt P1
  (Sättigung).
- **Bezug zu I1:** Ein Chan–Paton-Endpunkt trägt die Fundamentaldarstellung, also genau das irreduzible Dublett. Die neue
  Bedingung gibt dieselbe T-Regel wie die Stringlesart, aber ohne die Annahme „T = String-Sektor“ (Guard 1 von CT-004). Sie
  könnte Guard 1 ersetzen; das Register wird hier nicht geändert.

## Annahmen und Grenzen
- **(A) ist die eigentliche Lücke:** Warum die Frame-Abbildungen des Feld-Dubletts auf Horizont-Punktierungen wirken, ist
  nicht gezeigt.
- **Asymmetrie gesetzt:** Warum T Irreduzibilität verlangt und M nicht, ist eine Setzung. Eine mögliche Lesart: T ist über
  eine Frame-Abbildung erreicht, also darf eine T-Auslesung kein Merkmal tragen, das diese Abbildungen nicht sehen; M ist
  der Ruhframe und liest alle Stufen.
- **M braucht P1:** Ohne „extremal“ folgt das SU(2)-Gewicht (γ_L = 2,15, außerhalb aller Fenster).
- **Nicht blind, kein Test:** Ein Test bräuchte eine Folgerung aus (A) und der Irreduzibilitätsbedingung, die nicht γ_L ist.
- H104 bleibt bestehen: Mit anderem Flächenspektrum gäbe dieselbe Bedingung andere Werte.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
