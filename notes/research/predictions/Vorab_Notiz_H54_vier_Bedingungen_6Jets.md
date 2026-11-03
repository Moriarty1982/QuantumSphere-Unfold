# Vorab-Notiz H54: Genau vier versteckte Bedingungen an 6-Jets

Festgeschrieben vor der Rechnung (3. November 2026). Betrifft nur das OP5-Vergleichsmodell. OP5 bleibt offen.

## Ausgangslage

- H53 (ungültig): Über dem reparierten 4-Jet gibt F₇ P₅₆ = 852 (sauber), F₈ P₅₆ = 848.
- Erkundung `Erkundung_Spencer_geeichtes_Symbol.md`: H^{5,2}(g') = 4. Höchstens 4 versteckte Bedingungen an 6-Jets
  sind möglich, also P₅₆ ≥ 852 − 4 = 848.
- Spektren von F₈ (bereits vorhanden, `f8_work`): volles F₈ … 9,8e-6, **2,7e-6** | 4,0e-12 …, Rang 7957.
  F₈ ohne die Spalten von c₅ und c₆: … 4,9e-6, 1,9e-7, 1,1e-7, **1,0e-9** | 2,9e-14 …, Rang 5445.
  P₅₆ = (10200 − 7957) − (6840 − 5445) = 848.
- Die reduzierte Matrix (Spalten c₇, c₈; Zeilen Grad 4 … 7) enthält **keine** Grad-3-Koeffizienten von A und B, nur
  Grad ≤ 1. Diese stammen aus der genauen m = 4, 5-Linearisierung.

## Argument (Weyl)

Ein Fehler ΔE verschiebt jeden Singulärwert um höchstens ‖ΔE‖₂. Ist der Fehler im vollen F₈ klein gegen 2,7e-6, kann
dessen Rang nicht kleiner als 7957 sein. Ist der Fehler der reduzierten Matrix klein gegen 1,0e-9, ist deren Rang
mindestens 5445. Daraus folgt P₅₆ ≤ 848. Mit der Spencer-Schranke folgt P₅₆ = 848.

## Hypothese H54

Über dem reparierten 4-Jet gibt es genau 4 versteckte Bedingungen an 6-Jets: P₅₆(F₈) = 848.

## Rechnung

1. Die Grad-3-Linearisierung (m = 5, 6) wird mit Speicherung der vier Einzelschätzungen B^{(ν)} wiederholt. Varianten:
   die zwei B^{(ν)} mit der größten Abweichung vom Mittel. ΔE_k = E(Variante k) − E(Standard), mit denselben Zeilen- und
   Spaltennormen wie E. η = max_k ‖ΔE_k‖₂ (relativ zum größten Singulärwert von E).
2. Fehler der reduzierten Matrix: Gleiches Vorgehen mit den vier Einzelschätzungen von B bis Grad 1 aus der
   m = 4, 5-Rechnung, η_red.
3. Volles F₈ mit jeder der zwei Varianten: Rang und Lücke.

## Kriterium

- **Bestätigt:** η ≤ 1e-8 (mindestens 270-fach unter 2,7e-6), η_red ≤ 1e-10 (mindestens 10-fach unter 1,0e-9), und
  beide Varianten geben Rang 7957 mit Lücke ≥ 1e4.
- **Widerlegt:** Eine Variante gibt mit sauberer Lücke einen anderen Rang, sodass P₅₆ ≠ 848.
- **Ungültig:** η > 1e-8 oder η_red > 1e-10 (Fehlerschranke zu grob) oder eine Variante ohne saubere Lücke.

## Grenzen

- Der Fehler wird empirisch aus der Streuung unabhängiger Schätzungen bestimmt, nicht streng beschränkt. Fehler in A
  vom Grad 3 werden nur über die B-Streuung mit erfasst; deshalb der große Sicherheitsabstand (270-fach).
- Bestätigt hieße: Das geeichte System ist am Keim bei Ordnung 6 nicht formal integrabel; es gibt 4 weitere
  Bedingungen. Wie sie lauten, ist damit nicht bestimmt.
