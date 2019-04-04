from __future__ import print_function

import six

if six.PY3:
    unicode = str

__author__ = 'BS-DEV-QT-VFOURRIER'
__documentation__ = ''


class Loader(object):

    def __init__(self):
        self.market_data = None
        self.futures_data = None
        self.query = None

    def get_data(self):
        return None
