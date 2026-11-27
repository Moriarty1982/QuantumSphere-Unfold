"""Kern stabilisieren: HDL-Kern ueber die Bruecke gegen Qiskit und Wolfram pruefen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.bridge_check --cases 300 --seed 7
    python -m qam.examples.coprocessor.bridge_check --write-wolfram     # Wolfram-Skript neu schreiben

Pruefungen
1. Qiskit-Schaltung -> OpenQASM 3 (qasm3.dumps) -> Bruecke -> Gatterfolge: gleich der Ausgangsfolge.
2. Gatterfolge -> OpenQASM 3 (Bruecke, ohne Qiskit) -> qasm3.loads -> Bruecke: Rundweg ohne Verlust.
3. HDL-Simulation des Rundweg-Bands gleich Qiskit-Statevector der Ausgangsschaltung (Abstand <= 1e-12, ohne
   Phasenausgleich, weil der Kern exakt rechnet); JSON-Zustand hin und zurueck verlustfrei.
4. Wolfram: wolfram/bridge_exakt.wl enthaelt feste Faelle mit den exakten HDL-Zustaenden. Der Lauf erzeugt den
   Inhalt neu und verlangt Gleichheit mit der gespeicherten Datei (so gilt die gespeicherte Wolfram-Ausgabe
   bridge_exakt_out.txt weiter). Ist wolframscript im Suchpfad, wird das Skript zusaetzlich ausgefuehrt.
"""

import argparse
import json
import random
import shutil
import subprocess
from pathlib import Path

from . import bridge
from .check import NAMES, OPS

HERE = Path(__file__).resolve().parent
WL = HERE / "wolfram" / "bridge_exakt.wl"
WOLFRAM_CASES = 8


def random_circuit(rng, n):
    from qiskit import QuantumCircuit

    qc = QuantumCircuit(2)
    for _ in range(n):
        name, tgt = rng.choice(list(OPS)), rng.randint(0, 1)
        if name == "cx":
            qc.cx(1 - tgt, tgt)
        elif name == "nop":
            qc.id(tgt)
        else:
            getattr(qc, name)(tgt)
    return qc


def wolfram_script(cases, states):
    lines = [
        "(* Erzeugt von bridge_check.py: exakte Gegenprobe der Bruecke. Je Fall die Gatterfolge (aus OpenQASM)",
        "   und der exakte HDL-Zustand; Wolfram rechnet den Zustand mit Kronecker-Matrizen nach. *)",
        "w=(1+I)/Sqrt[2];id=IdentityMatrix[2];",
        'g1["x"]={{0,1},{1,0}};g1["z"]=DiagonalMatrix[{1,-1}];g1["s"]=DiagonalMatrix[{1,I}];'
        'g1["sdg"]=DiagonalMatrix[{1,-I}];',
        'g1["t"]=DiagonalMatrix[{1,w}];g1["tdg"]=DiagonalMatrix[{1,Conjugate[w]}];'
        'g1["h"]={{1,1},{1,-1}}/Sqrt[2];g1["nop"]=id;',
        'op[{"cx",t_}]:=Module[{m=ConstantArray[0,{4,4}]},Do[With[{c=BitAnd[i,If[t==1,1,2]]!=0},'
        'm[[If[c,BitXor[i,If[t==1,2,1]],i]+1,i+1]]=1],{i,0,3}];m];',
        "op[{n_,0}]:=KroneckerProduct[id,g1[n]];op[{n_,1}]:=KroneckerProduct[g1[n],id];",
        "data={",
    ]
    rows = []
    for n, (gates, state) in enumerate(zip(cases, states)):
        gs = ",".join(f'{{"{NAMES[o]}",{t}}}' for o, t in gates)
        rows.append(f"  {{{n},{{{gs}}},{bridge.to_wolfram(state)}}}")
    lines.append(",\n".join(rows))
    lines += [
        "};",
        "Do[{n,gs,hdl}=d;psi=Fold[Expand[op[#2].#1]&,{1,0,0,0},gs];",
        ' Print["Fall ",n,": Gatter ",Length[gs],", exakte Differenz ",Expand[ComplexExpand[psi-hdl]]],{d,data}]',
    ]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cases", type=int, default=300)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--write-wolfram", action="store_true")
    args = ap.parse_args()

    from qiskit import qasm3
    from qiskit.quantum_info import Statevector

    rng = random.Random(args.seed)
    circuits = [random_circuit(rng, rng.randint(1, 30)) for _ in range(args.cases)]
    originals, taped = [], []
    for n, qc in enumerate(circuits):
        gates = bridge.circuit_to_gates(qc)
        via_qasm = bridge.qasm_to_gates(qasm3.dumps(qc))
        if via_qasm != gates:
            raise SystemExit(f"Fall {n}: Qiskit-QASM -> Bruecke {via_qasm} != {gates}")
        back = bridge.qasm_to_gates(bridge.gates_to_qasm(gates))
        if back != gates:
            raise SystemExit(f"Fall {n}: Rundweg ueber Bruecken-QASM {back} != {gates}")
        tape_gates, _ = bridge.tape_to_gates(bridge.gates_to_tape(back))
        originals.append(gates)
        taped.append(tape_gates)
    print(f"QASM: {len(circuits)} Schaltungen, Qiskit -> OpenQASM 3 -> Bruecke -> Band -> OpenQASM 3 -> Bruecke "
          f"verlustfrei")

    states = bridge.run(taped)
    max_dev, ok = 0.0, 0
    for n, (qc, state) in enumerate(zip(circuits, states)):
        if state["status"] != "continue":
            raise SystemExit(f"Fall {n}: Status {state['status']}")
        if bridge.from_json(json.dumps(state)) != state:
            raise SystemExit(f"Fall {n}: JSON-Rundweg nicht verlustfrei")
        want = Statevector.from_instruction(qc).data
        got = bridge.to_statevector(state).data
        dev = max(abs(a - b) for a, b in zip(got, want))
        max_dev = max(max_dev, dev)
        if dev > 1e-12:
            raise SystemExit(f"Fall {n}: HDL weicht von Qiskit ab ({dev}); {originals[n]}")
        ok += 1
    print(f"HDL ueber Bruecke = Qiskit-Statevector in {ok} von {len(circuits)} Faellen, "
          f"max Abstand {max_dev:.2e}; JSON-Zustand verlustfrei")

    script = wolfram_script(taped[:WOLFRAM_CASES], states[:WOLFRAM_CASES])
    if args.write_wolfram:
        WL.write_text(script, encoding="utf-8")
        print(f"Wolfram-Skript geschrieben: {WL.relative_to(HERE)}")
    elif WL.read_text(encoding="utf-8") != script:
        raise SystemExit("HDL-Zustaende weichen von den in wolfram/bridge_exakt.wl gespeicherten ab "
                         "(neu pruefen und --write-wolfram)")
    else:
        print(f"Wolfram: {WOLFRAM_CASES} gespeicherte exakte Faelle gleich der aktuellen HDL-Ausgabe "
              f"(Ausgabe des Wolfram-Laufs: wolfram/bridge_exakt_out.txt)")
    engine = shutil.which("wolframscript")
    if engine and not args.write_wolfram:
        out = subprocess.run([engine, "-file", str(WL)], capture_output=True, text=True, check=True).stdout
        diffs = [line for line in out.splitlines() if "Differenz" in line]
        if len(diffs) != WOLFRAM_CASES or any(not line.endswith("{0, 0, 0, 0}") for line in diffs):
            raise SystemExit("Wolfram meldet Abweichungen:\n" + out)
        print(f"Wolfram ausgefuehrt: {WOLFRAM_CASES} Faelle exakt gleich")


if __name__ == "__main__":
    main()
