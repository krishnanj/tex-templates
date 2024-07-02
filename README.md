# TeX Templates

This repository contains a collection of useful LaTeX templates that I have used for many years. These templates are designed to streamline the process of creating reports, presentations, theses, and articles, making it easier to focus on the content rather than the formatting.

## Directory Overview

### reports/
The `reports/` directory includes several simple templates that can help you get started on writing any report or assignment. To compile these templates, use `pdflatex`.

### presentation/
The `presentation/` directory contains a few templates with simple Beamer themes that provide a useful starting point for creating a slide deck. To compile these templates, use `pdflatex`.

### thesis/
The `thesis/` directory contains a comprehensive set of TeX files for writing a full-fledged thesis. It also includes a final PDF version to give you an idea of what you can expect. These files were adapted from the [MIT thesis](https://web.mit.edu/thesis/tex/) to write [my PhD thesis](https://publications.rwth-aachen.de/record/775112). To compile, simply run `python3 run.py`.

### beamerarticle/
The `beamerarticle/` directory includes a LaTeX template for maintaining a document that can generate both a verbose article and a Beamer presentation simultaneously. Although it may be tricky to get used to, it is incredibly useful in the long run. This approach allows you to avoid repeating text, floats, and math between a document for your project and the presentations you give about it. To compile, run `pdflatex main.article.tex` and `pdflatex main.beamer.tex`. For more information on Beamer, check [here](http://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf). 

## Summary of Repository Contents

This repository includes various LaTeX templates organized into directories for reports, presentations, theses, and combined Beamer articles. Each directory contains example LaTeX files and related resources to help you quickly set up and compile your documents. These templates are designed to save time and ensure consistency across different types of documents.

## Contributions

[Ajay Mandyam Rangarajan](https://armandyam.github.io/) contributed to the thesis and Beamer article MWE (Minimum Working Example) included in this repository. His contributions have helped enhance the functionality and usability of these templates.

Happy TeXing!
