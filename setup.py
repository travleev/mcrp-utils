#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setuptools should be used for both Python 3 and Python 2, see
# https://docs.python.org/2.7/library/distutils.html#module-distutils
from setuptools import setup, find_packages


setup(name='mcrp_utils',
      # version: X.Y.Z, where:
      #    X -- major version. Different major versions are not back-compatible.
      #         New major version number, when code is rewritten
      #
      #    Y -- minor version. Increase, when new functionality is added.
      #
      #    Z -- update, increase, when a bug is fixed.
      version='1.0.1',
      description='MCNP-related packages. Uitlities',
      author='A. Travleev',
      author_email='anton.travleev@kit.edu',
      packages=find_packages('.'),
      package_dir={'': '.'},
      )
