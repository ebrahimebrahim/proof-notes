#!/bin/bash
set -e

PDF_LATEX_COMMAND="pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "
$PDF_LATEX_COMMAND lec_notes.tex
