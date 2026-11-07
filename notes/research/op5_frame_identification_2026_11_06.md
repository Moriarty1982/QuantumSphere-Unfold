# OP5-Neuaufbau: Referenzzustand, Feldrapidität und β_sym

**6. November 2026. Quellenrekonstruktion und nicht blinde algebraische Einordnung, kein neuer Test.** Basis `918305e`. Selbstprüfung durch Codex; spätere Quellen korrigieren hier die zunächst anhand von r17 allein formulierte offene Zuordnung. Keine neue externe Literaturprüfung oder numerische Evidenz.

## 1. Ergebnis

**Die Referenzbenennung ist im Projekt bereits korrigiert; die physikalische Identifikation bleibt unvollständig.** r24 trennt ausdrücklich R (reiner Referenzzustand) und P (lichtartiger Zustand im Register). Der endliche Faktor γ_L vergleicht innerhalb dieser Lesart M mit R, nicht M mit P. Eine weitere Rechnung über einen endlichen Boost „zum Photon“ würde diese Korrektur wieder übergehen.

r17 gibt eine algebraische Parametrisierung der Register-Eigenwerte durch eine Feldrapidität an. Die Wahl, gerade den projektweiten γ_L beziehungsweise β_sym auf einen bestimmten physikalischen Feldzustand anzuwenden, folgt daraus nicht. r61 hält den konsistent bezeichneten M-Wert weiterhin als Eingabe und OP1 als offen fest. Die Zähl-Lesart r63–r68 ergänzt benannte Annahmen, keine unabhängige allgemeine Herleitung des Werts.

## 2. Quellen und Vorwissen

- `notes/research/v4_9_0_r17_r19/rounds/v490_r17_round.tex`, r17.1–r17.3: Feldrapidität, Eigenwerte, Skalenkoordinate und unterschiedliche Bezugspunkte.
- Gleicher Ordner, `v490_r18_round.tex` und `v490_r19_round.tex`: Trennung von additiver Rapidität/Skalentransport und zustandsabhängigen Auslesegrößen; keine Gleichsetzung der Transformationsgesetze.
- `sources/research/parts/v490-post-release-layers.tex`, `subsec:v490-r22-frame-rule`, `subsec:v490-r24-corrections`, `subsec:v490-r24-convention`: Konvention F und Korrektur des alten Photon-Bezugs zu R.
- `notes/research/v4_10_0_r61/llm/Pruefung_OP_Frames.md`: reine Hopf-Konfiguration und gemischter Materiezustand nicht gleichsetzen; β-Herkunft offen.
- `notes/research/v4_10_0_r63_r64/README.md`, r67/r68, sowie `notes/research/predictions/Vorab_Notiz_H96_Omega_M_beta2.md`: spätere Zählannahmen, Zuordnung von β² zum Materieanteil und ihre Grenzen.
- `sources/research/parts/v410-state-mediator-synthesis.tex`: voller lokaler Feldträger und reduzierte Auslesungen bleiben verschiedene Informationsstände.

Die Prüfung berührt T1, T6 und T9. Die zurückgestellte Idee I1 wird durch den Bezug γ_BI/γ_string ihrem Auslöser 3 nach berührt: String-/LQG-Verbindung bleibt ein möglicher separat zu begründender Ausweg, wird hier aber nicht als Herleitung verwendet oder wieder aufgenommen. I3 ist durch den kosmologischen Bezug berührt, seine geprüften Formen sind schon gescheitert. Keine neue Skala oder Kondensatannahme wird eingeführt.

## 3. Drei Parameter mit verschiedenen Aufgaben

| Größe | Definition beziehungsweise Verwendung | Reichweite |
|---|---|---|
| η_f | feld-/beobachterbezogener Parameter der beschriebenen Boostfamilie gegenüber einem Bezug mit E parallel B | nicht automatisch universeller Frame-Versatz; nicht-nulles Feld und geeignete Vergleichsfamilie vorausgesetzt |
| σ | Koordinate einer skalierten Familie X(σ) = exp(kσ)X(0) | das additive Transportgesetz darf nicht mit einem beliebigen Lorentzfaktor multiplizierend identifiziert werden |
| η_sym, β_sym | projektweiter Versatz mit β_sym = tanh η_sym und γ_L = cosh(2η_sym) in der verwendeten Lesart | Zahl und physikalische Zuordnung benötigen die ausdrücklich benannten zusätzlichen Voraussetzungen |

Eine algebraisch passende Parametrisierung ist kein Nachweis, dass ein bestimmtes physikalisches Feld gerade η_f = η_sym besitzt. r03 hatte diese konkrete Feldidentifikation ausdrücklich offen gelassen. Die spätere Konvention ordnet die Lesarten; sie ersetzt den unabhängigen Nachweis eines realisierten Zustands nicht.

## 4. R und P sind keine zwei Namen desselben Registerzustands

| Zustand in der r24-Lesart | Registerlänge V = |b| | Eigenwerte λ₊, λ₋ | Bedeutung |
|---|---|---|---|
| R | 1 | 1, 0 | reiner Referenzzustand; Nullpunkt der alten Skalenlinie |
| M bei gewähltem γ_L | 1/γ_L | (1+1/γ_L)/2, (1−1/γ_L)/2 | gemischter Zustand der gewählten Ausleseparametrisierung |
| P | 0 | 1/2, 1/2 | Register eines nichtverschwindenden nullen elektromagnetischen Felds |

Im beschriebenen Zugang von nicht-nullartigen Feldern zu V → 0 wächst η_f unbegrenzt. Das macht ein bereits nulles Feld nicht zu einem massiven Beobachter in einem eigenen Ruhesystem; ein solches Ruhesystem wird hier nicht konstruiert. Die Grenzparametrisierung darf nicht als endliche physische Beobachterfahrt zu einem Photon interpretiert werden.

r24 sagt ausdrücklich: Das frühere „Λ = 0 im Photon-Frame“ beziehungsweise das Verschwinden des angesetzten Frame-Terms betrifft in dieser Lesart R. Am P-Zustand hat der verwendete β²-Parameter den Grenzwert 1. Damit fällt die Identifikation „neutrale Referenz = Photon = verschwindender vollständiger Vakuumterm“ als Schlusskette auseinander. Auch in R bleibt das Verschwinden des angesetzten Terms kein Vollständigkeitsnachweis für eine physikalische Wirkung.

## 5. Eigenwertverhältnis ist kein beliebiger Portanteil

Die bereits vorhandene r17-Parametrisierung lautet V = sech(2η_f) und λ± = (1±V)/2. Daher ist

q = λ₋/λ₊ = (1−V)/(1+V) = tanh²η_f.

Diese algebraische Beziehung ist eine Umrechnung des Registerkontrasts. Wird η_f mit η_sym identifiziert, ergibt sich q = β_sym². Der kleinere **normierte Eigenanteil** ist dagegen λ₋ = β_sym²/(1+β_sym²), nicht β_sym². r17 benennt diese Unterscheidung ausdrücklich.

Ein fest gewählter Kompensatorport liest p_C = tr(ρC) aus. Dieser Wert ist nur bei entsprechender Ausrichtung des Analysators mit einem der Eigenwerte gleich. Eine Eigenbasis-Auslesung und die Auslesung eines festgehaltenen σ_x-Ports sind nicht generell dieselbe Messfrage. Der Winkel des Registers zum Analysator muss mitgeführt werden.

Damit stehen mindestens drei unterschiedliche Größen nebeneinander: ein Eigenwertverhältnis, ein normierter Messportanteil und ein kosmologischer Dichteanteil. Die erste Formel beweist die Gleichheit dieser drei Größen nicht.

## 6. Was nach der gesamten bisherigen Rekonstruktion übrig bleibt

Die folgenden Abbildungen sind getrennt zu belegen:

`vollständiges Feld F → normiertes Register ρ → Eigenwertverhältnis q → Auswahl η_f = η_sym → Identifikation q = Ω_M(heute)`.

- Die ersten beiden Ausleseschritte sind lokal im erklärten Feldmodell bestimmt; Orientierung und absolute Skala gehen bei der Reduktion verloren.
- Die Wahl des symmetrischen Parameters ist keine Folge beliebiger Eingangsfelder.
- Die letzte Identifikation ist die bestehende kosmologische Hypothese, nicht ein Ergebnis der Registeralgebra.
- Eine absolute Λ-Skala kommt in dieser Kette weiterhin nicht vor.

H96 bleibt mit seinen registrierten Voraussetzungen und Kriterien offen. Seine Prüfung wäre eine empirische Prüfung dieser zusätzlichen Lesart; sie ist weder eine Kontrolle des abstrakten Schließungssatzes noch ein Ersatz für die ursprüngliche spektrale Auslöschung.

## 7. Konkrete nächste Verpflichtung

Für die kosmologische Lesart ist jetzt die engste Frage lokalisiert: **Welcher im Paper unabhängig definierte physikalische Zustand oder welche Grundgesamtheit wählt genau das Registerverhältnis q aus, und weshalb wird dieses Verhältnis als Ω_M gemessen?**

Zuerst die bestehenden r31-Flüsse und r63–r68-Zählgrößen daraufhin vergleichen, was ihre Nenner zählen. Kein neuer Wirkungsansatz und kein neuer Parameter sind dafür nötig. Falls der Text nur die Gleichsetzung vorgibt, ist das Ergebnis eine explizite zusätzliche Hypothese, keine dynamische oder algebraische Ableitung.

Keine bestehenden Theoreme, Runden oder Kriterien geändert; Guards unverändert. Dies ist keine neue nummerierte Forschungsschicht. W1/W2 bleibt eingefroren; H97 bleibt widerlegt.
