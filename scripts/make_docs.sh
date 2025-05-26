rm -rf docs/_autosummary
rm -rf docs/autoapi
mkdir docs/_static
make -C docs clean
make -C docs html
