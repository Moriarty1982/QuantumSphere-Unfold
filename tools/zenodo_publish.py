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


def put_file(bucket_url: str, token: str, path: Path, attempts: int = 3) -> Dict[str, Any]:
    """Stream one file into the deposition bucket.

    Zenodo's bucket API expects application/octet-stream with an explicit
    Content-Length; the file is streamed rather than read into memory, and a
    dropped connection is retried, since a PUT to the same key replaces it.
    """
    filename = path.name
    url = bucket_url.rstrip("/") + "/" + urllib.parse.quote(filename)
    size = path.stat().st_size
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream",
        "Content-Length": str(size),
    }
    last: Optional[Exception] = None
    for attempt in range(1, attempts + 1):
        try:
            with path.open("rb") as f:
                req = urllib.request.Request(url, data=f, headers=headers, method="PUT")
                with urllib.request.urlopen(req, timeout=900) as resp:
                    body = resp.read().decode("utf-8")
                    if resp.status not in (200, 201):
                        raise ZenodoError(f"Unexpected status {resp.status} uploading {filename}: {body[:500]}")
                    return json.loads(body) if body else {}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise ZenodoError(f"HTTP {exc.code} uploading {filename}: {body[:1000]}") from exc
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
            print(f"Upload attempt {attempt}/{attempts} for {filename} failed: {exc}")
            time.sleep(5 * attempt)
    raise ZenodoError(f"Network error uploading {filename} after {attempts} attempts: {last}")


def note(message: str) -> None:
    """Print a line; inside GitHub Actions also emit it as a notice annotation."""
    print(message)
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("::notice::" + message.replace("\n", " "))


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


def create_new_version(api_base: str, token: str, previous_id: str) -> Dict[str, Any]:
    """Create a new-version draft of an existing published deposition.

    Unlike a plain POST to /deposit/depositions, this keeps the record under the
    existing concept DOI.  Zenodo returns the *previous* deposition; the new
    draft is reached through links.latest_draft.
    """
    result = request_json("POST", f"{api_base}/deposit/depositions/{previous_id}/actions/newversion", token, payload={})
    draft_url = result.get("links", {}).get("latest_draft")
    if not draft_url:
        raise ZenodoError("newversion response did not include links.latest_draft")
    return request_json("GET", draft_url, token)


def reserved_doi(dep: Dict[str, Any]) -> Optional[str]:
    return (dep.get("metadata", {}).get("prereserve_doi") or {}).get("doi")


def remove_draft_files(api_base: str, token: str, deposition_id: str) -> List[str]:
    """Delete files a new-version draft inherited from its predecessor."""
    files = request_json("GET", f"{api_base}/deposit/depositions/{deposition_id}/files", token)
    removed: List[str] = []
    for entry in files if isinstance(files, list) else []:
        request_json("DELETE", f"{api_base}/deposit/depositions/{deposition_id}/files/{entry['id']}", token)
        removed.append(entry.get("filename", entry["id"]))
    return removed


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
    parser.add_argument("--new-version-of", default=None,
                        help="Published deposition ID to create a new-version draft from (keeps the concept DOI)")
    parser.add_argument("--replace-files", action="store_true",
                        help="Delete files inherited by the draft before uploading")
    parser.add_argument("--reserve-only", action="store_true",
                        help="Create or fetch the draft, set metadata, print the reserved DOI; upload nothing")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print manifest only")
    parser.add_argument("--publish", action="store_true", help="Publish after upload")
    parser.add_argument("--confirm-publish", action="store_true", help="Required together with --publish")
    parser.add_argument("--sleep-after-upload", type=float, default=0.0, help="Optional pause before publish")
    args = parser.parse_args()

    api_base = SANDBOX_API if args.environment == "sandbox" else ZENODO_API
    token_env = args.token_env or ("ZENODO_SANDBOX_TOKEN" if args.environment == "sandbox" else "ZENODO_TOKEN")

    payload = normalize_metadata(load_json(Path(args.metadata)))
    validate_metadata(payload)
    files = expand_files(args.files, allow_missing=args.dry_run or args.reserve_only)

    print(f"Zenodo environment: {args.environment}")
    print(f"API base: {api_base}")
    print(f"Metadata: {args.metadata}")
    print_manifest(files)

    if args.publish and not args.confirm_publish:
        raise ZenodoError("--publish requires --confirm-publish")

    if args.new_version_of and args.deposition_id:
        raise ZenodoError("Use either --new-version-of or --deposition-id, not both")

    if args.reserve_only and args.publish:
        raise ZenodoError("--reserve-only cannot be combined with --publish")

    if not args.dry_run and not files and not args.reserve_only:
        raise ZenodoError("Non-dry-run requires at least one upload file")

    if args.dry_run:
        print("Dry-run only: metadata validated; no Zenodo API mutation performed.")
        if not files:
            print("Note: no files were present. Add release files before non-dry-run upload.")
        return 0

    token = token_from_env(token_env)
    if args.new_version_of:
        dep = create_new_version(api_base, token, args.new_version_of)
        note(f"Created new-version draft of deposition {args.new_version_of}.")
    else:
        dep = create_or_fetch_deposition(api_base, token, args.deposition_id)
    deposition_id = str(dep.get("id"))
    links = dep.get("links", {})
    bucket_url = links.get("bucket")
    if not deposition_id or not bucket_url:
        raise ZenodoError("Deposition response did not include id and bucket link")
    if dep.get("submitted"):
        raise ZenodoError(f"Deposition {deposition_id} is already published; refusing to modify it")

    doi_before = reserved_doi(dep)
    note(f"Using draft deposition id: {deposition_id}")
    note(f"Reserved DOI: {doi_before or 'none reported'}")

    updated = set_metadata(api_base, token, deposition_id, payload)
    note("Metadata set.")
    doi_after = reserved_doi(updated)
    if doi_before and doi_after and doi_after != doi_before:
        raise ZenodoError(f"Reserved DOI changed from {doi_before} to {doi_after}; stopping")

    if args.reserve_only:
        print(json.dumps({"deposition_id": deposition_id, "reserved_doi": doi_after or doi_before,
                          "published": False, "files_uploaded": 0}, indent=2))
        print("Draft reserved. Put the reserved DOI on the title page, build, then re-run with "
              "--deposition-id and the final files.")
        return 0

    if args.replace_files:
        removed = remove_draft_files(api_base, token, deposition_id)
        note(f"Removed {len(removed)} inherited file(s): {', '.join(removed) or '-'}")

    for path in sorted(files, key=lambda p: p.stat().st_size):
        print(f"Uploading {path.name} ...")
        put_file(bucket_url, token, path)
        note(f"Uploaded {path.name} ({path.stat().st_size} bytes)")
    note("Files uploaded.")

    if args.sleep_after_upload > 0:
        time.sleep(args.sleep_after_upload)

    if args.publish:
        result = publish_deposition(api_base, token, deposition_id)
        print("Published deposition.")
        print(json.dumps({"deposition_id": deposition_id, "record_url": result.get("links", {}).get("html")}, indent=2))
    else:
        print(json.dumps({"deposition_id": deposition_id, "reserved_doi": doi_after or doi_before,
                          "published": False}, indent=2))
        print("Draft prepared. Re-run with --publish --confirm-publish only after manual review.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ZenodoError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        if os.environ.get("GITHUB_ACTIONS") == "true":
            print("::error::" + str(exc).replace("\n", " ")[:900])
        raise SystemExit(2)
    except Exception as exc:  # unexpected: report the type, never the token
        print(f"UNEXPECTED {type(exc).__name__}: {exc}", file=sys.stderr)
        if os.environ.get("GITHUB_ACTIONS") == "true":
            print(f"::error::UNEXPECTED {type(exc).__name__}: " + str(exc).replace("\n", " ")[:900])
        raise SystemExit(3)
