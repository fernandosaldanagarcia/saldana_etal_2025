----------------------------------------------

This repository contains code used in the following manuscript. 

Saldana F, Velasco-Hernández J, Ezanno P, Cecilia H (2025) 
Multiscale Modeling of Vector-Borne Diseases: The Role of Dose-Dependent Transmission


## Repository Structure

```
scripts/
    BH_Sobol_g.ipynb
    HistoFinal.ipynb
    multi_root.py
    varphi_psi_July9.ipynb
    WH_equilibriumG.ipynb
    WH_model.ipynb
    WVg.ipynb
```

## Requirements

The code is written in Python and uses Jupyter notebooks. The following Python libraries are required:

- numpy
- scipy
- matplotlib
- SALib

You can install the required libraries using pip:

```sh
pip install numpy scipy matplotlib SALib
```

If you want to run the notebooks, you will also need Jupyter:

```sh
pip install notebook
```

## Usage

1. Clone this repository.
2. Install the required libraries (see above).
3. Open the notebooks in the `scripts/` directory using Jupyter Notebook or JupyterLab.
4. Run the cells to reproduce the analyses and figures.

## Notes

- Some scripts (e.g., `HistoFinal.ipynb`) import helper functions from `multi_root.py`, so keep all files in the same directory.
