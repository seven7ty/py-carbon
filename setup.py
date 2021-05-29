#!/usr/bin/env python
import setuptools
from carbon import __version__

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    dependencies = [_.strip() for _ in requirements]


setuptools.setup(
    name='py-carbon',
    version=__version__,
    description='Fully asynchronous Python library for carbon.now.sh',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='statch',
    author_email='poki@pokurt.me',
    url='https://github.com/itsmewulf/py-carbon',
    packages=setuptools.find_packages(exclude='example.py'),
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=dependencies,
    python_requires='>=3.9',
)