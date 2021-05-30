#!/usr/bin/env python
import setuptools
import re

with open('README.md') as readme:
    long_description = readme.read()

with open('carbon/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


setuptools.setup(
    name='py-carbon',
    version=version,
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
