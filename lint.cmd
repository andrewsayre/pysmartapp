@echo off
pip install -r test-requirements.txt --quiet
pylint pysmartapp pysmartapp
flake8 pysmartapp pysmartapp
pydocstyle pysmartapp pysmartapp