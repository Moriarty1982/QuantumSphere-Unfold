"""Collision-checked local numeric cache; never load Python pickle data."""
from collections import OrderedDict
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import threading
from typing import Any, Callable, Dict, Optional, Tuple
import uuid
import zipfile

import numpy as np


SCHEMA = 1
ArrayMap = Dict[str, np.ndarray]
Builder = Callable[[], ArrayMap]


@dataclass
class _MemoryEntry:
    packet: bytes
    outputs: ArrayMap
    size: int


def _array(value: Any) -> np.ndarray:
    array = np.array(value, copy=True, order="C", subok=False)
    if array.dtype.kind not in "biufc" or not np.all(np.isfinite(array)):
        raise ValueError("Cache arrays must be finite, non-object numeric arrays")
    return array


def _encode(operation: str, inputs: Any) -> Tuple[str, ArrayMap]:
    if not isinstance(operation, str) or not operation:
        raise ValueError("A nonempty operation name is required")
    arrays = {}

    def visit(value):
        if isinstance(value, (np.ndarray, np.generic)):
            array = _array(value)
            name = "input_"+str(len(arrays))
            arrays[name] = array
            kind = "numpy-scalar" if isinstance(value, np.generic) else "array"
            return [kind, name, array.dtype.str, list(array.shape)]
        if value is None:
            return ["none"]
        if isinstance(value, bool):
            return ["bool", value]
        if isinstance(value, int):
            return ["int", str(value)]
        if isinstance(value, float):
            if not np.isfinite(value):
                raise ValueError("Nonfinite cache input")
            return ["float", value.hex()]
        if isinstance(value, complex):
            if not np.isfinite(value):
                raise ValueError("Nonfinite cache input")
            return ["complex", value.real.hex(), value.imag.hex()]
        if isinstance(value, str):
            return ["str", value]
        if isinstance(value, bytes):
            return ["bytes", value.hex()]
        if isinstance(value, dict):
            if not all(isinstance(key, str) for key in value):
                raise ValueError("Cache dictionaries require string keys")
            return ["dict", [[key, visit(value[key])] for key in sorted(value)]]
        if isinstance(value, (list, tuple)):
            return ["tuple" if isinstance(value, tuple) else "list", [visit(item) for item in value]]
        raise ValueError("Unsupported cache input type: "+type(value).__name__)

    descriptor = json.dumps([SCHEMA, operation, visit(inputs)], ensure_ascii=True,
                            separators=(",", ":"))
    return descriptor, arrays


def _packet(descriptor: str, arrays: ArrayMap) -> bytes:
    pieces = [descriptor.encode("ascii")]
    pieces.extend(arrays[name].tobytes(order="C") for name in sorted(arrays))
    return b"".join(len(piece).to_bytes(8, "big")+piece for piece in pieces)


def _manifest(arrays: ArrayMap) -> Dict[str, dict]:
    return {name: {"dtype": value.dtype.str, "shape": list(value.shape),
                   "sha256": hashlib.sha256(value.tobytes(order="C")).hexdigest()}
            for name, value in arrays.items()}


def _copy(arrays: ArrayMap) -> ArrayMap:
    return {key: value.copy() for key, value in arrays.items()}


class MatrixCache:
    def __init__(self, root: Any, *, enabled: bool = True,
                 fingerprint: Optional[Callable[[bytes], str]] = None,
                 memory_limit_bytes: int = 128*1024*1024):
        self.root = Path(root)
        self.enabled = enabled
        self.fingerprint = fingerprint or (lambda data: hashlib.sha256(data).hexdigest())
        self.memory_limit_bytes = max(0, int(memory_limit_bytes))
        self.memory: OrderedDict[str, list[_MemoryEntry]] = OrderedDict()
        self.memory_bytes = 0
        self.lock = threading.RLock()
        self.stats = {"hits": 0, "disk_hits": 0, "misses": 0, "corrupt": 0, "write_errors": 0}

    def _remember(self, digest: str, packet: bytes, outputs: ArrayMap) -> None:
        """Retain a defensive copy within the byte budget; caller holds the lock."""
        size = len(packet)+sum(value.nbytes for value in outputs.values())
        if size > self.memory_limit_bytes:
            return
        bucket = self.memory.setdefault(digest, [])
        if any(entry.packet == packet for entry in bucket):
            return
        bucket.append(_MemoryEntry(packet, _copy(outputs), size))
        self.memory_bytes += size
        self.memory.move_to_end(digest)
        while self.memory_bytes > self.memory_limit_bytes:
            _, removed = self.memory.popitem(last=False)
            self.memory_bytes -= sum(entry.size for entry in removed)

    def _read(self, path: Path) -> Tuple[bytes, ArrayMap]:
        with path.open("rb") as stream, np.load(stream, allow_pickle=False) as archive:
            meta_array = archive["metadata"]
            if meta_array.dtype != np.dtype("uint8") or meta_array.ndim != 1:
                raise ValueError("Invalid cache metadata")
            meta = json.loads(meta_array.tobytes().decode("ascii"))
            if (not isinstance(meta, dict) or meta.get("schema") != SCHEMA
                    or not isinstance(meta.get("descriptor"), str)
                    or not isinstance(meta.get("inputs"), dict)
                    or not isinstance(meta.get("outputs"), dict) or not meta["outputs"]):
                raise ValueError("Unsupported cache schema")
            inputs = {key: _array(archive[key]) for key in meta["inputs"]}
            outputs = {key: _array(archive["output_"+str(i)])
                       for i, key in enumerate(meta["outputs"])}
            if _manifest(inputs) != meta["inputs"] or _manifest(outputs) != meta["outputs"]:
                raise ValueError("Cache array integrity failure")
            return _packet(meta["descriptor"], inputs), outputs

    def _write(self, digest: str, descriptor: str, inputs: ArrayMap,
               outputs: ArrayMap) -> None:
        bucket = self.root / digest
        bucket.mkdir(parents=True, exist_ok=True)
        # No shared index: concurrent writers create independent atomic bucket entries.
        meta = {"schema": SCHEMA, "descriptor": descriptor,
                "inputs": _manifest(inputs), "outputs": _manifest(outputs)}
        payload = dict(inputs)
        payload.update({"output_"+str(i): value for i, value in enumerate(outputs.values())})
        payload["metadata"] = np.frombuffer(json.dumps(meta, separators=(",", ":")).encode("ascii"), dtype=np.uint8)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=bucket, suffix=".tmp", delete=False) as file:
                temporary = Path(file.name)
                np.savez_compressed(file, **payload)
                file.flush()
                os.fsync(file.fileno())
            os.replace(temporary, bucket / (uuid.uuid4().hex+".npz"))
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)

    def _lookup(self, digest: str, packet: bytes) -> Optional[ArrayMap]:
        """Find an exact input match and return an isolated result."""
        with self.lock:
            for entry in self.memory.get(digest, []):
                if entry.packet == packet:
                    self.memory.move_to_end(digest)
                    self.stats["hits"] += 1
                    return _copy(entry.outputs)
            for path in sorted((self.root / digest).glob("*.npz")):
                try:
                    candidate, outputs = self._read(path)
                except (OSError, ValueError, KeyError, TypeError, EOFError, zipfile.BadZipFile):
                    self.stats["corrupt"] += 1
                    continue
                if candidate == packet:
                    self.stats["hits"] += 1
                    self.stats["disk_hits"] += 1
                    self._remember(digest, packet, outputs)
                    return _copy(outputs)
        return None

    @staticmethod
    def _compute(operation: str, inputs: Any, packet: bytes,
                 builder: Builder) -> ArrayMap:
        """Run without the cache lock, validating outputs and input stability."""
        built = builder()
        if not isinstance(built, dict) or not built or not all(isinstance(key, str) for key in built):
            raise ValueError("Cache builder must return a nonempty string-keyed array dictionary")
        outputs = {key: _array(value) for key, value in built.items()}
        after_descriptor, after_arrays = _encode(operation, inputs)
        if _packet(after_descriptor, after_arrays) != packet:
            raise ValueError("Cache inputs changed during calculation")
        return outputs

    def _publish(self, digest: str, descriptor: str, inputs: ArrayMap,
                 packet: bytes, outputs: ArrayMap) -> None:
        with self.lock:
            try:
                self._write(digest, descriptor, inputs, outputs)
            except OSError:
                self.stats["write_errors"] += 1
            self._remember(digest, packet, outputs)

    def get_or_compute(self, operation: str, inputs: Any, builder: Builder) -> ArrayMap:
        descriptor, input_arrays = _encode(operation, inputs)
        packet = _packet(descriptor, input_arrays)
        digest = self.fingerprint(packet)
        if not isinstance(digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", digest):
            raise ValueError("Fingerprint must contain 64 hexadecimal characters")
        digest = digest.lower()
        if self.enabled:
            found = self._lookup(digest, packet)
            if found is not None:
                return found
        with self.lock:
            self.stats["misses"] += 1
        outputs = self._compute(operation, inputs, packet, builder)
        if self.enabled:
            self._publish(digest, descriptor, input_arrays, packet, outputs)
        return _copy(outputs)


CACHE = MatrixCache(Path(__file__).resolve().parents[1] / "build/numerical-cache")


def cached(operation: str, inputs: Any, builder: Builder) -> ArrayMap:
    if os.environ.get("QSC_MATRIX_CACHE", "1") == "0":
        return MatrixCache(CACHE.root, enabled=False).get_or_compute(operation, inputs, builder)
    return CACHE.get_or_compute(operation, inputs, builder)


def svd(matrix: np.ndarray, *, full_matrices: bool = False
        ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Cache the decomposition, not a solve for a particular RHS or cutoff."""
    def build():
        u, singular, vh = np.linalg.svd(matrix, full_matrices=full_matrices)
        return {"u": u, "singular": singular, "vh": vh}
    result = cached("numpy.svd/v1", {"matrix": matrix, "full_matrices": full_matrices,
                                     "numpy_version": np.__version__,
                                     "implementation": hashlib.sha256(Path(__file__).read_bytes()
                                                                        .replace(b"\r\n", b"\n")).hexdigest()}, build)
    return result["u"], result["singular"], result["vh"]
