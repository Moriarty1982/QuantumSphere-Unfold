# Suche nach einem blinden Test aus den Runden r15–r17

15. November 2026, Claude Opus. **Erkundung, nicht blind**, ohne Kriterium. Auftrag des Autors: „Blinden Test suchen“.
Keine H-Nummer vergeben (H105 bleibt frei), Guards unverändert. Skript `neutrino_readout_checks.py`, Ausgabe
`run/neutrino_readout_checks_stdout.txt`.

## Vorgehen
Gesucht ist eine Folgerung der Strukturen aus r15–r17 (invariante Kugel χ, Zeitzyklus, Treue ½, Irreduzibilität,
Strang-Statistik), die eine noch nicht gemessene Größe festlegt, ohne neue freie Wahl. Erst dann wäre eine Vorab-Notiz
sinnvoll.

**Bereits durch offene Vorhersagen belegt** (`wiki/Vorhersagen-und-Tests.md`): θ₁₂ (H9), m_W (H15), θ₂₃ (H42, H46), Ω_M
(H96), R = Δm²₂₁/Δm²₃₁ (H100), m_τ (H102), normale Ordnung und Σm_ν = 0,0592 eV (H2, verträglich). Ein neuer Test bräuchte
eine andere Größe (etwa δ_CP, die leichteste Neutrinomasse, Majorana oder Dirac) oder eine schärfere Aussage über diese.

## Geprüfte Kandidaten
1. **Neutrinos als Auslesungen eines Objekts (Zeitzyklus mit positiven Gewichten, r16.9, r17.2).** Mit positiven
   Massenwurzeln ist K für Neutrinos höchstens 0,585 (normale Ordnung, m₁ = 0) bzw. 0,500 (invertiert); K = 2/3 ist nicht
   erreichbar. Neutrinos können in diesem Bild keine Koide-Auslesungen eines Objekts sein. Das ist bekannt (H2: K = 2/3 für
   Neutrinos nur mit negativer leichtester Wurzel) und kein Test.
2. **„Majorana heißt p₊ = p₋“** (beide Helizitätsanteile gleich, r16.9): Mit K = 2/3 folgt δ = 0, zwei gleiche Massen und
   R = 0 gegen beobachtet 0,0298. **Durch vorhandene Daten ausgeschlossen.**
3. **„Nur eine Helizität, p₋ = 0“** (flaches Oktant, leichtestes Neutrino masselos): Mit K = 2/3 folgt R = 0,0052 gegen
   0,0298. **Durch vorhandene Daten ausgeschlossen.**
4. **δ_CP aus dem Vorzeichen der Koide-Phase.** Das Vorzeichen kehrt sich nur unter antiunitärer Konjugation um (r15.5(c),
   r16.7); eine Abbildung auf die leptonische CP-Phase fehlt. Jede Zuordnung wäre eine neue Wahl.
5. **Majorana oder Dirac aus r16.5** (T bildet N auf das ladungskonjugierte N̄ ab, N ⊥ N̄). Daraus folgt kein Verbot von
   Majorana-Massen: Ein Majorana-Term ist eine Bilinearform auf N (r13.5), und r44 lässt genau diesen Term zu. Keine Aussage
   über den neutrinolosen Doppelbetazerfall.
6. **OP1, Strang-Statistik (r17.5).** Die Statistik ändert die Bündelung in einer Punktierung, nicht die Zählgleichung; γ und
   damit H15, H46, H96 bleiben gleich. Frame-abhängige logarithmische Entropiekorrekturen wären eine Folgerung, sind aber nicht
   messbar.

## Ergebnis
**Kein blinder Test gefunden.** Die Strukturen aus r15–r17 formulieren bekannte Größen um oder führen sie auf Setzungen
zurück; wo sie eine neue Aussage machen (Kandidaten 2 und 3), widerspricht sie schon vorhandenen Daten. Ein blinder Test
braucht eine neue Struktur, die eine heute freie Größe festlegt: Σp² = 2/3 (Treue ½), die Biegung (γ_M) oder die Statistik je
Frame (S2). Bis dahin bleiben die offenen Vorhersagen H9, H15, H42, H46, H96, H100, H102 und H2 die Prüfsteine.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.

## Nachtrag 15.11.2026: H2 nachgerechnet
Auftrag des Autors: „rechne h2 nochmal nach“. Vorab-Notiz `../v4_8_0_r03_r12/llm/Vorab_Notiz_H2_Neutrino_Triole.md`
(Commit 434c5a8), Skript `k15_test_h2.py`, Ergebnis `Ergebnis_H2_Neutrino_Triole.md` (v4.8.0-r12). Nachrechnung mit
`h2_recheck.py`, Ausgabe `run/h2_recheck_stdout.txt`.

1. **Reproduktion:** Das unveränderte Skript k15 gibt dieselben Werte wie das Ergebnis vom 20.10.: normale Ordnung
   m = (0,364; 8,662; 50,131) meV, Σ = 0,05916 ± 0,00023 eV, leichteste Wurzel negativ, K = 0,666667; invertierte Ordnung
   Σ = 0,10201 eV (über der Grenze 0,0642 eV, auch an den 2σ-Rändern).
2. **Neuere Eingaben** (normale Ordnung):

   | Δm²₂₁-Quelle | Σm_ν | Abstand zur Untergrenze (m₁ = 0) |
   |---|---|---|
   | NuFIT 6.0 (vorab festgelegt) | 0,05916 ± 0,00023 eV | 0,37 meV |
   | JUNO 2026 (erste Daten, 7,50 ± 0,12) | 0,05916 ± 0,00021 eV | 0,37 meV |
   | SNO+ (7,63 ± 0,17) | 0,05925 ± 0,00022 eV | 0,38 meV |
   | NuFIT 6.1 vollständig (7,537; Δm²₃₁ = 2,511) | 0,05917 ± 0,00021 eV | 0,38 meV |

   Die Vorhersage ist stabil: **Σm_ν = 0,0592 eV, m₁ ≈ 0,37 meV**, unabhängig von der Quelle.
3. **Urteil unverändert:** nach dem vorab festgelegten Kriterium (Grenze 0,0642 eV) **verträglich**. Die Einordnung von
   damals bleibt richtig: schwach trennend, nur etwa 0,4 meV über der Untergrenze der normalen Ordnung.
4. **Kosmologie, nachträglich und nicht Teil des Kriteriums:** Die Feldman–Cousins-Variante der DESI-Auswertung gibt
   Σ < 0,053 eV und läge unter H2, aber ebenso unter der Untergrenze 0,0588 eV jeder normalen Ordnung. Das ist eine Spannung
   zwischen ΛCDM-Kosmologie und Oszillationsdaten, kein besonderer Befund gegen H2; mit dynamischer dunkler Energie lockert
   sich die Grenze (bis 0,163 eV).
5. **Berichtigung im Wiki:** `wiki/Vorhersagen-und-Tests.md` führte H2 mit „normale Ordnung von JUNO gestützt“ (eingefügt
   mit Commit 3ab4980, ohne Fundstelle). Das stimmt nicht: Die ersten JUNO-Daten (59,1 Tage) messen θ₁₂ und Δm²₂₁ und sind
   unter Annahme der normalen Ordnung ausgewertet; die Ordnung bestimmt JUNO erst mit mehrjährigen Daten. Die Zeile ist
   berichtigt.

**Nebenbei berichtigt:** In der Antwort an den Autor zur Datenlage hieß es, der neueste NuFIT sei 6.0. Das Repo hat seit dem
13.11. die Primärtabelle von **NuFIT 6.1** (Ergebnis H99); H100 wartet auf die Version danach. Der Befund „keine neue
Version nach 6.1“ bleibt.
