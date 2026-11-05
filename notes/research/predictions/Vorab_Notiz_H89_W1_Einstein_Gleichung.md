# Vorab-Notiz H89: Die Einstein-Gleichung von W1 in Teilen (Energie-Impuls-Tensor aus der Vierbein-Variation)

**Stand:** 5. November 2026, kurz vor Mitternacht, vor der Rechnung festgelegt. **Nicht blind:** Die Erwartungen sind analytisch vorgerechnet. Autor 23:39: „dann versuche das mal“ (die in H88 offen gebliebene Einstein-Gleichung). Rechnung mit Wolfram, wo die Laufzeitgrenze (≈ 100 s) es erlaubt, sonst mit sympy; das wird je Teil angegeben.

## Vorwissen geprüft
`Wirkung_W1_Dixon_U1.md`: Feldgleichung 3 „G̃_μν = κ(T^Weyl + T^Maxwell + T^(4f))_μν, ohne Λ“ (aus der Standardtheorie übernommen) und die Lesart „der Vier-Fermionen-Anteil verhält sich bei homogener Dichte wie eine Materie mit p = ρ und ρ ∝ −κn² (bekanntes Einstein–Cartan-Verhalten, Vorzeichen konventionsabhängig), nicht wie Λ“. H88 (Weyl-Gleichung, Torsion −(3/16)κ j·j, Ward bestätigt). Die Spinoren sind Skalare unter Koordinatenwechseln und tragen Frame-Indizes; j^a = ψ†σ̄^aψ hängt nicht vom Vierbein ab.

## Teile
- **H89a (Vier-Fermionen-Anteil allein):** Die Variation von e·L_4f, L_4f = −(3/16)κ η_ab j^a j^b, nach dem Vierbein bei festen ψ gibt T^(4f)_μν = −g_μν L_4f = (3κ/16)·j²·g_μν. Für sich genommen hat dieser Anteil die Form eines Λ-Terms (p = −ρ), mit einer Höhe ∝ j², nicht konstant.
- **H89b (homogener Zustand, ganzer Energie-Impuls-Tensor):** Zwei Weyl-Felder mit entgegengesetztem Spin, Gesamtstrom j = (n, 0, 0, 0), räumlich homogen, auf Lösungen der Weyl-Gleichung aus H88 (ψ_s = e^{−iEt}χ_s mit E = 3κn/8). Mit T_μν = T^Bel_μν − g_μν L_gesamt (Belinfante-Teil plus Spur) ergibt sich ρ = p = (3κ/16)n², also p = ρ mit **positivem** ρ.
- **H89c (Belinfante aus der Vierbein-Variation):** In erster Ordnung um den flachen Raum, e^a_μ = δ^a_μ + h^a_μ, mit dem torsionsfreien Spinzusammenhang erster Ordnung (aus de + ω∧e = 0 gelöst, nicht eingesetzt), ist −δS_Weyl/δh^a_μ bis auf ein Gesamtvorzeichen gleich dem Belinfante-Tensor (i/4)(ψ†σ̄_μ∂_νψ + ψ†σ̄_ν∂_μψ − c.c.) minus η_μν L_kin und symmetrisch in μν. Das rechtfertigt die Form in H89b.
- **Nicht geprüft:** die volle nichtlineare Einstein-Gleichung und die Bianchi-Identität auf allgemeinen Lösungen.

## Kriterien und Umgang mit Abweichungen
Jeder Teil gilt als bestätigt, wenn der symbolische Rest 0 ist (H89c: bis auf Gesamtvorzeichen und Gesamtableitung). Vergleich mit der W1-Notiz: Stimmt H89b, ist die Aussage „p = ρ“ der Notiz richtig für den ganzen Tensor, das Vorzeichen „ρ ∝ −κn²“ aber nicht (hier positiv); und die Aussage „nicht wie Λ“ ist für den Vier-Fermionen-Anteil allein (H89a) falsch formuliert. Abweichungen werden wie in H88 erst auf Konventionen, dann auf Rechenfehler, dann auf die Notiz zurückgeführt. Ob r81–r85 betroffen sind, wird danach bewertet (r81 stützt sich für „kein Vakuumterm“ auf diese Lesart).

Code: `llm/k204_w1_einstein.wl` bzw. `llm/k204_w1_einstein.py`.
