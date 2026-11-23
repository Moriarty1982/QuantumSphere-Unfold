# Zeitumkehr- oder Spiegelbild in der Familie der vervollständigten ersten Jets: unterbestimmt (Erkundung, 22./23.11.2026)

**Ergebnis in einem Satz:** Die vervollständigten Modellbedingungen R = (F, G, dg) legen am OP5-Keim nur 31 der 96 ersten Ableitungen fest.
In der verbleibenden Familie gibt es einen Jet, in dem der Gegenstrom-Block exakt das Zeitumkehrbild der mitlaufenden Blöcke ist, und
ebenso einen, in dem er exakt ihr Spiegelbild ist. Der erste Jet entscheidet die Frage also nicht, und der Befund „keines passt“ aus r42 hängt
an der gespeicherten Lösung. **Nach dem vorab festgelegten Raster: unterbestimmt.**

Auftrag des Autors: „weiter“ nach r42. Verfahren vorab: `Methoden_Notiz.md` (Commit 1a23dd7a). Teilweise nicht blind (Abzählung
31 + 40 < 96). Skript `jet_family_images.py` (Python, mpmath 40 Stellen; Keimordner und Repo-Wurzel als Argumente; der feste Pfad im
vorhandenen Bau wird beim Laden ersetzt). Wolfram nicht nötig, Qiskit nicht geeignet. Keine H-Nummer.

## Läufe
- `run/jet_family_images_lauf1.txt`: ungedämpftes Newton-Verfahren mit 3 Schritten. Bildbedingungen erfüllt, R aber nicht (|R| = 0,30
  bis 3,8): zu wenige Schritte, ohne Aussage.
- `run/jet_family_images_lauf2_abbruch.txt`: Abbruch durch einen Definitionsfehler im Skript (`STEPS`), vor dem Newton-Teil.
- `run/jet_family_images_lauf3.txt`: maßgeblich. Gedämpftes Newton-Verfahren (Halbierung, bis zu 12 Schritte), unabhängige Zeilen einmal
  gewählt, Verlauf je Schritt.

## Ergebnis (Lauf 3)
| Schritt | Befund |
|---|---|
| (1) Ausgangsjet | vervollständigt gegen primitiv: Abstand 1,7·10⁻¹⁴, \|R\| = 2·10⁻⁴⁰; r42-Maß unverändert (T 1,28, R 1,87, I 0,72) |
| (2) Familie | Jacobi-Matrix von R: Rang 31 von 32, also eine 65-dimensionale lineare Familie. [R; m_X] hat für X = T, R, I vollen Rang 71; [R; m_T; m_R] Rang 79 von 111 |
| (3) T | nach 9 Schritten \|R\| = 1,7·10⁻⁴⁰, Bildabweichung 7·10⁻⁴¹; verträglich. Änderung der Ableitungen bis 3,2 |
| (3) R | nach 8 Schritten \|R\| = 3,0·10⁻⁴⁰, Bildabweichung 3·10⁻⁴¹; verträglich. Änderung bis 2,6 |
| (3) I | nach 12 gedämpften Schritten \|R\| = 0,15, Bildabweichung 0,019; nicht erreicht |
| (4) T und R zugleich | Liniensuche bei kleinster Dämpfung, kein Fortschritt (\|R\| wächst auf 1,3·10⁻⁶, Bildabweichungen bleiben 1,28 und 1,87); nicht erreicht |

## Lesart
- Am ersten Jet ist die Frage aus r41 nicht zu entscheiden: Sowohl ein lokales Zeitumkehrbild als auch ein lokales Spiegelbild sind mit
  allen Modellbedingungen verträglich. Erst höhere Ordnungen oder eine regionale Lösung könnten unterscheiden.
- Korrektur der Lesart aus r42 (r42 bleibt unverändert, append-only): „keines passt“ beschreibt die gespeicherte Lösung, nicht den Keim.
  Die Einschränkung der Gleichgewichtung auf den Keimpunkt gilt nur in diesem Sinn.
- Dass T und R nicht zugleich erreicht wurden und I nicht, ist ein Befund dieses Verfahrens, kein Unmöglichkeitsbeweis.
- Die verträglichen Jets ändern die Ableitungen um Beträge der Größenordnung 3; sie liegen nicht nahe an der gespeicherten Lösung.
- OP5 und H96 bleiben offen; OP3 ruht und wird nicht berührt.
