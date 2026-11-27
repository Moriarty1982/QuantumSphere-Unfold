# Ergebnis H189: Auch über ein drehendes Vakuum erreichen die Ableitungsterme die Quarkmassen nicht

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H189_Bewegtes_Vakuum_und_Quarkmassen.md` (Commit 017a2be, vor der Rechnung). Skripte
`k392_test_h189.py` (`k392_out.txt`) und `k392b_gegenprobe.wl` (`k392b_out.txt`).

Werkzeuge: Python (numpy, scipy): quadratische Formen exakt durch Polarisation auf den 36 Farbrichtungen von ℂ ⊗ H₃(𝕆), Moden wie k390, vier
Vakua; Prüfung gegen die Daten als exakte Zulässigkeitsfrage (lineare Ungleichungen in den zwei Kopplungen, Ecken aufgezählt), Zufallskontrolle
mit 2000 erfundenen Datensätzen. Wolfram Language: H189a symbolisch, H189b exakt, H189c (Variante 1) im reduzierten Modell mit denselben
Funktionen. Qiskit nicht eingesetzt. Warnungen in Wolfram: nur Hinweise der Auswerteumgebung.

**Ergebnis in einem Satz:** Bei drehendem Vakuum ändern K₁ bis K₄ nicht die Ruhefrequenzen, sondern nur die Ausbreitung der Farbschwingungen,
und zwar mit sauber bestimmten Funktionen des Paars; die träge Masse, die daraus folgt, trifft die sechs Quarkmassen in keinem der 24 Fälle
(bester Abstand 14σ).

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H189a | K₁, K₂, K₄ verschwinden für ∂_xδW = 0 identisch (auch bei bewegtem Vakuum); K₃ ist von der Ordnung ε⁴ | exakt null | **bestätigt** (nicht blind) |
| H189b | Ruhefrequenzen √h ± ω; Aufspaltung 2ω für jede Generation und beide Ladungen gleich (Abweichung 10⁻¹⁴) | unabhängig von Generation und Ladung | **bestätigt** (nicht blind): die Drehung allein gibt die Massen nicht |
| H189c | alle sechs Gradientenformen diagonal in den Moden (Eigenrest ≤ 2·10⁻¹³), Funktionen des Paars (Rest ≤ 7·10⁻¹⁴), ladungsgerade | Rest und Eigenrest < 10⁻⁸ | **bestätigt** |
| H189d | kein Fall unter 3σ; bester Abstand 14,1σ (Variante 1, Zuordnung B, κ₂ und κ₄) | alle vier Verhältnisse < 3σ | **widerlegt** |
| Kontrolle | 2000 erfundene Datensätze: Treffer nur mit κ₂ oder nur mit κ₄ 0,00 %; mit beiden 3,95 % (Kontroll-Lesart 2,85 %) | Bericht | – |

Verglichen: 24 Fälle (2 Varianten, 2 Lesarten, 2 Zuordnungen, 3 Wahlen der Kopplungen), je 64 Paare von Potentialfunktionen.

Zu H189b: In der Vorab-Notiz steht √(h + ω²) ± ω; dort ist h die Krümmung im mitdrehenden Bild. Mit h als Krümmung des Potentials lautet die
Formel (Ω ± ω)² = h. Die Aussage (gleiche Aufspaltung für alle) ist dieselbe.

## Was die Ableitungsterme bei drehendem Vakuum tun (ohne Daten)
Hintergrund X_t = B₀ = ∂_tW, Schwingung mit Gradient ∂_xδW in einer Farbrichtung zum Paar (i, j); l_k ist der dritte Eigenwert. In zweiter
Ordnung entsteht je Term eine Gradientenform (Koeffizient von (∂_xδW)², bei ω = 1, je Einheit der Koordinatennorm):

| Term | Variante 1 (W = e^{iωt}W₀) | Variante 2 (U auf den Nebendiagonalen) |
|---|---|---|
| K₁ Fläche | 2(l_i² + l_j²) + 2l_k² = 2 Tr W₀² (konstant) | konstant (6 am Lepton-Vakuum) |
| K₂ Kommutator | **2(l_i − l_j)²** | ⅔(l_i² + l_j²) + 4/3 l_i l_j − 8/3 l_k(l_i + l_j) + 8/3 l_k² |
| K₄ Normdefekt | **−2(l_i² + l_j²) − 4l_k²** = −2 Tr W₀² − 2l_k² | −2(l_i² + l_j²) + 8/3 l_i l_j + 4/3 l_k(l_i + l_j) − 4/3 l_k² |

- Alle Formen sind für Ladung ⅓ und ⅔ gleich. Die Ableitungsterme unterscheiden Up und Down nicht.
- K₃ trägt in zweiter Ordnung nichts bei (drei Richtungen nötig).
- In Variante 2 sind g₂ und g₄ bis auf eine Konstante dieselbe Funktion (g₂ − 3g₄ = 5g₁); dort gibt es nur eine unabhängige Kopplung.
- Lesart: Die Schwingung zum Paar (i, j) breitet sich mit c² = 1 + κ₂g₂ + κ₄g₄ aus. K₂ misst den Abstand der zwei Eigenwerte des Paars, K₄ den
  dritten Eigenwert. Das ist hergeleitet, nicht gewählt.

## Gegen die sechs Massen
Träge Masse m_g = A·√f_g/(1 + κ₂g₂ + κ₄g₄), f aus R je Sektor frei, κ für beide Sektoren gleich. Bester Abstand (größte Abweichung der vier
Verhältnisse beim besten κ):

| Variante, Zuordnung | nur κ₂ | nur κ₄ | κ₂ und κ₄ |
|---|---|---|---|
| 1, A | nicht erreichbar | 49,6σ | 28,8σ |
| 1, B | 66,7σ | 63,5σ | **14,1σ** |
| 2, A | nicht erreichbar | nicht erreichbar | nicht erreichbar |
| 2, B | 66,7σ | 66,7σ | 66,7σ |

Kontroll-Lesart m = A·f/(…): bester Abstand 22,8σ. „Nicht erreichbar“ heißt: Mit positiven Nennern lässt sich die Reihenfolge der Massen nicht
herstellen. Im besten Fall stehen die Nenner im Verhältnis 2885 : 88 : 1; die schwerste Generation entstünde dadurch, dass ihre
Ausbreitungsgeschwindigkeit fast null wird. Auch mit dieser Feinabstimmung bleibt der Abstand bei 14σ.

## Lesart
- **Die Ableitungsterme sind als Quelle der Quarkmassen in dieser Lesart ausgeschöpft.** Ruhendes Vakuum: kein Beitrag (H188). Drehendes
  Vakuum: nur die Ausbreitung ändert sich, für beide Ladungen gleich, und die daraus folgende träge Masse trifft nicht.
- **Up und Down werden von keinem der Ableitungsterme getrennt.** Der einzige bisher bekannte Unterschied bleibt der Term mit dem
  Ladungsoperator im Potential (H182, H186).
- **Als Nebenergebnis bleibt** die Herleitung der Gradientenformen, die für jede spätere Rechnung mit drehendem Vakuum gilt.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger, Vakuumwert, Symmetrie | wie H185 bis H188 | – | – |
| Bewegung | W = e^{uωt}W₀, u = i oder U; homogen | Aufspaltung ±ω für alle gleich | ob es diese Lösung gibt (Potential) |
| Ableitungsterme | K₁ bis K₄ mit Matrixprodukt und hermitescher Norm | Gradientenformen je Paar, ladungsgerade | – |
| Masse | träge Masse Ω₀/c², Ω₀² aus R | kein Fall trifft | welche Abbildung gilt |

Zur Regel „Bilanz der Setzungen“: H184 bis H189 betreffen dieselbe offene Voraussetzung (Quarkmassen als Farbschwingungen um das
Leptonvakuum). Sechs Tests haben Zahl und Form der Zustände bestätigt und jede geprüfte Quelle für die Massen ausgeschlossen oder als frei
erwiesen: Potential (H184, H185), Ladungsterm (H186), Adjunkte (H187), kinetische Normierung (H188), Ableitungsterme (H188, H189). Die
stillschweigende Annahme, die dem Autor vorgelegt wird, ist die Lesart selbst.

## Grenzen
Keine Lösung der vollen Feldgleichung: Existenz und Stabilität des drehenden Vakuums nicht geprüft; die Verschiebung ±ω der Ruhefrequenz in
H189d nicht mitgeführt. Nicht gerechnet: räumlich verdrehte Vakua (∂_xW₀ ≠ 0), Drehungen in den Generationen (SU(3) ⊂ F₄), andere
Produktordnungen in K₂ und K₄. Wolfram-Gegenprobe zu H189c nur für Variante 1 im reduzierten Modell. Massen bei M_Z ohne Laufen. Kein Vorzeichen
gesetzt. Die nachträgliche gemeinsame Form aus H188 ist hiervon nicht berührt und bleibt ungeprüft. OP3 und OP4 bleiben offen.

## Nächster Schritt (Vorschlag, Entscheidung beim Autor)
Die Lesart wechseln: Quarks auf einer anderen HS-Stufe oder als getrennte Felder prüfen. Alternativ die gemeinsame Form aus H188 mit einer
unabhängigen Vorhersage testen oder Drehungen in den Generationen rechnen. Vergeben: H189, k392. Nächste frei: H190, k393.
