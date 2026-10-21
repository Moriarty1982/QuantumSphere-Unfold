# Ergebnis H11: Massen aus einer natürlichen Funktion auf dem Tripel-Raum

Vorab-Notiz: `Vorab_Notiz_H11_Massen_Tripelraum.md`, Commit 8e5eaa9 (2026-10-20 16:10 UTC), vor der Prüfung.
Skript: `k30_test_h11.py`. Kriterium unverändert.

## Ergebnisse (M)

**H11a (Triality-Form bei fester Gesamtnorm).** Maximum und Minimum von t = Re((ab)c) auf S = 3 liegen bei gleichen
Normen (1, 1, 1), t = ±1, also K = 1/3; die übrigen kritischen Punkte haben zwei leere Plätze, K = 1. Keine Hierarchie.

**H11b (allgemeinstes invariantes Potential bis Grad 4).** V = −S + βS² + γQ − κP auf einem Gitter von 210
beschränkten Parameterpunkten:

| Muster des globalen Minimums | Anzahl |
|---|---|
| drei gleiche Normen (K = 1/3) | 180 |
| ein besetzter Platz (0, 0, n), K = 1 | 25 |
| drei verschiedene, von null verschiedene Normen | **0** |
| flach (γ = κ = 0: Minimum ist eine ganze Kugel, keine bestimmten Massen) | 5 |

Analytische Kontrolle (bestätigt): An jedem kritischen Punkt mit n_k ≠ 0 erfüllt x_k = n_k² dieselbe Gleichung
(2α + 4βS)·x + 4γ·x² = κP. Sie ist quadratisch, also gibt es höchstens zwei verschiedene Normen.

Zwei Auswertungsfehler wurden vor dem Urteil behoben, beide ohne Änderung von Kriterium oder Daten: Die flachen Fälle
γ = κ = 0 hatte der Optimierer zunächst als „drei verschiedene Normen“ gezählt, und eine Toleranz von 10⁻⁶ hatte
Rechenrauschen als verschiedene Normen gewertet (jetzt 10⁻⁴). Die Toleranz weicht damit vom verbindlichen Verfahren
der Notiz (10⁻⁶) ab. Mit 10⁻⁶ wären Rauschfälle zugunsten der Hypothese gezählt worden. Das Urteil hängt aber nicht
an der Toleranz: Die quadratische Gleichung schließt drei verschiedene Normen analytisch aus.

**Mindestgrad.** Erst ein Term vom Grad 6 (etwa μ·Σn⁶) macht die Gleichung kubisch und erlaubt drei verschiedene
Normen. Notwendig, nicht hinreichend: Im geprüften Gitter mit Sextik-Term trat kein solches Minimum auf.

## Urteil nach dem festgelegten Kriterium

**H11a und H11b sind widerlegt.** Kein kritischer Punkt bzw. kein Minimum hat drei verschiedene, von null
verschiedene Normen; die drei verschiedenen Leptonmassen (√m/√m_τ = 0,017; 0,244; 1; K = 0,666664) sind nicht
darstellbar.

## Einordnung

- Mit natürlichen Invarianten bis Grad 4 erzwingt die Generationen-S₃ ein entartetes Paar oder leere Plätze. Eine
  Massenhierarchie braucht Terme ab Grad 6 oder eine explizite Brechung der S₃.
- Jeder solche Schritt bringt mindestens zwei neue Parameter. Die zwei Lepton-Verhältnisse ließen sich dann anpassen,
  aber nicht vorhersagen. K = 2/3 wäre nur eine Bedingung an die Parameter, keine Folge der Struktur.
- Das entspricht dem Befund von r10 und v4.9: Die Triole liefert die Form, nicht die Dynamik.
