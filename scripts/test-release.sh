#!/usr/bin/bash

# local install
python setup.py sdist
python setup.py install
pip uninstall expkit

# test publish and install
python setup.py sdist upload -r pypitest
pip install --index-url https://test.pypi.org/simple/ expkit
pip uninstall expkit

# publish
python setup.py sdist upload -r pypi
