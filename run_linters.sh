#!/usr/bin/env bash

black --line-length=120 src/
flake8 --config conf/flake8.cfg src/
pylint --rcfile conf/pylintrc.cfg src/
mypy --strict --config=conf/mypy.ini --allow-untyped-calls src/
