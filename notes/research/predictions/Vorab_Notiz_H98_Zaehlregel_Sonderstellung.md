# Vorab-Notiz H98: Ist das Zählregel-Paar (DL/M für M, ABCK für T) unter natürlichen Zählregeln das einzige, das alle drei Daten trifft?

Festgelegt am 2026-11-07, **vor** der Rechnung. Autor: „mach das“ (auf den Vorschlag, die Zählregel je Frame, die am stärksten belastete Annahme
nach v4.10.0-r08.3, zu begründen).

## Warum dieser Test und nicht eine Herleitung
Eine Herleitung der Zuordnung „M zählt alle Spins mit Gewicht 2, T nur j = ½“ aus den Frames gibt es im Korpus nicht (OP1 seit r63). Bevor man
eine sucht, ist zu klären, wie viel die bisherigen Übereinstimmungen überhaupt über die Zuordnung aussagen. Der γ_L-Kern trifft drei bekannte
Werte: das Leptonfenster (β_sym), m_W (H15-Relation) und Ω_M (H96-Relation). Ob das bemerkenswert ist, hängt davon ab, wie viele andere natürliche
Paare von Zählregeln dasselbe täten. Die parallele Erkundung (Prinzip „Unschärfesättigung + Energiebedingung je Frame“) läuft getrennt und ohne
Kriterium.

## Vorwissen geprüft
- r63/H47 (`Vorab_Notiz_H47_Zaehlregel_beta_sym.md`, `Ergebnis_H47_…`, `k102_zaehlregeln.py`): drei Zählungen gerechnet (ABCK, DL/M, Ghosh–Mitra);
  DL/M im Leptonfenster, GM nicht; nicht blind.
- r63.2–r63.4: Unschärfesättigung (m = ±j), Tachyon-Boden; Zuordnung zu den Frames ausdrücklich nicht hergeleitet.
- r68 (`Nachrechnung_r63_r67.md`): Literatur bevorzugt SU(2) (γ ≈ 0,274); ein SU(2)-Paar hat denselben Boden; U(1)-Wahl durch das Fenster.
- H15-Offenlegung: Look-elsewhere für cot θ_W ≈ 0,17 (drei Dokumentkonstanten). r56: 14 Korpus-Kandidaten treffen nicht über Zufall (p = 0,019).
- v4.10.0-r07.4: N (Normierung des Flächengesetzes) fällt in γ_L heraus; v4.10.0-r08.3: H15, H46, H96 hängen am γ_L-Kern.
- Alle drei Beobachtungsgrößen sind Funktionen von γ_L allein: β² = (γ_L − 1)/(γ_L + 1), Ω_M = β², m_W = m_Z·γ_L/√(1 + γ_L²).

## Festgelegter Regelraum S (wird nicht erweitert)
Flächenspektrum a(j) = √(j(j+1)); eine Regel ist ein Spinbereich und ein Gewicht; γ ist die positive Lösung von Σ_{j∈Bereich} g(j)·e^{−2πγ·a(j)} = 1.
- Spinbereiche: **A** alle j ≥ ½; **H** nur halbzahlige j; **I** nur ganzzahlige j ≥ 1; **S½** nur j = ½; **S1** nur j = 1.
- Gewichte: **g = 2** (nur m = ±j, U(1)-Art) und **g = 2j + 1** (alle m).
- Gleiche Regeln werden einmal gezählt (bei S½ fallen beide Gewichte zusammen). Regeln ohne positive Lösung entfallen.
- Paare: geordnet (Regel_M, Regel_T) mit γ_M > γ_T (sonst γ_L ≤ 1), γ_L = γ_M/γ_T. Die Zuordnung „welches ist M“ folgt aus γ_L > 1.
- Summen bis j_max = 4000, Restglied < 1e−12.

## Datenfenster (bekannt, nicht blind)
1. Leptonfenster: β_sym ∈ [0,545; 0,570] (r61.1(e)).
2. m_W: PDG 2025 80,3692 ± 0,0133 GeV, 2σ; m_Z = 91,1880 GeV.
3. Ω_M: DESI DR2 BAO 0,2975 ± 0,0086, 2σ.

## Hypothese H98
Im Regelraum S trifft **genau ein** Paar alle drei Fenster, und zwar (A, g = 2) für M mit (S½) für T, also DL/M mit ABCK.

## Kriterium (verbindlich)
- **Bestätigt**, wenn genau dieses eine Paar alle drei Fenster trifft.
- **Widerlegt**, wenn ein weiteres Paar alle drei trifft oder wenn das Paar selbst ein Fenster verfehlt.
- Unabhängig vom Ausgang werden berichtet: Zahl der gültigen Paare, Zahl der Treffer je Fenster einzeln, und der Anteil der Paare im m_W-Fenster
  (Maß für die Seltenheit).

## Offenlegung
- **Nicht blind gegenüber den Daten:** Alle drei Werte sind bekannt, und dass DL/M + ABCK alle drei trifft, ist bekannt (β = 0,5494; m_W = 80,361,
  0,6σ; Ω_M = 0,302, 0,5σ). Unbekannt ist nur, wie viele andere Paare in S dasselbe tun.
- Erwartung vor der Rechnung (Kopfschätzung): Das m_W-Fenster verlangt γ_L auf etwa ± 0,003 genau. Bei rund 30 Paaren mit γ_L zwischen 1 und einigen
  Einheiten erwarte ich höchstens ein Paar im Fenster. Eine Bestätigung sagt dann: Die drei Treffer zusammen sind selten; sie sagt nicht, warum
  gerade diese Zuordnung physikalisch richtig ist. Die m_W-Relation wurde selbst nachträglich gefunden (H15-Offenlegung), das schwächt jede
  Seltenheitsaussage.
- Der Raum S ist eine Wahl. Er enthält die Literaturregeln (ABCK, DL/M, GM) und naheliegende Varianten; er ist vor der Rechnung festgelegt.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
