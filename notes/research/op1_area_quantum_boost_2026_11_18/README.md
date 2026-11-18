# OP1: Kann ein Boost das Flächenquant ändern? Literaturprüfung zu r10 (Erkundung, keine Rechnung, 18.11.2026)

**Ergebnis in einem Satz:** Nein, ein unitär wirkender Boost ändert das Flächenspektrum nicht (Rovelli–Speziale). Damit kann das
frame-abhängige Flächenquant, mit dem die Zuordnung DL → M, ABCK → T nach r10 gleichwertig ist, weder aus dem Boost-Anteil noch aus dem
Dualitäts-Anteil der Frame-Abbildung kommen. Übrig bleiben eine nicht-unitäre Frame-Abbildung oder die Lesart über Mittelwerte statt Eigenwerte.

Auftrag des Autors: „Weiter an OP1“. Literatur mit dem verbundenen Werkzeug (alphaXiv) gelesen, nicht aus Vorwissen. Keine H-Nummer.

## Vorwissen geprüft
- `../v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md`: Z1 ist gleichwertig mit γ_M/γ_T = γ_L (frame-abhängiges Flächenquant). Die Dualitätsdrehung allein
  lässt alles Geometrische fest; es bräuchte den Boost-Anteil, „der aber den Horizont nur umparametrisiert“. Nicht mit Literatur belegt.
- `../op3_horizon_shadow_2026_11_15/README.md`, Punkt 3: „T sieht denselben Kern lorentzkontrahiert“ gibt γ_L als Lorentz-Faktor, zirkulär (η über γ_L).
- `../op1_one_number_2026_11_17/`: γ_L = Lorentz-Faktor des Beobachterpaars (M, M̄), nicht (M, T); T ist das J_B-Bild (iπ/2).
- `../op1_two_readings_2026_11_17/`: Lesart (B), M ist gegen R mit η geboostet.
- Wiki, Nachtrag Literatur (EPRL, Bianchi): Der Boost-Teil liefert kein frame-abhängiges Flächenquant (dort für den Rindler-Horizont).
- Suche nach FitzGerald, Rovelli–Speziale, Alexandrov im Repo: keine Fundstelle zum Flächenspektrum.

## Literatur (gelesen)
- **Rovelli, Speziale, „Reconcile Planck-scale discreteness and the Lorentz-Fitzgerald contraction“, gr-qc/0205108:** Ein geboosteter Beobachter misst
  einen anderen Operator A′, der mit A nicht vertauscht. Ist der Boost unitär, haben A und A′ dasselbe Spektrum mit derselben kleinsten Fläche. Was sich
  stetig ändert, ist die Wahrscheinlichkeitsverteilung der Eigenwerte. Der **Mittelwert** der Fläche kann lorentzkontrahiert sein, die kleinste Fläche
  nicht. Die Unitarität ist dort eine Bedingung an den Boost-Erzeuger, kein Beweis.
- Gefunden, nur die Kurzfassung gelesen: arXiv:2601.01198 (2026) zeigt in einem Modell, dass diskrete Fläche und unitäre Boosts verträglich sind;
  gr-qc/0103105 (Alexandrov) berechnet das Flächenspektrum in der Lorentz-kovarianten Formulierung. Beide nicht ausgewertet.

## Folge für die Zuordnung
1. **Unter Lesart (B) sind M und M̄ durch einen echten Boost verbunden** (Lorentz-Faktor γ_L = cosh 2η). Nach Rovelli–Speziale sehen beide dasselbe
   Flächenspektrum, also dasselbe γ. Das Verhältnis γ_M/γ_T kann nicht aus dem Boost (M, M̄) kommen.
2. **Der Dualitäts-Anteil (J_B) lässt die Geometrie fest** (r10). Er kann das Quant ebenfalls nicht ändern.
3. **Damit fällt jede Zerlegung der Frame-Abbildung in Boost und Dualität als Quelle eines frame-abhängigen Flächenquants**, solange der Boost
   unitär wirkt. Das schärft r10: Z1 ist mit der Standard-LQG nur verträglich, wenn
   - (a) die Abbildung M → T **nicht unitär** ist (T als J_B-Bild mit imaginärer Rapidität iπ/2 ist kein echter Boost; das wäre die einzige Stelle),
     oder
   - (b) γ_T **kein Eigenwert-Parameter** ist, sondern ein Mittelwert: T liest die M-Eigenwerte im Mittel kontrahiert. Ein Mittelwert ist aber
     keine Zählregel, und die Kontraktion um γ_L verlangt Rapidität 2η zwischen den Lesern, also wieder das Paar (M, M̄) und η über γ_L (zirkulär wie
     im Horizontschatten).
4. Die Lesart „ABCK ist die frühere Näherung der Literatur“ (T-Regel-Notiz) wird dadurch nicht berührt.

## Lesart
- Neu ist eine **Einschränkung mit Literaturbeleg:** Ein frame-abhängiges Flächenquant ist mit unitären Boosts in LQG unverträglich. Die Zuordnung
  braucht deshalb entweder eine nicht-unitäre Frame-Abbildung (a) oder eine Umdeutung von γ_T als Mittelwert (b). Für (a) ist im Bestand die einzige
  Kandidatin die J_B-Abbildung mit iπ/2; ob sie auf dem Flächenoperator nicht-unitär wirkt und das Spektrum um γ_L skaliert, ist eine prüfbare Frage.
- Kein blinder Test. OP1 offen; H98, H102, H112 unverändert.
