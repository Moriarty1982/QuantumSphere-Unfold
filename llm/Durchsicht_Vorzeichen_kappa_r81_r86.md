# Durchsicht: Welche Ergebnisse aus r81–r86 hängen am Vorzeichen der Gravitationswirkung?

**6. November 2026. Erkundung (Durchsicht ohne Kriterium).** Anlass: H90 und die Autorentscheidung, W1 auf S_grav = −(1/2κ)∫e R zu korrigieren (`Bestandsaufnahme_Wirkungsansaetze.md`, Eintrag 6.11.). Geprüft wurden die Ergebnis- und Erkundungsnotizen H69–H89 und die zugehörigen Skripte. Gesucht wurde nach κ, Einstein, Graviton, Newton, Torsion, 3/16 und dem Vier-Fermionen-Term.

## Betroffen (Vorzeichen kehrt sich um, Betrag und Form bleiben)
| Stelle | Bisher (Wirkung wie notiert) | Nach der Korrektur |
|---|---|---|
| r81.1(b), H88, k173, k203: Elimination der Torsion | L_eff = −(3/16)κ j·j | L_eff = +(3/16)κ j·j; K_cab = +(κ/4) ε_cabd j^d |
| Weyl-Gleichung von W1 | … − (3κ/8) j_a σ̄^a ψ | … + (3κ/8) j_a σ̄^a ψ |
| H89a: T^(4f) | +(3κ/16) j² g | −(3κ/16) j² g (Λ-Form, negativ) |
| H89b: homogener Zustand | ρ = p = +(3κ/16) n² | ρ = p = −(3κ/16) n² < 0 |
| r86.4: Korrektur zur W1-Notiz | „ρ ∝ −κn² trifft nicht zu“ | die ursprüngliche Lesart „ρ ∝ −κn²“ der W1-Notiz stimmt; r86.4 nimmt sie zu Unrecht zurück |
| r82.4 (`Erkundung_Torsion_Kondensat.md`, k190): Paarkanal | anziehend, H_int ⊃ −(3/4)κ Φ†Φ, Kondensat an der Planck-Skala, ν^c-Majorana mit M_R ~ M_P, See-saw m_ν ~ 10⁻⁶ eV | **abstoßend**, H_int ⊃ +(3/4)κ Φ†Φ; über diesen Kanal kein Kondensat, die ν^c-Majorana- und See-saw-Lesart fällt |

## Nicht betroffen
- **H69** (M–T-Paar im flachen Raum): Nettostrom und Nettoenergie-Impuls sind null. G = 0 und Torsion 0 sind für beide Vorzeichen konsistent.
- **H70–H73** (Versatz, Massenpartner, Vakuumterm aus Tachyonmoden, w = −β²/3): Diese Rechnungen betreffen nur die Quellenseite, nicht das Vorzeichen der Kopplung.
- **H74:** Direkte Kopplung, keine Gravitation.
- **H75** (k189): Gerechnet mit Newtonscher Anziehung, also schon mit dem physikalischen Vorzeichen. Das passt zur korrigierten W1.
- **H76** (k191): Rate ∝ κ⁴/M_P⁴ mit dem gewöhnlichen Graviton-Propagator. Das Vorzeichen von κ geht nicht ein.
- **H77–H81, H84–H86:** keine Gravitationskopplung.
- **H82, H83:** Dort werden Gewichte und Phasen des Einstein–Cartan-Terms unter den Frame-Abbildungen verglichen. Ein gemeinsames Vorzeichen des Terms ändert das Verhältnis zwischen Materie- und Bildanteil nicht.
- **H48:** Hehl–Datta-Vorzeichen aus der Literatur, nicht aus W1.
- **r81:** „W1 erzeugt keinen Vakuumterm“ bleibt richtig.

## Folge für die zurückgestellten Ideen
I3 (Λ als Folge der Dunkle-Materie-Rechnung): Der Vier-Fermionen-Anteil hat Λ-Form und ist nach der Korrektur negativ, T^(4f) = −(3κ/16) j² g. Seine Höhe hängt an j², ist also nicht konstant. Für den ganzen Tensor eines homogenen Zustands gilt p = ρ < 0 (steif, negativ), kein Λ. Dem Autor als Berührung von I3 genannt.

## Nächster Schritt
Runde v4.10.0-r01: H90, die Autorentscheidung und die Korrekturen der obigen Tabelle (append-only, frühere Runden bleiben wörtlich).
