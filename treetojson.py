# !/usr/bin/env python
# coding: utf-8

"""
Converts a list or a list with a given regex grammar which contains a tree structure into a valid JSON.

This module works with both Python 2 and 3.
"""

__version__ = '0.1'
version = __version__

import logging
import nltk
import json

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


def depict_tree(data, grammar=None):
    """Converts the provided list into a tree structure
    Arguments:
    - data contains a list which should look like,
        [('I', 'NN'), ('am', 'NN'), ('a', 'NN'), ('good', 'VB'), ('boy', 'NN')]
    - grammar is optional, it accepts NLTK regexp grammar.
    """
    LOG.info('Inside depict_tree()')

    if grammar:
        parser = RegexpParser(grammar)
    else:
        parser = RegexpParser('''
                ''')
    return parser.parse(data)


def create_inner_json_subtree(inner_json_value):
    inner_json = "["
    for index in xrange(len(inner_json_value)):
        if index == len(inner_json_value) - 1:
            inner_json += "{\"" + inner_json_value[index][1] + "\":\"" + inner_json_value[index][0] + "\"}"
        else:
            inner_json += "{\"" + inner_json_value[index][1] + "\":\"" + inner_json_value[index][0] + "\"},"
    inner_json += "]"
    return inner_json


def create_inner_json(tree, index, inner_json_value):
    if index == len(tree) + 1:
        inner_json = "{\"" + inner_json_value[1] + "\":\"" + inner_json_value[0] + "\"}"
    else:
        inner_json = "{\"" + inner_json_value[1] + "\":\"" + inner_json_value[0] + "\"},"
    return inner_json


def create_outer_json(tree, subtree, index, inner_json):
    if index == len(tree) + 1:
        outer_json = "{\"" + subtree.label() + "\":" + inner_json + "}"
    else:
        outer_json = "{\"" + subtree.label() + "\":" + inner_json + "},"
    return outer_json


def traverse_tree(tree):
    json_value = ""
    index = 1
    for subtree in tree:
        index += 1
        if type(subtree) == nltk.tree.Tree:
            if subtree.height() > 2:
                if index == len(tree) + 1:
                    outer_json = "{\"" + subtree.label() + "\": [" + traverse_tree(subtree) + "]}"
                else:
                    outer_json = "{\"" + subtree.label() + "\": [" + traverse_tree(subtree) + "]},"
            else:
                print subtree
                print type(subtree)
                inner_json_value = json.loads(json.dumps(subtree, ensure_ascii=False))
                print inner_json_value
                inner_json = create_inner_json_subtree(inner_json_value)
                outer_json = create_outer_json(tree, subtree, index, inner_json)
        else:
            inner_json_value = json.loads(json.dumps(subtree, ensure_ascii=False))
            outer_json = create_inner_json(tree, index, inner_json_value)
        json_value += outer_json
    return json_value


def get_json(data, grammar=None):
    """Provides a JSON output for a given list
    Arguments:
    - data contains a list which should look like,
        [('I', 'NN'), ('am', 'NN'), ('a', 'NN'), ('good', 'VB'), ('boy', 'NN')]
    - grammar is optional, it accepts NLTK regexp grammar.
    """
    LOG.info('Inside get_json()')

    tree = depict_tree(data, grammar=grammar)
