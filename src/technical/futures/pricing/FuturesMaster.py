from __future__ import print_function

from abc import ABCMeta, abstractmethod

import six

if six.PY3:
    unicode = str

__author__ = 'BS-DEV-QT-VFOURRIER'
__documentation__ = ''


class Futures(metaclass=ABCMeta):

    def __init__(self):
        super(Futures, self).__init__()

    @abstractmethod
    def price(self):
        raise NotImplementedError
