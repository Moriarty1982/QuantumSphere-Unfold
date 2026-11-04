# Ergebnis H66: bestätigt (nicht blind). R ist auf Werteebene kovariant

Grundlage ist die Vorab-Notiz H66 (f62dce4, vor der Rechnung). Gerechnet hat `k166_kovarianz_werte.py`: das Verfahren von k165b mit Saat 66 und fünf Paaren, dazu eine negative Kontrolle. Das Log ist `k166_log.txt`.

| Fall | F | G | dg | Mischung zwischen Blöcken |
|---|---|---|---|---|
| Kontrolle positiv | 1.6e-14 | 3.2e-13 | 3.3e-14 | 5e-13 |
| Kontrolle negativ (Hintergrund fest) | **57** | **1.2e3** | 6.3 | 1.5e3 |
| reine Drehung | 1.2e-13 | 1.2e-12 | 5.9e-14 | 3e-12 |
| reiner Boost | 6.6e-14 | 3.4e-13 | 8.8e-15 | 7e-13 |
| reine Koordinatenänderung | 6.3e-12 | 1.9e-11 | 2.2e-11 | 5e-11 |
| gemischt 1 | 3.2e-13 | 1.4e-11 | 1.2e-12 | 3e-11 |
| gemischt 2 | 1.0e-13 | 2.4e-12 | 2.1e-14 | 2e-11 |

## Prüfung der Kriterien
- Die positive Kontrolle liegt bei ≤ 1e-9.
- Die negative Kontrolle liegt bei ≥ 1e-3.
- Alle Testwerte liegen bei ≤ 2.2e-11, also unter 1e-8.

**H66 ist bestätigt.**

## Lesart
- R ist kovariant, und zwar mit allen Termen niedrigerer Ordnung, außerhalb der Lösungsmenge und unter linearen Koordinatenänderungen wie unter inneren Lorentz-Transformationen. Der Hintergrund wird dabei tensoriell mittransformiert.
- Die Zeilentransformation C hat Blockgestalt.
- Ω wird aus R allein abgeleitet und ist damit kovariant.
- Die vier Bedingungen stammen aus R zusammen mit der Eichung. Sie sind höchstens unter so(1,2) kovariant, dem Stabilisator der Eichung nach H65(b).
