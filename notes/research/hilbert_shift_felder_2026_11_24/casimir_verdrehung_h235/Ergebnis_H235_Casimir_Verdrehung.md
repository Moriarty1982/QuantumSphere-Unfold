# Ergebnis H235 (k450): Die Casimir-Verdrehung bricht den Sektortausch, legt φ aber nicht auf den Messwert

**Datum:** 2026-11-28. **Vorab:** `Vorab_H235_Casimir_Verdrehung.md` (Commit 13cf65b, vor der Rechnung). **Urteil: widerlegt.**
**Werkzeuge:**
- Python: `k450_test_h235.py` → `k450_out.txt`.
- Wolfram, unabhängig: `k450b_gegenprobe.wl` → `k450b_out.txt`. Minimiert wird mit FindMinimum über 16 Startwerte, die Verdrehung exakt über
  PolyLog. Alle gemeinsamen Zahlen stimmen überein.
- Nachtrag bei kleinem q: `k450c_kleines_q.py` → `k450c_out.txt` (nachträglich, nicht gewertet).
- Qiskit ist nicht einschlägig.

## Frage
Kann eine Casimir-Verdrehungsenergie zwischen innerem und äußerem Feld (k449) den Sektortausch aus H225 brechen und φ auf x = 0,0395773 legen?
Die Gewichte sind Zählzahlen: 2 für den geladenen Im-Sektor (komplex), 1 für den neutralen Re-Sektor (reell). Das Vorzeichen ist das der Fermionen.
Die Stärke κ ist frei.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| Vorprüfung | Baum tauschsymmetrisch (Differenz 0). Verdrehung mit (1,1) symmetrisch, mit (2,1) **gebrochen** (Differenz ~1) | — | wie erwartet |
| A (teilweise blind) | o_Im(φ_x) = x schon bei φ_x = 2,23·10⁻⁵. Vorhersage **x_ν = o_Re(φ_x) = 0,06295, +9,20σ** | \|z\| ≤ 2 | **nein** |
| B1 (blind) | κ* = +0,1056 (κ*/\|q\| = 1,239) > 0. Zweite Ableitung +0,1415, also lokales Minimum | κ* > 0, Minimum | ja |
| B2 (blind) | Das globale Minimum liegt bei φ = 2,0443 (E = −2,30534 gegen −1,97015 bei φ_x). Dort ist o_Im = −0,0043 und o_Re = 0,1107 | global | **nein** |

**Gesamturteil nach Vorab: widerlegt** (A verfehlt).

## Was das heißt
- **Ein Term, der nur von φ abhängt, kann die Neutrino-Vorhersage nicht ändern.** Das war vorab als Satz notiert und ist jetzt bestätigt.
  - Die Versätze sind reine Baumfunktionen. Wer o_Im = x verlangt, bekommt x_ν,pred = o_Re(φ_x), egal welcher Brecher, welche Gewichte, welches
    Vorzeichen.
  - Im H225-Modell mit dem Fit q = −0,0852 aus H167 sind das 0,0630, also +9,2σ.
  - Grund: q allein liefert bereits den ganzen Im-Versatz (o_Im(0) = 0,03956). Der Re-Sektor antwortet auf dasselbe q stärker (0,0629). φ selbst
    ist dort praktisch null.
- **Die Verdrehung bricht den Tausch, wählt aber den falschen Partner.** Mit den Gewichten 2:1 fällt die Energie am tiefsten bei φ ≈ 2π/3 − 0,05.
  Dort hat der Im-Versatz das falsche Vorzeichen bzw. fast keinen Wert. Der Datenpunkt ist nur ein lokales Minimum, wie schon in H226 und H232.
- κ* = 0,106 ist etwa so groß wie q selbst, kein Schleifenfaktor (1/(16π²) = 0,0063, α|q| = 0,0006). Eine Casimir-Schleife wäre also
  17-mal zu schwach, um den Datenpunkt überhaupt stationär zu machen. Nur berichtet, nicht gewertet.

## Nur Bericht
- **(1, 0), nur der geladene Sektor koppelt:** κ*/|q| = 2,48, lokales Minimum, nicht global.
- **(2, 2), Dirac-Neutrinos:** symmetrisch, bei φ_x kein Minimum.
- **(1, 2):** kein Minimum.
- **(4, 1):** κ*/|q| = 0,62, lokales Minimum, nicht global.
- **Globales Minimum als Funktion von κ (2,1):**
  - κ = 0: Das Minimum liegt bei π/8 wie in H225.
  - κ = 10⁻³: Es springt auf φ ≈ 1,44.
  - Für große κ wandert es gegen 2π/3. Bei keinem untersuchten κ liegt der Im-Versatz des globalen Minimums bei +x.

## Nachtrag bei kleinem q (nachträglich, nicht gewertet, `k450c`)
Kommt der Versatz ganz aus φ statt aus dem q-Fit, rückt die Neutrino-Vorhersage an den gemeinsamen Versatz heran:

| q | x_ν,pred | Abstand zu x_ν |
|---|---|---|
| −0,01 | 0,04238 | −0,46σ |
| −0,001 | 0,03986 | −1,64σ |
| −10⁻⁴ | — | −1,76σ, wie H213 |

- κ*/|q| ≈ 1,31 bleibt dabei fast konstant.
- φ_x ist **nie global**: Das globale Minimum liegt bei φ ≈ 2π/3 − 0,04, mit Im-Versatz ≈ −x (Spiegelpartner mit falschem Vorzeichen).
- Die Spannung zwischen q-Fit und φ ist damit sichtbar: Das H225-Modell zählt den Versatz doppelt, wenn q aus H167 und φ zusammen stehen.
  Das betrifft auch die Zahlen in H226 und H232. H225 ist nicht betroffen, weil das Minimum dort für jedes q bei π/8 liegt. Ob die Urteile von H226
  und H232 bei kleinem q gleich bleiben, ist nicht nachgerechnet. Hier (H235) bleibt φ_x in beiden Lesarten nicht global.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:**
  - Ein Brecher, der nur von φ abhängt, lässt x_ν,pred unverändert (Satz).
  - Werte von κ*, zweiter Ableitung und globalem Minimum (zwei Werkzeuge).
  - Bruch des Tauschs durch ungleiche Gewichte.
- **Gesetzt:**
  - Baum-Modell H225 mit q = −0,0852 (H167).
  - Zuordnung α_R = 2φ, α_I = π/2 − 2φ.
  - Gewichte 2:1 als Zählzahlen (Majorana-Lesart des Re-Sektors).
  - Fermionen-Vorzeichen.
  - Stärke κ frei.
- **Nachträglich:**
  - Doppelzählung von q und φ und die Rechnung bei kleinem q (k450c).
  - Der Spiegelpartner mit o_Im ≈ −x als globales Minimum.

## Folgerung
Die Casimir-Verdrehung ist ein natürlicher Tauschbrecher (Zählgewichte statt Fit). Sie wählt aber nicht x:
- Sie zieht den Modulus zum Spiegelpartner mit falschem Vorzeichen des Im-Versatzes.
- Für die Neutrinos kann sie grundsätzlich nichts beitragen.

φ bleibt eine Messzahl, OP3 bleibt offen. Neu ist eine Klarstellung: In H225–H232 wurden der q-Fit (H167) und φ zugleich gesetzt. Für einen
späteren Neustart des φ-Strangs müsste zuerst entschieden werden, welcher der beiden den Versatz trägt.

Vergeben: H235, k450. Nächste frei: H236, k451 (vor Vergabe gegen `main` prüfen).
