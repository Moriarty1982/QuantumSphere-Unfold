# Vorab-Notiz H83: Wie gehen Gravitation und Eichfelder unter der zweiten Lesart ein? Drei Regeln gegen r19

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Die Erwartungen sind analytisch vorgerechnet. Autor 21:51: „Mach das mal … irgendwie habe ich das Gefühl, dass es doch schon in Richtung vereinheitlichte Feldtheorie geht, aber die vergangenen Tests evtl. immer beide Effekte gemessen haben könnten.“

## Vorwissen geprüft
- H82 / k197: Mit Regel R1 passen α, α_s, θ_W zu r19, G_N (1 statt 2) und ℓ_P (½ statt 3/2) nicht. Offene Frage dort: Einstein–Cartan-Term mit K oder K².
- H77 (Lesart B: Kinematik fortgesetzt, X ↦ −X, Potentiale bleiben); H79 (vollständiger komplexer Boost, holomorphe Adjungierte; das Minus für den Weyl-Term kam aus F3, als Gewicht 1 gesetzt).
- r19: k(α) = k(α_s) = 1, k(G_N) = 2, k(ℓ_P) = 3/2, θ_W Auslesegröße.
- Beobachtung vorab: Lesart B für ein Skalarfeld ist dasselbe wie g ↦ −g bei festen Feldern (√|g| unverändert, g^{μν} ↦ −g^{μν}). Unter dem vollständigen Boost (det Λ(iπ) = +1, ε_abcd invariant, Orientierung erhalten) bleiben alle kovarianten Terme ohne Phase; die Phase kommt allein aus der Lesart B.

## Drei Regeln (Gewicht eines Terms im Bild: Phase s, Beitrag a + s·b)
- **R1 (H82):** Terme mit Ableitung s = −1, ohne Ableitung s = +1; Einstein–Cartan, Yang–Mills, |Dφ|², Weyl-Kinetik je s = −1.
- **R2 (g ↦ −g, Vierbein e ↦ i·e, Felder fest):** Phase = (−1)^(Zahl der inversen Metriken) bzw. (−i)^(Zahl der inversen Vierbeine). Erwartung: Einstein–Cartan (zwei inverse Vierbeine) −1; Skalar-Kinetik −1; Yang–Mills (zwei inverse Metriken) +1; Potential, Massen, Yukawa +1; Weyl-Kinetik (ein inverses Vierbein) −i, also nicht reell.
- **R3 (gemischte Metrik g_eff = c·g mit c = a − b, eine Wirkung):** reine Umskalierung der Metrik; dimensionslose Kopplungen bleiben, dimensionsbehaftete skalieren mit Potenzen von c nach ihrer Dimension.

## Hypothese H83 und Kriterium
**H83:** Mindestens eine der drei Regeln liefert zugleich die r19-Gewichte k(α) = 1 und k(G_N) = 2 (als Betrag des γ-Exponenten) und eine reelle Wirkung.
**Erwartung (nicht blind):** keine. R1: α 1, G 1. R2: α 0 (Yang–Mills geht mit a + b ein), G 1, Weyl-Term komplex. R3: α 0 (dimensionslos), G ±1 je nach Konvention.
**Bestätigt**, wenn eine Regel beide Gewichte trifft; sonst widerlegt.

## Folge, vorab festgelegt
- Widerlegt: Die Gewichte aus r19 folgen nicht aus der zweiten Lesart allein; der Treffer bei α in H82 hängt an R1, der am wenigsten begründeten Regel für eichkovariante Terme. Die Lesart des Autors („gemessen wird immer beides“) bleibt als Deutung richtig: In der reduzierten Theorie sind alle gemessenen Konstanten Mischwerte. Eine Vereinheitlichung ergibt sich daraus aber nicht von selbst.
- R2 zeigt zusätzlich eine Spannung: Aus g ↦ −g folgt für Spinoren die Phase −i, nicht das F3-Minus aus H79. Das wäre dem Autor vorzulegen (Verbindung zur komplexen Lesart K).

Skript: `llm/k198_gravitation_zweite_lesart.py` (nach dem Commit dieser Notiz).
