# OP1: Herkunft von β_sym, Test H165 (26.11.2026)

| Datei | Inhalt |
|---|---|
| `Sichtung_Herleitungsversuche.md` | 37 frühere Versuche, β_sym herzuleiten, mit Befund; schon geprüfte Kandidaten; notwendige Bedingungen |
| `Ergebnis_H165_Herkunft_Beta_sym_Schliessung.md` | Ergebnis-Notiz (widerlegt; Bilanz der Setzungen) |
| `k356_test_h165.py`, `k356_out.txt` | mpmath, sympy, Qiskit `quantum_info`; Aufruf ohne Argumente |
| `k357_werte_exakt_gegen_gerundet.py`, `k357_out.txt` | Erkundung: abgeleitete Zahlen beim exakten Wert gegen 0,5493482; kein Urteil kippt |
| `Nachrechnung_k358_Empfindlichkeit.md` | Erkundung: alle von β_sym, γ_L oder γ_M abhängigen Zahlen bei 0,5493, 0,5493482 und dem exakten Wert; Empfindlichkeit, σ-Abstände, Schwellen; kein Urteil kippt |
| `k358_empfindlichkeit.py`, `k358_out.txt` | mpmath; geschlossene Formeln, Messabstände, Schwellen, H102 |
| `k358b_maske_h46.py`, `k358c_maske_h134.py` mit `_out.txt` | Maskenscans von k105 und k263 mit ausgetauschtem ε |
| `k358d_gegenprobe.wl`, `k358d_out.txt` | Wolfram Language, Gegenprobe zu k358 |
| `k356b_gegenprobe.wl`, `k356b_out.txt` | Wolfram Language, unabhängige Gegenprobe; Ausgabe und Hinweis auf den Vorlauf |

Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H165_Herkunft_Beta_sym_Schliessung.md` (Commit e81f649).
Vergeben: H165, k356, k356b, k357, k358, k358b, k358c, k358d. Nächste freie Nummern: H166, k359.

Nachtrag 26.11.2026, 11:18 UTC: Der Autor nimmt die Zählregel als Postulat an. Die Runde dazu ist v4.10.0-r67 (`notes/research/v4_10_0_r67_zaehlpostulat/`).

Nachtrag 26.11.2026: Die Nachrechnung k358 steht als Runde v4.10.0-r68 im Companion (`notes/research/v4_10_0_r68_nachrechnung/`).
