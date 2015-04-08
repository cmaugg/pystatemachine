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
    long_description=open('README.rst').read(),
    author='Christian Maugg',
    author_email='software@christianmaugg.de',
    url='https://github.com/cmaugg/pystatemachine',
    py_modules=['pystatemachine', ],
    download_url='https://github.com/cmaugg/pystatemachine/tarball/{0}'.format(version),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='state finite-state machine automaton',
)
