from __future__ import print_function

import six
import sys

import os
import traceback

from Technical.SaveLog import SaveLog

if six.PY3:
    unicode = str

sys.stdout = SaveLog()
print(os.path.basename(__file__))

__author__ = 'BS-DEV-QT-VFOURRIER'
__documentation__ = ''


