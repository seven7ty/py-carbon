# -*- coding: utf-8 -*-

"""
Carbon code snippet generation
~~~~~~~~~~~~~~~~~~
Fully asynchronous Python library for carbon.now.sh.
:copyright: (c) 2021-2021 wulf
:license: MIT, see LICENSE for more details.
"""

from collections import namedtuple
from . import utils
from .carbon import *
from .errors import CarbonError
from .opts import *

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=0, micro=4, releaselevel='final', serial=0)

__version__ = f'{version_info.major}.{version_info.minor}.{version_info.micro}'
__title__ = 'py-carbon'
__license__ = 'MIT'
__author__ = 'wulf'
__email__ = 'paul@przybyszew.skie'
__uri__ = "https://github.com/statch/py-carbon"
__copyright__ = 'Copyright 2021-2023 %s' % __author__

__path__ = __import__('pkgutil').extend_path(__path__, __name__)
