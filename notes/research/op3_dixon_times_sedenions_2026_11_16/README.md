# C⊗H⊗O⊗S: Dixon-Algebra mal Sedenionen (Erkundung, nicht blind)

16. November 2026. Frage des Autors: „was passieren würde, wenn man an die Dixon-Algebra noch die Sedenionen heranmultipliziert (also quasi
HS(7), wenn die Logik sich so fortsetzen lässt)“, präzisiert: C⊗H⊗O⊗S. Struktursätze, numerisch nachgerechnet; kein Datenvergleich, keine
H-Nummer. Skript `dixon_sedenions.py`, Ausgabe `run/dixon_sedenions_stdout.txt`.

## Vorwissen geprüft
- r13 und Notizen vom 13./14.11. (`../op3_sedenion_reference_2026_11_13.md`, `../op3_sedenion_charge_2026_11_13.md`,
  `../op3_sedenion_generations_estar_2026_11_14.md`, `../op3_third_generation_singlet_2026_11_14.md`): C⊗S (O durch S ersetzt, „Weg A“)
  trägt unter der Ladung Q_* zwei Generationen; der Zyklus ψ aus Aut(S) = G₂ × S₃ ist darin eine Phase, kein Generationsschritt.
- K28 (`../v4_8_0_r03_r12/llm/Trennung_Farbe_Generation.md`): S = (1,1) ⊕ (1,sgn) ⊕ (7,2) unter G₂ × S₃.
- Atlas r58/r59 und r27.2: Vorsicht vor „sedenionenartiger“ Erweiterung (Leckregister statt freier Sedenionen).
- `../op3_frame_algebras_observer_2026_11_16/`: Kopien von HS(8) = Kleinsche Vierergruppe der Frame-Abbildungen.
- Neu gegenüber dem Bestand ist nur das Produkt C⊗H⊗O⊗S (S **zusätzlich** zu O, nicht statt O).

## Ergebnis

**1. Die Stufe ist HS(10), nicht HS(7).** Jeder Faktor der Kette verdoppelt die Dimension nicht, sondern multipliziert sie:

| Träger | reelle Dimension | Stufe |
|---|---|---|
| C⊗H⊗O (Dixon) | 64 | HS(6) |
| C⊗H⊗O⊗C | 128 | HS(7) |
| C⊗H⊗O⊗H | 256 | HS(8) |
| C⊗H⊗O⊗O | 512 | HS(9) |
| **C⊗H⊗O⊗S** | **1024** | **HS(10)** |
| C⊗H⊗S (O durch S ersetzt) | 128 | HS(7) |

„Quasi HS(7)“ wäre C⊗H⊗S, also der Ersatz von O durch S (Weg A von r13, zwei Generationen). Setzt man die Logik des Turms fort, so heißt
der nächste Faktor C (HS(7), zwei Kopien) und danach H (HS(8), vier Kopien).

**2. Das Kopienregister von HS(8) ist schon ein H-Faktor.** In der Cayley-Dickson-Basis gilt für C, H, O und S gleichermaßen
$e_ae_b=\pm e_{a\oplus b}$ (Indizes bitweise XOR, geprüft): Die Einheiten bilden eine verdrehte Gruppe $\mathbb Z_2^k$. Für H sind das die
Kleinsche Vierergruppe und, bis auf Vorzeichen, die Frame-Abbildungen $-i\sigma_z,-i\sigma_x,-i\sigma_y$ ($R$, $T$, $J_B$; geprüft). Die
Lesart „Algebra je Frame, Kopie 00 als Betrachter“ ist also wörtlich C⊗H⊗O⊗H: ein zweites H, dessen Einheiten die Frame-Abbildungen sind.
Ein S-Faktor gäbe 16 Kopien mit $\mathbb Z_2^4$; auf $\chi$ gibt es aber nur vier Frame-Abbildungen (r16.7). Zwölf Kopien hätten keine
Frame-Bedeutung.

**3. Was S gegenüber einer bloßen Kopienverdopplung ändert.** Als Vektorraum ist S = O ⊕ O·e₈, also C⊗H⊗O⊗S = (C⊗H⊗O⊗O)². Neu ist allein
das verdrehte Produkt, und das bricht drei Eigenschaften, die O noch hat (geprüft an 2000 Zufallspaaren):
- keine Alternativität (Abweichung bis 1,3·10², bei O 10⁻¹⁴);
- keine Normmultiplikativität, $|ab|\neq|a||b|$ (Abweichung bis 6,6);
- Nullteiler: $(e_1+e_{10})(e_4-e_{15})=0$.

Für das Projekt heißt das: Produkte normierter Zustände sind nicht mehr normiert, und Gewichte hängen von der Reihenfolge der Produkte ab. Die
verschachtelten Normierungen (H107) und die Gram-Lesart ($|\det V|^2=\det G$, r25) setzen Normmultiplikativität voraus und gelten auf dem
S-Faktor nicht mehr. Nullteiler sind Kanäle, in denen ein von null verschiedener Zustand verschwindet. Das ist genau das Leck, vor dem der
Atlas warnt (Grund (b) in r27.2). Der Atlas setzt dafür Projektor und Leckregister ein; C⊗H⊗O⊗S bräuchte das auch.

**4. Clifford-Struktur: S gibt Cl(8) und damit Trialität.** Alle Linksmultiplikationen $L_{e_i}$ mit Basiseinheiten quadrieren zu −1, aber
höchstens 8 der 15 antivertauschen paarweise. Das ist genau die Radon-Hurwitz-Grenze auf $\mathbb R^{16}$. Bei O antivertauschen alle 7
(Grenze 7). Die acht erzeugen Cl(0,8) ≅ M₁₆(ℝ) auf S = ℝ¹⁶, also Spin(8) mit 8_s ⊕ 8_c. Der Dixon-Weg (Clifford aus Linksmultiplikation) setzt
sich deshalb nur mit einer Auswahl von 8 Einheiten fort, nicht mit allen 15.

**5. Eine Parallele, nicht gezeigt.** Das Zentrum von Spin(8) ist $\mathbb Z_2\times\mathbb Z_2$, und die Trialität vertauscht seine drei
nichttrivialen Elemente. Die Frame-Abbildungen bilden ebenfalls $\mathbb Z_2\times\mathbb Z_2$, und der Generationszyklus vertauscht $R$, $T$,
$J_B$ (H109, Zuordnungen Z1–Z3). r18 hat das Neutrino-ℤ₂ schon mit dem Spin(8)-Zentrum gleichgesetzt. Ob das S₃ von Aut(S) = G₂ × S₃ diese
Trialität ist und ob es die zyklische Frame-Zuordnung nativ liefert, ist hier nicht geprüft.

## Für OP3
C⊗H⊗O⊗S liefert keinen neuen Zahlenwert für den Rest 0,012376 und keine Festlegung der Sichtbarkeit λ aus der Betrachter-Erkundung. Was es
liefert, ist eine mögliche native Herkunft der Zyklussymmetrie der Frames (Punkt 5, offen). Der Preis sind Nullteiler und der Verlust der
Normmultiplikativität, also genau die Eigenschaften, auf denen die Kopien- und Gram-Lesarten stehen. Ohne Leckregister ist der Träger für
diese Lesarten nicht brauchbar. Kein Test angelegt. OP3 offen.
