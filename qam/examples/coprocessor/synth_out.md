| Baustein | synthesefest | Zellen (synth -noabc, sofern nicht anders genannt) |
|---|---|---:|
| qcop2_top W=16 | ja | 20049 |
| qcop2p_top W=16, 4 Kontexte (Pipeline) | ja | 24751 |
| qcop2_sys W=16 (mit Boot-Monitor, 1024 Worte; iCE40-Zellen, 8 Block-RAM) | ja | 9469 |
| qboot | ja | 968 |
| qband 128 Zellen, 16 Abschnitte | nein: Warning: Latch inferred for signal `\qband.\len_j' from process `\qband.$qam/examples/coprocessor/hdl/qband.sv:77$proc$228': $auto$proc_dlatch.cc:649:proc_dlatch$24235 | 16656 |
| tape_core direkt | ja | 427 |
| tape_core zyklisch | ja | 463 |
| guard_stream | ja | 1025 |
| context_filter | ja | 200 |
