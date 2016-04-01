#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    requires = [line.strip() for line in f if line.strip()]

setup(
    name='Power Rangers',
    version='0.1',
    description='A Python wrapper for Power Rangers API',
    author='Reinier van der Windt',
    author_email='hello@blueyes.io',
    url='http://powerapi.blueyes.nl',
    install_requires=requires,
    test_suite='tests',
)
