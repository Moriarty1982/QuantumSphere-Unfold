# Ergebnis H226 (k440): Kein einfacher tauschbrechender Term legt φ auf den Messwert; der Konjugationsterm macht ihn nur zu einem lokalen Minimum

**Datum:** 2026-11-28. **Vorab:** `Vorab_H226_Tauschbruch_phi.md` (Commit 422d12f, vor der Rechnung). **Urteil: widerlegt.**
**Werkzeuge:** Python (`k440_test_h226.py` → `k440_out.txt`), Wolfram unabhängig (`k440b_gegenprobe.wl` → `k440b_out.txt`); führende Ordnung, Globalitätsprüfung
und Teil B stimmen überein (Wolfram auf Gitterauflösung). Qiskit nicht einschlägig. Die führende Ordnung war vorab bekannt (nicht blind), Globalität und B blind.

## Frage
H225: Die gemeinsame Vakuumenergie beider Lepton-Sektoren legt den Modulus φ wegen des exakten Sektortauschs auf π/8. Welcher Term, der Im- und Re-Sektor
unterscheidet, macht den Messwert φ = x = 0,0395773 zum globalen Minimum, und sagt er dann den Neutrino-Versatz richtig voraus?

## Ergebnis
| Term | A: Grenzfall q → 0⁻ (Verhältnis für Stationarität bei x) | A: global? | B: q/α′ = −0,0852, geladener Sektor angepasst → x_ν,pred | Entscheidung |
|---|---|---|---|---|
| Kontrolle ohne Term | — | Minimum bei π/8 (H225 reproduziert) | — | — |
| T1 Konjugationsterm nur Im (c·α cos 2δ) | α = 2,425·q (Wolfram 2,4246 in führender Ordnung), Krümmung positiv | **nein**: x ist nur **lokales** Minimum, globales bei φ = −0,70 (E tiefer um 3,5·10⁻⁴) | α = +0,120: φ* = 0,4895, δ_Re = 0,0286 → x_ν,pred = **0,495 (+212σ)** | kein Treffer |
| T2 q_Re = λ q, λ > 0 | Stationarität verlangt λ = −0,623 (außerhalb λ > 0) | — | δ_Im erreicht δ* nicht (0,011 … 0,155) | kein Treffer |
| T3 \|α′_Re\| = κ | keine Stationarität bei x (κ wirkt in führender Ordnung nicht) | — | δ_Im erreicht δ* nicht (0,043 … 0,116) | kein Treffer |
| T4 α cos 2δ in beiden (Kontrolle, tauscherhaltend) | α = −2,63·\|q\|, aber Krümmung **negativ** (Maximum) | nein | Lösungen nur mit δ_Re = δ_Im (gleiches Spektrum), x_ν,pred = 0,301 (+121σ) | wie erwartet tauscherhaltend |

Rahmenzahlen (vorab, 21 Werte): nächste zu T1 ist −2 (+21 %), kein Treffer innerhalb 2 %.
**Gesamturteil nach Vorab: widerlegt** (kein Term macht x mit natürlicher Größe zum globalen Minimum; B für keinen Term innerhalb 2σ).

## Lesart
- **Der Konjugationsterm bricht den Tausch, aber falsch herum.** Mit α = 2,42 q wird φ = x ein stabiles lokales Minimum, doch die Vakuumenergie liegt bei φ ≈ −0,70 tiefer.
  Wählt man α so, dass das globale Minimum die geladenen Leptonen richtig gibt, landet der neutrale Sektor fast im Oktanten-Gegenpunkt (x_ν,pred 0,495 statt 0,043).
- **Ungleiche Stärken reichen nicht.** Ungleiche kubische Stärke bräuchte das falsche Vorzeichen (und damit die verworfene Zweigwahl), ungleiche Spin-1-Stärke greift in φ
  gar nicht.
- **Kontrolle bestätigt H225.** Ein Term, der in beiden Sektoren gleich steht (T4), lässt den Tausch stehen: Lösungen geben beiden Sektoren dasselbe Spektrum.
- **Bilanz der φ-Wege (H221–H226):** Skala (H221) gibt ungleiche Versätze; Wigner-Drehung (H224) trifft nicht; Modulus mit symmetrischem Potential (H225) landet auf π/8;
  einfacher Tauschbruch (H226) gibt höchstens ein lokales Minimum. Hergeleitet ist: Versatz = Drehwinkel (dimensionslos, gleich in beiden Sektoren), Zweig = Vorzeichen.
  Gesetzt bleibt: Vorzeichen und der Wert φ. Die offene Wahl ist nicht gewandert; sie sitzt seit H221 im Wert von φ. Ob das Ziel selbst eine gesetzte Eingabe ist
  (φ als Anfangsbedingung, z. B. ein metastabiles Vakuum wie bei T1), ist eine Weggabelung für den Autor.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** Verhältnisse der führenden Ordnung (symbolisch), Globalität (numerisch), Vorhersage x_ν je Term.
- **Gesetzt:** Kandidatenliste T1–T4, q/α′ = −0,0852 (H167), q < 0, Zirkulantensektor, Baumniveau, K = ⅔, H99, α′_ν = −1.
- **Nachträglich bemerkt:** Unter T1 ist φ = x ein lokales, stabiles Minimum (metastabil). Das wurde nicht vorab als Kriterium formuliert und wird nicht gewertet.

## Grenzen
Nur vier einfache Terme; höhere oder nicht zirkulante Terme nicht gerechnet. Keine Quantenkorrekturen. Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H226_Tauschbruch_phi.md`, `k440_test_h226.py`/`k440_out.txt`, `k440b_gegenprobe.wl`/`k440b_out.txt`, `README.md`.

Vergeben: H226, k440. Nächste frei: H227, k441 (vor Vergabe gegen `main` prüfen).
