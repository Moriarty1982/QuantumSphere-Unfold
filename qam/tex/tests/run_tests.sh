#!/bin/sh
# Runs the qam.sty tests: pass*.tex must compile, fail*.tex must stop with the expected qam error.
cd "$(dirname "$0")"; export TEXINPUTS=..:
tmp=$(mktemp -d); ok=0; bad=0
for f in pass*.tex; do
  if pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$tmp" "$f" >/dev/null 2>&1; then echo "ok    $f"; ok=$((ok+1)); else echo "FAIL  $f (should compile)"; bad=$((bad+1)); fi
done
for f in fail*.tex; do
  if pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$tmp" "$f" >"$tmp/out.txt" 2>&1; then echo "FAIL  $f (should stop)"; bad=$((bad+1));
  elif grep -q "Package qam Error" "$tmp/out.txt"; then echo "ok    $f: $(grep -A1 'Package qam Error' "$tmp/out.txt" | head -2 | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-150)"; ok=$((ok+1));
  else echo "FAIL  $f (stopped, but not with a qam error)"; grep -m3 '^!' "$tmp/out.txt"; bad=$((bad+1)); fi
done
echo "$ok passed, $bad failed"; [ "$bad" -eq 0 ]
