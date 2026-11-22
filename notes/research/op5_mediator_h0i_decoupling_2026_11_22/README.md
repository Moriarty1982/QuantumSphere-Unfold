# Warum koppeln H_0i nicht? Trägt teilweise (Erkundung, teilweise nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Keine Dynamik der Zeit-Quer-Komponenten erzeugt die Entkopplung aus r39 von selbst: Fierz–Pauli auf dem
Unterraum sieht die erhaltene Quelle gar nicht, und Hilfsfelder H_0i geben einen zweiten Pol, außer im eingefrorenen Grenzfall. Exakt folgt
w = 0 dagegen, wenn der Austausch die beiden Zeitorientierungen seiner Enden gleich gewichtet: Dann heben sich die zeitungeraden Vertizes
J_0i weg. **Nach dem vorab festgelegten Raster: trägt teilweise** (die gleichen Gewichte sind eine benannte, nicht hergeleitete Bedingung).

Auftrag des Autors: „H_0i-Entkopplung begründen“. Verfahren vorab: `Methoden_Notiz.md` (Commit 0e57242a). Skript `h0i_decoupling.wl`,
Ausgabe `run/h0i_decoupling.txt`, Wolfram exakt. Qiskit nicht geeignet (kein Schaltkreis, klassischer Feldaustausch). Keine H-Nummer.

## Ergebnis
| Kandidat | Befund |
|---|---|
| K1 Fierz–Pauli (D = 3) | Zähler −½(c−1)(x−a)²(a+m²−x)(…)/m⁴: bei c = 1 identisch null, sonst am Pol null (nur Kontaktterme). Nie ∝ N_m. |
| K2 H_0i als Hilfsfelder | Über E_ij = ∂_tH_ij − ∂_iH_0j − ∂_jH_0i und Steifigkeit μ: Differenz zum Ziel −2a x d_m/(μ(x − x_μ)) mit zweitem Pol bei x_μ = (m² + r_m q)(1 − 2a/μ). Kein endliches μ gibt N_m; nur μ → ∞ (H_0i = 0 erzwungen). μ = 0: Zusatz −x(m² + r_m q)/d_m. |
| K3 Zeitumkehr-Parität | Unter ω ↦ −ω sind J_00 und J_ij gerade, J_0i ungerade, für jedes c. Zeitumkehr-Invarianz verbietet H_0iJ_0i genau dann, wenn H_0i T-gerade ist, also H unter T nicht wie ein Raumzeittensor transformiert. |
| K4 Orientierungsmittel | Gewicht p für gleiche, 1 − p für umgekehrte relative Zeitorientierung: exakt N(c, w = 2p − 1). N_m genau für p = (3c² − 2c + 1)/4; bei erhaltener Kopplung c = 1 also p = ½, λ = 3. p = 0: 2(x − a)² (Lorentz-Fall), p = 1: 2(x² + a²). Gegenprobe Tachyon-Abbildung: komplexer Zähler, keine Aufhebung. |

## Lesart
- Die Lesart aus r39 („Fierz–Pauli-artige Hilfsfelder ohne eigenen Pol“) hält nicht: K1 gibt null, K2 einen zusätzlichen Pol. Korrektur
  hiermit (r39 bleibt unverändert, append-only).
- Gewicht w und Orientierung hängen genau zusammen: w = 2p − 1. Die Entkopplung bedeutet, dass der Austausch gerade unter der relativen
  Zeitumkehr seiner beiden Enden ist. Das ist dieselbe Zeitumkehr (komplexe Konjugation), die nach H118 (r31.1) die Orientierung des
  Oktanten umkehrt und die kein Kandidat festlegt. „Nicht festgelegt“ ist aber nicht „gleich gewichtet“; die Bedingung p = ½ ist benannt,
  nicht hergeleitet.
- Zurückgestellte Idee I1, Auslöser 1 berührt: Zwei Enden mit unabhängiger Zeitorientierung passen zu einem String zwischen M und T (r37);
  unter G2 liegt T vor, M nach dem Urknall. Ob die Brücke beide Orientierungen gleich trägt, ist offen; dem Autor als Ausweg genannt.
- OP5 und H96 bleiben offen; OP3 ruht und wird nicht berührt.
