# QAM methods paper

*A typed bookkeeping language for verifiable research with language models: design, Lean verification, and a case study*

Draft, 4 Nov 2026, 12 pages. Publication on Zenodo only (no arXiv). Keywords: logic in computer science, formal verification, Lean 4,
programming-language semantics, AI-assisted research, reproducibility, research integrity.

PDF: [`qam_paper_draft.pdf`](qam_paper_draft.pdf).

Build: `TEXINPUTS=../../qam/tex: pdflatex main.tex` twice (the paper uses its own package `qam.sty`) (standard TeX Live; no bibtex, bibliography is inline).

| file | content |
|---|---|
| `main.tex` | preamble, abstract, bibliography |
| `s1_intro.tex` | three error classes, contributions |
| `s2_language.tex` | object kinds, relations, two-sided display, witnesses/branches/status, reindexing |
| `s3_machine.tex` | store, instructions (MML), transition semantics (MMA), certificates |
| `s4_lean.tex` | theorems of `QSFormal.QAM`, `Models`, `Route`, `Store`, `StoreProgress`, `Provenance` |
| `s4b_tex.tex` | the LaTeX package `qam.sty`: compile-time checks and generated QAM notation |
| `s5_case.tex` | case study: process, register, error classes, translation table |
| `s6_related.tex` | related work |
| `s7_limits.tex` | limits, cost, next steps, conclusion |
| `a1_build.tex` | Lean modules, build, disclosure of language-model use |
| `outline.md` | original outline |

Open: final title; an independent referee pass; the related-work survey is short and not systematic.
