# Vorab-Notiz H96: Ω_M heute = β_sym² = 0,30185 (Λ-Auslesung, Epoche „heute“)

**Stand:** 6. November 2026, vor dem Vergleich mit künftigen Daten festgelegt. Autorentscheidungen vom 6.11.: OP5 getrennt (Λ-Auslesung als eigener Teil) und Epoche der Kaskaden-Verzweigung „Heute“. Diese Vorhersage hat keinen freien Parameter; sie folgt aus dem eingefrorenen Stand.

## Hypothese
**H96:** Der heutige Materieanteil in flachem ΛCDM ist die Verzweigung der Kaskade:
  Ω_M = β_sym² = (γ_L − 1)/(γ_L + 1),  γ_L = γ_BI/γ_string,
mit γ_string = ln 2/(π√3) (exakt) und γ_BI als positiver Lösung von Σ_{j=½,1,…} 2·exp(−2πγ√(j(j+1))) = 1 (Meissner/Domagała–Lewandowski; dieselbe Eingabe wie H15). Numerisch: γ_BI = 0,2375330, γ_L = 1,864700, **Ω_M = 0,30185**, Ω_Λ = 0,69815.

Folgerungen in flachem ΛCDM, ohne eigenen Test, weil sie von Ω_M abhängen: q₀ = (3Ω_M − 2)/2 = −0,547 und Übergangsrotverschiebung (1 + z_t)³ = 2Ω_Λ/Ω_M, also z_t = 0,666.

## Vergleichsdaten (verbindlich)
Der **erste Wert von Ω_m in flachem ΛCDM, der nach dem 2026-11-06 veröffentlicht wird**, aus einer der folgenden Quellen, je nachdem welche zuerst erscheint:
- (a) DESI DR3, BAO allein (das Gegenstück zu DR2: 0,2975 ± 0,0086);
- (b) Euclid, erste Kosmologie-Veröffentlichung, Hauptergebnis in flachem ΛCDM.

Nicht gezählt werden Kombinationen mit dem CMB, Reanalysen älterer Daten und Einzelarbeiten außerhalb der Kollaborationen.

## Kriterium
- **Bestätigt**, wenn |Ω_m − 0,30185| ≤ 2σ (σ = angegebene 1σ-Unsicherheit; bei asymmetrischen Fehlern die zur Vorhersage weisende Seite).
- **Widerlegt**, wenn die Abweichung größer als 2σ ist.

## Offenlegung (vor dem Festschreiben bekannt; nicht blind gegenüber diesen Werten, sie zählen nicht)
- Websuche vom 6.11.2026, nur Zusammenfassungen gelesen:
  - DESI DR2 BAO 0,2975 ± 0,0086 (arXiv:2503.14738);
  - DESI BAO + Lyα 0,3012 ± 0,0079, mit CMB 0,3042 ± 0,0033;
  - DR1-Reanalyse 0,2973 ± 0,0050 (arXiv:2601.16165);
  - DES/DESI-Konsistenzstudie 0,2948 ± 0,0039 (arXiv:2606.18374);
  - Planck 2018 0,3153 ± 0,0073.
- Die Vorhersage liegt im Bereich der DESI-Werte und etwa 1,8σ unter Planck. Die Datensätze streuen untereinander um etwa 2,5σ. Das Kriterium ist daher auf eine Quelle festgelegt, damit nicht nachträglich die passende gewählt wird.
- Der Wert von β_sym stammt aus dem Kern (T6, OP1: eingesetzt, nicht hergeleitet). Die Gleichsetzung Ω_M = β² stand schon in `thm:dark-energy`. Die Epoche „heute“ ist eine Autorentscheidung vom 6.11.; sie ist kein Ergebnis.
- Die Hopf-Variante β² = 1/3 aus `thm:dark-energy` ist hier **nicht** die Vorhersage. Sie wäre verträglich nur mit Werten nahe 0,333.

## Nachtrag (6.11.2026, vor jeder Datenprüfung; Vorwissen ergänzt)
Beim Weitersuchen gefunden; das hätte in „Offenlegung“ gehört. Hypothese und Kriterium bleiben unverändert.
- **v4.8.0-r17** hat die Epochenfrage schon behandelt und drei Auswege notiert: (a) `thm:dark-energy` gilt nur heute, (b) β läuft rückwärts, (c) eine andere Funktion der Kaskadenwahrscheinlichkeiten. Die Autorentscheidung „heute“ ist Ausweg (a). Dort steht auch: Dann verlieren `prop:H0-tension` und `prop:saturation` ihre Grundlage (beide inzwischen archiviert), und die Übereinstimmung wird „eine Aussage über eine Epoche“.
- **v4.8.0-r03 F11:** γ_L = γ_BI/γ_string ist das Verhältnis zweier Bestimmungen **desselben** LQG-Parameters: der korrigierten Zählung (Domagała–Lewandowski/Meissner, 0,2375) zur überholten (Ashtekar–Baez–Corichi–Krasnov, 0,12738). Der Companion liest dieses Verhältnis als Lorentzfaktor. Eine Herleitung beider Werte aus der Struktur gibt es nicht. H96 prüft also auch diese Lesart.
- **r68:** Die Literatur bevorzugt die SU(2)-Behandlung der Horizontzustände (γ ≈ 0,274). Damit wäre γ_L ≈ 2,15 und Ω_M ≈ 0,365, weit weg von allen Daten. H96 setzt die U(1)-Zählung voraus.
