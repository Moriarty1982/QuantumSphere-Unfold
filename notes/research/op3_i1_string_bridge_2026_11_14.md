# Erkundung: I1 als Ausweg für CT-002, ein String vom Lepton-Sektor zu einer Horizont-Punktierung

14. November 2026. Autorenentscheidung: „Ja, I1 verfolgen“ (Zurückgestellte Idee I1, Auslöser 4). Erkundung, nicht
blind: Das Ziel (γ_M/2) war bekannt, und die Bedingung „eine Lichtquerung“ wurde mit diesem Ziel gewählt. Es gibt keine
H-Nummer, keinen MMA-Beleg und keine Änderung an Guards. Einordnung T5/T8/T11, OP3. Skript
`op3_i1_string_bridge_2026_11_14.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `counterterms/CT-001_gamma_halbe_einheit_entwurf.md`, Schritte 1–3:
  - Die ½ ist die normierte Sektorfläche.
  - Der Wert von γ_M stammt aus der Zählregel.
  - γ ist im Unruh-Bild von r10.1 die γK-Phase pro Radiant und Spingewicht.
  - Offen ist allein die Kopplung (CT-002): Warum durchläuft der Lepton-Fluss genau einen Radianten? Die Daten geben
    κ = 0,99964 ± 0,00016.
- `v4_10_0_w1/Zurueckgestellte_Ideen.md`, I1: Schon zweimal ausgelöst (5.11.: H78-Lichtkegel, Konnektormassen und
  Stringstufen). `op3_string_length_exploration_2026_11_12.md` hat I1 nicht als Mehrsystem-Wirkung aktiviert. Eine
  Rechnung zu einem String, der an einer Horizont-Punktierung endet, gab es nicht.
- r10.1 (Frodden–Ghosh–Perez, Unruh-Statistik): Der Horizont ist im euklidischen Bild das Zentrum, die euklidische Zeit
  der Drehwinkel.

## Rückwärts: was der String leisten muss
1. Ein Ende liegt an einer Horizont-Punktierung (Frame M, also γ_M), das andere im Lepton-Sektor.
2. Die Phase am Ende ist γ × (normierte Fläche), was nach Schritt 3 der γK-Lesart entspricht.
3. Die Dauer muss aus der Stringgeometrie selbst folgen und **einen** Radianten geben.

## Ergebnis

**1. Die Weltfläche ist ein Kreissektor.** Ein gerader String vom Horizont bis zum Abstand ℓ überstreicht im
euklidischen Bild einen Sektor mit A_ws = ℓ²φ/2. Das freie Ende läuft den Bogen s = ℓφ. Also gilt A_ws/s = ℓ/2 für
jede Dauer; das ist der Autorhinweis „Kreisfläche im Verhältnis zur Bogenlänge“.

**2. Vier Dauerbedingungen, vorab aufgelistet:**

| Bedingung | φ | A_ws/ℓ² | ΔΦ = γ_M · A_ws/ℓ² | gegen die Daten |
|---|---|---|---|---|
| (a) eine Lichtquerung, s = ℓ | 1 | ½ | 0,118767 | +2,2σ (wie H102) |
| (b) halbe Querung, s = ℓ/2 | ½ | ¼ | 0,0594 | ausgeschlossen |
| (c) hin und zurück, s = 2ℓ | 2 | 1 | 0,2375 | ausgeschlossen |
| (d) thermischer Umlauf | 2π | π | 0,746 | ausgeschlossen |

Nur (a) passt. Mit ihr ist **Bogen = Stringlänge**, und daraus folgt A/ℓ² = ½. Die ½ kommt damit aus derselben
Fläche wie der Radiant, ohne dass |m| = ½ angenommen werden muss.

**3. Lorentzsche Fassung.** φ wird zur Rapidität η. Die Eigenzeit des freien Endes ist ℓη. Eine Lichtquerung eines
Stabs der Länge ℓ in seinem momentanen Ruhesystem dauert ℓ, also η = 1. „Ein Radiant“ heißt damit: **Die Information
quert die Brücke einmal.** Das ist genau die Rolle des Strings in I1 („Brücke, über die Information läuft“).

**4. Übereinstimmung mit Schritt 3.** γ·w·κ mit κ = φ = 1 und w = ½ ist dieselbe Zahl wie γ·A_ws/ℓ².

## Bewertung
- **I1 liefert eine geschlossene Lesart für CT-002:** Der Lepton-Fluss ist die γK-Phase, die bei **einer
  Informationsquerung** eines Strings zu einer Horizont-Punktierung anfällt. Sie ist gleich γ_M mal der normierten
  Weltfläche dieser Querung, also γ_M/2. Damit ist die Kette vollständig, und jeder Faktor hat eine Herkunft:
  - γ_M: Zählregel;
  - Winkelbedeutung: Unruh-Bild;
  - ½ und der eine Radiant: Sektor mit Bogen = Länge.
- **Was das nicht ist:** keine Herleitung. Offen und als Guards zu führen sind:
  - warum genau eine Querung und nicht mehrere;
  - warum der String an einer Punktierung des Materie-Frames endet;
  - die Fortsetzung zwischen euklidischem Winkel und Rapidität, also Phase gegen Gewicht;
  - die Stringdynamik selbst, denn ein gerader, ruhender String ist nur angenommen.
- Die Bedingung (a) wurde mit bekanntem Ziel gewählt. Die Tabelle zeigt nur, dass die naheliegenden Alternativen nicht
  passen; das ist eine Auswahl unter vier und kein Test.
- Die Daten liegen 2,2 bis 2,3σ neben einer Querung (κ = 0,99964 ± 0,00016). Das ist die Spannung von H102, und die
  nächste PDG-Ausgabe entscheidet darüber.
- OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert. H100 und H102 bleiben unberührt.

## Nächste Fragen
- Gibt es in der String-LQG-Lesart (T11, `thm:string-lqg-duality`) einen Grund für **eine** Querung, etwa als kleinste
  Anregung oder als Shift um eine Stufe (Autorhinweis vom 5.11. zur QAM-Verschiebung)?
- Ließe sich daraus eine Vorhersage mit neuer Information gewinnen, etwa für die Neutrinophase oder für die
  Quarkfamilien? Dafür wäre vorher eine Vorab-Notiz nötig.
