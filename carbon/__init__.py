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
from .opts import *

__version__ = '1.0.0'
__title__ = 'py-carbon'
__license__ = 'MIT'
__author__ = 'wulf'
__email__ = 'support@statch.tech'
__uri__ = "https://github.com/statch/py-carbon"
__copyright__ = 'Copyright 2021-2021 %s' % __author__

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=0, micro=0, releaselevel='final', serial=0)