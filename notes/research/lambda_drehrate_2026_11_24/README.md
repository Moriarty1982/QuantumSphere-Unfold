# Λ und die Drehrate der Scheibe: lässt sich das verknüpfen? (Erkundung, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Eine Verknüpfung ist möglich, aber nur in einer Form, und die legt Λ nicht fest: Positives Λ ist genau die
Drehrate der euklidischen Zeit (Λ = 3Ω², Periode 2π/Ω, Gibbons–Hawking), und in der Scheibe entspricht ihm Λ/3 ↔ Ω² − ω₀², positiv genau
wenn die Drehung schneller ist als die Eigenfrequenz des Strings. Als räumliche Wirbelung ist die Verknüpfung ausgeschlossen (Gödel gibt
Λ = −ω², CMB-Schranke, Verdünnung mit a⁻⁴). Die Skala bleibt in jedem Fall frei: Sie wandert von Λ zu Ω oder zur Stringlänge ℓ. Ohne eine
unabhängige Festlegung von Ω oder ℓ ist Λ ∝ Ω² eine Umbenennung.

Auftrag des Autors (Chat 24.11.2026): „hast du nicht sowas gesagt wie, dass die kosmologische konstante evtl. etwas mit der
winkelgeschwindigkeit der drehung zu tun haben könnte?“, „prüfe erstmal ob man überhaupt verknüpfen kann“, ergänzt: „es könnte auch eine
kombination aus umlaufrichtung der scheibe, drehgeschwindigkeit und eigenfrequenz und/oder länge des sektorstrings sein.“
**Erkundung, nicht blind** (Ergebnisse Standardphysik oder vorher analytisch klar). Keine Vorab-Notiz, keine H-Nummer (**H125 bleibt frei**),
keine Runde. Vergeben: Skript **k251**.

Werkzeuge: Wolfram Language (MCP-Kernel, exakt) für Gödel-Krümmung, Vorzeichen-Kalibrierung an de Sitter, euklidische Periode, Spintessence,
Drehsystem und Zahlen. Qiskit nicht eingesetzt: kein Zustands- oder Messproblem. Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Ablauf).

## Vorwissen geprüft
- **T9** (`wiki/Gesamtbild.md`, Federmodell, Λ = 0 im Photon-Frame, Dunkle Energie als Frame-Versatz): großteils nicht tragfähig; r50/r51:
  ein Medium aus dem Photon-Frame stützt T9 nicht. Ein Λ aus einem mitrotierenden Bezugssystem wäre derselbe Fehlertyp (Abschnitt 3).
- **r56** (`notes/research/v4_10_0_r56/`): In der Klasse 𝒦 ist Λ Eingabe; r56.3: alle festgelegten Zahlen dimensionslos und von Ordnung
  eins, Λℓ_P² = 2,85·10⁻¹²²; r56.4: Ω_M = β² tauscht Λ gegen die Epoche, Λ = 3(1 − β²)H*².
- **r57/H124**: Attraktor εβ²/3 der Kaskade, „warum heute“ offen; Idee I7.
- **r06** (Dorau–Much): Modulargruppe = Boost, KMS bei 2π/κ, Λ freie Integrationskonstante. Das ist die Rindler-Fassung von Abschnitt 2.
- **Scheibenbild** (`licht_vermittler_zeit_2026_11_24/`, k247–k249): Zeit als Restdrehung, Schwelle ω_c = 2√(K/I) (k248), Drehsinn überall
  gesetzt; Holonomie k246 (`holonomie_restdrehung_2026_11_24/`, Randzyklus −π). k250 (Drehsinn aus Lichtgewicht, anderer Faden): a − b wählt
  den Drehsinn nicht.
- Repo nach Gödel, Raychaudhuri (nur r06), Gibbons–Hawking, Spintessence durchsucht: keine Vorbefunde zur Verknüpfung Λ ↔ Drehrate.
- Zurückgestellte Ideen: I7 (Attraktor-Weg) berührt, aber kein Auslöser getroffen; I1 nicht berührt.

**Suchrichtung:** Rückwärts. Ziel „Λ = F(s, Ω, ω₀, ℓ) mit Λ > 0, zeitlich konstant, Skala nicht frei“. Notwendige Bedingungen:
(N1) Vorzeichen positiv, (N2) w = −1, also keine Verdünnung, (N3) mit Beobachtungen verträglich, (N4) eine unabhängige Skala. Jede Lesart wird
an N1–N4 geprüft.

## 1. Dimension
[Λc²] = 1/s², [Ω²] = 1/s². Λ ∝ Ω²/c² ist dimensional die einfachste Form. Zahlen (k251): Λ = 3Ω²/c² verlangt Ω = 1,82·10⁻¹⁸ s⁻¹ = 0,83 H₀;
Λ = Ω²/c² verlangt 1,44 H₀. Die Drehrate müsste also eine Umdrehung pro Hubble-Zeit sein. Gegen die Planck-Frequenz fehlen 10⁶¹ (ln = 140,5,
die Hälfte von r56.3). Die Dimension erlaubt die Verknüpfung, liefert aber keine Zahl.

## 2. Lesarten der Drehung
| Lesart | Ergebnis | N1–N4 |
|---|---|---|
| **(a) Räumliche Wirbelung, statisch (Gödel)** | Einstein mit Staub: Λ = −ω², 8πGρ = 2ω² (exakt, Vorzeichen an de Sitter kalibriert) | N1 verfehlt |
| **(b) Räumliche Wirbelung, expandierend** | Raychaudhuri: +2ω² wirkt beschleunigend wie Λ, aber ω ∝ a⁻² (Drehimpuls), also 2ω² ∝ a⁻⁴ wie Strahlung | N2 verfehlt |
| (b′) Beobachtung | CMB: (ω/H)₀ < 4,7·10⁻¹¹ (Saadeh u. a. 2016) → Λ_rot/Λ_obs < 2·10⁻²¹ | N3 verfehlt |
| **(c) Drehung im inneren Raum (Phase eines Feldes, Spintessence)** | w = (K − V)/(K + V); w = −1 genau für Ω = 0 und ḟ = 0. Kreisbahn in V = m²f²/2: w = 0 (Staub). Ladung f²Ωa³ erhalten → Drehenergie ∝ a⁻³ | N2 verfehlt: die Drehenergie selbst ist nie Λ |
| **(d) Euklidische Zeit als Drehwinkel (de Sitter)** | statischer Patch: Regularität am Horizont erzwingt Periode 2π/κ, κ = H = √(Λ/3), also **Λ = 3Ω²** mit Ω = Drehrate der euklidischen Zeit. AdS (Λ < 0): kein Horizont, keine erzwungene Periode | N1–N3 erfüllt, N4 verfehlt |

Lesart (d) ist die einzige, die das positive Vorzeichen von selbst liefert: Kompakte, geschlossene Drehung der Zeit gehört zu Λ > 0, die
Gödel-Wirbelung zu Λ < 0. Sie passt zum Bild „Zeit = aufgelaufene Drehung“ und ist im Repo schon als r06 (KMS bei 2π/κ) vorhanden. Aber sie
ist eine Identität der de-Sitter-Geometrie: Ω ist hier über Λ definiert, nicht umgekehrt. Die räumliche Beobachtungsschranke (b′) trifft (d)
nicht, weil keine Materie räumlich rotiert.

**Achtung Frames (r51, r81):** Der Übergang zur euklidischen Zeit ist eine Wick-Drehung t ↦ −it. Sie erinnert an die Tachyon-Abbildung
z ↦ iz, ist aber nicht als dieselbe Abbildung nachgewiesen. Keine Gleichsetzung ohne erklärte Abbildung.

## 3. Kombination aus Umlaufsinn, Drehrate, Eigenfrequenz und Stringlänge (Ergänzung des Autors)
Ansatz: Λ = F(s, Ω, ω₀, ℓ, c). Buckingham: Λ = ℓ⁻²·f(Ωℓ/c, ω₀ℓ/c, s). Für einen relativistischen Sektorstring ist ω₀ = πc/ℓ, also sind ω₀
und ℓ eine Größe. Übrig bleiben **eine** Skala (ℓ), **ein** Verhältnis r = Ω/ω₀ und das Vorzeichen s.

- **Umlaufsinn s:** Λ ist skalar, gerade unter Raumspiegelung und Zeitumkehr. Im Drehsystem steht s nur als s² = 1 (k251). Ein Term linear
  in sΩ braucht einen zweiten ungeraden Faktor; das Produkt τε aus H123 wäre ein solcher, ein Term τε·Ω·X ist aber nirgends hergeleitet.
  Der Drehsinn kann Λ nicht wählen, höchstens in einem Produkt zweier Orientierungen auftreten.
- **Differenz Ω² − ω₀² (der beste Fund dieser Erkundung):** Im mitrotierenden System gilt für die radiale Mode r̈ = (Ω² − ω₀²) r. Im
  statischen de-Sitter-Patch gilt r̈ = (Λ/3) r. Die Form stimmt überein: **Λ/3 ↔ Ω² − ω₀²**, positiv genau für Ω > ω₀, also wenn die Drehung
  die Eigenfrequenz überholt (überkritisch, die radiale Mode läuft auseinander). Λ < 0 (AdS) entspricht der stabilen Schwingung. Damit liefert
  die Kombination das Vorzeichen, das Gödel verfehlt.
  Grenzen: (i) Der Fliehkraftterm gehört zum mitrotierenden System, Λ ist frame-unabhängig; die Gleichsetzung ist ein Formvergleich, keine
  Herleitung, und hätte denselben Fehlertyp wie T9 (Frame-Versatz). (ii) Die Bedingung Ω > ω₀ ist nicht die Schwelle aus k248 (ω_c = 2√(K/I));
  wie beide zusammenhängen, ist offen.
- **Stringlänge ℓ als Skala:** Mit Ω = rω₀ und ω₀ = πc/ℓ: Λ = 3π²(r² − 1)/ℓ². Für r² − 1 ≈ 1 braucht man ℓ = 5,2·10²⁶ m = 3,8 Hubble-Radien.
  Für ℓ = Planck-Länge braucht man r² − 1 = 10⁻¹²³. Die Feinabstimmung wandert in das Verhältnis Ω/ω₀ statt in Λ.
- **Schwebung:** (Ω − ω₀)² ist immer ≥ 0 und wählt kein Vorzeichen. Nahe der Resonanz Ω = ω₀ + δ ist Ω² − ω₀² ≈ 2ω₀δ; ein kleines Λ hieße dann
  Fast-Resonanz, also wieder eine Feinabstimmung, jetzt in δ.

Fazit zur Kombination: Sie bringt Form und Vorzeichen, aber keine neue Skala. Im Bestand ist ℓ dimensionslos (Längenmodell vom 12.11.: nur
Verhältnisse ℓ_i), und r56.3 sagt, dass 𝒦 keine Skala enthält.

## 4. Urteil
| Frage | Antwort |
|---|---|
| Lässt sich Λ mit der Drehrate verknüpfen? | **Ja, aber nur konventionell**: Λ = 3Ω² mit Ω als Drehrate der euklidischen Zeit, in der Scheibe Λ/3 ↔ Ω² − ω₀² |
| Als räumliche Drehung? | **Ausgeschlossen**: falsches Vorzeichen (Gödel), Verdünnung a⁻⁴, CMB-Schranke 10⁻²¹ |
| Als Drehenergie eines inneren Feldes? | **Ausgeschlossen**: Drehenergie hat w > −1 und verdünnt sich |
| Liefert der Umlaufsinn etwas? | Nein, nur als Quadrat oder als Produkt zweier Orientierungen (τε), dort nicht hergeleitet |
| Ist Λ damit festgelegt? | **Nein**: die Skala wandert zu Ω oder ℓ; ohne unabhängige Festlegung ist es Umbenennung, wie bei r56.4 (Λ gegen Epoche) |

**Was nötig wäre, um Ω unabhängig festzulegen:** (1) eine Zeitmessung der Scheibenperiode, die nicht über H oder Λ läuft (in der Kosmologie
nicht in Sicht); (2) eine Herleitung von ℓ in physikalischen Einheiten aus einer anderen Messgröße (etwa einer Teilchenmasse) samt dem
Verhältnis r aus der Holonomie (k246); mit Teilchenskalen ergibt sich aber Λ um viele Zehnerpotenzen zu groß, außer r² − 1 ist winzig;
(3) ein dynamischer Grund, warum Ω ≈ H gerade heute gilt. Das ist die Koinzidenzfrage von r57 in neuer Form.

## Nachträglich bemerkt (nicht tragend)
r56.4 gibt Λ = 3(1 − β²)H*². Mit β² = 0,3018466 ist 3(1 − β²) = 2,09446, nahe 2π/3 = 2,09440, also β² ≈ 1 − 2π/9 (Abstand 2,2·10⁻⁵). Das sähe
nach „ein Drittel Umdrehung“ aus, ist aber ohne Mechanismus Zahlenspielerei; β² ist anders hergeleitet ((γ_L − 1)/(γ_L + 1)), und die
Messunsicherheit von Ω_M (≈ 0,007) trennt die beiden Werte nicht. Nicht als Befund führen.

## Grenzen
- Erkundung, nicht blind; Literaturwerte (Gödel 1949, Gibbons–Hawking 1977, Saadeh u. a. 2016, Boyle–Caldwell–Kamionkowski 2002) aus Vorwissen,
  hier nur die Formeln nachgerechnet; die CMB-Schranke nicht neu geprüft.
- Die Gleichsetzung Λ/3 ↔ Ω² − ω₀² ist ein Formvergleich zweier radialer Bewegungsgleichungen, keine Herleitung.
- OP5 offen, H96 offen, r56 unverändert (No-go für 𝒦 gilt weiter); kein Guard berührt.

## Mögliche nächste Schritte (nur auf Entscheidung)
- Prüfen, ob die Schwelle k248 und die Bedingung Ω > ω₀ dieselbe Grenze sind (Drei-Mulden-Modell im mitrotierenden System).
- Ob das Verhältnis r = Ω/ω₀ aus der Holonomie (k246) folgt; nur dann wäre in Λ = 3π²(r² − 1)/ℓ² ein Faktor hergeleitet. Die Skala ℓ bliebe frei.

## Dateien
`k251_lambda_drehrate.wl` (Ausgabe `k251_out.txt`).
