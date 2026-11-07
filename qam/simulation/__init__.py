"""Finite QAM models on the optional Qiskit statevector backend."""

from collections import defaultdict
from dataclasses import dataclass

from qiskit.quantum_info import Statevector


@dataclass(frozen=True)
class Basis:
    """Ordered QAM labels, indexed by Qiskit's computational basis."""

    frame: str
    labels: tuple

    def __post_init__(self):
        size = len(self.labels)
        if not self.frame or size < 2 or size & (size - 1):
            raise ValueError("Declare a frame and a power-of-two basis of size >= 2.")
        if len(set(self.labels)) != size:
            raise ValueError("Basis labels must be distinct.")

    def prepare(self, label):
        return EncodedState(self, Statevector.from_int(self.labels.index(label), len(self.labels)))


@dataclass(frozen=True)
class EncodedState:
    basis: Basis
    vector: Statevector

    def evolve(self, circuit, *, target=None):
        """Apply a circuit. An explicit target declares the output interpretation."""
        target = self.basis if target is None else target
        if len(target.labels) != len(self.basis.labels):
            raise ValueError("A circuit transition requires equal basis dimensions.")
        return EncodedState(target, self.vector.evolve(circuit))

    def readout(self, frame, observable):
        """Group basis probabilities by a diagonal observable's output."""
        if frame != self.basis.frame:
            raise ValueError("Readout frame differs from the state frame. Declare a transition first.")
        probabilities = defaultdict(float)
        for label, probability in zip(self.basis.labels, self.vector.probabilities(), strict=True):
            probabilities[observable(label)] += float(probability)
        return dict(probabilities)
