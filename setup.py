#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setuptools should be used for both Python 3 and Python 2, see
# https://docs.python.org/2.7/library/distutils.html#module-distutils
from setuptools import setup

with open('README.md', 'r') as f:
    long_descr = f.read()
    long_descr_type = 'text/markdown'

setup(
    name='mcrp_utils',
    use_scm_version=True,
    description='MCNP-related packages. Common uitlities',
    long_description=long_descr,
    long_description_content_type=long_descr_type,
    author='A. Travleev',
    author_email='anton.travleev@gmail.com',
    url='https://github.com/travleev/mcrp_utils',
    packages=['mcrp_utils'],
    keywords='MCNP utilities',
    setup_requires=['setuptools_scm'],
    provides=['mcrp_utils'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
    ],
    )
