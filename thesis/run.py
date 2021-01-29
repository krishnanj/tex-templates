##
## run.py
## lazy compile TeX files

import subprocess as sp

sp.call(" pdflatex main ; makeglossaries main;  biber main ;  pdflatex main;  pdflatex main", shell=True)
