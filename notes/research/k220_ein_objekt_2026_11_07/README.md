> **Herkunft (Vermerk vom 15.11.2026):** Diese Erkundung lag bis zum 15.11.2026 nur auf dem lokalen Zweig
> `claude/quantenphysik-paper-herleitung-e723a3` (Commit 4b615e1, 7.11.2026, Dateien `llm/Erkundung_Ein_Objekt.md`,
> `llm/k220_bahnen_ein_objekt.py`, `llm/k220_out.txt`). Sie ist hier unverändert übernommen; die Nummer k220 war seither
> vergeben (vgl. `../predictions/Vorab_Notiz_H99_Neutrino_Phase_Bogenrand.md`). Das Skript liegt jetzt neben dieser Notiz,
> die Ausgabe vom 7.11. unter `run/k220_out_2026_11_07.txt`, ein Kontrolllauf vom 15.11. unter `run/k220_out_2026_11_15.txt`.
> Der dort vorgeschlagene nächste Schritt „als Runde v4.10.0-r12 einbauen“ ist überholt: r12 wurde am 13.11. mit anderem
> Inhalt vergeben, k220 ist in keiner Runde. Bezug zur späteren Arbeit: Die invariante Kugel
> `../op3_helicity_axis_2026_11_15/README.md` (χ = (√s₊, √s₋)) baut auf denselben Bahnen von SO(3, C) und der Dualität auf.

# Erkundung: Was heißt „ein Objekt“? Bahnen auf dem Träger und Art jeder Gleichsetzung des Kerns

**7. November 2026. Status: Erkundung, analytisch mit numerischer Kontrolle (k220), ohne Kriterium.** Anlass: Vorschlag aus der
Codex-Rekonstruktion (`notes/research/qsc_back_to_basic_idea_2026_11_06.md`, v4.10.0-r11 Konsequenz), vor jedem weiteren Spin- oder Zählzweig zu klären,
was „ein Objekt“ bedeutet. Autor: „weiter“.

## Vorwissen geprüft
- v4.8.0-r06.3: Bahnen von SO(3,ℂ) auf ℂ³ sind die Niveaumengen s = c (c ≠ 0), der punktierte Nullkegel und {0}; z ↦ iz bildet s ↦ −s ab.
- v4.8.0-r20.1: z ↦ iz vertauscht mit SO(3,ℂ). v4.9.0-r02: z ↦ −z = C = PT; J_B antilinear.
- v4.9.0-r22 (Konvention F): Photon = entarteter Fixpunkt. r24: Hauptkorpus-„Photon-Frame“ = Bezugsframe R (reiner Zustand). r61: Hopf liest reinen
  R-Zustand (2/3, 1/3) als gemischten M-Zustand (3/4, 1/4). r69.1: I/2-Mischung = P.
- v4.10.0-r07.2: Gravitation koppelt an den hermiteschen Tensor (dualitätsinvariant). r10.3: Zählregel ⇔ frame-abhängiges Flächenquantum.
- v4.10.0-r11.2(f) (Codex, nachgerechnet): |s| unter Lorentz und Dualität erhalten; s ≠ 0 erreicht s = 0 nicht; Kompensatorbild nicht null;
  „ein Objekt“ hat mindestens vier Bedeutungen: (1) gleicher Träger, (2) gleicher physikalischer Zustand, (3) Zustände, die eine aktive Operation
  verbindet, (4) verschiedene Auslesungen eines Zustands.

## 1. Bahnen der Symmetriegruppe (neu: die positive Hälfte)
G = SO(3,ℂ) × U(1)_Dualität wirkt auf z = E + iB. r11.2(f) zeigt, dass |s| erhalten bleibt. Hier die Umkehrung, konstruktiv geprüft (k220, 2000 Paare):
**G wirkt auf jeder Schale |s| = r > 0 transitiv.** Zu z₁, z₂ mit |s₁| = |s₂| gibt es α und L ∈ SO(3,ℂ) mit z₂ = L e^{iα} z₁ (Residuum ≤ 1,2·10⁻¹⁴,
L^T L = 1 und det L = 1 auf 6·10⁻¹⁴). Negativkontrolle: verschiedene Schalen lassen sich nicht verbinden (Residuum 0,84).

Die Bahnen von G sind also genau: die Schalen |s| = r > 0, der punktierte Nullkegel, und {0}. In der s-Ebene dreht die Dualität s um e^{2iα};
**s = 0 ist ihr einziger Fixpunkt.** Das ist die genaue Fassung von „Photon = entarteter Fixpunkt“ (Konvention F).

## 2. Was daraus für „ein Objekt“ folgt
- **Materie und Tachyon** (s > 0 und s < 0 bei gleichem |s|) liegen auf **einer Bahn**: Bedeutung (3), verbunden durch eine aktive Symmetrie des freien
  Trägers. Für das freie Maxwell-Feld sind sie bis auf diese Symmetrie gleichwertig; mit elektrischen Ladungen ist die Dualität gebrochen, und sie sind
  physikalisch verschieden. „Derselbe Zustand“ (2) sind sie nicht.
- **Licht** (s = 0) liegt auf einer **anderen Bahn**. Keine invertierbare Operation aus G verbindet es mit M oder T. „Ein Objekt“ gilt für Licht nur in
  Bedeutung (1) (gleicher Träger ℂ³) oder als Grenzwert r → 0 beziehungsweise als Fixpunkt der Dualität, nie als aktive Umwandlung.
- Die Grundidee „Materie, Licht und Tachyon sind Auslesungen eines gemeinsamen Objekts“ ist damit **für M und T im starken Sinn (3) präzise, für P nur
  im schwachen Sinn (1)**. Wer mehr will, braucht nicht invertierbare Schritte (Projektion, Mischung, Grenzwert), und die verlieren Information.

## 3. Art jeder Gleichsetzung im Kern
| Gleichsetzung | Quelle | Art |
|---|---|---|
| M ↔ T über z ↦ iz | r22, r28, r20.1 | (3) aktive Symmetrie, gleiche Bahn |
| z ↦ −z = C = PT | r02 | (3) aktive Symmetrie (zentral) |
| J_B (E ↔ B mit Zeitumkehr) | r02, r30 | (3) aktive, antilineare Operation |
| Boost zwischen Beobachtern, γ_L als Lorentzfaktor | thm:frame-offset, r11.5(b) | (4) zwei Auslesungen desselben Felds durch zwei Beobachter |
| Gravitation in M und T | r07.2 | (4) Auslesung durch den hermiteschen Tensor; auf der Bahn konstant |
| Zählregel je Frame (Flächenquantum) | r63, r09, r10.3 | keine der vier: eine Zusatzannahme über die Geometrie, nicht durch G vermittelt |
| T als zweite Lesart desselben Felds | r84, G2 | (4) nach Autorentscheidung, aber in verschiedenen Gebieten (vor/nach dem Urknall) |
| R (reiner Bezugszustand) ↔ P | r24, r69.1 | **Informationsverlust**: P = I/2 ist eine Mischung; R ≠ P |
| Kompensator C = ½(1 + J), C(z) = (z + i z̄)/2 | r30, r11.2(f) | **Informationsverlust** (Projektion); Bild nicht null, also nicht P |
| Hopf: R (2/3, 1/3) als M (3/4, 1/4) | r61 | **Vermischung** von Zustand und Auslesung (schon in r61 als Frame-Fehler markiert) |
| β_sym, q als Ω_M | thm:dark-energy, r31, H96 | (4) nur mit einer Messabbildung Register → Dichte; die fehlt (r11.2(b), vier Nenner) |

## Ergebnis
1. **„Ein Objekt“ hat auf dem Träger eine genaue Form:** eine Bahn von G. M und T sind ein Objekt in diesem Sinn, P nicht; P ist der Fixpunkt.
2. Die Gleichsetzungen des Kerns gehören zu verschiedenen Arten. Symmetrien (3) und Beobachterwechsel (4) erhalten Information. Kompensator, Mischung und
   die Hopf-Lesart verlieren oder vermischen Information. Die Zählregel je Frame gehört zu keiner Art; sie ist eine Zusatzannahme.
3. Für die offene Front heißt das: Ein frame-abhängiges Flächenquantum (r10.3) kann nicht aus G kommen, denn G lässt alles Geometrische und den
   hermiteschen Tensor fest. Es müsste von außerhalb des Trägers kommen.

## Grenzen
- Nur Lesart B und der freie Träger. Mit Ladungen und Wechselwirkung ist die Dualität keine Symmetrie mehr; dann sind M und T auch als Bahnen verschieden.
- Die Tabelle ordnet ein, sie entscheidet nicht über die Wahrheit der Gleichsetzungen.

## Mögliche nächste Schritte
1. Als Runde v4.10.0-r12 einbauen.
2. Die Grundidee in der präzisen Form festhalten (M, T eine Bahn; P Fixpunkt) und prüfen, welche Hauptkorpus-Aussagen P als „dasselbe Objekt“ im starken
   Sinn lesen (Statusvermerk-Kandidaten).
