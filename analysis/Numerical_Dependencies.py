"""Composition root for scoped numerical services, without global resolution."""
from dataclasses import dataclass
import hashlib
from pathlib import Path
import threading
from typing import Protocol

import numpy as np


class NumericCache(Protocol):
    stats: dict

    def get_or_compute(self, operation, inputs, builder): ...


class SVDBackend(Protocol):
    @property
    def identity(self) -> dict: ...

    def svd(self, matrix, *, full_matrices=False): ...


class NumPySVDBackend:
    @property
    def identity(self):
        return {"backend": "numpy.linalg.svd", "version": np.__version__}

    def svd(self, matrix, *, full_matrices=False):
        return np.linalg.svd(matrix, full_matrices=full_matrices)


@dataclass(frozen=True, slots=True)
class NumericalServices:
    matrix_cache: NumericCache
    backend: SVDBackend

    def cached(self, operation, inputs, builder):
        return self.matrix_cache.get_or_compute(operation, inputs, builder)

    def svd(self, matrix, *, full_matrices=False):
        identity = self.backend.identity
        if (not isinstance(identity, dict) or not identity.get("backend")
                or not identity.get("version")):
            raise ValueError("Injected SVD backend requires an explicit versioned identity")

        def build():
            left, singular, right = self.backend.svd(matrix, full_matrices=full_matrices)
            return {"u": left, "singular": singular, "vh": right}

        implementation = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        result = self.cached("injected.svd/v1", {
            "matrix": matrix, "full_matrices": full_matrices,
            "backend": identity, "implementation": implementation}, build)
        return result["u"], result["singular"], result["vh"]


class NumericalContainer:
    """Own singleton providers for one calculation scope; inject only services."""
    def __init__(self, cache_factory, backend_factory=NumPySVDBackend):
        self._cache_factory = cache_factory
        self._backend_factory = backend_factory
        self._services = None
        self._lock = threading.Lock()

    def services(self) -> NumericalServices:
        with self._lock:
            if self._services is None:
                self._services = NumericalServices(self._cache_factory(), self._backend_factory())
            return self._services
