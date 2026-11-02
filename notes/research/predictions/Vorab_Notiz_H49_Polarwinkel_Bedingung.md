# Vorab-Notiz H49: Versteckte Bedingung der Polarwinkel-Richtung abseits des Äquators

Festgeschrieben am 2. November 2026, vor der Rechnung. Kontext: `Erkundung_OP5_Symbolstruktur_Grad7.md` (k110–k132).

## Hintergrund

Im festen OP5-Vergleichsmodell hat das vervollständigte Erstordnungssymbol J von R = (F, G, dg) an jeder Lösung
eine freie Richtung: den Diffeomorphismus entlang c = ρ∂_z − z∂_ρ (∝ ∂_ϑ). Analytisch gilt c·∇h = 0 und c·spin = 0.
Die Feldstärke G(t, ρ) ∝ 1/ρ wird aber gebrochen, mit c·∇G ∝ z/ρ². Dieser Bruch ist niederer Ordnung und verschwindet nur
auf dem Äquator z = 0. Am Äquatorkeim (1, 3/5, 0, 0) ist die Projektion R₂ → R₁ nach den Notizen des anderen Modells
surjektiv; die erste versteckte Bedingung (Ω) erscheint dort erst bei den dritten Ableitungen.

## Hypothese H49

Abseits des Äquators erzeugt der Bruchterm schon beim Übergang von ersten zu zweiten Ableitungen eine versteckte
Bedingung. Für generische Lösungen j von R = 0 am Punkt (ψ mitgeführt) ist das System ∂_μR = 0 dann für die zweiten
Ableitungen nicht lösbar. Am Äquator ist es lösbar.

## Rechnung (Skript k133, eigener Aufbau, nicht der Code des anderen Modells)

- **Gleichungen:** ∂_μR = R_p[μ] + R_ψ·ψ_μ + Σ_ν R_{j_ν}·ψ_{νμ}. Das sind 128 Gleichungen für 240 reelle zweite Ableitungen.
  Die partiellen Ableitungen werden durch zentrale Differenzen bestimmt.
- **Unverträglichkeit κ:** κ = |Projektion der rechten Seite auf den Linkskern| / |rechte Seite|. Den Rang legen
  Singulärwertlücken fest.
- **Kontrollen bei z = 0:** der Keim, ein Nachbarpunkt (1,02; 0,6; 0,03; 0) und zwei weitere Lösungen am Keimpunkt
  (Schritte auf der Lösungsmenge wie in k128).
- **Testpunkte z ≠ 0:** (1; 0,6; 0; z) mit z ∈ {0,02; 0,05; 0,1; 0,2}, außerdem (1,03; 0,58; 0,05; 0,1). Jeweils durch
  Fortsetzung vom Keim (wie k130).

## Entscheidungskriterium (vorab)

- **Bestätigt**, wenn beide Bedingungen gelten:
  1. κ an allen Kontrollpunkten ≤ 1e-6;
  2. κ an allen Testpunkten mit |z| ≥ 0,05 ≥ 100 × max(κ an den Kontrollen) und mindestens 1e-5.
- **Widerlegt**, wenn κ an den Testpunkten mit |z| ≥ 0,05 im Bereich der Kontrollen bleibt (< 10 × Kontrollmaximum).
- **Unentschieden** in allen anderen Fällen, etwa wenn schon die Kontrollen über 1e-6 liegen.

Nebenbeobachtung, nicht Teil des Kriteriums: die z-Abhängigkeit von κ (erwartet etwa linear) und der Anteil der
Unverträglichkeit, der zur ϑ-Richtung gehört.

## Grenzen

Endliche Differenzen in float64, Erstjets nur numerisch. Ein Treffer belegt eine versteckte Bedingung auf Ordnung 2
abseits des Äquators im Vergleichsmodell, keine physikalische Aussage und keinen Existenzsatz. Dass Ω mit dieser
Bedingung zusammenhängt, bleibt auch bei Bestätigung eine Lesart.
