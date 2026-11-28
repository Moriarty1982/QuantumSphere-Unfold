# Ergebnis H236 (k451): φ trägt den Versatz, q ist nur ein Vorzeichen. Kein früheres Urteil kippt

**Datum:** 2026-11-28. **Vorab:** `Vorab_H236_Doppelzaehlung.md` (Commit 14c5f3f, vor der Rechnung). **Urteil: trägt.**

**Werkzeuge:**
- Python: `k451_test_h236.py` → `k451_out.txt` (Teil A) und `k451_teilB_h226.py` → `k451_teilB_out.txt` (Teil B, mit den unveränderten Funktionen aus k440).
- Wolfram unabhängig: `k451b_gegenprobe.wl` → `k451b_out.txt` (FindRoot in φ und q). Alle gemeinsamen Zahlen stimmen auf mindestens 6 Stellen überein.
- Qiskit ist nicht einschlägig.
- Blindheit: Die Lesarten Q und Φ waren nicht blind, die Lesart M und Teil B waren blind.

## Frage
Seit H225 standen im Baum-Modell zwei Größen, die beide den Lepton-Versatz tragen können:
- der Fit q = −0,0852 aus H167 (Term sechster Ordnung mit Skala),
- die gemeinsame Drehung φ (H221).

Welche der beiden trägt den Versatz, und welche früheren Ergebnisse hängen an der Doppelzählung?

## Ergebnis Teil A
| Lesart | q | φ | x_ν,pred | Abstand |
|---|---|---|---|---|
| Q: q trägt (nicht blind) | −0,0852 | 2,2·10⁻⁵ | 0,06295 | **+9,20σ** |
| Φ: φ trägt (nicht blind) | → 0⁻ | x = 0,03958 | 0,03958 | **−1,78σ** |
| M: beide frei, Mittelwert (blind) | −0,01351 | 0,03331 | = Daten (2 Zahlen, 2 Größen) | — |
| M: 2σ-Bereich (blind) | **[−0,0289; 0]** | | | |

- **2σ-Bereich von q:** Die Obergrenze entspricht x_ν + 2σ. Die Untergrenze q = 0 kommt daher, dass x_ν − 2σ = 0,0391 kleiner als x ist. Das ginge nur mit
  q > 0, also mit dem anderen Zweig, den H222 verwirft.
- **Kriterium A:** q = 0 liegt im 2σ-Bereich, q = −0,0852 liegt dreimal so weit draußen. Also **trägt φ den Versatz, und q ist nur ein Vorzeichen (H222)**.
- **Beitrag von q im Mittelwert:** Der Mittelwert der Mischung hätte q einen Anteil von 15,8 % am Im-Versatz. Das ist nur die Übersetzung der Spannung
  x_ν − x (1,78σ) in eine Skala und kein Befund.

## Ergebnis Teil B (blind)
H226 Teil B wurde in der Φ-Lesart wiederholt, also mit kleinem q statt −0,0852.

| q | T1 (Konjugationsterm nur Im) | T2 (q_Re = λq) | T3 (\|α′_Re\| = κ) |
|---|---|---|---|
| −0,0852 (H226) | x_ν,pred = 0,495, +212σ | keine Lösung | keine Lösung |
| −0,01 | 0,486, +207,7σ | keine Lösung | keine Lösung |
| −0,001 | 0,484, +207,0σ | keine Lösung | keine Lösung |

**Das Urteil von H226 bleibt** (widerlegt). Das Kriterium B ist erfüllt.

## Teil C: Bestandsaufnahme
| Test | q als Zahl im Skript? | Lesart | betroffen? | Urteil |
|---|---|---|---|---|
| H221 | ja (Weg S geprüft) | entscheidet für Φ (+9,2σ gegen Q) | nein, ist die Quelle der Klärung | bleibt |
| H222 | nein (q = −ε, ε → 0) | Φ (nur Vorzeichen) | nein | bleibt |
| k436, H223, H224 | nein | Φ | nein | bleibt |
| H225 | ja, q-Abtastung −0,001 … −0,3 | gemischt | nein: Minimum bei π/8 für jedes q | bleibt |
| H226 | ja: Teil A bei q = −10⁻⁴ (Φ), Teil B bei −0,0852 (doppelt) | B doppelt | Teil B in Φ nachgerechnet (oben) | **bleibt** |
| H227 (Massen, Σm_ν = 59,30 meV, m_β, m_ββ, R +1,80σ) | nein | Φ (gemeinsames φ) | **nein** | bleibt, Vorhersagen unverändert |
| H228 | ja, q ∈ {−0,01; −0,0852; −0,3} | gemischt | Zahl ändert sich: t_x/τ = 0,1321 (Φ, führende Ordnung) statt 0,1231 | bleibt (keine Uhr trifft auf 2σ). Die Bemerkung „⅛ nur 1,5 % daneben“ gilt nur bei q = −0,0852; in Φ sind es 5,7 % |
| H229, H230, H231 | nein | Φ | nein | bleibt |
| H232 | ja: Teil B bei −0,0852, Teil C abgetastet | B doppelt | in Teil C schon da: bei q = −0,001 off_Re −1,30σ, aber x **nie global** | bleibt (B verlangt global) |
| H233, H234 | nein (nur φ-Wert) | Φ | nein | bleibt |
| H235 | ja: Teil A bei −0,0852, Nachtrag k450c | A doppelt | in Φ (k450c): x_ν −0,5σ … −1,8σ, x nie global | bleibt (widerlegt; in Φ würde A bestehen, B2 scheitert weiter) |

## Was das heißt
- **Die Frage ist entschieden:** φ trägt den Versatz, q ist nur das Vorzeichen der Zweigwahl. Das war seit H221/H222 so gemeint. H225, H226 (Teil B),
  H228, H232 (Teil B) und H235 (Teil A) haben trotzdem den H167-Fit mitgeschleppt.
- **Kein Urteil kippt.** Alle betroffenen Tests scheitern an der Globalität oder an Größenordnungen, die von q nicht abhängen.
- **Zahlen, die sich ändern:**
  - In H232 und H235 rückt die Neutrino-Vorhersage in der Φ-Lesart von +22,8σ bzw. +9,2σ auf −1,3σ bzw. −1,8σ. Sie ist dann einfach der gemeinsame
    Versatz aus H213.
  - In H228 liegt die Uhr bei 0,1321 statt 0,1231.
- **Die Leptonenmassen und alle festgeschriebenen Vorhersagen (H227) sind nicht betroffen**: Σm_ν = 59,30 ± 0,24 meV, m_β, m_ββ und R gelten unverändert.
- Für künftige Rechnungen gilt das Baum-Modell mit **q → 0⁻** (Vorzeichen gesetzt, Wert null) und dem Versatz in φ. Wer endliches q will, muss es als
  Skalenanteil begründen. Die Daten erlauben bis |q| = 0,029 (2σ), verlangen aber keines.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:**
  - 2σ-Bereich von q aus den zwei Versätzen, mit zwei Werkzeugen.
  - H226 Teil B in der Φ-Lesart.
  - Prüfung aller Skripte H221–H235 auf q (grep, Ergebnis-Notizen).
- **Gesetzt:** Baum-Modell H225, Zweig nach H222 (q < 0), Daten x und x_ν (H213), Polmassen (H214).
- **Nachträglich:** Die Doppelzählung selbst fiel erst in H235 (k450c) auf.

## Urteil
**Trägt:** A gibt „φ trägt“, B gibt „Urteil bleibt“. OP3 bleibt offen, φ bleibt eine Messzahl.

Vergeben: H236, k451. Nächste frei: H237, k452 (vor Vergabe gegen `main` prüfen).
