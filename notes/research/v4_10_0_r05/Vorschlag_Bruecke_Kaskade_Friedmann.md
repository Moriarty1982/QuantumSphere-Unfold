# Vorschlag: Eine Brücke von der Kaskade (r31) zur Friedmann-Gleichung

**6. November 2026. Status: Vorschlag zur Entscheidung des Autors, mit einer groben Vorschau (offengelegt, keine Vorhersage).** Anlass: `Fundstellen_Dynamik_Lambda_Auslesung.md`. Die einzige Dynamik für das Verhältnis β² : (1 − β²) ist die r31-Kaskade; eine Brücke zur kosmischen Zeit fehlt.

## Zutaten aus dem Companion (nichts davon neu)
- Strata: S⁸ (Quelle), S⁴ (Materie), S² (Photon-Grundzustand; nach `thm:dark-energy` das, was als dunkle Energie erscheint).
- Der Fluss aus S⁸ geht zu β² nach S⁴ und zu 1 − β² nach S² (r31, für jede Rate).
- Rückweg S² → S⁸ durch Paarerzeugung aus dem Vakuum (r29, r31), Rate offen.

## Drei mögliche Brücken
1. **Besetzungen sind Dichten.** p₄/p₂ = β²·r hängt an der Rückweg-Rate r, gibt also nicht β². Verworfen.
2. **Feste Zufuhr.** Eine äußere Quelle Q(t) speist S⁸. Das bringt eine neue freie Funktion und ist ohne Begründung aus der Struktur nicht zu empfehlen.
3. **Rückgekoppelte Kaskade (Empfehlung).** Der Inhalt von S² ist Vakuumenergie (w = −1). Er wird mit der Rate Γ über den Rückweg nach S⁸ gebracht und dort sofort aufgeteilt: β² nach S⁴ (Materie), 1 − β² zurück nach S². Netto zerfällt Vakuum mit der Rate β²Γ in Materie:
   - ρ̇_Λ = −β²Γ ρ_Λ,
   - ρ̇_M + 3Hρ_M = +β²Γ ρ_Λ,
   - Strahlung und Baryonen wie üblich.

   **Zeit je Schritt:** Γ = ε·H, also ein Kaskadenschritt je 1/(εH). Die natürliche Wahl ε = 1 (ein Schritt je Hubble-Zeit) lässt **keinen freien Parameter**. Dann ist ρ_Λ ∝ a^{−β²}, die effektive Zustandsgleichung des Vakuums w = −1 + β²/3 ≈ −0,90, und Energie fließt vom Vakuum in die Materie. Mit Ω_M heute = β² (H96, als Eingabe) liegt H(z) dann vollständig fest.

## Grobe Vorschau (vor jeder Vorab-Notiz gerechnet; deshalb wäre ein Test damit nicht blind)
H(z) im Verhältnis zu flachem ΛCDM mit gleichem Ω_M heute:

| ε | w_Vakuum | z = 0,5 | z = 1 | z = 2 |
|---|---|---|---|---|
| 0,5 | −0,95 | 0,988 | 0,971 | 0,952 |
| 1 | −0,90 | 0,975 | 0,939 | 0,897 |

Bei ε = 1 liegt H(z) um z ~ 1 etwa 6 % unter ΛCDM. BAO-Abstände sind auf wenige Prozent vermessen (Vorwissen). Ich erwarte daher, dass ε = 1 an den DESI-Daten scheitert, ε = 0,5 vermutlich auch. Das ist eine Vermutung, nicht geprüft.

## Was der Autor festlegen müsste, bevor gerechnet wird
1. **Brücke 3**, also der Inhalt von S² als Vakuumenergie, die mit dem Rückweg in Materie zerfällt.
2. **ε**: entweder fest ε = 1 (keine freie Größe, schärfster Test) oder frei (dann nur eine Schranke an ε, kein Test der Struktur).
3. **Prüfdaten:** der Vergleich der Abstände D_M/r_d und D_H/r_d mit DESI DR2 BAO. Das sind bekannte Daten; der Test wäre also **nicht blind**, aber ohne freien Parameter. Eine blinde Variante wäre DESI DR3.

## Einordnung
- Brücke 3 ist ein bekanntes Modell (ein mit Materie wechselwirkendes Vakuum, „running vacuum“). Neu wäre nur, dass die Struktur die Rate (β²·H) ohne freien Parameter festlegt.
- Scheitert ε = 1 an den Daten, ist diese einfachste Brücke ausgeschlossen. Dann bleibt die Λ-Auslesung eine Aussage über eine Epoche (H96), ohne Dynamik.
- Auch eine Bestätigung würde das „warum jetzt“ nicht erklären, denn Ω_M heute = β² ist hier Eingabe.
