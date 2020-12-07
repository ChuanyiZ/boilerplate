# Boilerplate packages

A basic boilerplate for building packages aiming for distributing via pip and conda.

## python

1. Create a environment with `conda-build`. `conda create --name test python=3.6 conda-build`.
2. Activate the env `conda activate test`.
3. In `python/recipe/` folder, `conda-build ./ -c conda-forge -c bioconda` and get the path to the package.
4. Install to the local machine and test: `conda install -c bioconda -c file://<path> pack`, and then `pack -h`.
