"""Reversible finite-band realization of the Companion's example machine."""

import argparse
import json
from pathlib import Path

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


STATUSES = ("running", "halted", "boundary", "stuck")


class FiniteBand:
    """XOR the next configuration and status into a separate output register."""

    def __init__(self, program, cells):
        if cells < 1:
            raise ValueError("The tape must have at least one cell.")
        self.cells = cells
        self.states = program["states"]
        self.halt = program["halt"]
        if len(set(self.states)) != len(self.states) or self.halt not in self.states:
            raise ValueError("State names must be unique and include the halt state.")

        rules = {}
        for row in program["rules"]:
            key = row["state"], row["read"]
            if (key in rules or row["state"] not in self.states or row["state"] == self.halt
                or row["next"] not in self.states or row["read"] not in (0, 1)
                or row["write"] not in (0, 1) or row["move"] not in (-1, 0, 1)):
                raise ValueError(f"Invalid or duplicate rule: {row}")
            rules[key] = row

        self.head_bits = max(1, (cells - 1).bit_length())
        state_bits = max(1, (len(self.states) - 1).bit_length())
        self.width = cells + self.head_bits + state_bits
        circuit = QuantumCircuit(2 * self.width + 2, name="zuse_step")
        for cell in range(cells):
            circuit.cx(cell, self.width + cell)
        head_and_state = list(range(cells, self.width))

        for state_code, state in enumerate(self.states):
            for head in range(cells):
                for read in (0, 1):
                    rule = rules.get((state, read))
                    next_head, next_state, write = head, state_code, read
                    if state == self.halt:
                        status = "halted"
                    elif rule is None:
                        status = "stuck"
                    elif not 0 <= head + rule["move"] < cells:
                        status = "boundary"
                    else:
                        next_head = head + rule["move"]
                        next_state = self.states.index(rule["next"])
                        write = rule["write"]
                        status = "halted" if rule["next"] == self.halt else "running"

                    # Every row is scheduled; only the matching controls activate a row.
                    controls = [head, *head_and_state]
                    control_value = read | (self._position_code(head, state_code) << 1)
                    output_value = (
                        ((read ^ write) << head)
                        | (self._position_code(next_head, next_state) << cells)
                        | (STATUSES.index(status) << self.width)
                    )
                    for bit in range(self.width + 2):
                        if (output_value >> bit) & 1:
                            circuit.mcx(controls, self.width + bit, ctrl_state=control_value)
        self.circuit = circuit

    def _position_code(self, head, state_code):
        return head | (state_code << self.head_bits)

    def step(self, configuration):
        if configuration["status"] != "running":
            return configuration
        tape = configuration["tape"]
        head = configuration["head"]
        if len(tape) != self.cells or any(bit not in (0, 1) for bit in tape):
            raise ValueError("Expected a binary tape of the circuit's fixed length.")
        if not 0 <= head < self.cells:
            raise ValueError("The head must point to an existing cell.")
        if self.circuit.num_qubits > 18:
            raise ValueError("This Statevector example is limited to 18 qubits.")

        position = self._position_code(head, self.states.index(configuration["state"]))
        encoded = sum(bit << cell for cell, bit in enumerate(tape)) | (position << self.cells)
        initial = Statevector.from_int(encoded, (2,) * self.circuit.num_qubits)
        outcomes = initial.evolve(self.circuit).probabilities_dict(decimals=12)
        if len(outcomes) != 1:
            raise RuntimeError("Expected a single basis output.")
        (key, probability), = outcomes.items()
        result = int(key, 2)
        mask = (1 << self.width) - 1
        if probability != 1 or result & mask != encoded:
            raise RuntimeError("The output is not deterministic or the input changed.")
        output = result >> self.width
        return {
            "tape": [(output >> cell) & 1 for cell in range(self.cells)],
            "head": (output >> self.cells) & ((1 << self.head_bits) - 1),
            "state": self.states[(output & mask) >> (self.cells + self.head_bits)],
            "status": STATUSES[output >> self.width],
        }

    def trace(self, example):
        current = {key: example[key] for key in ("tape", "head", "state")}
        current["status"] = "halted" if current["state"] == self.halt else "running"
        trace = [current]
        for _ in range(example["steps"]):
            if current["status"] != "running":
                break
            current = self.step(current)
            trace.append(current)
        return trace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("program", nargs="?", type=Path,
                        default=Path(__file__).with_name("machine.json"))
    args = parser.parse_args()
    program = json.loads(args.program.read_text(encoding="utf-8"))
    for example in program["examples"]:
        machine = FiniteBand(program, len(example["tape"]))
        print(json.dumps({"example": example["name"], "mode": "fixed",
                          "trace": machine.trace(example)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
