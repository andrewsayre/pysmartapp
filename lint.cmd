@echo off
pip install isort --quiet
isort tests demo pysmartapp --recursive
pip install -r test-requirements.txt --quiet
pylint tests pysmartapp
flake8 tests pysmartapp
pydocstyle tests pysmartapp