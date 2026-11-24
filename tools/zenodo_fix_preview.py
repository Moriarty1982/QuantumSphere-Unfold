"""Set the default preview of an already published Zenodo record (metadata-only edit, files unchanged).

Opens an edit draft of the published record, sets files.default_preview, publishes the edit and checks the result.
Usage: python tools/zenodo_fix_preview.py --record 24500009 --file NAME.pdf [--apply]
Without --apply it only reports the current state.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zenodo_publish import ZENODO_API, ZenodoError, rdm_request  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", required=True)
    ap.add_argument("--file", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    token = os.environ["ZENODO_TOKEN"]
    base = f"{ZENODO_API}/records/{args.record}"
    rec = rdm_request("GET", base, token)
    files = rec.get("files") or {}
    names = sorted((files.get("entries") or {}).keys())
    print(f"Record {args.record}, version {rec.get('metadata', {}).get('version')}, published={rec.get('is_published')}")
    print(f"Files: {', '.join(names)}")
    print(f"Current default_preview: {files.get('default_preview')}")
    if args.file not in names:
        raise ZenodoError(f"{args.file} is not a file of record {args.record}")
    if files.get("default_preview") == args.file:
        print("Preview already correct; nothing to do.")
        return 0
    if not args.apply:
        print("Dry run: would set the preview with a metadata-only edit.")
        return 0
    draft = rdm_request("POST", f"{base}/draft", token)  # edit draft of the published record
    draft.setdefault("files", {})["default_preview"] = args.file
    draft = rdm_request("PUT", f"{base}/draft", token, draft)
    if (draft.get("files") or {}).get("default_preview") != args.file:
        raise ZenodoError("Draft did not accept the preview")
    rdm_request("POST", f"{base}/draft/actions/publish", token)
    rec = rdm_request("GET", base, token)
    now = (rec.get("files") or {}).get("default_preview")
    print(f"default_preview after edit: {now}")
    return 0 if now == args.file else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ZenodoError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
