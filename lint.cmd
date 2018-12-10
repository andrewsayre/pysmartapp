@echo off
pip install -r test-requirements.txt --quiet
pylint tests pysmartapp
flake8 tests pysmartapp
pydocstyle tests pysmartapp