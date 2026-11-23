# Methoden-Notiz: Lassen sich das Zeitumkehr- und das Spiegel-Jet zu einem zweiten Jet fortsetzen? (Erkundung, vor der Rechnung festgelegt)

23. November 2026. Auftrag des Autors: „weiter“ nach Runde v4.10.0-r43. Keine H-Nummer. Blind im Ergebnis: Vor der Rechnung ist
nicht bekannt, ob die Verträglichkeitsbedingungen zweiter Ordnung die Familie überhaupt einschränken.

## Suchrichtung
r41–r43 hängen an derselben offenen Voraussetzung (Zeitumkehr oder Spiegelung). Nach AGENTS.md wurde geprüft, ob eine Rückwärtssuche
günstiger ist. Ziel: eine Eigenschaft, die das Modell am Keim festlegt und die sich unter Zeitumkehr und Spiegelung verschieden verhält.
Werte: nein (r41, beide Bilder gleich). Erster Jet: nein (r43, 65-dimensionale Familie). Nächste notwendige Bedingung: Ein erster Jet ist
nur zulässig, wenn er sich fortsetzen lässt. Das prolongierte System für den zweiten Jet hat 128 Gleichungen, 240 Unbekannte und Rang
113 (`analysis/op5-field-slices/state-sufficiency-2026-10-30/PRECISION_HIGHER_JET_CHECKPOINT.md`, `precision_second_jet.py`); die 15
abhängigen Zeilen sind Verträglichkeitsbedingungen an den ersten Jet. Die zurückgestellte Idee I1 (String M–T) ist ein anderer Weg und wird
dem Autor getrennt vorgelegt, nicht hier umgesetzt.

## Vorwissen geprüft
- r43: Die Familie der vervollständigten ersten Jets enthält einen Jet mit exaktem Zeitumkehrbild (T-Jet) und einen mit exaktem
  Spiegelbild (R-Jet); beide ändern die Ableitungen um bis zu etwa 3.
- `precision_second_jet.py`: Am gespeicherten ersten Jet ist das prolongierte System lösbar (voller Rest 1,1·10⁻⁶⁶).
- r42: Am gespeicherten Jet ist keines der Bilder erfüllt.

## Werkzeug
Python mit mpmath, 40 Stellen, auf dem vorhandenen Bau (`precision_completed_rebuild.py`, Pfade als Argumente). Wolfram nicht nötig
(numerische lineare Algebra an einem Punkt), Qiskit nicht geeignet. Skript `second_jet_images.py`, Ausgabe `run/second_jet_images.txt`.

## Rechnung
Für jeden ersten Jet v mit R(v) = 0: Symbol J(v) (Jacobi-Matrix von R nach den 96 ersten Ableitungen) und rechte Seite b(v) (totale
Ableitung von R bei verschwindendem zweitem Jet, wie in `precision_second_jet.py`) neu berechnen, das 128×240-System A(v)c + b(v) = 0
aufstellen und den kleinsten vollen Rest über alle c bestimmen (unabhängige Zeilen, Lösung minimaler Norm, Rest aller 128 Zeilen).
Geprüfte Jets:
1. gespeicherter vervollständigter Jet (Kontrolle, erwartet ≈ 0);
2. T-Jet und R-Jet aus r43 (mit demselben Newton-Verfahren neu erzeugt und abgelegt);
3. zwei zufällige Glieder der Familie (Schritt der Länge 1 in einer zufälligen Richtung des Nullraums, Newton zurück auf R = 0,
   feste Startwerte 1 und 2) als Kontrolle dafür, ob die Bedingungen die Familie überhaupt einschränken.
Zusätzlich: Rang von A(v) an jedem Jet.

## Raster (vorab)
Ein Jet heißt fortsetzbar, wenn der volle Rest ≤ 10⁻²⁰ ist, sonst nicht fortsetzbar (Rest ≥ 10⁻⁶; dazwischen unklar).
- **Zeitumkehr entschieden:** T-Jet fortsetzbar, R-Jet nicht.
- **Spiegelung entschieden:** R-Jet fortsetzbar, T-Jet nicht.
- **keine Einschränkung:** auch die zufälligen Glieder fortsetzbar. Dann entscheidet der zweite Jet nicht, die Bedingungen sind auf der
  Familie automatisch erfüllt.
- **beide nicht fortsetzbar, Zufallsglieder ebenso:** Die Bedingungen schränken die Familie ein, aber die in r43 gefundenen Jets liegen
  außerhalb; dann ist neu zu suchen (T- und R-Bedingung zusammen mit den Verträglichkeitsbedingungen), in einer eigenen Runde.

Frames: Keim im Materie-Frame M, Koordinaten des Vergleichsmodells. OP5 bleibt offen.
