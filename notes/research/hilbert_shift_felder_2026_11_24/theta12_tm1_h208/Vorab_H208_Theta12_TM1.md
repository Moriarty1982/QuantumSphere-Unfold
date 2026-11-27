# Vorab-Notiz H208 (k418): Ist sin²θ₁₂ ≈ 0,318 strukturell erzwungen (TM1-Vorhersage) oder struktur-erhaltend senkbar?

**Datum:** 2026-11-27. **Strang:** Lepton-Mischung (Strang 3), Fortsetzung H205/H206/H207.
**Status:** Test mit Entscheidungskriterium, vor der Rechnung festgeschrieben. **Nicht blind** in einem Teil: dass die reine K₂-Richtung sin²θ₁₂ = 0,3195 gibt, ist aus H206 bekannt; neu ist die Frage, **ob dieser Wert erzwungen ist**.

## Ausgangslage (aus H205–H207)
- Neutrino-Form N̂ = [[1,b,c],[b,1,−b],[c,−b,1]] (A-invariant, Ein-Feld-Form). Die Spalte **v₀ = (1,0,1)/√2 ist Eigenvektor von N̂ für JEDES b,c** (H205, baumunabhängig).
- Die θ₁₃-Korrektur im Ladungssektor liegt in der Ebene ⊥ v₀, Richtung **K₂** ist durch Massen-Erhaltung **eindeutig erzwungen** (H206, Wolfram exakt).
- Mit K₂ und dem gemeinsamen Versatz x (H207): θ₁₃ getroffen, θ₂₃ ≈ 45°, |sin δ_CP| ≈ 1 — alles innerhalb ~1,5σ, null freie Parameter.
- **Einziger Rest:** sin²θ₁₂ = 0,3195 (+2,5σ gegen NuFIT 0,3036). Das ist das klassische TM1-Problem: TM1 sagt sin²θ₁₂ = (1 − 3 s₁₃)/(3(1 − s₁₃)) ≈ 0,318 voraus.

## Frage
Ist sin²θ₁₂ ≈ 0,318 eine **strukturell erzwungene Vorhersage** (an die feste Spalte v₀ und damit an die Massen-Erhaltung gekoppelt), oder gibt es eine **struktur-erhaltende** Deformation, die sin²θ₁₂ auf die gemessenen 0,3036 senkt, **ohne** θ₁₃ aus dem Fenster zu schieben, **ohne** die Massen-Erhaltung und **ohne** die maximale CP-Verletzung zu brechen?

## Vorwissen geprüft
- `mischung_h173/Ergebnis_H173_Drehwinkel_aus_Spektrum.md`: TM1-Baum, sin²θ₁₂ = ⅓ bei θ₁₃ = 0.
- `mischung_h174/k370_test_h174.py`: Maschinerie N̂, C(ρ,δ), PMNS, Versätze X_LEP = 0,0395773407, X_R = 0,043359.
- `mischung_h175/Ergebnis_H175_Term_aus_Ladungsrichtung.md`: Daten verlangen die Ladungsrichtung nicht (erlaubter Term-Raum 5-dim).
- `mischung_h176/`: gefitteter Ein-Zahl-Kandidat x = 0,04478 (festgeschrieben, nicht erzwungen).
- `winkel_in_ebene_h206/Ergebnis_H206_Winkel_in_Ebene.md`: K₂ (massenerhaltend) → sin²θ₁₂ = 0,3195; gefittete Halbierende (K₁+K₂)/√2 → sin²θ₁₂ = 0,2979 (trifft), aber **bricht** Massen (Koide ρ → 0,985) und CP (|sin δ| → 0,964).
- `staerke_h168_h207/`: reiner H168-Versatz, θ₁₂ bleibt +2,5σ.

## Rechnung (geplant)
1. **Erste PMNS-Spalte explizit.** |U_e1|², |U_μ1|², |U_τ1|² im Schema bestimmen. Prüfen, ob die feste Spalte v₀ exakt der TM1-Spalte (|U_e1|² = ⅔) entspricht und ob sin²θ₁₂ dadurch **allein durch θ₁₃** festgelegt ist: sin²θ₁₂ = (1 − 3 s₁₃)/(3(1 − s₁₃)). numpy + **Wolfram exakt**.
2. **Pinning-Test.** Alle freien Knöpfe variieren (Neutrino-Versatz x bzw. b,c; Ladungs-Stärke κ; Vorzeichen) und prüfen, ob sin²θ₁₂ auf der TM1-Kurve f(θ₁₃) bleibt. Bleibt v₀ unter allen Variationen Eigenvektor ⇒ θ₁₂ gepinnt.
3. **Rückwärtssuche (AGENTS-Regel).** Zielwert sin²θ₁₂ = 0,3036 ⇒ notwendige Bedingung |U_e1|² = cos²θ₁₂ cos²θ₁₃ = 0,6808 (≠ ⅔ = 0,6667). Welche Spalte müsste fest sein? Ist diese Spalte strukturell verfügbar (anderes Eigenvektor-Muster von N̂), oder nur durch Brechen der Ein-Feld-Form?
4. **Struktur-erhaltende Senkung?** Systematischer Scan: gibt es eine Deformation (N̂-Zusatz oder Ladungs-Richtung), die θ₁₂ senkt und zugleich (a) θ₁₃ ∈ 3σ, (b) Massen-Erhaltung (Koide ρ = 1 ± 1e-3), (c) |sin δ_CP| > 0,99 hält? Richtung und Kosten festhalten.
5. **JUNO-Diskriminierung.** Mit NuFIT-Fehler (0,0064) und projiziertem JUNO-Fehler (~0,0005) quantifizieren, wie scharf die Vorhersage 0,318 testbar ist.

## Entscheidungskriterium (vorab)
- **„Hergeleitet — Vorhersage":** Wenn (2) sin²θ₁₂ auf der TM1-Kurve gepinnt ist (v₀ unter allen Variationen Eigenvektor) UND (4) keine Deformation θ₁₂ auf 0,3036 senkt, ohne (a)/(b)/(c) zu brechen — dann ist sin²θ₁₂ = (1 − 3 s₁₃)/(3(1 − s₁₃)) ≈ 0,318 eine **strukturell erzwungene, falsifizierbare Vorhersage** (kein freier Parameter), in milder (2,5σ) Spannung mit NuFIT, von JUNO scharf testbar. Die feste Spalte (θ₁₂) und die Massen-Erhaltung sind dann an dasselbe Strukturelement gekoppelt.
- **„Verborgene Freiheit":** Wenn (4) eine struktur-erhaltende Deformation θ₁₂ auf 0,3036 senkt, ohne (a)/(b)/(c) zu brechen — dann ist θ₁₂ doch einstellbar; Richtung, Stärke und was sie kostet, werden berichtet (positiver Befund).
- **„Teilweise":** Wenn eine Deformation θ₁₂ senkt, aber genau eine der Bedingungen (a)/(b)/(c) leicht verletzt — dann festhalten, welche und wie stark (Austausch quantifizieren).

## Werkzeugwahl
numpy für Scans/PMNS; **Wolfram Language exakt** für: (i) v₀ Eigenvektor von N̂ für symbolische b,c; (ii) die exakte TM1-Beziehung sin²θ₁₂ = (1 − 3 s₁₃)/(3(1 − s₁₃)); (iii) exakte Massen-Erhaltungs-Kopplung an v₀.

## Ehrlicher Status
OP4 (Mischung/Massen) bleibt offen. Append-only. H-/k-Nummer gegen `main` geprüft (H208, k418 frei).
