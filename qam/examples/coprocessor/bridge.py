"""Bruecke zwischen dem HDL-Kern (Baustufe 0) und Qiskit, Wolfram und OpenQASM.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.bridge run schaltung.qasm --json zustand.json --wolfram zustand.wl
    python -m qam.examples.coprocessor.bridge band schaltung.qasm          # Befehlsband ausgeben
    python -m qam.examples.coprocessor.bridge qasm band.txt                # Band -> OpenQASM 3

Austauschformate
- Gatterfolgen: OpenQASM 2 oder 3 (Gatter id x z s sdg t tdg h cx auf zwei Qubits). Qiskit liest und schreibt
  das direkt (qiskit.qasm3.loads/dumps); fuer OpenQASM 3 braucht Qiskit das Paket qiskit-qasm3-import.
- Befehlsband: das Textformat der Testbench (C adr wert / B / G op ziel / E), eine Zelle je Zeile.
- Zustand: JSON "qcop-state-1" mit den exakten ganzen Koeffizienten, k und Status, dazu Gleitkomma-Amplituden.
  to_statevector() macht daraus einen Qiskit-Statevector, to_wolfram() einen exakten Wolfram-Ausdruck.

Der Kern selbst bleibt unveraendert; die Bruecke sitzt aussen herum.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from .check import NAMES, OPS, STATUS, CFG, decode, default_cfg, reference, run_hdl

QASM_ALIASES = {"id": "nop"}
FORMAT = "qcop-state-1"


# ------------------------------------------------------------------ Gatterfolgen
def circuit_to_gates(circuit):
    """Qiskit-QuantumCircuit (2 Qubits) -> Liste (opcode, ziel). Nicht unterstuetzte Gatter: ValueError."""
    if circuit.num_qubits != 2:
        raise ValueError(f"Baustufe 0 rechnet zwei Qubits, die Schaltung hat {circuit.num_qubits}")
    gates = []
    for inst in circuit.data:
        name = QASM_ALIASES.get(inst.operation.name, inst.operation.name)
        qubits = [circuit.find_bit(q).index for q in inst.qubits]
        if name == "barrier":
            continue
        # qasm3.dumps schreibt id als U(0, 0, 0); das ist die Identitaet.
        if name in ("u", "u3") and all(abs(float(p)) < 1e-12 for p in inst.operation.params):
            name = "nop"
        if name not in OPS:
            raise ValueError(f"Gatter {inst.operation.name!r} ist im Kern nicht vorhanden "
                             f"(vorhanden: {', '.join(sorted(OPS))})")
        if name == "cx":
            control, target = qubits
            if control == target:
                raise ValueError("cx braucht zwei verschiedene Qubits")
            gates.append((OPS["cx"], target))
        else:
            gates.append((OPS[name], qubits[0]))
    return gates


def qasm_to_gates(text):
    """OpenQASM 2 oder 3 -> Liste (opcode, ziel)."""
    from qiskit import qasm2, qasm3

    head = text.lstrip()
    circuit = qasm3.loads(text) if head.startswith("OPENQASM 3") else qasm2.loads(text)
    return circuit_to_gates(circuit)


def gates_to_qasm(gates):
    """Liste (opcode, ziel) -> OpenQASM 3 (ohne Qiskit)."""
    lines = ["OPENQASM 3.0;", 'include "stdgates.inc";', "qubit[2] q;"]
    for op, tgt in gates:
        name = NAMES.get(op)
        if name is None:
            raise ValueError(f"unbekannter Opcode {op}")
        if name == "nop":
            lines.append(f"id q[{tgt}];")
        elif name == "cx":
            lines.append(f"cx q[{1 - tgt}], q[{tgt}];")
        else:
            lines.append(f"{name} q[{tgt}];")
    return "\n".join(lines) + "\n"


def gates_to_circuit(gates):
    from qiskit import QuantumCircuit

    qc = QuantumCircuit(2)
    for op, tgt in gates:
        name = NAMES[op]
        if name == "cx":
            qc.cx(1 - tgt, tgt)
        elif name == "nop":
            qc.id(tgt)
        else:
            getattr(qc, name)(tgt)
    return qc


# ------------------------------------------------------------------ Befehlsband
def gates_to_tape(gates, cfg=None):
    lines = [f"C {CFG[key]} {value}" for key, value in (cfg or {}).items()]
    lines.append("B")
    lines += [f"G {op} {tgt}" for op, tgt in gates]
    lines.append("E")
    return "\n".join(lines) + "\n"


def tape_to_gates(text):
    """Befehlsband -> (gates, cfg). Liest einen Fall (die Zellen bis zum ersten E)."""
    gates, cfg = [], {}
    names = {v: k for k, v in CFG.items()}
    for raw in text.splitlines():
        cell = raw.split("#", 1)[0].split()
        if not cell:
            continue
        if cell[0] == "C":
            cfg[names[int(cell[1])]] = int(cell[2])
        elif cell[0] == "G":
            gates.append((int(cell[1]), int(cell[2])))
        elif cell[0] == "E":
            break
    return gates, cfg


# ------------------------------------------------------------------ Zustaende
def make_state(status, k, done, flat):
    amps = decode(k, flat)
    return {
        "format": FORMAT,
        "qubits": 2,
        "order": "Qiskit (Bit q des Index = Qubit q)",
        "omega": "exp(i*pi/4)",
        "status": STATUS[status],
        "gates_done": done,
        "k": k,
        "coeffs": [flat[4 * i:4 * i + 4] for i in range(4)],
        "amplitudes": [[a.real, a.imag] for a in amps],
    }


def to_statevector(state):
    from qiskit.quantum_info import Statevector

    return Statevector([complex(re, im) for re, im in state["amplitudes"]])


def to_wolfram(state):
    """Exakter Wolfram-Ausdruck: Liste der vier Amplituden in Z[w]/Sqrt[2]^k."""
    terms = []
    for c in state["coeffs"]:
        terms.append(f"({c[0]} + {c[1]} w + {c[2]} w^2 + {c[3]} w^3)/Sqrt[2]^{state['k']}")
    return "With[{w = (1 + I)/Sqrt[2]}, {" + ", ".join(terms) + "}]"


def from_json(text):
    state = json.loads(text)
    if state.get("format") != FORMAT:
        raise ValueError(f"kein {FORMAT}-Zustand")
    return state


# ------------------------------------------------------------------ Ausfuehren
def run(gates_list, width=16, cfgs=None, simulate=True, iverilog=None, vvp=None):
    """Fuehrt Gatterfolgen aus: auf dem HDL-Kern (simulate=True, braucht iverilog) oder auf der exakten
    Python-Referenz mit denselben Regeln. Liefert je Folge einen qcop-state-1-Zustand."""
    cfgs = cfgs or [None] * len(gates_list)
    if not simulate:
        return [make_state(*reference(g, width, c)) for g, c in zip(gates_list, cfgs)]
    iverilog = iverilog or shutil.which("iverilog") or "iverilog"
    vvp = vvp or shutil.which("vvp") or "vvp"
    # Register behalten ihren Wert ueber Faelle hinweg: bei gemischten Konfigurationen jeden Fall voll schreiben.
    full = [{**default_cfg(width), **(c or {})} for c in cfgs] if any(cfgs) else None
    with TemporaryDirectory() as tmp:
        rows = run_hdl(gates_list, width, tmp, iverilog, vvp, cfgs=full, tag="_bridge")
    return [make_state(r[0], r[1], r[2], r[3]) for r in rows]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_run = sub.add_parser("run", help="OpenQASM oder Band auf dem HDL-Kern ausfuehren")
    p_run.add_argument("datei")
    p_run.add_argument("--width", type=int, default=16)
    p_run.add_argument("--json", help="Zustand als qcop-state-1 schreiben")
    p_run.add_argument("--wolfram", help="Zustand als exakten Wolfram-Ausdruck schreiben")
    p_run.add_argument("--referenz", action="store_true", help="Python-Referenz statt HDL-Simulation")
    p_band = sub.add_parser("band", help="OpenQASM -> Befehlsband")
    p_band.add_argument("datei")
    p_qasm = sub.add_parser("qasm", help="Befehlsband -> OpenQASM 3")
    p_qasm.add_argument("datei")
    args = ap.parse_args()

    text = Path(args.datei).read_text(encoding="utf-8")
    is_qasm = text.lstrip().startswith("OPENQASM")
    if args.cmd == "band":
        sys.stdout.write(gates_to_tape(qasm_to_gates(text)))
    elif args.cmd == "qasm":
        sys.stdout.write(gates_to_qasm(tape_to_gates(text)[0]))
    else:
        gates, cfg = (qasm_to_gates(text), {}) if is_qasm else tape_to_gates(text)
        state = run([gates], args.width, [cfg or None], simulate=not args.referenz)[0]
        out = json.dumps(state, indent=2)
        if args.json:
            Path(args.json).write_text(out + "\n", encoding="utf-8")
        else:
            print(out)
        if args.wolfram:
            Path(args.wolfram).write_text(to_wolfram(state) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
