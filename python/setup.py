#! /usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='pack',
    packages=["pack"],
    description="Example package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    url='http://github.com',
    author='Someone',
    author_email='someone@illinois.edu',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pack = pack.pack:main'
        ],
    },
    install_requires=[
        "pysam",
        "numpy",
    ],
)
