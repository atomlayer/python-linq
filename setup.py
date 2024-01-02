#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Atomlayer
:license: GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007, see LICENSE file
:copyright: (c) 2024 Atomlayer
"""

version = '1.0.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-linq',
    version=version,

    author='Atomlayer',
    author_email='test@test.com',

    description=(
        u''
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/atomlayer/python-linq',
    download_url='https://github.com/atomlayer/python-linq/archive/main.zip',

    license='GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007, see LICENSE file',

    packages=['python-linq'],
    install_requires=[],

    classifiers=[
        'License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)