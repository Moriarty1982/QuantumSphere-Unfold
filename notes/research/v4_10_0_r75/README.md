# Layer v4.9.0-r75: Millennium matrix renamed to compensator matrix

Author decision, 3 November 2026: the 16×16 matrix 𝓜₁₆ of `sec:millennium-hc` is called the **compensator matrix**
(German: Kompensatormatrix). It carries several Heisenberg compensators and extends C = ½(id + J) to all layers.

| Record | Content |
|---|---|
| r75.1 | Naming rule. Symbol 𝓜₁₆, all labels (e.g. `sec:millennium-hc`) and the abbreviation MM (MM/HC, MM split) stay. Earlier layers, inherited appendices and notes keep the old wording; read “compensator matrix”. |
| r75.2 | Changed places: main body (nomenclature, probe–closure system, structural core, HC hypotheses, master model incl. section title and definition, which names the former term once), the 4.8 sections on the native operator link and the coupling candidate, PDF keywords. Local monolith: 27 patches, `llm/revision_spec_v490_r75.py`; main body word-identical again. Bibliography title “Third Millennium Edition” untouched. |

No definition, theorem, proof, number, register entry or guard changes. Guards: R_glob = (0,1,1,1,1), Γ_guard = (1,1,1,1,1), β₄ = 1/256 unspent.

Files: `rounds/v490_r75_round.tex` (verbatim copy of the layer), `llm/revision_spec_v490_r75.py` (patch list for the local monolith).
