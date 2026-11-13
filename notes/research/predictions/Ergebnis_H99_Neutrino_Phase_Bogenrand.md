# Ergebnis H99: Neutrino-Phase = Lepton-Phase + π/12 ist mit NuFIT 6.0 verträglich (1,3σ), mit den JUNO-Daten an der 2σ-Grenze

**13. November 2026. Vorab-Notiz `Vorab_Notiz_H99_Neutrino_Phase_Bogenrand.md` (Commit 5b23c5a). Skript `k221_test_h99.py`, Ausgabe `k221_out.txt`. Status: H99a bestätigt als verträglich (nicht blind); H99b nicht entscheidbar (Unsicherheit von Δm²₂₁ in NuFIT 6.1 nicht gefunden, Primärtabelle nicht eingesehen).**

## Kontrollen
| Kontrolle | Wert | Schranke | erfüllt |
|---|---|---|---|
| 1: K − 2/3 der Neutrino-Triole | 1,1·10⁻¹⁶ | 10⁻¹² | ja |
| 2: Lepton-Polmassen zurückgewonnen | 3,4·10⁻¹⁴ relativ | 10⁻¹⁰ | ja |
| 3: leichteste Wurzel negativ | Wurzeln (−0,1958; 0,9440; 2,2518)·t | Vorzeichen | ja |

## Ergebnis
θ_e = 0,2222248 (aus den Polmassen), θ_ν = θ_e + π/12 = 0,4840241, **R_pred = Δm²₂₁/Δm²₃₁ = 0,030839 ± 0,000001** (Unsicherheit aus m_τ).

| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H99a, NuFIT 6.0 (wie H2) | R_obs = 0,029805 ± 0,000792; Abweichung +0,001034 = +1,31σ | ≤ 2σ | **bestätigt als verträglich, nicht blind** |
| H99b, NuFIT 6.1 | Zentralwerte nur aus einer Sekundärquelle (arXiv:2601.18781, Tab. I: Δm²₂₁ = 7,53; Δm²₃₁ = 2,519 bzw. 2,529; σ(Δm²₃₁) = 0,021); σ(Δm²₂₁) nicht gefunden; Aufruf der NuFIT-Seite blieb ohne Freigabe | ≤ 2σ | **nicht entscheidbar** |

Ersatzrechnungen zu H99b, außerhalb des Kriteriums: Mit σ(Δm²₂₁) = 0,12 (JUNO allein, obere Grenze für den Fehler des globalen Fits) ergeben sich +1,76σ bzw. +1,99σ; mit 0,097 (JUNO-Nachanalyse in arXiv:2601.09791) +2,06σ bzw. +2,33σ. Das Urteil hängt also an der fehlenden Zahl und liegt an der Grenze.

## Warum es trägt und wo es eng wird
- Die Bedingung legt das Verhältnis der beiden Massendifferenzen ohne freie Zahl fest. Gegen die Daten vor JUNO passt es innerhalb von 1,3σ.
- Die Vorhersage liegt über dem Messwert: Mit Δm²₃₁ = 2,511 bis 2,529·10⁻³ eV² verlangt sie Δm²₂₁ = 7,74 bis 7,80·10⁻⁵ eV². JUNO hat 7,50 ± 0,12 gemessen; das sind +2,0 bis +2,5σ (nachträglich, ohne den Fehler von Δm²₃₁). JUNO wird Δm²₂₁ in den nächsten Jahren auf Bruchteile eines Prozents bestimmen; damit wird die Bedingung scharf prüfbar und ist derzeit eher unter Druck als gestützt.
- Abgeleitet mit der Skala aus Δm²₃₁ (nicht Teil des Kriteriums): Massen 0,38; 8,81; 50,13 meV, Summe 0,0593 eV, normale Ordnung. Das sind praktisch die Werte von H2.

## Lesart
- Das Kriterium gibt her: Die Bedingung „gleiche Überlappung ρ² = 1/2, Phase um die halbe Bogenbreite π/12 verschoben“ ist mit NuFIT 6.0 verträglich. Mehr nicht. Der Test war nicht blind; die Größenordnung war vorher überschlagen, und die Beziehung stammt aus der Literatur (Brannen).
- Nachträglich: Die Variante θ_e − π/12 gibt R = 0,0003 und scheidet aus.
- Keine Herleitung von K, der Phase oder der Verschiebung π/12; „Massenwurzel = Eigenwert“ bleibt Annahme. OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert.
- Mögliche nächste Frage, nur mit eigener Vorab-Notiz: R = 0,030839 als Vorhersage gegen das nächste JUNO-Ergebnis zu Δm²₂₁ festschreiben. Nach heutigem Stand wäre das eine Vorhersage mit Widerlegungsrisiko.
