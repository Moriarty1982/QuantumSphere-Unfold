# Koide overlap reading — novelty check (15 Nov 2026)

**Question:** is the Koide material of v4.11.0 and v4.10.0-r12 to r15 a candidate for a first standalone paper?

**Answer:** not as it stands. The central reading (three qubit states from the three mutually unbiased bases, pairwise overlap
1/2, phase π/4, neutrino shift π/12) is in the literature since 2010. What remains is small or speculative. No text has been
written; this file records the check only.

## 1. Statement by statement

| Statement | Where in the repository | Prior work found | Verdict |
|---|---|---|---|
| `K = 2/3` ⇔ the square-root mass vector is at 45° to `(1,1,1)` | implicit in `K = (1 + 2ρ²)/3`, r12.2 | Foot, arXiv:hep-ph/9402242 (1994); restated by Rivero and Gsponer, arXiv:hep-ph/0505220 | known |
| Circulant form `√m_k ∝ 1 + √2 cos(δ + 2πk/3)`, `δ ≈ 2/9` | "Brannen form", r12.3, r44 | Brannen (2006, unpublished; 2010); Żenczykowski, Phys. Rev. D 86 (2012) 117303 and 87 (2013) 077302 for `δ ≈ 2/9` | known; the repository says so |
| Gram reading: three unit states, `K = Tr G²/(Tr G)² = (1 + 2ρ²)/3`, so `K = 2/3` ⇔ `ρ² = 1/2` | r12.2, r14.5 | the same content as Foot's angle and the "equal singlet and doublet norm" of the circulant form (e.g. Shulga, J. Phys. G 53 (2026) 105001, arXiv:2605.10245); the Gram-matrix wording itself was not found | restatement; one line of algebra |
| Octant triple: one eigenstate each of `σ_x`, `σ_y`, `σ_z`; overlap 1/2; Bargmann phase π/4; boundary of the Koide arc | r12.4(c) | Brannen, *Spin path integrals and generations*, Found. Phys. 40 (2010) 1681, arXiv:1006.3114: projectors `X, Y, Z` of the three mutually unbiased bases, `ZXYZ = √(i/8) Z` with `√i = e^{iπ/4}`, each transition of magnitude `1/√2` | known |
| The Brannen phase is one third of the Bargmann phase | r12.5(c), note `op3_eta_form_search_2026_11_13.md` | arXiv:1006.3114: the amplitudes are "the roots of the equation `z³ = (1+i)/4`" | known in substance |
| Neutrino phase = lepton phase + π/12 (H99) | r12.5(a), pre-registration H99 | Brannen (2006 talk; 2010 Eq. 69, 72): `2/9 + π/12`, with "the π/12 arises due to quantum phase". The H99 note already credits Brannen via a secondary source | known; now confirmed at the primary source |
| Koide as complete complementarity: one state per basis of a complete MUB set, `K = 2/(d+1)`, only `d = 2` gives three states | r15.4 | the `d = 2` case with three generations is the starting point of arXiv:1006.3114; the general-`d` formula was not found | `d = 2` known; general `d` is a two-line computation |
| One generation per frame map (`T`, `J_B`, `R` as `σ_z`, `σ_x`, `σ_y`) | r15.5, r16.7 | none found; depends on the frame doublet of the Companion | own reading; on one generation excluded by the commutant (r19.1, r19.2): needs copies set beforehand |
| `det G = (√2 cos φ − 1)/2`; flat octant ⇔ one mass zero; `φ = 2/3` gives the lepton ratios | r14.5 | determinant of the circulant at `ρ = 1/√2`; zero-electron-mass limit `m_τ/m_μ = ((1+√3)/(1−√3))²` in arXiv:hep-ph/0505220 | elementary consequence |
| Bend `π/4 − 2/3 = 0.118731` read as `γ_M/2`; guarded core as a flux-free cap; exactly one core | r14.5 to r14.7, H102 | none found | own, speculative; rests on CT-001/CT-002 and coincides with OP1 |
| Spin-1 triangle: `φ = 3 arccos(1 − 1/√2) − π = 0.679042`, rank three without a core | r15.3 | none found | own exact computation; misses 2/3 by 0.0124, no native axis found |
| Finite-gap constraints on a phase-averaged readout (`N = 15` at `D = 68`) | v4.11 section | none found | own; conditional on an assumed readout and a chosen `D` |

## 2. What this means

1. The reading that carries the Koide material — generations as the three mutually unbiased directions of a qubit, with the
   Koide value and a phase π/4 from the product of the three projectors — is Brannen's. A paper built on it would have to cite
   arXiv:1006.3114 as its starting point and could not present the octant, the π/4 or the π/12 as findings.
2. The research layers r12 to r15 did not cite arXiv:1006.3114 or Foot's note; they used "Brannen form" and "Brannen phase"
   as names. The H99 pre-registration credited Brannen for π/12 through a secondary source. Done on 15 Nov: round
   v4.10.0-r19.4 (PR #144) attaches both references to r12.2, r12.4(c), r12.5(c), r14.5, r15.4, r16.7 and H99.
3. Reception: arXiv:1006.3114 is published but disputed (a PhysicsOverflow review argues that three generations are not
   demonstrated). Building on it inherits that dispute.
4. The items without prior work are the weakest scientifically: the core/flux reading is tied to placeholders and to OP1, the
   spin-1 triangle misses the lepton phase, and the finite-gap section is conditional. None is a result that carries a paper.
5. The open predictions H100 and H102 are unaffected. H102 (`m_τ = 1777.134 MeV` from `γ_M`) is the only item here that
   could turn the own part into something testable; it is pending and rests on CT-001/CT-002.

## 3. Limits of the check

Searches: alphaXiv and web, 15 Nov 2026. arXiv:1006.3114 and arXiv:hep-ph/0505220 were read through an automated summary of
the ar5iv full text with targeted questions, not line by line; the quoted formulas and equation numbers come from that summary
and need to be confirmed in the PDF before they are cited. arXiv:2605.10245 was read in full. Foot's note was judged from its
abstract and from two papers that restate it. Brannen's 2006 talk was not read. "None found" means two searches without a hit,
not proof of absence.

## 4. Consequence for the paper plan

Neither the algebra kernel (`../kernel-note/outline.md`) nor the Koide reading supplies a new result for a research paper.
The candidates with their own content that remain, in the order of how self-contained they are:

- the QAM methods paper (`../qam/`, 12 pp. draft, Zenodo only by author decision of 4 Nov);
- the OP5 comparison model for mathematicians (`../op5/`, starting material only);
- the `C⊗H⊗O` generation section of `../short/`, whose novelty the referee report rates as weak (M4 to M7).

No open problem and no guard is affected by this file.

## Sources

- R. Foot, arXiv:hep-ph/9402242
- A. Rivero, A. Gsponer, arXiv:hep-ph/0505220
- C. A. Brannen, Found. Phys. 40 (2010) 1681, arXiv:1006.3114
- P. Żenczykowski, Phys. Rev. D 86 (2012) 117303; Phys. Rev. D 87 (2013) 077302, arXiv:1301.4143
- K. Shulga, J. Phys. G 53 (2026) 105001, arXiv:2605.10245
