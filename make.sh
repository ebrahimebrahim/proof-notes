#!/bin/bash
set -e

PDF_LATEX_COMMAND="pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "

$PDF_LATEX_COMMAND lec_notes.tex
$PDF_LATEX_COMMAND lec_notes.tex
$PDF_LATEX_COMMAND lec_notes.tex

python3 create_thms_only.py
$PDF_LATEX_COMMAND lec_notes_thms_only.tex
$PDF_LATEX_COMMAND lec_notes_thms_only.tex
$PDF_LATEX_COMMAND lec_notes_thms_only.tex

pdftk lec_notes.pdf lec_notes_thms_only.pdf cat output proofs.pdf
