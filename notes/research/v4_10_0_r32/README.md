# v4.10.0-r32: Durchgerechneter OP5-Fall (Stand 22.11.)

22. November 2026. Auftrag des Autors: Runde schreiben, „so, dass das Hauptpaper die Quelle bleibt“. Die Runde ist die maßgebliche
Fassung des OP5-Falls, den das Physik-Paper (Abschnitt 6.9) und der deutsche Preprint (Abschnitt 4.4, Anhang B) verkürzt wiedergeben.
Sie steht als `rounds/v4100_r32_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Keine neue
H-, k- oder CT-Nummer, kein Guard ausgegeben.

| Eintrag | Inhalt |
|---|---|
| r32.0 | gesetzt: Antriebsoperator 𝒫 (Form aus dem Vergleichsmodell, Koeffizienten gewählt) und die Gleichsetzung δJ_OP5 = δ𝒥_h |
| r32.1 | Higgsquelle einer Kompression: δ𝒥_h = (Σ y n₀) ∇·u, δε|_v = −v δ𝒥_h |
| r32.2 | elastische Zwei-Komponenten-Präparation mit Paarfeder; δT; 𝓛∇S = K_L∇ΔS, δ𝒥_h = (β_ρK_L/v)Δ²S |
| r32.3 | kompakter gewöhnlicher Außenbeitrag: γ̄ = −16πG T_* (ohne die Gleichsetzung) |
| r32.4 | gerichteter Kontrast auf derselben Achse: 16𝒜P/(m²R⁴) (unter der Gleichsetzung) |
| r32.5 | Bündelfaktor 1 − 36κ⟨ξ⟩; planare Kontrolle |
| r32.6 | zweite Ordnung: Schaltarbeit −k R_F·ḋ; Piola-Term (1 + 1/c_σ)N(H) |
| r32.7 | Status: OP5, H96 offen |

Prüfung: `llm/r32_op5_derivations.wl` mit Ausgabe `llm/r32_op5_derivations.txt` (exakt, Wolfram; dieselbe Prüfung wie im Preprint-Prüfordner
`paper/preprint-de/audit/anhang-b/`). Guard-Linter: 0 Kandidaten in den Zeilen 4482–4676.

OP1–OP5, C5, C6/T2 offen.
