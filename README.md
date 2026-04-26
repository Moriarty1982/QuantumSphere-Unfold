# QSC release workflow patch

Copy these files into the repository root.

Files:
- `.github/workflows/qsc-latex-build.yml`
  - Preview builds only for `main` pushes and manual dispatch.
- `.github/workflows/qsc-tagged-release-bundle.yml`
  - Runs only when a `v*` tag is pushed.
  - Builds PDFs from the tagged source.
  - Creates `releases/{version}/`.
  - Adds PDFs, source ZIP, release bundle ZIP, logs, audit files, and SHA256SUMS.
  - Commits `releases/{version}/` back to `main`.
  - Does not create a GitHub Release.

Typical use:
```bash
git tag v3.37.0
git push origin v3.37.0
```
