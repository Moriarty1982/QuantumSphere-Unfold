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

## Nachtrag 15.11.2026: Brücke (A) über die Barbero-Verbindung? Nur teilweise
Auftrag des Autors: „weiter“. **Erkundung, nicht blind** (die Formeln sind Standard). Skript `barbero_doublet.py`, Ausgabe
`run/barbero_doublet_stdout.txt`.

**Suchrichtung:** Gesucht ist ein Grund, warum die Frame-Abbildungen des Feld-Dubletts auf Horizont-Punktierungen wirken.
Die Punktierungen tragen Spins der SU(2) der Ashtekar–Barbero-Verbindung A_γ = Γ + γK. Kandidat: Die Gravitation hat
dieselbe Zerlegung in selbst- und antiselbstduale Anteile wie das Maxwell-Feld (r05.2(c): Weyl-Krümmung =
gravito-elektrisch + i gravito-magnetisch). Vorwissen: Im Repo kommt die Zerlegung A_γ = c₊A₊ + c₋A₋ nicht vor;
`../op3_flux_two_thirds_2026_11_13.md` nennt γ als Holonomie-Phase bzw. topologischen Winkel.

**Ergebnisse**
1. Mit A± = Γ ± iK gilt exakt A_γ = c₊A₊ + c₋A₋, c± = (1 ∓ iγ)/2. **Reelles γ liegt auf dem Äquator** des Dubletts (A₊, A₋)
   (|c₊| = |c₋|), die selbst- bzw. antiselbstdualen Ashtekar-Variablen γ = ±i an den **Polen**: dieselbe Geometrie wie bei χ
   (reelle Felder auf dem Äquator, selbstduale an den Polen).
2. Wirken die Frame-Abbildungen auf (c₊, c₋) wie auf χ, dann auf γ als R: γ ↦ −1/γ, T: γ ↦ −γ, J_B: γ ↦ 1/γ.
3. **Keine bildet γ_M auf γ_T ab** (Bilder von γ_M: −4,21; −0,2375; 4,21; γ_T = 0,1274). Der Unterschied der Flächenquanten
   (r10.3) ist also kein Frame-Bild der Verbindung.
4. In γ-Sprache sind die sechs Pole von r16.7 die Werte γ = 0 bzw. ∞ (T-Achse), ±1 (J_B-Achse), ±i (R-Achse).

**Folgerung:** Die Barbero-Verbindung bietet eine natürliche Stelle, an der die Frame-Abbildungen auf die Gravitation wirken,
nämlich auf γ selbst. Das ist aber nicht die Brücke (A): (A) verlangt eine Wirkung auf die Spinzustände einer Punktierung
(exp(−iπJ_k)), nicht auf den Parameter γ. Und die Wirkung auf γ erzeugt den Frame-Unterschied γ_M/γ_T nicht. Das passt zur
Lesart der Erkundung oben: Der Unterschied liegt in der Zählung, nicht in einer Transformation von γ. (A) bleibt offen.

Nachträglich gesehen und nicht verwertet: Der Äquatorwinkel 2 arctan γ_M = 26,72° liegt nahe der Uhr-Toleranz
arctan ½ = 26,57° (v4.9.0-r12.2); das war nicht vorab gelistet.

## Nachtrag 15.11.2026: Brücke und Asymmetrie als Statistik von Penrose-Strängen
Auftrag des Autors: „Ja, prüfen“. **Erkundung, nicht blind.** Skript `strand_bundles.py`, Ausgabe
`run/strand_bundles_stdout.txt`.

**Vorwissen:** Penrose-Stränge kommen im Paper nicht vor (Volltextsuche nach Penrose und Binor ohne Treffer). T11
(`thm:string-lqg-duality`, v470/10) nennt den Kompensator-Sektor C = ½(1 + J) „symmetrisch, bosonisch – Stringtheorie“ und
A = ½(1 − J) „antisymmetrisch, fermionisch – LQG“. Gemeint ist dort die **J-Parität eines Objekts**, nicht die
Austauschsymmetrie vieler Stränge (so auch die Berichtigung zu CT-004: T11 ordnet nach J-Parität).

**Ergebnisse**
1. **Brücke (A) aus Bündeln.** Auf Sym^{2j}(ℂ²) ist σ_k^{⊗2j} bis auf eine Phase gleich exp(−iπJ_k) (geprüft für 2j = 1 bis 8,
   Abweichung höchstens 2·10⁻¹⁵). Ist eine Spin-j-Kante ein symmetrisiertes Bündel aus 2j elementaren Zweikomponenten-Strängen
   (Penrose) und ist der elementare Strang ein Quant des Dubletts χ, dann wirken die Frame-Abbildungen auf der Punktierung
   genau wie in (A) angenommen. (A) wird damit auf eine Zuordnung zurückgeführt: **elementarer Strang = Quant von χ**.
2. **Asymmetrie als Statistik.** Antisymmetrische Potenzen eines Dubletts: Λ¹ = Dublett (j = ½, Frame-Abbildungen
   irreduzibel), Λ² = Singulett (j = 0, keine Fläche), Λⁿ = 0 für n ≥ 3. Symmetrische Potenzen geben alle j. **Bosonisch
   gelesene Stränge geben die Spins von M, fermionisch gelesene genau j = ½, die Regel von T.** „Irreduzibel“, „einzelner
   Strang“ und „Pauli-Ausschluss auf dem Dublett“ sind dieselbe Bedingung; die Kramers-Regel (alle halbzahligen j) ist davon
   verschieden.
3. **Ausgerichtete Bündel.** |↑⟩^{⊗2j} und |↓⟩^{⊗2j} sind in Sym^{2j} genau |j, ±j⟩: Das Extremdublett von M (P1) sind die
   ausgerichteten, kohärenten Bündel.

**Abgleich mit den Guards von CT-004** (Register nicht geändert):

| Guard | Stringlesart (I1) | Strang-Lesart |
|---|---|---|
| T-GLEICH-STRING | nötig, ohne Stütze | nicht nötig |
| CHAN-PATON | Endpunkte in der Fundamentaldarstellung | ersetzt durch „elementarer Strang = Quant von χ“ |
| STATISTIK | T11 nennt den String-Sektor bosonisch, gezählt wird Spin ½ | T liest Stränge fermionisch (Austausch); T11 meint J-Parität, ein anderer Begriff, daher kein Widerspruch im Inhalt |
| SPEKTRUM | Sonderstellung hängt am Spektrum (H104) | unverändert |

**Neue Setzungen statt der alten:** (S1) elementarer Strang = Quant von χ; (S2) T liest Stränge fermionisch, M bosonisch;
(S3) M zählt nur ausgerichtete Bündel (P1). Für (S2) gibt es eine Lesart, keinen Grund: Die Tachyon-Abbildung quadriert auf
dem Dublett zu −1 (r14.3(d)), das Vorzeichen eines Fermions unter voller Drehung.

**Grenzen:** Nicht blind; kein neuer Test. Die Statistik betrifft die Bündelung in einer Punktierung, nicht die Verteilung der
Punktierungen; die Zählgleichung und damit γ ändern sich nicht. OP1 bleibt offen.
