from __future__ import print_function

from abc import ABCMeta, abstractmethod

import six

if six.PY3:
    unicode = str

__author__ = 'BS-DEV-QT-VFOURRIER'
__documentation__ = ''


class IBotMaster(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def market_screen(self):
        raise NotImplementedError

