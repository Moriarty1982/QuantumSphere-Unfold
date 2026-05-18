#!/usr/bin/env python3
"""Zenodo release helper for Quantum Sphaera Companion.

This script is intentionally conservative:
- it never stores or prints the Zenodo token;
- dry-run is the default in the GitHub Actions workflow;
- publishing requires an explicit --publish flag and --confirm-publish;
- production and sandbox endpoints are selected explicitly.

It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ZENODO_API = "https://zenodo.org/api"
SANDBOX_API = "https://sandbox.zenodo.org/api"


class ZenodoError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except JSONDecodeError as exc:  # type: ignore[name-defined]
        raise ZenodoError(f"Invalid JSON in {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ZenodoError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ZenodoError(f"Metadata file must contain a JSON object: {path}")
    return data


def normalize_metadata(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Accept either Zenodo's {'metadata': {...}} shape or a direct metadata object."""
    if "metadata" in raw and isinstance(raw["metadata"], dict):
        return raw
    return {"metadata": raw}


def validate_metadata(payload: Dict[str, Any]) -> None:
    md = payload.get("metadata", {})
    required = ["title", "upload_type", "creators", "description"]
    missing = [key for key in required if not md.get(key)]
    if missing:
        raise ZenodoError(f"Missing required metadata fields: {', '.join(missing)}")
    if not isinstance(md.get("creators"), list) or not md["creators"]:
        raise ZenodoError("metadata.creators must be a non-empty list")
    for creator in md["creators"]:
        if not isinstance(creator, dict) or not creator.get("name"):
            raise ZenodoError("each creator must be an object with a non-empty 'name'")


def expand_files(patterns: Iterable[str], *, allow_missing: bool = False) -> List[Path]:
    files: List[Path] = []
    for pattern in patterns:
        matches = sorted(Path(p) for p in glob.glob(pattern))
        if not matches and not allow_missing:
            raise ZenodoError(f"File pattern matched nothing: {pattern}")
        files.extend(p for p in matches if p.is_file())
    unique: Dict[str, Path] = {}
    for path in files:
        unique[str(path.resolve())] = path
    return list(unique.values())


def request_json(
    method: str,
    url: str,
    token: str,
    payload: Optional[Dict[str, Any]] = None,
    expected: Tuple[int, ...] = (200, 201, 202, 204),
) -> Dict[str, Any]:
    data = None
    headers = {"Authorization": f"Bearer {token}"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read().decode("utf-8") if resp.status != 204 else ""
            if resp.status not in expected:
                raise ZenodoError(f"Unexpected status {resp.status} from {url}: {body[:500]}")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise ZenodoError(f"HTTP {exc.code} from {url}: {body[:1000]}") from exc
    except urllib.error.URLError as exc:
        raise ZenodoError(f"Network error calling {url}: {exc}") from exc


def put_file(bucket_url: str, token: str, path: Path) -> Dict[str, Any]:
    filename = path.name
    url = bucket_url.rstrip("/") + "/" + urllib.parse.quote(filename)
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": mime,
    }
    with path.open("rb") as f:
        data = f.read()
    req = urllib.request.Request(url, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            body = resp.read().decode("utf-8")
            if resp.status not in (200, 201):
                raise ZenodoError(f"Unexpected status {resp.status} uploading {filename}: {body[:500]}")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise ZenodoError(f"HTTP {exc.code} uploading {filename}: {body[:1000]}") from exc


def token_from_env(env_name: str) -> str:
    token = os.environ.get(env_name)
    if not token:
        raise ZenodoError(f"Environment variable {env_name} is not set")
    return token


def print_manifest(files: List[Path]) -> None:
    if not files:
        print("Upload manifest: no files selected")
        return
    print("Upload manifest:")
    for path in files:
        print(f"  {path}  size={path.stat().st_size}  sha256={sha256_file(path)}")


def create_or_fetch_deposition(api_base: str, token: str, deposition_id: Optional[str]) -> Dict[str, Any]:
    if deposition_id:
        return request_json("GET", f"{api_base}/deposit/depositions/{deposition_id}", token)
    return request_json("POST", f"{api_base}/deposit/depositions", token, payload={})


def set_metadata(api_base: str, token: str, deposition_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"{api_base}/deposit/depositions/{deposition_id}", token, payload=payload)


def publish_deposition(api_base: str, token: str, deposition_id: str) -> Dict[str, Any]:
    return request_json("POST", f"{api_base}/deposit/depositions/{deposition_id}/actions/publish", token, payload={})


def main() -> int:
    parser = argparse.ArgumentParser(description="Create/update/publish a Zenodo deposition.")
    parser.add_argument("--metadata", required=True, help="Path to Zenodo metadata JSON")
    parser.add_argument("--files", nargs="*", default=[], help="File paths or glob patterns to upload")
    parser.add_argument("--environment", choices=["sandbox", "production"], default="sandbox")
    parser.add_argument("--token-env", default=None, help="Environment variable containing the token")
    parser.add_argument("--deposition-id", default=None, help="Existing draft deposition ID to update")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print manifest only")
    parser.add_argument("--publish", action="store_true", help="Publish after upload")
    parser.add_argument("--confirm-publish", action="store_true", help="Required together with --publish")
    parser.add_argument("--sleep-after-upload", type=float, default=0.0, help="Optional pause before publish")
    args = parser.parse_args()

    api_base = SANDBOX_API if args.environment == "sandbox" else ZENODO_API
    token_env = args.token_env or ("ZENODO_SANDBOX_TOKEN" if args.environment == "sandbox" else "ZENODO_TOKEN")

    payload = normalize_metadata(load_json(Path(args.metadata)))
    validate_metadata(payload)
    files = expand_files(args.files, allow_missing=args.dry_run)

    print(f"Zenodo environment: {args.environment}")
    print(f"API base: {api_base}")
    print(f"Metadata: {args.metadata}")
    print_manifest(files)

    if args.publish and not args.confirm_publish:
        raise ZenodoError("--publish requires --confirm-publish")

    if not args.dry_run and not files:
        raise ZenodoError("Non-dry-run requires at least one upload file")

    if args.dry_run:
        print("Dry-run only: metadata validated; no Zenodo API mutation performed.")
        if not files:
            print("Note: no files were present. Add release files before non-dry-run upload.")
        return 0

    token = token_from_env(token_env)
    dep = create_or_fetch_deposition(api_base, token, args.deposition_id)
    deposition_id = str(dep.get("id"))
    links = dep.get("links", {})
    bucket_url = links.get("bucket")
    if not deposition_id or not bucket_url:
        raise ZenodoError("Deposition response did not include id and bucket link")

    print(f"Using draft deposition id: {deposition_id}")
    set_metadata(api_base, token, deposition_id, payload)
    print("Metadata set.")

    for path in files:
        print(f"Uploading {path.name} ...")
        put_file(bucket_url, token, path)
    print("Files uploaded.")

    if args.sleep_after_upload > 0:
        time.sleep(args.sleep_after_upload)

    if args.publish:
        result = publish_deposition(api_base, token, deposition_id)
        print("Published deposition.")
        print(json.dumps({"deposition_id": deposition_id, "record_url": result.get("links", {}).get("html")}, indent=2))
    else:
        print(json.dumps({"deposition_id": deposition_id, "published": False}, indent=2))
        print("Draft prepared. Re-run with --publish --confirm-publish only after manual review.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ZenodoError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
