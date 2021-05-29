#!/usr/bin/env python
import setuptools
from carbon import __version__

with open('README.md') as readme:
    long_description = readme.read()


setuptools.setup(
    name='py-carbon',
    version=__version__,
    description='Fully asynchronous Python library for carbon.now.sh',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    license='MIT',
    author='statch',
    author_email='wulf.developer@gmail.com',
    url='https://github.com/itsmewulf/py-carbon',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.9',
)
