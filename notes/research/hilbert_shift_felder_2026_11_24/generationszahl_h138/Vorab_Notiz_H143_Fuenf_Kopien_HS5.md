# Vorab-Notiz H143: Noch eine Generation mehr – fünf Oktonion-Kopien auf HS(5)

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Die Kerndimensionen folgen durch Abzählen aus H138/H142
(dim K = 40 − 1 − 7·Rang), und H142 hat einen Mechanismus nahegelegt (Relation der Richtungen mit Koeffizientensumme 0). Dieser Mechanismus
wird hier als Regel vorab formuliert und an allen Auswahlen und allen Orientierungen geprüft. Anlass: Autor (25.11.2026, 20:14): „prüfe jetzt
bitte, was passiert, wenn du noch eine Generation dazu nimmst“, Auftrag über den Koordinator: fünf Kopien, Rest, vollständige Generationen oder
nur Nullteiler/Leck, gemeinsame Ladung, Orientierungsabhängigkeit offenlegen.

## Vorwissen geprüft
- H142 (1bc8fb4, Nachtrag f578bff; k325, k325c, k325d): vier Kopien auf HS(5); vollständige ladungsstabile Generation im Rest genau in den 9
  Auswahlen mit Relation v₁ − v₂ + v₃ − v₄ = 0 (Summe 0); bei Relation mit Summe 3 nur Quarks; bei Rang 4 nur Singuletts ½; keine gemeinsame Ladung.
- H141 (k324): Rest der drei Sedenion-Kopien = Quark-Satz + Singuletts ½. H139: Nullteiler = flaches Kopienprofil; Rest-Komponenten keine Nullteiler.
- HS(5) hat 9 oktonionische Kopien, also reichen fünf Kopien ohne HS(6).

## Aufbau
Wie k325: v = a ⊗ b (a, b ∈ {f₀, f₁₂₀, f₂₄₀}), Orientierung durch die Automorphismen transportiert; getrennte Träger V = ⊕ C_v (40 Zustände),
Φ: V → ℂ⊗A₅, Kern K. Neu: der **größte ladungsstabile Teilraum** W ⊂ K (Q_⊕ W ⊂ W, iterativ), sein Spektrum und seine su(3)-Zerlegung;
Zahl vollständiger Generationen n_gen = Zahl der Eigenwerte 0 in W (je Generation ein Neutrino-Zustand), geprüft gegen die Zahl der Eigenwerte 1.
Alle 126 Fünferauswahlen, dazu (nicht gewertet, nur offengelegt) alle 2⁴ relativen Orientierungen je Auswahl. Gemeinsame Ladung wie k325.
Skript k326 (Python), Gegenprobe k326b (Wolfram, exakt für eine Auswahl je Klasse, falls der Kernel verfügbar ist).

## Hypothesen und Kriterien
Bezeichnung: R⁰ = Raum der Relationen Σ c_k v_k = 0 (mit orientierten v_k) mit Σ c_k = 0.
- **H143a (Regel für vollständige Generationen):** In jeder Auswahl und jeder Orientierung gilt n_gen = dim R⁰. Bestätigt, wenn das in allen
  126 × 16 Fällen stimmt; widerlegt bei einer Abweichung.
- **H143b (vollständige Generationen gibt es weiter):** Bei der transportierten Orientierung gibt es Fünferauswahlen mit n_gen ≥ 1, und keine mit
  n_gen ≥ 2. Bestätigt, wenn beides zutrifft.
- **H143c (keine gemeinsame Ladung):** In keiner Klasse min Leck² < 10⁻³.
- **H143d (Leck bleibt):** Jede Auswahl hat leckende Singuletts mit gestauchter Ladung ½ (Zahl berichtet), und keine Komponente eines Kernelements
  ist ein Nullteiler (smin > 10⁻⁶ in 200 Stichproben je Klasse).
- **Kontrolle:** Für die Vierer-Teilauswahlen reproduziert die Regel H142 (9 Auswahlen mit n_gen = 1).

## Folge, vorab festgelegt
- a bestätigt: Die Zahl vollständiger Generationen im Rest zählt genau die Relationen mit Summe 0; sie ist damit eine lineare Eigenschaft der
  Kopienrichtungen und hängt über die Orientierung am offenen Vorzeichen.
- b bestätigt: Eine fünfte Kopie bringt höchstens eine vollständige Rest-Generation; b widerlegt (n_gen ≥ 2): Der Rest kann mehrere Generationen tragen.
- Was in keinem Fall folgt: Massen, Mischung, physikalische Realität der Rest-Zustände. Vorzeichen offen. OP3, OP4 offen; kein Guard berührt.
- Vergeben: H143, k326.
