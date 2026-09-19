#!/bin/sh
set -e
rm -rf dist build stararchiver.egg-info
python3 -m build
if [ -n "$VIRTUAL_ENV" ]; then
  # Inside a virtualenv --user installs are rejected; a plain install
  # already targets the environment.
  python3 -m pip install dist/*.whl
else
  python3 -m pip install --user dist/*.whl
fi
