##
## flush.py
## lazy remove auxilliary files

import subprocess as sp

sp.call(" rm *.log; rm *.lof; rm *.aux; rm *.bcf; rm *.run.xml; rm *.maf; rm *.out; rm *.alg; rm *.mtc*; rm *.xdy; rm *.acn; rm *.acr; rm *.syg; rm *.bbl; rm *.blg; rm *.glg; rm *.glo; rm *.gls; rm *.glsdefs; rm *.ist; rm *.lot; rm *.maf; rm *.ptc; rm *.sbl; rm *.sym; rm *.toc", shell=True)
