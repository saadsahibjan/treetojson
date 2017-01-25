# !/usr/bin/env python
# coding: utf-8

"""
Converts a list or a list with a given regex grammar which contains a tree structure into a valid JSON.

This module works with both Python 2 and 3.
"""

__version__ = '0.1'
version = __version__

import logging

from nltk.chunk.regexp import *

LOG = logging.getLogger("treetojson")


def set_debug(debug=True, filename='dicttoxml.log'):
    if debug:
        import datetime
        print('Debug mode is on. Events are logged at: %s' % (filename))
        logging.basicConfig(filename=filename, level=logging.INFO)
        LOG.info('\nLogging session starts: %s' % (
            str(datetime.datetime.today()))
                 )
    else:
        logging.basicConfig(level=logging.WARNING)
        print('Debug mode is off.')
