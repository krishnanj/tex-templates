# tex-templates
This repository has some useful LaTeX templates that I have used for many years now. 

  The reports/ directory has a bunch of simple templates that can get you started on writing any report or assignment. To compile use pdflatex. 
  
  The presentation/ directory has a few templates with simple beamer themes that can be a useful start to create a slide-stack right away. To compile use pdflatex
  .
  
  The thesis/ directory has a bunch of TeX files for writing a full-fledged thesis. It also has a final pdf version to give you an idea of what you can expect. I adapted these files from the [MIT thesis](https://web.mit.edu/thesis/tex/) to write [my PhD thesis](https://publications.rwth-aachen.de/record/775112). To compile simply run python3 run.py.

The beamerarticle/ directory has the LaTeX template for maintaining a document that can generate a verbose article as well as a beamer at the same time. Its a bit tricky to get used to it, but super useful in the long run in my opinion. A lot of the text, float and math need not be repeated between a document you maintain for your project and presentations you may give about it time to time.  To read more about beamerarticle check [here](http://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf). To compile simply run pdflatex main.article.tex & pdflatex main.beamer.tex. [Ajay Mandyam Rangarajan](https://www.aices.rwth-aachen.de/en/people/rangarajan) also contributed to the thesis and beamerartcile MWE that lives in this repository.

Happy TeXing!
