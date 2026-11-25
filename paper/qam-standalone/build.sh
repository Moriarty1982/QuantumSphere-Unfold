#!/bin/sh
# Build the article three times and refresh the record snapshot shown in Appendix C.
# Usage: sh build.sh   (from paper/qam-standalone)
set -e
export TEXINPUTS=../../qam/tex:
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
  grep -v '^%' main.qam > record_snapshot.qam
done
python3 ../../qam/tools/qamhash.py verify main.qam
