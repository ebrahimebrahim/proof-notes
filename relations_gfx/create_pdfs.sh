#!/bin/bash

FILES=./*.svg
for f in $FILES
do
  echo "Processing $f..."
  inkscape --export-pdf="$(basename $f .svg).pdf" $f
done
