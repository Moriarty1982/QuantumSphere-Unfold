# Erkundungsprotokoll: Weinberg-Winkel und Tachyon-Kegel

Angelegt am 2026-10-21 nach dem Ergebnis von H14 (`llm/Ergebnis_H14_Kegelwinkel_Weinberg.md`). Skript
`llm/k44_erkundung_weinberg.py`.

## Regeln

1. **Kein Test.** Nichts in diesem Protokoll zählt als Bestätigung. Ein Test braucht eine eigene Vorab-Notiz mit einer
   Größe, die vor ihrer Festlegung unbekannt ist.
2. **Jede Variante wird eingetragen**, mit Ergebnis, auch Fehlschläge und Einfälle, die beim Rechnen auftauchen. Die
   Zahl der Einträge ist die Zahl der Versuche und geht in jede spätere Bewertung ein.
3. **Eingaben werden nicht nachträglich angepasst**, um einen Treffer zu erzeugen. Eine Variante ändert genau eine Sache
   und sagt, welche.
4. **Physik vor Zahl.** Eine Variante braucht eine physikalische Begründung, bevor sie gerechnet wird. Ist sie beim
   Rechnen aufgefallen, wird sie als „aufgefallen“ markiert.
5. **Ziel** ist eine Erklärung, die etwas Neues vorhersagt, nicht eine, die die Abweichung wegerklärt.

## Ausgangslage

Vorhersage aus ϑ_c = 2θ_W: sin²θ_W = (1 − β_sym)/2 = 0,22533 (β_sym = 0,54935). On-shell aus den Massen: 0,22321 ±
0,00026, MS-bar: 0,23122. Die Lücke zum On-shell-Wert beträgt +0,00212. Das entspricht einer um 110 MeV kleineren
W-Masse oder einer Änderung von Δρ um −0,00275.

Daten: PDG 2024 mit Update 2025 (Summary Tables; Review „Electroweak Model and Constraints on New Physics“, Stand
15. April 2026), abgerufen 2026-10-21. Δρ_t = 0,00934 · (m_t/172,61 GeV)² nach Gl. (10.16) dort. Die Varianten E2–E5 sind
Abschätzungen in führender Ordnung, mit einer Genauigkeit von etwa 10⁻³ in sin²θ_W.

## Einträge

| Nr. | Variante | Begründung | Ergebnis | Bewertung |
|---|---|---|---|---|
| E1 | β_sym durch den Tribonacci-Wert β_T = 0,54369 ersetzen | r01.3: γ_L liegt 1,37 % über 𝕋 (Gitterkorrektur) | Vorhersage 0,22816; Abstand zu on-shell +0,00495 statt +0,00212 | **Fehlschlag**: verschiebt in die falsche Richtung |
| E2 | On-shell-Winkel ohne den Top-Beitrag Δρ_t | Der Kegel käme aus der Feldstruktur, die von schweren Teilchen nichts weiß | On-shell ohne Top: 0,23039; Abstand −0,00506 | **Fehlschlag**: Das Herausrechnen schiebt den Messwert über die Vorhersage hinaus, nahe an MS-bar |
| E3 | Baumgraphen-Winkel aus (α, G_F, m_Z) | Wert ganz ohne Schleifen, mit α(0) bzw. α̂(M_Z) | 0,21215 bzw. 0,23361; Abstand +0,01318 bzw. −0,00829 | **Fehlschlag**: Die Wahl von α allein spannt 0,02 auf; kein Wert liegt nahe |
| E4 | Bruchteil von Δρ_t, der die Vorhersage genau trifft (*aufgefallen* beim Rechnen von E2) | keine | 70,5 % von Δρ_t, also ein Top-Beitrag wie bei m_t,eff = 145 GeV | **Kein Befund**: Die Zahl hat keine Bedeutung, weder m_W, m_Z noch m_H. Nur als Versuch gezählt |
| E5 | Neutrinos als fehlender Betrag (Vorschlag des Autors) | Neutrinos stecken in denselben Schleifen wie das Top-Quark; das Dokument behandelt Neutrinomassen eigens | siehe unten | **Fehlschlag** für alle bekannten Neutrinos; offen nur für neue Physik |

### E5 im Einzelnen

- **Richtung.** Nötig ist *weniger* Δρ als im Standardmodell, um 0,00275. Ein Dublett mit Massenaufspaltung liefert
  immer Δρ ≥ 0. Zusätzliche Teilchen dieser Art verschieben also in die falsche Richtung, wie das Top-Quark selbst.
- **Leichte Neutrinos.** Im Dublett mit dem Elektron tragen sie Δρ ≈ 3 · 10⁻¹⁴ bei. Nötig wäre 3 · 10⁻³, also elf
  Größenordnungen mehr. Ihre Masse ist zu klein, um irgendetwas zu bewirken.
- **Gemessene Massen.** Der On-shell-Winkel ist aus gemessenen Massen gebildet. Neutrinos können eine Messung nicht
  ändern. Sie könnten nur Teil einer Korrektur zwischen einem „strukturellen“ und dem gemessenen Winkel sein, wie in E2.
- **Was übrig bleibt.** Ein *negativer* Beitrag bräuchte neue Physik. Genannt werden in der Literatur etwa schwere
  Majorana-Teilchen oder Neutrinomischungen außerhalb der Unitarität. Das ist hier nicht nachgeprüft. Die Größe wäre
  erheblich, gleichwertig mit 110 MeV in m_W. Vor jeder weiteren Verfolgung müssten die bestehenden Schranken für solche
  Effekte geprüft werden.

## Stand

5 Versuche, 0 Treffer. Keine Variante hat die Lücke physikalisch erklärt. Die beiden naheliegenden Korrekturen, Top und
Tribonacci, verschieben in die falsche Richtung. Die Vorhersage liegt weiterhin zwischen den Schemata, ohne dass sich
ein Schema oder eine Skala als „das richtige“ ausweisen lässt.

## Offene Fragen

- Aus welcher Größe von Lesart B ließe sich ein Schema oder eine Skala ableiten, statt sie zu wählen?
- Lässt sich für E5 (negative Beiträge) eine Schranke aus der Literatur angeben, bevor weitergerechnet wird?
