# Ergebnis H51: Cartan-Test des ϑ-geeichten OP5-Symbols

Vorab-Notiz: `Vorab_Notiz_H51_Cartan_Test_geeichtes_Symbol.md`, lokaler Commit 10693a0 (3. November 2026), vor der
Rechnung. Rechnung: `k137_cartan_test.py` (Protokoll `k137_log.txt`), Eichdaten aus `k136_eichung.py`
(`k136_eichdaten.npy`). Betrifft nur das OP5-Vergleichsmodell.

## Gültigkeit

- dim g'_p = 273, 371, 481, 606, 745 für p = 4…8. Das stimmt mit g_p − C(p+3, 3) und mit der Vorab-Notiz überein.
- Alle verwendeten Ränge haben saubere Lücken. Das kleinste Lückenverhältnis ist 1e7 (Kriterium: ≥ 1e4).
- Die Ungleichung dim g'_{p+1} ≤ Σ_k dim g'^{(k)}_p gilt überall. Die drei Koordinatensysteme (Seeds 1, 2, 3) geben
  dieselben Zahlen.

## Ergebnis: bestätigt

| p | dim g'^{(k)}_p, k = 0…3 | Summe | dim g'_{p+1} | Befund |
|---|---|---|---|---|
| 4 | 273, 85, 14, 0 | 372 | 371 | nicht involutiv |
| 5 | 371, 98, 14, 0 | 483 | 481 | nicht involutiv |
| 6 | 481, 111, 14, 0 | 606 | 606 | **involutiv** |
| 7 | 606, 125, 14, 0 | 745 | 745 | involutiv |

Das geeichte, Ω-erweiterte Symbol besteht den Cartan-Test erstmals bei p = 6, wie vorhergesagt.

## Lesart

- dim g'^{(3)} = 0: Nach der Eichung bleibt keine freie Funktion von vier Variablen. Die ϑ-Freiheit war die einzige.
- dim g'^{(2)} = 14 und g'_p = 481 + 125(p − 6) + 7(p − 6)(p − 5): Formal hängen die Lösungen, soweit das Symbol
  es sagt, von 14 reellen Funktionen von drei Variablen ab. Das ist die Größe von Anfangsdaten auf einer Hyperfläche.
- Die Ω-Gleichung (Ordnung 3) und die Vervollständigung (F, G, dg) zusammen mit der Eichung ergeben bei Ordnung 6 ein
  involutives Symbol. Die Grad-5-Frage aus `RANK_RESOLUTION_2026-10-30.md` verschiebt sich damit auf die Frage, ob
  das System bis Ordnung 6 formal integrabel ist.

## Grenzen

- Geprüft ist nur das Symbol. Für Involution des Systems fehlt die formale Integrabilität: Die Projektion R'_7 → R'_6
  des geeichten Systems muss surjektiv sein, also ohne neue Integrabilitätsbedingungen. Das ist der nächste Schritt.
- θ stammt vom älteren Keim (Abweichung etwa 1e-7). Die Lücken (≥ 1e7) sprechen für Struktur, eine Wiederholung mit
  hochgenauem θ steht aus.
- Kein Existenzsatz für das QSC-Modell. OP5 bleibt offen.
