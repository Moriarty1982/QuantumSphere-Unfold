# Ergebnis H53: Fortsetzung des ϑ-geeichten Systems über dem reparierten Jet bis Grad 4

Vorab-Notiz: `Vorab_Notiz_H53_Fortsetzung_ab_Grad4.md`, lokaler Commit 64fd43b (3. November 2026), vor der Rechnung.
Rechnung: `k140_fortsetzung_exakt.py`, für F₈ in Einzelschritten `k140_f8_schritte.py`; Protokoll `k140_log_H53.txt`.

## Verfahrensänderungen nach der Festschreibung (ohne Kenntnis von F₈-Ergebnissen)

- F₈ braucht A und B bis Grad 3. Die festgeschriebene Linearisierung reichte nur bis Grad 2 (Programmfehler, F₈ brach
  ab). Verallgemeinert: Sonden m = d + 2 und d + 3, Basis-Jet bis Grad d + 1. Für Grad ≤ 2 bleiben die genaueren
  m = 4, 5-Werte, für Grad 3 kommen m = 5, 6 hinzu. Die Grad-3-Werte sind ungenauer: Die Streuung der vier
  B-Schätzungen beträgt 2,6e-6 bei |B| ≈ 786, also etwa 3e-9 relativ.
- Wegen des Speichers (Container-Abbrüche) wird F₈ ohne Singulärvektoren ausgewertet: κ als Abstand der rechten Seite
  zum Bild von E (lstsq, Schnitt in der Ranglücke), Projektionen als P_S = dim ker E − dim ker(E ohne Spalten von S).
  Gegenprobe an F₇: κ 4,01e-12 statt 3,99e-12, Projektionen gleich.

## Messwerte

| Größe | Vorhersage | F₇ | F₈ |
|---|---|---|---|
| κ (Schranke 100·ε_ref = 4,6e-12) | ≤ 4,6e-12 | 4,0e-12 | **3,9e-10** |
| P₅ | 371 | 371 (Lücke 4e4) | 371 (Lücke **4e3**) |
| P₅₆ | 852 | 852 (3e8) | **848** (3e4) |
| P₅₆ − P₅ | 481 | 481 | **477** |
| P₅₆₇ − P₅₆ | 606 | – | 606 (1e10) |

Referenz ε_ref = 4,6e-14, Positivkontrolle κ_pos = 3,5e-3 (Verhältnis 8e10). Rang von F₈: 7957 (Lücke 7e5).

## Ergebnis: ungültig

Der Rang für P₅ in F₈ hat keine saubere Lücke (4e3 < 1e4). Nach dem Vorab-Kriterium ist der Test ungültig. Nach
Wortlaut wären auch T1 (κ(F₈)) und T2 (P₅₆ − P₅ in F₈) verfehlt.

## Was trotzdem feststeht

- **F₇ erfüllt alle Vorhersagen mit sauberen Lücken.** Über dem reparierten 4-Jet gibt es eine Fortsetzung bis
  Grad 7 (κ auf Rundungsniveau). Die 5-Jet-Faser hat die Dimension 371 und die 6-Jet-Faser über einem 5-Jet die
  Dimension 481, so viel wie das geeichte Symbol g'. Bis zu den Gleichungen vom Grad 6 gibt es also keine Bedingungen
  außer (F, G, dg), Ω und der Eichung.
- **F₈ zeigt 4 zusätzliche Bedingungen an 6-Jets**, falls die Werte echt sind: P₅₆ fällt von 852 auf 848, beide mit
  sauberer Lücke, sobald die Gleichungen vom Grad 7 dazukommen. Die Faser der 7-Jets hat dagegen genau dim g'_7 = 606.
  Die Zahl 4 passt zu H^{5,2} = 4 und zu dim g_7 = 726 gegen 722 bei zufälligem θ (Erkundung Symbolstruktur).

## Warum F₈ nicht entscheidet

Die kleinsten beteiligten Singulärwerte (1e-9 bei P₅₆, 2e-10 bei P₅) und κ(F₈) = 3,9e-10 liegen genau auf der
Fehlerhöhe der Grad-3-Linearisierung (etwa 1e-9 relativ). Ein Matrixfehler dieser Größe kann einen exakt
verschwindenden Singulärwert auf 1e-9 heben. Die 4 neuen Bedingungen sind deshalb möglich, aber nicht gesichert.

## Folgerung

- Die Linearisierung bis Grad 3 muss genauer werden: Sondenamplitude H anpassen, damit Rundung gegenüber dem linearen
  Anteil kleiner wird, oder höhere Genauigkeit (mpmath) nur für die Sonden.
- Danach als eigener Test (H54, mit Vorab-Notiz): Gibt es über dem reparierten 4-Jet genau 4 Bedingungen an 6-Jets,
  die erst mit den Gleichungen vom Grad 7 sichtbar werden (P₅₆(F₈) = 848 gegen P₅₆(F₇) = 852)? Falls ja, ist das
  geeichte System bei Ordnung 6 nicht formal integrabel. Die 4 Bedingungen wären dann ins System aufzunehmen und der
  Cartan-Test (H51) zu wiederholen.
