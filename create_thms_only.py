# This script assumes that every theorem, axiom, and definition appears at the beginning of a line
# and that it ends at the next lone curly brace } on its own line

import re

THM_RE = [r"^\\THM\{",r"^\\DEFN\{",r"^\\THMP\{",r"^\\THMPL\{",r"^\\THMNP\{",r"^\\THMN\{",r"^\\AXIOM\{",r"^\\AXIOMN\{",r"^\\DEF\{"]

LINE_REPLACEMENTS = {
  r"\\newcommand\{\\THMP\}" : "\\newcommand{\THMP}[2]{\\thmbox{\\textbf{Theorem \putThmNumber:} \\thmcolonspace #1} }\n",
  r"\\newcommand\{\\THMPL\}" : "\\newcommand{\THMPL}[3]{\\thmbox{\\textbf{Theorem \putThmNumber{#3}:} \\thmcolonspace #1} }\n",
  r"\\newcommand\{\\THMNP\}" : "\\newcommand{\THMNP}[3]{\\thmbox{\\textbf{Theorem \putThmNumber\ (#1):} \\thmcolonspace #2} }\n",
  r"\\parskip1em" : "\\parskip0.5em",
  r"\\newcommand\{\\thmbox\}" : "\\newcommand{\\thmbox}[1]{\n\n\parbox{\\textwidth}{{#1}}}",
}

INCLUDE_TOKEN = "% INCLUDE THESE LINES IN THMS ONLY VERSION"
ENDINCLUDE_TOKEN = "% END INCLUDE"

def thm_cmd_in_line(line):
  for thm_cmd in THM_RE:
    if re.search(thm_cmd,line): return True
  return False

def replace_line_if_needed(line):
  for r in LINE_REPLACEMENTS.keys():
    if re.match(r,line) : return LINE_REPLACEMENTS[r]
  return line

def line_should_always_be_included(line):
  if re.search(r"^\\def",line): return True
  if "\\end{document}" in line : return True
  return False


fr = open("lec_notes.tex")
fw = open("lec_notes_thms_only.tex",'w')

inside_document_environment = False
writing_mode = True

for line in fr:
  if "\\begin{document}" in line:
    inside_document_environment = True
    fw.write(line)
    writing_mode = False
  if inside_document_environment and (thm_cmd_in_line(line) or INCLUDE_TOKEN in line) :
    writing_mode = True
  if writing_mode:
    fw.write(replace_line_if_needed(line))
  elif line_should_always_be_included(line):
    fw.write(line)
  if (re.search(r"^}\s*\n",line) or ENDINCLUDE_TOKEN in line) and inside_document_environment:
    writing_mode = False

fw.close
fr.close()
