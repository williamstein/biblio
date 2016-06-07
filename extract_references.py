#!/usr/bin/python
import os, sys

argv = sys.argv

if len(argv) == 1:
    print "Usage: %s key1 key2 ..."%argv[0]
    sys.exit(0)

file = "\\documentclass{article}\\usepackage{url}\n\\begin{document}\n"

for i in range(1,len(argv)):
    file = file + "\\cite{%s}\n"%argv[i]

file = file + \
       "\\bibliographystyle{amsalpha}\n\\bibliography{biblio}\n" + \
       "\\end{document}\n"

open("test.tex","w").write(file)

os.system("pdflatex test 1> log 2>>log; bibtex test 1>>log 2>>log")
os.system("pdflatex test 1> log 2>>log; bibtex test 1>>log 2>>log")

if not os.path.exists("test.bbl"):
    print "Error creating bibtex file."
    sys.exit(0)
    
bbl = open("test.bbl","r").read()
bbl = bbl[bbl.find("begin{thebibliography}"):]
bbl = bbl[bbl.find("\n")+1:]

print bbl[:bbl.find("\\end{thebibliography}")]
