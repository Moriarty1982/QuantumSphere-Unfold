# Ergebnis H54: Genau vier versteckte Bedingungen an 6-Jets?

Vorab-Notiz: `Vorab_Notiz_H54_vier_Bedingungen_6Jets.md`, lokaler Commit ec705ec (3. November 2026), vor der Rechnung.
Rechnung: `k142_h54.py`, Protokoll `k142_log_H54.txt`. Betrifft nur das OP5-Vergleichsmodell.

## Abweichung vom festgeschriebenen Verfahren

Die festgeschriebenen Varianten (B vom Grad 3 durch Einzelschätzungen ersetzen) ändern F₈ nicht: B vom Grad 3 geht gar
nicht ein (|β| − |α| ≤ 2), nur A vom Grad 3. ΔE war exakt 0 (nan in der Normrechnung). Das hätte η = 0 trivial
„bestanden“. Stattdessen der in der Notiz angekündigte Ersatz: A vom Grad 3 wird für jedes μ um die gemessene Streuung
B^{(ν)} − B̄ vom Grad 3 verschoben. Das ist strenger als festgeschrieben.

## Messwerte

| Größe | Schranke | Messwert |
|---|---|---|
| η_red (reduzierte Matrix, Grad ≤ 1) | ≤ 1e-10 | 7,3e-13 und 3,1e-13 |
| η (volles F₈, Ersatzvariante) | ≤ 1e-8 | 4,9e-9 und 2,2e-9 |
| Rang volles F₈, Variante ν = 0 | 7957, Lücke ≥ 1e4 | 7957, Lücke **3e3** |
| Rang volles F₈, Variante ν = 2 | 7957, Lücke ≥ 1e4 | 7957, Lücke **7e3** |

## Ergebnis: ungültig

Beide Varianten haben eine Lücke unter 1e4. Nach dem Vorab-Kriterium ist der Test ungültig.

Das Kriterium war in sich unvereinbar: Die absichtlich gestörte Matrix hat ein Rauschniveau in der Größe der Störung
(etwa 1e-9). Das Verhältnis zu 2,72e-6 kann damit nicht 1e4 erreichen. Das war vorher absehbar und ist ein Fehler der
Testplanung, nicht der Rechnung.

## Was trotzdem feststeht

Alle Bausteine des Weyl-Arguments sind erfüllt:

- Die reduzierte Matrix (Spalten c₇, c₈) hat einen Fehler von höchstens 7e-13. Ihr kleinster gezählter Singulärwert
  1,0e-9 ist damit 1400-fach gesichert; Rang ≥ 5445.
- Das volle F₈ hat einen Fehler um 5e-9, also 550-fach unter dem kleinsten Nicht-Null-Wert 2,72e-6. Auch unter beiden
  gestörten Varianten bleibt der Rang 7957, und die Werte oberhalb der Lücke ändern sich in keiner angezeigten Stelle.
- Daraus folgt P₅₆ ≤ 848. Mit H^{5,2}(g') = 4 (Erkundung) folgt P₅₆ ≥ 848.

Inhaltlich spricht damit alles für genau 4 versteckte Bedingungen an 6-Jets über dem reparierten 4-Jet. Das geeichte
System wäre bei Ordnung 6 nicht formal integrabel. Formal ist das nicht bestätigt.

## Folgerung

Ein echter Test braucht neue Daten, nicht dieselben Matrizen mit besserem Kriterium. Vorschlag H55: einen anderen
Grundpunkt der Faser über dem 3-Jet wählen (reparierter 4-Jet plus ein Element von g'_4, auf R₄ zurückgeführt) und
dort vorher P₅₆(F₈) = 848 und P₅₆(F₇) = 852 vorhersagen. Danach die 4 Bedingungen explizit bestimmen, ins System
aufnehmen und den Cartan-Test (H51) wiederholen.
