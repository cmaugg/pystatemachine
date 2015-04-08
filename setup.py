#!/usr/bin/env python
# -*- coding: UTF-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pystatemachine import version

setup(
    name='pystatemachine',
    version=version,
    description='Simple Finite-State Machines',
    author='Christian Maugg',
    author_email='software@christianmaugg.de',
    url='https://github.com/cmaugg/pystatemachine',
    py_modules=['pystatemachine', ],
)
