#!/usr/bin/env python

import os
from setuptools import setup

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
    name='Power Rangers',
    version='0.1',
    description='A Python wrapper for Power Rangers API',
    author='Reinier van der Windt',
    author_email='hello@blueyes.io',
    url='http://powerapi.blueyes.nl',
    install_requires=[
        'requests==2.9.1'
    ],
)
