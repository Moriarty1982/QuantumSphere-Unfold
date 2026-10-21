# Vorab-Notiz H13: Auslesefaktor als Wigner-Holonomie einer Boost-Schleife in Triolen-Richtungen

Festgelegt am 2026-10-21, **vor** jeder Berechnung der Holonomie. Bezug: K39 (Rückwärtsanalyse), K40/K41 (r19).

## Rahmen

r19 zeigt: Eine kontinuierliche Holonomie braucht geschlossene Wege in einer SO(3,ℂ)-Bahn und eine Transportregel;
das Dokument liefert beides nicht. K39 hat als einzigen tragfähigen Auslese-Ansatz einen Faktor f(+) = 0,9436 ± 0,0083
(in der Rapidität, gegen die Hopf-Starteinstellung) gefunden. H13 prüft, ob eine fest gewählte, parameterfreie
Holonomie diesen Faktor liefert.

## Hypothese (V)

**H13:** f(+) ist der Kosinus der Wigner-Rotation, die bei einer geschlossenen Schleife aus reinen Boosts zwischen
drei Materie-Frames in Triolen-Richtungen entsteht.

## Konstruktion (verbindlich)

- **Gruppe:** SO⁺(1,3) ≅ SO(3,ℂ) (Lesart B, r06), Übergänge innerhalb des Materiesektors.
- **Richtungen:** drei Einheitsvektoren n_k = (cos 2πk/3, sin 2πk/3, 0), k = 0, 1, 2 (Triole, 120°).
- **Rapidität:** jeder Frame k bewegt sich mit Rapidität η_H = artanh(1/√3) in Richtung n_k gegen den Bezugsframe
  (Hopf-Starteinstellung wie in K39).
- **Transportregel:** Der Übergang von Frame k nach Frame k+1 ist der reine Boost, der die Geschwindigkeit v_k in v_{k+1}
  überführt (Geodäte im Geschwindigkeitsraum).
- **Schleife:** v₀ → v₁ → v₂ → v₀. Die Komposition der drei reinen Boosts ist eine Rotation um den Winkel δ (Wigner).
- **Vergleichsgröße:** f₁₃ = cos δ.

## Offenlegung (vor dem Festschreiben bekannt)

1. **Wert unbekannt.** δ ist nicht berechnet, auch nicht überschlagen.
2. **Wahlen.** Die Konstruktion enthält drei diskrete Wahlen: Richtungen (Triole), Rapidität (η_H statt η aus β_sym),
   Vergleichsgröße (cos δ statt etwa 1 − δ). Jede ist motiviert, keine hergeleitet. Andere Wahlen werden **nicht**
   gerechnet und nicht berichtet.
3. **Weiches Ziel.** f(+) aus K39 ist selbst eine Anpassung an zwei Werte, einer davon über die nachträglich gefundene
   H9-Relation (JUNO), und gilt nicht als Test. Ein Treffer wäre deshalb höchstens ein Grund für einen echten Test, der
   f(+) ohne JUNO festlegt; er wäre kein Beleg.
4. **Lesart B gegen alte Lesart.** Die Übergänge liegen im Materiesektor; eine Lorentz-Verbindung zum Photon oder Tachyon
   gibt es in Lesart B nicht (r19.1). H13 behauptet keine.
5. **Gelesen:** K39, r19, die Formeln für Wigner-Rotation und hyperbolische Dreiecke aus der Lehrbuchliteratur.

## Verfahren (verbindlich)

Skript `llm/k35_test_h13.py`, erst nach dem Commit dieser Notiz:
1. v_k = tanh(η_H) n_k; reine Boosts als 4×4-Matrizen; Komposition L = B(v₀←v₂) B(v₂←v₁) B(v₁←v₀).
2. Prüfen, dass L eine reine Rotation ist (Boostanteil numerisch null); δ aus der Spur des räumlichen Blocks.
3. Gegenprobe: δ gleich der Fläche des hyperbolischen Dreiecks mit Ecken v_k (Winkeldefekt).
4. Berichten: δ, cos δ, Abstand zu f(+) in Einheiten von 0,0083.

## Entscheidungskriterium (verbindlich)

z = (cos δ − 0,9436) / 0,0083.
- |z| < 2: **verträglich** — nur Anlass für einen echten Test (f(+) ohne JUNO, Vorab-Notiz), kein Beleg.
- 2 ≤ |z| < 3: **Spannung**.
- |z| ≥ 3: **widerlegt** für diese Konstruktion. Dann gilt die Holonomie-Route mit Triolen-Boosts für f(+) als
  geschlossen; andere Konstruktionen bräuchten eine eigene Notiz.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
