from __future__ import print_function

from iBot.iBotMaster import IBotMaster
import six
import sys

import os
import traceback

if six.PY3:
    unicode = str


__author__ = 'BS-DEV-QT-VFOURRIER'
__documentation__ = ''


class IBotFutures(IBotMaster):

    def __init__(self):
        super(IBotFutures, self).__init__()

    def connect(self):
        raise NotImplementedError

    def market_screen(self):
        # todo: read the JSON file for market and strategy to implement
        # todo: set iBotMaster attributes to read the parameters
        raise NotImplementedError

    def execute(self):
        self.market_screen()
        # todo: create an object in order to call market_screen.instruments etc
        connexion = self.connect()
        # the connexion to the trading account to get data
