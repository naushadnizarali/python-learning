# Python Workspace

A monorepo consists of several Jupyter notebooks to learn Python

## Setup

To run the code, you need the packages `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `pandas` and `pillow`.
Some of the visualizations of decision trees and neural networks structures also require `graphviz`. The chapter
on text processing also requires `nltk` and `spacy`.

The easiest way to set up an environment is by installing [Anaconda](https://www.continuum.io/downloads).

### Installing packages with conda:

If you already have a Python environment set up, and you are using the `conda` package manager, you can get all packages by running

    conda install numpy scipy scikit-learn matplotlib pandas pillow graphviz python-graphviz

For the chapter on text processing you also need to install `nltk` and `spacy`:

    conda install nltk spacy

### Installing packages with pip

If you already have a Python environment and are using pip to install packages, you need to run

    pip install numpy scipy scikit-learn matplotlib pandas pillow graphviz

You also need to install the graphiz C-library, which is easiest using a package manager.
If you are using OS X and homebrew, you can `brew install graphviz`. If you are on Ubuntu or debian, you can `apt-get install graphviz`.
Installing graphviz on Windows can be tricky and using conda / anaconda is recommended.
For the chapter on text processing you also need to install `nltk` and `spacy`:

    pip install nltk spacy

### Downloading English language model

For the text processing chapter, you need to download the English language model for spacy using

    python -m spacy download en
