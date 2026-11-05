# Vorab-Notiz H66: R ist auf Werteebene kovariant (Wiederholung von H65(a) mit tragfähiger Kontrollschranke)

**Geschrieben und committet am 4. November 2026 vor der Rechnung. Status: vorregistriert, nicht blind.** Die Werte aus Lauf 2 von H65 sind bekannt.

## Vorwissen geprüft
- H64 zeigt Kovarianz auf Symbolebene.
- H65(a) ist ungültig: Lauf 2 lag bei Residuen ≤ 1.1e-10, die Kontrolle bei ≤ 5.6e-11, die Schranke war 1e-12.
- H65(b) bestätigt den Stabilisator der Eichung als so(1,2).
- Eine andere Prüfung von R auf Werteebene liegt nicht vor (Suche wie bei H65).

## Messung (`k165b_werte.py`, unverändert, neue Saat)
- Für jedes feste (M, S) wird C = R'·R⁺ aus 80 zufälligen Datensätzen außerhalb der Lösungsmenge bestimmt.
- Geprüft wird an 20 weiteren Datensätzen. Gemeldet wird das größte relative Residuum je Block F, G und dg sowie die Mischung zwischen den Blöcken.
- Geprüft werden fünf Paare (M, S) mit neuer Saat 66: eine reine Drehung, ein reiner Boost, eine reine Koordinatenänderung und zwei gemischte Paare.

## Hypothese H66
R ist auf Werteebene kovariant: Für jedes Paar sind alle Residuen ≤ 1e-8.

## Kontrollen
- Positiv: M = 1 und S = 1 ergeben ≤ 1e-9.
- Negativ: Bei gemischtem (M, S) werden die Hintergrundfelder A, ∂A und ∂h nicht mittransformiert. Das muss für F und G ein Residuum ≥ 1e-3 ergeben.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | alle Residuen ≤ 1e-8, beide Kontrollen erfüllt |
| widerlegt | ein Residuum ≥ 1e-5 bei erfüllten Kontrollen |
| ungültig | sonst |
