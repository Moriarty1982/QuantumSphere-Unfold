#!/usr/bin/env python3
"""Independent recomputation of the QAM hash chain, and release manifests.

  qamhash.py verify FILE.qam            recompute every claim hash and the record hash
  qamhash.py manifest FILE.qam OUT.json [FILES...] [--note TEXT]
                                        write SHA-256 sums of FILE.qam and FILES plus the record hash

Hash of a claim (same rule as qam.sty): MD5, upper-case hex, of the canonical line
    kind;key;frame;status;inputs;sources;statement
kind is input, claim, thesis, derive or convert(<map>); inputs are the listed inputs, sources the
hashes of the premises, both comma-separated; statement is empty except for a thesis.
Record hash: MD5 of all claim hashes in declaration order, each followed by a comma.
Only the standard library is used.
"""
import hashlib, json, os, sys


def md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest().upper()


def braces(field: str, name: str) -> list:
    assert field.startswith(name + " {") and field.endswith("}"), f"expected '{name} {{...}}', got '{field}'"
    inner = field[len(name) + 2:-1]
    return [x.strip() for x in inner.split(",") if x.strip()]


def parse(path):
    header, claims = {}, []
    with open(path, encoding="utf-8") as f:
        for n, raw in enumerate(f, 1):
            line = raw.rstrip("\n").strip()
            if not line:
                continue
            if line.startswith("%"):
                w = line[1:].split()
                if len(w) >= 4 and w[0] == "source" and w[2] == "md5":
                    header["source"], header["source_md5"] = w[1], w[3]
                elif len(w) == 2 and w[0] == "record":
                    header["record"] = w[1]
                continue
            if " := " not in line:
                continue  # map, compare, independent: no hash
            key, rhs = line.split(" := ", 1)
            parts = rhs.split("; ")
            body, frame, status, inputs, hsh, sources = parts[:6]
            statement = "; ".join(parts[6:])
            if statement.startswith("statement "):
                statement = statement[len("statement "):]
            if body.startswith("<6,"):
                kind, prem = "input", []
            elif body in ("claim", "thesis"):
                kind, prem = body, []
            elif body.startswith("derive(") and body.endswith(")"):
                kind, prem = "derive", [x.strip() for x in body[7:-1].split(",") if x.strip()]
            elif body.startswith("convert(") and body.endswith(")"):
                g, p = [x.strip() for x in body[8:-1].split(",")]
                kind, prem = f"convert({g})", [p]
            else:
                raise ValueError(f"{path}:{n}: unknown declaration '{body}'")
            claims.append(dict(line=n, key=key, kind=kind, prem=prem,
                               frame=frame.removeprefix("frame "), status=status.removeprefix("status "),
                               inputs=braces(inputs, "inputs"), hash=hsh.removeprefix("hash "),
                               sources=braces(sources, "sources"), statement=statement))
    return header, claims


def verify(path):
    header, claims = parse(path)
    errors, known = [], {}
    for c in claims:
        expected_sources = [known.get(p, "?") for p in c["prem"]]
        if c["sources"] != expected_sources:
            errors.append(f"line {c['line']}: {c['key']}: sources {c['sources']} are not the hashes of its premises {c['prem']}")
        canon = ";".join([c["kind"], c["key"], c["frame"], c["status"], ",".join(c["inputs"]),
                          ",".join(c["sources"]), c["statement"]])
        h = md5(canon)
        if h != c["hash"]:
            errors.append(f"line {c['line']}: {c['key']}: hash {c['hash']} does not match its content (recomputed {h})")
        known[c["key"]] = c["hash"]
    record = md5("".join(c["hash"] + "," for c in claims))
    if header.get("record") != record:
        errors.append(f"record hash {header.get('record')} does not match (recomputed {record})")
    src = header.get("source")
    if src:
        sp = os.path.join(os.path.dirname(path), src)
        if os.path.exists(sp):
            with open(sp, "rb") as f:
                m = hashlib.md5(f.read()).hexdigest().upper()
            if m != header["source_md5"]:
                errors.append(f"source {src} has md5 {m}, the record says {header['source_md5']}")
    return header, claims, record, errors


def sha256(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(argv):
    if len(argv) >= 2 and argv[0] == "verify":
        rc = 0
        for path in argv[1:]:
            _, claims, record, errors = verify(path)
            if errors:
                rc = 1
                print(f"{path}: {len(errors)} problem(s)")
                for e in errors:
                    print("  " + e)
            else:
                print(f"{path}: {len(claims)} claim hashes and the record hash {record[:8]} recomputed, all match")
        return rc
    if len(argv) >= 3 and argv[0] == "manifest":
        note = None
        if "--note" in argv:
            i = argv.index("--note"); note = argv[i + 1]; argv = argv[:i] + argv[i + 2:]
        qam, out, files = argv[1], argv[2], argv[3:]
        header, claims, record, errors = verify(qam)
        if errors:
            print("\n".join(errors)); return 1
        man = {"record_hash": record, "source": header.get("source"), "source_md5": header.get("source_md5"),
               "claims": {c["key"]: c["hash"] for c in claims},
               "files": {os.path.basename(p): sha256(p) for p in [qam] + files}}
        if note:
            man["checked"] = note
        with open(out, "w", encoding="utf-8") as f:
            json.dump(man, f, indent=1, ensure_ascii=False)
        print(f"{out}: manifest for {len(man['files'])} file(s), record {record[:8]}")
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
