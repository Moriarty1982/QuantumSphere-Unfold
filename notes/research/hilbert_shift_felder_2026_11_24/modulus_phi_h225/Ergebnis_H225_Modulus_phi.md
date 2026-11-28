# Ergebnis H225 (k439): φ als Modulus stellt sich auf π/8 ein, nicht auf den Messwert. Grund ist der Tausch der beiden Lepton-Sektoren

**Datum:** 2026-11-28. **Vorab:** `Vorab_H225_Modulus_phi.md` (Commit caf173e, vor der Rechnung). **Urteil: widerlegt.**
**Werkzeuge:** Python (`k439_test_h225.py` → `k439_out.txt`), Wolfram unabhängig (`k439b_gegenprobe.wl` → `k439b_out.txt`; Tauschsymmetrie und führende Ordnung
symbolisch, Minimierung mit FindMinimum). Alle gemeinsamen Zahlen stimmen überein (E(φ*) bei q = −0,0852: −2,1594588 in beiden). Qiskit nicht einschlägig.
Teil a war nicht blind (analytisch vorab bekannt), b und c blind, d nachträglich.

## Frage
Bei q = 0 ist der gemeinsame Drehwinkel φ eine exakt flache Richtung: Jeder Sektor hat das Minimum −1 für jedes φ (H221). φ ist also ein Modulus. Legt der einzige
skalenfreie Term, der schon im Bild steht (der kubische Zweigwahl-Term q cos 3δ, Vorzeichen q < 0 gesetzt), φ fest, wenn die gemeinsame Vakuumenergie beider Sektoren
minimal sein soll?

## Ergebnis
| Teil | Messwert | Kriterium (Minimum innerhalb 1 % von x = 0,0395773) | Entscheidung |
|---|---|---|---|
| a (nicht blind) | führende Ordnung: tan 3φ* = 1 + √2/w; w = 1 gibt **φ* = π/8 = 0,3927** (exakt, Wolfram: tan 3π/8 − (1 + √2) = 0); für w ∈ [½, 2] liegt φ* zwischen 0,347 und 0,438, für jedes w > 0 im Fenster (π/12, π/6) | nein (+892 %) | kein Treffer |
| b (blind) | exakte Minimierung in δ für q/α′ = −0,001 … −0,3: globales Minimum **immer genau π/8**, unabhängig von q; am Datenpunkt φ = x ist E nicht stationär (dS/dφ = 4,83), 67 % der Gitterpunkte liegen tiefer | nein (+892 %) | kein Treffer |
| c (blind) | Ordnung 6 allein, r cos 6δ: r < 0 → φ* = π/8, r > 0 → φ* = 7π/24 | nein (+892 % bzw. +2215 %) | kein Treffer |

**Gesamturteil nach Vorab: widerlegt** (b ohne Treffer, c ohne Treffer).

## Warum genau π/8 (d, nachträglich, nicht in der Vorab-Notiz)
Die beiden Sektorpotentiale gehen exakt ineinander über: V_Re(−δ; π/4 − φ) = V_Im(δ; φ), für jedes q und r (Wolfram symbolisch: Differenz 0; Python 1,3·10⁻¹⁵).
Deshalb ist E(φ) = e_Im(φ) + e_Im(π/4 − φ) spiegelsymmetrisch um φ = π/8, und π/8 ist für **jeden** J-verträglichen Spektralterm ein stationärer Punkt. Bei π/8 liegen die
Phasen der beiden Sektoren bei −π/24 und +π/24, also auf **demselben Spektrum** (m/m_max = 0,00335 : 0,0365 : 1 in beiden Sektoren). Die minimierte Vakuumenergie
treibt die Sektoren zur Gleichheit. Die Daten zeigen das Gegenteil: δ_Im = 0,2222 (geladene Leptonen) und δ_Re = 0,4840 (Neutrinos) sind deutlich verschieden.

## Lesart
- **Ein symmetrisches Potential kann φ = x nicht wählen.** Jeder Term, der in beiden Sektoren mit gleichem Koeffizienten steht, erbt die Tauschsymmetrie und legt φ auf
  π/8 oder 7π/24. Der Messwert φ = 0,0396 (2,27°) bricht den Sektortausch. Wer φ dynamisch festlegen will, braucht also einen Term, der Im- und Re-Sektor
  **unterscheidet** (ungleiche Gewichte w ≠ 1 reichen in führender Ordnung nicht: für w > 0 bleibt φ* über π/12).
- **Was das für φ heißt.** φ bleibt eine gemessene Zahl. Neu ist: Sie ist kein Gleichgewichtswert der Vakuumenergie in diesem Bild, sondern liegt ausdrücklich abseits davon.
  Das ist ein Hinweis, dass φ eher eine Anfangs- oder Randbedingung (oder ein Bruch des Sektortauschs) ist als ein dynamisch eingestellter Modulus.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** Lage des Modulus-Minimums (führende Ordnung exakt, endliches q numerisch), Tauschsymmetrie V_Re(−δ; π/4 − φ) = V_Im(δ; φ) (symbolisch),
  gleiches Spektrum bei π/8.
- **Gesetzt:** Annahme „φ minimiert die gemeinsame Vakuumenergie“ (die Hypothese selbst); Universalität der Koeffizienten, w = 1; Vorzeichen q < 0 (Autor, 28.11.);
  Zirkulantensektor, Baumniveau, K = ⅔, H99; α′_ν = −1 (H168).
- **Nachträglich:** Teil d (Symmetriegrund und gleiches Spektrum) war nicht vorab formuliert.

## Grenzen
Kein Quantenbeitrag zur Modulus-Energie (Coleman-Weinberg bräuchte Massenskalen und eine Renormierungsskala). Nur cos 3δ und cos 6δ getrennt; eine Mischung mit freiem
Verhältnis kann jeden Wert treffen und wird nicht gewertet. Ein sektorunterscheidender Term ist nicht gerechnet. Kein Guard berührt; OP3/OP4 offen.

## Dateien
- `Vorab_H225_Modulus_phi.md`, `k439_test_h225.py`/`k439_out.txt`, `k439b_gegenprobe.wl`/`k439b_out.txt` (ein erster Wolfram-Versuch mit Solve auf Beträgen lief nicht durch,
  siehe Kopf der Ausgabe), `README.md`.

Vergeben: H225, k439. Nächste frei: H226, k440 (vor Vergabe gegen `main` prüfen).
