# Vorab-Notiz H207 (k417): Ist die Korrektur-Stärke ein struktureller Versatz? (H168-Spannung)

**Datum:** 2026-11-27. **Strang:** Lepton-Mischung (Strang 3). **Auslöser:** Autor, 27.11., „mach das und merge und push" nach H206 (Stärke / H168-Spannung angehen). Einordnung: `wiki/Gesamtbild.md` T8, OP4.

## Frage
Nach H205/H206 ist die θ₁₃-**Richtung** vollständig strukturell bestimmt (Ebene ⊥ v₀, in der Ebene die massenerhaltende Richtung K₂). Frei bleibt die **Stärke** κ der K₂-Korrektur (sie stellt θ₁₃ ein). Die H168-Idee war **ein** Versatz x für beide Sektoren; H176 fand dafür eine 5,7σ-Spannung (nötiges x = 0,04478 gegen Lepton-Versatz x_lepton = 0,039577) — allerdings mit der **angepassten Halbierenden**, nicht mit der jetzt festgelegten Richtung K₂.

**H207:** Ist die K₂-Stärke κ, die θ₁₃ trifft, gleich einem **strukturellen** Versatz — insbesondere dem Neutrino-Versatz x_ν = X_R = 0,043359 (der R festlegt), oder dem Lepton-Versatz x_lepton = 0,039577, oder ε = artanh β_sym? Falls κ = tan(x_ν): dann liefert **ein** Neutrino-Versatz x_ν **sowohl** das Massenverhältnis R **als auch** θ₁₃ (θ₁₃ wird aus R vorhergesagt, null zusätzliche Parameter) — H168 auf der Neutrino-Seite wiederhergestellt.

## Was gerechnet wird (k417)
Maschinerie aus k371 (obs mit K-2, X_LEP, X_R, β_sym). Richtung fest = K₂ (H206).
1. **κ*(θ₁₃):** die Stärke, die sin²θ₁₃ = 0,02248 (Daten) trifft, mit ihrer datengetriebenen Unsicherheit σ_κ (aus σ(sin²θ₁₃)).
2. **Kandidaten-Versätze:** tan(x_ν), x_ν, tan(x_lepton), x_lepton, ε = artanh(β_sym) und einfache Vielfache. Für jeden: setze κ = Kandidat, berechne sin²θ₁₃, sin²θ₁₂, sin²θ₂₃, sin δ; z-Werte gegen NuFIT/JUNO.
3. **Gemeinsamer Versatz (H168):** Gibt es ein einziges x, das (a) das Neutrino-Spektrum Nhat(π/6−x) → R trifft **und** (b) als κ = tan(x) in K₂-Richtung θ₁₃ trifft? Wie weit ist dieses x von x_lepton (5,7σ-Frage mit K₂ statt Halbierender)?
4. **θ₁₂-Rest:** bei κ = tan(x_ν) bleibt sin²θ₁₂ (aus H206 ~0,320, +2,5σ) — festhalten, dass θ₁₃ ggf. gelöst, θ₁₂ nicht.

## Entscheidungskriterien (vorab)
- **K1 (Stärke strukturell, θ₁₃ aus R vorhergesagt):** κ* stimmt mit **tan(x_ν)** (oder x_ν) innerhalb der datengetriebenen Unsicherheit überein (|κ* − tan x_ν| < σ_κ), sodass sin²θ₁₃ bei κ = tan(x_ν) innerhalb 2σ der Daten liegt. Dann ist θ₁₃ mit der festen Richtung (H205/H206) **aus dem Neutrino-Versatz (R) vorhergesagt**, ein echter Parametergewinn; H168 auf der Neutrino-Seite wiederhergestellt.
- **K2 (Stärke frei / H168 gebrochen):** kein struktureller Kandidat trifft θ₁₃ innerhalb 2σ; die Stärke bleibt ein freier Eingabewert (wie die Quark-Kopplungen), und der gemeinsame Versatz ist genuin gebrochen.

## Erwartung (ehrlich, teilweise nicht blind)
**Teilweise nicht blind:** Aus den **veröffentlichten** H206-Zahlen (κ* ≈ 0,0436 für θ₁₃) und X_R = 0,043359 ist κ* ≈ x_ν bereits erkennbar; die Nähe ist also keine Überraschung. **Blind/neu geprüft** wird: ob es **tan(x_ν)** oder **x_ν** (oder keines exakt) ist, ob es innerhalb der datengetriebenen Unsicherheit **trägt**, ob θ₁₂/θ₂₃ dabei konsistent bleiben, und ob das ein **struktureller Link** (θ₁₃ aus R) oder nur eine Zahlenkoinzidenz ist (wie 2^(1−γ_L) ≈ β_sym, H181 — Zufallstreffer). Selbst bei K1 bleibt sin²θ₁₂ zu hoch (TM1-Problem, H206) und die Daten verlangen den Ladungssektor nach H175 nicht. Der Lepton-Versatz x_lepton = 0,039577 ist ein **anderer** (≈1,4σ entfernter) Wert; H168 gilt dann allenfalls auf der Neutrino-Seite, nicht sektorübergreifend.

## Vorwissen geprüft
- `winkel_in_ebene_h206/` (H206): Richtung = K₂ (massenerhaltend); κ* ≈ 0,0436; θ₁₂ +2,5σ.
- `drehwinkel_richtung_h205/` (H205): Ebene ⊥ v₀.
- `mischung_h173/` (H173b): x_ν (pure Neutrino-Drehung) → sin²θ₁₃ = 0,0155 (−7,7σ) — **anderer Mechanismus** als hier (K₂-Ladungskorrektur).
- `mischung_h175/h176`: H176-Fit (Halbierende) x = 0,04478, 5,7σ gegen x_lepton. β_sym = 0,5494056 (Memory); X_R = 0,043359, X_LEP = 0,0395773 (k370).
- H181: 2^(1−γ_L) ≈ β_sym war Zufallstreffer (Warnung vor Koinzidenzen).

## Werkzeuge
numpy (obs mit K-2, κ-Fit, Kandidatenvergleich). Wolfram nur falls eine exakte Identität auftaucht (κ = tan x_ν o. ä.); sonst nicht einschlägig. Qiskit nicht einschlägig.
