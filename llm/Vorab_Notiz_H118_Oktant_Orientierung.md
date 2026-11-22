# Vorab-Notiz H118: Legt der Bestand die Orientierung des Oktanten fest?

**Stand:** 22. November 2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Für einen Teil der Kandidaten (K1–K4) steht
die Einordnung aus r16.7, H115 und H116 analytisch fest; offen sind die Einordnung von K5–K9 und die Frage, ob einer davon eine
dokumentierte Abbildung auf den Oktanten hat. Auftrag des Autors vom 22.11.2026: „OP3: H118 vorbereiten“ (nächster Schritt nach
H116/H117: eine native, vorzeichenempfindliche Größe für die Wahl des Rückwegs).

## Worum es geht
Nach r16.7 sind die drei Auslesezustände Eigenzustände der drei Frame-Abbildungen R = σ_z, T = σ_x, J_B = σ_y auf der invarianten
Kugel χ. Es gibt genau acht solche Tripel, alle mit Überlappung ½, K = 2/3 und Bargmann-Phase ±π/4; die Frame-Abbildungen teilen sie
in zwei Bahnen zu vier, je eine pro Vorzeichen. „Das Vorzeichen der Phase“ steht dort ausdrücklich als offen. H116 zeigt, dass Beträge
und Endpunkte es nicht festlegen; H117 verlegt die Wahl in ein zweites Fenster, ohne eine Größe zu finden, die sie trifft.

Rückwärts gefragt (AGENTS.md, „Suchrichtung prüfen“): Eine Größe, die die Bahn auswählt, muss unter dem orientierungsumkehrenden
Θ = iσ_y K (Antipode, Zeitumkehr des Dubletts χ) ungerade sein und darf zugleich unter R, T, J_B nicht in die andere Bahn führen.
Gerade Größen (Beträge, Ränge, reelle Projektionen, boolesche Zertifikate) können die Bahn nicht wählen.

## Vorwissen geprüft
- r16.7 (`sources/research/parts/v4100-post-release-layers.tex`, Theoremlet v4.10.0-r16.7): acht Tripel, zwei Bahnen, Vorzeichen offen.
- r16.9 (ebenda): Dreierzyklus durch Zeitverschiebung um ein Drittel der Periode, U = diag(ω̄₃, 1, ω₃); Gewichte p_k aus den
  Leptonmassen bestimmt (bei Vorgabe φ = 2/3), also für eine Vorzeichenfrage zirkulär, sobald die Gewichte eingehen.
- `notes/research/op3_helicity_axis_2026_11_15/README.md`, Nachtrag: drei Feldvorzeichen sign Re s, sign Im s = sign E·B,
  Helizitätsvorzeichen; jede Frame-Abbildung kippt zwei davon (Kleinsche Vierergruppe).
- `notes/research/op3_topology_core_2026_11_16/README.md`: Antipode kehrt die Bargmann-Phase um; fixpunktfrei auf χ ist nur
  Θ = iσ_y K (antiunitär), eine zusätzliche Umkehrwalze neben r02/r04.
- `notes/research/op3_correction_term_2026_11_16/README.md`: Der Berry-Fluss ist pseudoskalar (Vorzeichenwechsel unter Konjugation).
- `notes/research/op3_repair_connected_family_2026_11_10.md`: vorzeichenbehaftetes Residuum Im ζ_sh im historischen
  Antiphasenkorridor; mitgeführtes Phasenregister als Vergleich, native Vorbereitung offen.
- `llm/Ergebnis_H115_Kompensator_Oktant.md`, `llm/Ergebnis_H116_Spinorband_Phasenquelle.md`, `llm/Ergebnis_H117_Zwei_Umlaeufe.md`.
- Einordnung: These T2/T5 und OP3 im Gesamtbild (`wiki/Gesamtbild.md`). Zurückgestellte Ideen I1–I5: kein Auslöser betrifft die
  Orientierung direkt.

## Kandidatenliste (vor der Auswertung festgelegt, vollständig)
| | Kandidat | Quelle |
|---|---|---|
| K1 | Frame-Abbildungen R, T, J_B | r16.7 |
| K2 | HC-Kompensator C = (I + J)/2 und die reelle Halbierung C_n | H115, `generation-coupling.tex` |
| K3 | Übergangswahrscheinlichkeiten, Gram-Ränge, Zertifikat L_loc (19Q), Θ/R-Closure, Teichmüller-Verzerrung | §19, 19Q, H116 |
| K4 | Umkehrwalze Θ = iσ_y K selbst | r02.2/r02.3, Topologie-Notiz |
| K5 | Richtung der Zeitverschiebung U gegenüber U⁻¹ (r16.9), ohne die Gewichte p_k | r16.9 |
| K6 | Polwahl der drei Feldvorzeichen: Materie statt Tachyon (sign Re s), sign E·B, Helizität (selbstdual statt antiselbstdual) | r16.3, Helizitäts-Notiz |
| K7 | Index bzw. Maske des doppelten Hilbert-Shifts | `07_qam_infrastructure.tex` |
| K8 | mitgeführtes Phasenregister | `op3_repair_connected_family_2026_11_10.md` |
| K9 | vorzeichenbehaftetes Residuum Im ζ_sh der HC-Mikro-Lock-Diagnose | ebenda, `15_hc_repair_and_transport.tex` |

## Aufbau
Wolfram Language (exakt), Skript `llm/h118_octant_orientation.wl`, Ausgabe `llm/h118_octant_orientation.txt`.
1. Die sechs Pole auf χ, die acht Tripel, ihre Bargmann-Phasen für beide Umlaufrichtungen.
2. Wirkung von R, T, J_B und Θ auf die Tripel (Bahnzugehörigkeit).
3. Für K6: Formel für die Phase eines Tripels als Funktion der drei Polvorzeichen und der Umlaufrichtung; Prüfung, ob die Polwahl
   „Materie, E·B > 0, selbstdual“ eine Bahn eindeutig festlegt.
4. Für K5: Vorzeichen von arg⟨ψ|Uψ⟩ unter U ↦ U⁻¹ und unter Θ, ohne Gewichte aus Massen.
5. K1–K4, K7–K9 werden nach Quellenlage eingeordnet; wo eine Formel vorliegt, wird ihre Parität unter Θ exakt geprüft.

Kein HDL/MMA-Vergleich: Die Schlussfolgerung hängt an einer algebraischen Parität, nicht an einem endlichen Such- oder Guard-Ablauf.
Eine Quantenschaltung ist nicht vorgegeben.

## Einordnung je Kandidat
Jeder Kandidat kommt in genau eine Klasse:
- **(G) gerade:** unter Θ unverändert oder hält jede Bahn fest; kann die Bahn nicht wählen.
- **(U) ungerade, nativ:** wechselt unter Θ das Vorzeichen, ist im Bestand vor dem 22.11.2026 ohne Leptondaten definiert und hat eine
  dokumentierte Abbildung auf den Umlauf des Oktanten.
- **(Z) ungerade, aber zirkulär:** wie (U), aber nur über Leptondaten oder über eine nachträglich gesetzte Zuordnung definiert.
- **(O) ungerade, ohne Abbildung:** ungerade, aber ohne dokumentierte Abbildung auf den Oktanten.
- **(S) Schalter:** vertauscht die Bahnen, wählt aber keine aus.

## Hypothesen und Kriterien
- **H118a (exakt):** Die Bargmann-Phase jedes der acht Tripel ist τ · ε · π/4 mit τ = ±1 für die Umlaufrichtung und ε = Produkt der
  drei Polvorzeichen (bei fester Zuordnung der Achsen); R, T, J_B erhalten ε, Θ kehrt ε um. Kriterium: alle 8 × 2 Fälle exakt, kein
  Rest ungleich null.
- **H118b (Entscheidung):** Mindestens ein Kandidat fällt in Klasse (U). Dann legt der Bestand die Orientierung fest, und das
  Vorzeichen wird für diesen Kandidaten ausgerechnet und berichtet. Fällt keiner in (U), ist H118b widerlegt; berichtet werden dann
  die Kandidaten in (Z) und (O) als die Stellen, an denen eine native Wahl ansetzen müsste.
- **Kontrolle:** Θ² = −1 auf χ; R, T, J_B bilden die acht Tripel auf Tripel ab; die Phasen des umgekehrten Umlaufs sind konjugiert
  (wie H116). Numerische Gegenprobe an 200 zufälligen Unitären nur als Plausibilität, Schranke 10⁻¹².

## Folge, vorab festgelegt
- H118b bestätigt: Die Orientierung des Oktantschritts ist im Bestand bedingt festgelegt; offen bleibt, ob der gefundene Kandidat
  physikalisch dieselbe Rolle spielt wie der Rückweg im Bandmodell (H117). Kein Vergleich mit Leptondaten; die Restbiegung (OP3) und
  die Kerngröße (OP1) bleiben unberührt.
- H118b widerlegt: Das Vorzeichen bleibt eine zusätzliche Wahl wie die Überlappung ½; der Befund gehört als Grenze in die nächste Runde.
- In beiden Fällen bleibt OP3 offen.
