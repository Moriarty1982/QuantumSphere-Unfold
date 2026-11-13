# Erkundung: Woher kommt ein Fluss von 2/3 rad durch das Platzdreieck der geladenen Leptonen?

13. November 2026, spät. Autorenauftrag: „Fluss 2/3 rad suchen“. Erkundung, **nicht blind** (Zielwert bekannt), kein
Test. Keine H-Nummer. Skript `op3_flux_two_thirds_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_selection_principle_2026_11_13.md`: Nur ein Fluss erhält Koide; geladene Leptonen tragen Φ_e = 3θ_e = 0,666674,
  vom Oktanten (π/4) aus ΔΦ = 0,118724.
- v4.8.0-r11 (H1): δ = K/3 bzw. 2/9 widerlegt (Quarks, laufende Massen); gilt nur bei Polmassen (Kalibrierung).
- `op3_phase_source_search_2026_11_12.md`: native ρ-ungerade Größen (Chiralität, Assoziator, Q_J, Frame-Versatz) tragen
  keinen Betrag. η-Notiz: native Phasen nur Vielfache von π/6.
- Annahmenliste r08: native Zahlen γ_BI = 0,237533 (L1, Literatur, kalibriert), γ_string, γ_L, β_sym, Ω_M, η, ε, β₄.

## Ergebnis
1. **Mechanismen für einen nicht quantisierten Fluss.** (a) Berry-Phase: Als Qubit-Phase verlangt Φ_e einen Raumwinkel von
   4/3 sr (der Oktant hat π/2). (b) U(1)-Fluss mit stetigem Feld. (c) Selbstbezug Φ = K (Brannens δ = K/3): von H1 als
   allgemeines Gesetz widerlegt. Keiner ist im Companion angelegt.
2. **Fester Scan nativer Zahlen** (Liste im Skript vor dem Vergleich festgelegt): 11 Konstanten × 7 einfache Faktoren ×
   2 Ziele = 154 Versuche, Fenster 1 %. **Ein Treffer:** ΔΦ = γ_BI/2 = 0,118766 gegen 0,118724 (+0,036 %). Bei zufälligen
   Werten wären 0,34 Treffer zu erwarten; ein einzelner Treffer ist also nicht auffällig.
3. **Schärfe des Treffers.** Nimmt man θ aus der Beziehung, θ = (π/4 − γ_BI/2)/3 = 0,2222106, und legt ρ² über das genau
   bekannte m_e/m_μ fest, folgen ρ² = 0,500014, K = 0,666676 und **m_τ = 1777,13 MeV** (PDG 1776,93 ± 0,09: **+2,3σ**).
   Exaktes Koide mit m_e, m_μ gibt dagegen 1776,97 MeV. Die Beziehung steht also bereits in Spannung mit m_τ.
4. **Abhängigkeit von der Zählweise.** γ_BI hängt von der Zählung ab: 0,2375 (Domagała–Lewandowski/Meissner, im Companion
   L1) passt, 0,2740 (ABCK, SU(2)) und γ_string geben 0,137 bzw. 0,064. Der Treffer hängt an der Wahl, die der Companion
   für die Lepton-Zählung schon getroffen hat.

## Bewertung
- Eine native Quelle für 2/3 rad ist nicht gefunden. Der einzige Scan-Treffer, ΔΦ = γ_BI/2 (Fluss vom Qubit-Oktanten zu den
  geladenen Leptonen gleich dem halben Barbero-Immirzi-Parameter), ist nachträglich, statistisch unauffällig und liegt
  bei 2,3σ gegen m_τ.
- Er ist aber scharf prüfbar: Er verlangt m_τ = 1777,13 MeV. Ein künftiger Wert von m_τ (Belle II, BES III) entscheidet;
  dafür wäre eine eigene Vorab-Notiz nötig. Ein Mechanismus, der γ_BI als Fluss durch das Generationsdreieck ausweist, fehlt.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.

## Nachtrag: Mechanismus für ΔΦ = γ/2 gesucht (13.11., spät, Autor: „Erst Mechanismus suchen“)

Vorwissen: v4.10.0-r07.4 (Zählungen auf das Flächengesetz kalibriert), r09 (Zählregel je Frame, H98), r10 (Zählgleichung als
Unruh-Statistik, E_j/T_U = 2πγ a(j); Zählregel als frame-abhängiges Flächenquantum), Annahmenliste Z1 (M zählt alle Spins,
T nur j = 1/2; U(1)-Behandlung). Skript, Abschnitt (5). Nicht blind, kein Test.

1. **γ ist nativ der M-Wert.** Aus der Zählregel des Companion folgen γ_M = 0,237533 (alle Spins, Gewicht 2) und
   γ_T = ln 2/(π√3) = 0,127384 (nur j = 1/2). Der Treffer benutzt γ_M, den Wert des Materie-Frames, in dem die geladenen
   Leptonen gelesen werden.
2. **Bisherige Rolle von γ im Companion:** nur als Parameter der Horizontzählung (Flächenquantum, Boltzmann-Gewicht
   e^{−2πγ a(j)}). Als Phase oder Holonomie tritt γ bisher nicht auf.
3. **Kandidaten für einen Mechanismus (Literatur-Lesarten, nicht im Companion angelegt):**
   - Ashtekar-Barbero-Verbindung A = Γ + γK: Die Holonomie des γK-Anteils gibt einem Spin-1/2-Objekt die Phase γκ/2, mit κ
     der aufintegrierten extrinsischen Krümmung entlang der Schleife. γ/2 verlangt κ = 1 rad; ein Grund dafür fehlt.
   - U(1)-Durchstoßpunkt (Z1: U(1)-Behandlung): Ein Spin-1/2-Punkt mit |m| = 1/2 trägt den Fluss γ · m in Einheiten des
     Flächenquantums; als Phase gelesen gibt das γ/2, wenn die Einheit genau 1 ist. Auch das ist nicht begründet.
   - γ als topologischer Winkel (Holst- bzw. Nieh-Yan-Term): eine Phase proportional zu γ je Einheit; die Einheit bleibt offen.
4. **Gemeinsame Struktur.** In allen Lesarten kommt der Faktor 1/2 vom Spin 1/2, wie beim Oktanten (Phase = halber
   Raumwinkel). Die Formel Φ_e = π/4 − γ_M/2 hieße dann: Beide Anteile des Flusses der geladenen Leptonen sind
   Spin-1/2-Phasen, ein geometrischer (Oktant) und einer aus der γ-gewichteten Holonomie.

**Bewertung.** Ein Mechanismus ist nicht hergeleitet. Es gibt eine zusammenhängende Lesart (Spin-1/2-Phase einer
γ-gewichteten Holonomie im Materie-Frame), aber jede Fassung braucht eine unbegründete Einheit (κ = 1 rad bzw. Fluss-Einheit 1),
das Vorzeichen bleibt offen, und eine Abbildung des Generationsdreiecks auf eine LQG-Schleife oder einen Durchstoßpunkt
gibt es im Companion nicht. Prüfbar bleibt die Zahl: m_τ = 1777,13 MeV. Ein zweites Delta hätte erst mit einem solchen
Mechanismus eine vorgegebene Form. OP3/OP4 offen; H100 unberührt.

## Nachtrag: Fläche und Phase zugleich, Holonomie-Fluss-Paarung gerechnet (13.11., spät, Autor: „versuche es mal“)

Frage des Autors: Kann γ zugleich Flächenquantum und Phase oder Holonomie sein, je nach Lesart? Skript, Abschnitt (6).

1. **Ja, strukturell.** In der Holonomie-Fluss-Algebra ist der Flussoperator E der Erzeuger der Drehungen der Holonomie; im
   Kommutator steht γ. Auf einer Spin-1/2-Kante mit magnetischer Zahl m hat E den Eigenwert γ·m (in Einheiten 8πGħ), und
   exp(iE) dreht die Kante um die Phase γ·m (Kontrolle: 0,11877 rad = γ_M/2). Dieselbe Zahl ist also Flächenbeitrag und
   Phasenrate. Die Frames liefern dafür eine feste Regel statt freier Wahl: Zählung = Fläche, Holonomie = Phase.
2. **Die Einheit ist aber nicht festgelegt.** Die Phase pro Einheitsdrehung hängt an zwei Konventionen:

   | Flächeneinheit | Spinwert | Phase | gegen γ/2 |
   |---|---|---|---|
   | 8πGħ = 1 | \|m\| = 1/2 | 0,11877 | **= γ/2** |
   | 8πGħ = 1 | √(j(j+1)) | 0,2057 | 1,73-fach |
   | Għ = 1 | \|m\| | 2,985 | 25,1-fach |
   | Għ = 1 | √(j(j+1)) (so r10) | 5,170 | 43,5-fach |

   γ/2 entsteht nur mit der Flächeneinheit 8πGħ und dem U(1)-Wert |m|. Der Companion benutzt in r10 die Fläche
   8πγℓ_P² √(j(j+1)); damit käme 43,5-mal γ/2 heraus.
3. **Das Dreieck.** Eine Holonomie um das Platzdreieck misst die Krümmung F der Verbindung, nicht den Fluss E. Beide sind nur
   über eine Randbedingung verknüpft (wie am Horizont, F ∝ (1 − γ²)π/a_H · E); deren Koeffizient hängt an einer Fläche und
   gibt keinen festen Wert γ/2.

**Bewertung.** Die Doppelrolle ist sauber: γ·m ist in der Holonomie-Fluss-Paarung zugleich Flächenbeitrag und Phasenrate,
mit einer festen Regel über die Frames. Die Normierung entscheidet aber, und γ/2 ergibt sich nur mit einer Konventionswahl
(Einheit 8πGħ, |m|), die nicht die des Companion ist. Die Einheit bleibt frei; ein Mechanismus ist nicht hergeleitet.
H102 unberührt; OP3/OP4 offen.
