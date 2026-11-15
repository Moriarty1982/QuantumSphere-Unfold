# OP3/OP1: Der Kern als Schatten eines Horizonts auf der Generationskugel

15. November 2026, Claude Opus. **Erkundung, nicht blind** (γ_M, π/4 − 2/3 und die Daten waren bekannt). Idee des
Autors: „naja, die eine kugel könnte einen schatten auf die andere werfen“, danach „halte das fest und lass uns sehen
was man damit machen kann“. Keine H-Nummer, kein CT-Eintrag, Guards unverändert. Einordnung T6, T8, T11, OP1, OP3.
Skript `shadow.py`, Ausgabe `run/shadow_stdout.txt`.

## Ausgangslage
Nach `../op3_guarded_core_flux_2026_11_15/README.md` und `../op1_i1_string_endpoints_2026_11_15/README.md` ist die
Generationsseite fertig: Oktant, flussfreier Kern im Dreieck, genau ein Kern, Gegenpol über die Umkehrwalze. Es fehlt
eine Brücke vom Horizont (Punktierungen, Zählregel je Frame) zur Generationskugel. Offen sind die Kerngröße und OP1.

## Vorwissen geprüft
- **Anker im Paper:** v470/12, Bemerkung `rem:hc-shadow-vs-core` („HC shadow versus HC kernel“). Verschiedene
  Auslesungen zeigen verschiedene *sichtbare Schatten* desselben Kerns. Der Schatten ist frame-abhängig, der Kern
  nicht; „it is the shadow, not the core, that vanishes“. Ebenso v470/12, Zeile 803: „different regime-readings
  expose different visible shadows of one common kernel“.
- **CT-001 Schritt 2** (`../ct001_sector_reading_2026_11_14.py`): Sektorlesart A_j/r_j² = γ/2 für alle j.
- v470/10, Abschnitt zu Schwarzen Löchern: Der Horizont ist die Grenze des Zuständigkeitsbereichs der Sphaera.
- Ein Schwarzloch-Schatten (Synge, Photonensphäre) kommt im Companion nicht vor. Volltextsuche nach Synge und
  Photonensphäre: keine Fundstelle; „shadow“ nur im Sinn der Auslesung.

## Was der Schatten leistet
1. **Er ist die fehlende Sorte Abbildung.** Ein Schatten macht aus einer Querschnittsfläche in einem Raum einen
   Raumwinkel im anderen, grob Ω ≈ A/d². Gesucht war genau eine Abbildung „Punktierungsebene → Generationskugel“.
2. **Er ist von selbst flussfrei.** Aus dem Schatten kommt kein Licht. Das ist die flussfreie Kappe des Kernbildes,
   ohne Zusatzannahme.
3. **Er hat einen Anker im Paper:** Der Kern auf der Generationskugel ist der *sichtbare Schatten* des bewachten
   Kollapskerns (`rem:hc-shadow-vs-core`), ausgelesen in einem Frame.

## Die Größe: drei Proben
| Lesart | Ergebnis | gegen γ_M = 0,237533 |
|---|---|---|
| Schwarzschild-Schatten (Synge), Beobachter bei r | Ω hängt von r ab: 3M Halbhimmel, 6M 1,840 sr, 10M 0,720 sr | Ω = γ_M erst bei r = 17,99 M (8,99 r_s); kein ausgezeichneter Abstand |
| Abstand aus dem Frame-Versatz (1 − 2M/r = 1 − β_sym², r = 6,63 M) | Ω = 1,537 sr | viel zu groß |
| flacher Schatten mit der Sektorlesart A/r² = γ/2 (CT-001) | Ω = γ/2 | halb so groß |

„Fast genau 9 r_s“ ist Zahlenspielerei und wird nicht verwertet: 18 M gibt 0,23719 statt 0,23753.

## Folgerungen
1. **Der Faktor 2 lässt sich nicht über die Ladung beheben** (`charge.py`, Ausgabe `run/charge_stdout.txt`). Zuerst
   lag nahe: Ein Spin-1-Objekt hat die Berry-Ladung 1 pro Steradiant, und dann gäbe der flache Sektorschatten
   Ω = γ/2 genau das Defizit γ/2. Die Rechnung zeigt, dass das nicht trägt:
   - Bei Spin ½ liegen drei Zustände mit Überlappung ½ im Abstand 90° (Oktant), Gram-Rang 2, Phase π/4. Der Kern
     muss dann Ω = γ_M haben (Kappenbild); der Sektorschatten liefert nur die Hälfte.
   - Bei **Spin 1** liegen drei kohärente Zustände mit Überlappung ½ im Abstand von 65,53° (cos = √2 − 1). Sie spannen
     schon von selbst C³ auf (**Gram-Rang 3**), und ihre Phase ist **3·arccos(1 − 1/√2) − π = 0,679042**. Sie sind also
     ohne jeden Kern schon gebogen, mit Wurzel-Verhältnissen 1 : 16,24 : 65,93 statt 1 : 14,38 : 58,97. Bis zur
     Lepton-Phase 2/3 fehlen nur noch 0,012376 rad. Der Sektorschatten (γ/2 = 0,1188) wäre dafür fast zehnmal zu groß.

   Die Ladung löst den Faktor 2 also nicht. Nebenbefund: Das Spin-1-Dreieck ist ein exakt bestimmtes, von selbst
   gebogenes Objekt mit drei positiven Massen, liegt aber deutlich neben den Leptonen.
2. **Der Schatten muss im Frame M gelesen werden.** Ein Schatten ist frame-abhängig (Aberration). Die Leptonmassen
   dürfen aber nicht von der Bewegung des Beobachters abhängen. Der Schatten, der die Massen bestimmt, muss deshalb
   in einem ausgezeichneten Frame gelesen werden, dem Ruhframe der Materie, also M. Zusammen mit r10.3 (das
   Flächenquant ist frame-abhängig) folgt: Der Kern hat die Größe des M-Quants γ_M, nicht des T-Quants γ_T. Das gibt
   dem Guard „Ende im Frame M“ von CT-002 einen Grund. Lesart, nicht hergeleitet.
3. **Das Verhältnis der Frames ist zirkulär.** Sieht T denselben Kern lorentzkontrahiert, ist das Verhältnis der
   Schatten ein Lorentz-Faktor zwischen den Frames, also γ_L = cosh 2η (r63). Das ist schlüssig, aber η ist über
   dasselbe γ_L definiert (β_sym = tanh η). Für OP1 folgt daraus nichts Neues.
4. **Drei Platzhalter in einem Bild.** CT-001 (Einheit), CT-002 (eine Punktierung, Frame M) und die Kerngröße lassen
   sich als ein Satz lesen: *Der Kern ist der im Frame M gelesene Schatten einer einzelnen Punktierung auf dem Himmel
   des Beobachters.* Offen bleibt die Größe: Bei Spin ½ muss der Schatten Ω = γ_M haben, der Sektor gibt nur γ/2. Das ist
   eine Zusammenfassung, keine Herleitung; eine neue Zahl folgt nicht.

## Was man damit noch machen kann (nicht gerechnet)
- **Ladung:** geprüft, siehe Folgerung 1; der Faktor 2 bleibt.
- **Ein Kern aus einem Schatten:** Ein einzelner Horizont wirft genau einen Schatten. Das passt zur topologischen
  Auszeichnung von genau einem Kern und wäre ein zweiter, unabhängiger Grund für „eine Querung“.
- **Gegenpol:** Licht, das um den Horizont herum gebogen wird, erscheint als Ring um den Schatten, nicht am Gegenpol.
  Ob der Gegenpol der Umkehrwalze im Schattenbild einen Platz hat, ist offen.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
