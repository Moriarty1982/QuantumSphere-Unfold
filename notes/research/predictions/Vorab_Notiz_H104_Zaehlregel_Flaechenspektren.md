# Vorab-Notiz H104: Hält die Sonderstellung des Zählregel-Paars, wenn das Flächenspektrum frei ist?

Festgelegt am 2026-11-14, **vor** der Rechnung. Autor: „dann OP3/1“ (OP1: die Zählregel je Frame). Einordnung T6, OP1.
Skript `k226_test_h104.py` (wird nach dieser Notiz geschrieben und ausgeführt).

## Anlass
H98 hat gezeigt: Unter 36 Paaren natürlicher Zählregeln trifft nur DL/M mit ABCK das Leptonfenster, m_W und Ω_M
zugleich. Der Regelraum hielt dort das Flächenspektrum a(j) = √(j(j+1)) fest. Nach v4.10.0-r10.3 ist die Zählregel je
Frame gleichwertig mit einem **frame-abhängigen Flächenquantum**. In dieser Lesart ist gerade das Flächenspektrum die
Größe, die sich zwischen den Frames unterscheiden darf. Ein Regelraum, der es festhält, prüft die Sonderstellung also
nicht in der Richtung, in der die Annahme heute formuliert ist.

## Vorwissen geprüft
- `Vorab_Notiz_H98_Zaehlregel_Sonderstellung.md`, `Ergebnis_H98_...`: Regelraum S, Fenster, Ergebnis (36 Paare, 1 Treffer).
  H98 legt fest, dass S nicht erweitert wird. H104 ist deshalb ein eigener Test und ändert das Ergebnis von H98 nicht.
- `v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md`, r10.3: Zählregel = frame-abhängiges Flächenquantum; kein Grund bekannt.
- `v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md`: Prinzip P; die Brücke in P2 trägt nicht (r10.2).
- `op5_spin_selection_audit_2026_11_06.md` (über r10.4, r11.2): Sättigung wählt m = ±j, nicht j = ½.
- `v4_10_0_r63_r64/llm/Ergebnis_H47_Zaehlregel_beta_sym.md`: Herkunft der Zähl-Lesart von β_sym.
- `v4_10_0_r08/Annahmenliste_Companion.md`, r08.3: H15, H46, H96 ruhen auf dieser Annahme.
- Suche nach „äquidistant“, „Flächenspektrum“, „a(j) = j“ in den Notizen: kein Test mit anderem Flächenspektrum.

## Festgelegter Regelraum S′ (wird nicht erweitert)
Eine Regel ist ein Flächenspektrum, ein Spinbereich und ein Gewicht; γ ist die positive Lösung von
Σ_{j∈Bereich} g(j)·e^{−2πγ·a(j)} = 1.
- Flächenspektren:
  - **W** a(j) = √(j(j+1)), das Standardspektrum der Schleifenquantengravitation (wie in H98);
  - **E** a(j) = j + ½, das äquidistante Spektrum (andere Operatorordnung);
  - **L** a(j) = j, das lineare Spektrum (Fluss-Lesart, Grenzfall großer Spins).
- Spinbereiche wie in H98: **A** alle j ≥ ½; **H** nur halbzahlige j; **I** nur ganzzahlige j ≥ 1; **S½**; **S1**.
- Gewichte wie in H98: **g = 2** und **g = 2j + 1**.
- Regeln mit gleichem γ (Abstand < 10⁻²⁰) werden einmal gezählt, auch über Spektren hinweg. Regeln ohne positive
  Lösung entfallen.
- Paare: geordnet (Regel_M, Regel_T) mit γ_M > γ_T, γ_L = γ_M/γ_T. M und T dürfen verschiedene Spektren haben.
- Summen bis j_max = 4000.

## Datenfenster (unverändert aus H98, bekannt, nicht blind)
1. Leptonfenster: β_sym ∈ [0,545; 0,570].
2. m_W: PDG 2025 80,3692 ± 0,0133 GeV, 2σ; m_Z = 91,1880 GeV; m_W = m_Z·γ_L/√(1 + γ_L²).
3. Ω_M: DESI DR2 BAO 0,2975 ± 0,0086, 2σ; Ω_M = β² = (γ_L − 1)/(γ_L + 1).

Die Fenster bleiben die von H98, damit die Ergebnisse vergleichbar sind, auch wenn es neuere Zahlen gäbe.

## Hypothese H104
Auch im erweiterten Regelraum S′ trifft **genau ein** Paar alle drei Fenster, und zwar (W, A, g = 2) für M mit
(W, S½) für T, also DL/M mit ABCK im Standardspektrum.

## Kriterium (verbindlich)
- **Bestätigt**, wenn genau dieses eine Paar alle drei Fenster trifft.
- **Widerlegt**, wenn ein weiteres Paar alle drei Fenster trifft.
- Unabhängig vom Ausgang werden berichtet: Zahl der Regeln und gültigen Paare, Treffer je Fenster einzeln, der Anteil
  der Paare im m_W-Fenster und jedes Paar, das zwei der drei Fenster trifft.

## Offenlegung
- **Nicht blind gegenüber den Daten.** Dass DL/M mit ABCK alle drei Fenster trifft, ist bekannt. Unbekannt ist, wie
  viele der neuen Paare dasselbe tun.
- **Was ich vor der Rechnung weiß:** einige geschlossene Werte, nämlich (L, A, 2): γ = ln 3/π ≈ 0,3497;
  (E, A, 2): γ = ln 2/π ≈ 0,2206; (E, S½): γ = ln 2/(2π) ≈ 0,1103; (L, S½): γ = ln 2/π (fällt mit (E, A, 2)
  zusammen). Daraus kenne ich einzelne Verhältnisse (2,000; 1,585; 2,153), keines davon im m_W-Fenster. Die übrigen
  Werte kenne ich nicht.
- **Erwartung (Kopfschätzung):** bis zu 27 Regeln, also einige hundert Paare. Das m_W-Fenster ist in γ_L etwa ± 0,003
  breit. Bei gleichmäßiger Streuung der γ_L zwischen 1 und etwa 3,5 erwarte ich im Mittel knapp ein weiteres Paar im
  m_W-Fenster. Eine Widerlegung ist also gut möglich; ich halte beide Ausgänge für etwa gleich wahrscheinlich.
- **Was der Ausgang bedeutet:**
  - Bestätigt: Die Sonderstellung übersteht eine rund zehnmal größere Auswahl. Sie bleibt eine Seltenheitsaussage
    und keine Herleitung; die m_W-Relation ist nachträglich gefunden.
  - Widerlegt: Die Sonderstellung aus H98 hängt am festgehaltenen Spektrum. Das schwächt das Argument für die
    Zählregel, widerlegt aber weder H98 in seinem Regelraum noch die Vorhersagen H15, H46, H96.
- Der Raum S′ ist eine Wahl. Die drei Spektren sind die in der Literatur zur Horizontzählung gebräuchlichen Formen;
  weitere (etwa mit Quantengruppen-Abschneidung) sind nicht aufgenommen.
- Guards unverändert. OP1 bleibt in jedem Fall offen.

## Status (nachgetragen am 14.11.2026)
**Widerlegt.** Ein zweites Paar, (L, A, g = 2j + 1) mit (E, H, g = 2j + 1), trifft alle drei Fenster. Siehe `Ergebnis_H104_Zaehlregel_Flaechenspektren.md`.
