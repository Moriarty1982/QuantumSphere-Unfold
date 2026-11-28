# Vorab-Notiz H217 (k430): Wählt die Schleifensuche die Casimir-Fläche?

Stand 28.11.2026, vor der Rechnung festgeschrieben. Auftrag des Autors vom 28.11.2026, 00:08 („alles drei“), Folgetest 2 zu H215.

## Frage

Die Zählregel Σ_{k≥1} 2^(1 − γ a_k) = 1 gibt je nach Flächengesetz ein anderes β = √((γ − 1)/(γ + 1)). Normiert ist jeweils a_1 = 1
(j = ½), mit k = 2j:

| Variante | a_k | γ | β |
|---|---|---|---|
| Casimir √(j(j+1)) (Postulat r67) | √(k(k+2)/3) | 1,864699764609 | 0,549405640975 |
| glatt j + ½ | (k + 1)/2 | 2 (exakt) | 1/√3 = 0,577350269190 |
| linear j | k | log₂ 3 = 1,584962500721 | 0,475704094507 |

H217 lässt die drei Werte in derselben Suche antreten, also in der Vorwärtsklasse aus H215 und der Umkehrklasse aus H216. Gefragt ist, ob
die Suche die Casimir-Fläche auszeichnet.

## Messgrößen

Für jede Variante und jede Klasse werden N(β) im Fenster ±6,5·10⁻⁴, der Rang unter den 2000 Zufallskontrollen und die exakten Treffer
(Rest < 10⁻²⁰) bestimmt. Das Einzelwort E bzw. E⁻¹ wird wie bisher getrennt berichtet.

## Kriterium

- **Casimir ausgezeichnet (trägt):** Casimir hat in mindestens einer Klasse einen exakten Treffer oder liegt über dem 99. Perzentil, und
  keine der beiden anderen Varianten erfüllt das.
- **Nicht trennscharf (widerlegt im Sinne „die Suche wählt Casimir nicht“):** sonst.
- Ein Erfolg einer anderen Variante zählt **nicht** gegen das Postulat r67, wenn er aus der Schlagseite der Klasse zu geschlossenen Formen
  folgt. Das wird für jeden exakten Treffer einzeln angegeben.

## Nicht blind (vor der Rechnung von Hand gefunden)

- **j + ½:** Wegen γ = 2 gilt E(1/√3) = ½ und G(1/√3) = ½. Damit hat das Umkehrwort E⁻¹G die exakte Fixstelle 1/√3. Es gibt also sicher
  mindestens einen exakten Treffer in der Umkehrklasse. Das liegt allein daran, dass γ ganzzahlig ist.
- **j:** Wegen γ = log₂ 3 gilt E(β_j) = ⅔, also β_j = E⁻¹(⅔). Ein exakter Treffer braucht zusätzlich ein Wort, das ⅔ auf β_j zurückführt.
  Das ist nicht von Hand bekannt.
- **Casimir:** Eine geschlossene Form ist nicht bekannt.
- Daraus folgt: Die Suche bevorzugt geschlossene Formen. Erwartet wird deshalb „nicht trennscharf“. Gerechnet ist das noch nicht.

## Prüfwege

Gemeinsames Skript mit H216 (`k429_test_h216.py`, Abschnitt H217) und Ausgabe in `k429_out.txt`, unter der Nummer k430 geführt. Die
Wolfram-Gegenprobe berechnet die drei γ unabhängig und prüft den exakten Treffer E⁻¹G(1/√3) = 1/√3 symbolisch.
