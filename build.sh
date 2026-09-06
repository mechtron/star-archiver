#!/bin/sh
set -e
rm -rf dist build stararchiver.egg-info
python3 -m build
python3 -m pip install --user dist/*.whl
