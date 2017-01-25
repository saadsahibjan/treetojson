# !/usr/bin/env python
# coding: utf-8

"""
Converts a tree structure in to a valid JSON.

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


def __depict_tree(data=None, words=None, label=None, grammar=None):
    """Converts the provided list into a tree structure
        Arguments:
        - data contains a list which should look like,
            [('I', 'NN'), ('am', 'NN'), ('a', 'NN'), ('good', 'VB'), ('boy', 'NN')]
        - words contains a split sentence, a sentence can be splitted and sent as an argument,
            ['I', 'am', 'a', 'good', 'boy']
        - label contains the specific label of the words given.
            ['NN', 'NN', 'NN', 'NN', 'VB']
        - grammar is optional, it accepts NLTK regexp grammar.
    """
    LOG.info('Inside __depict_tree()')

    if (words is None or label is None) and data is None:
        raise ValueError("Words and labels or data containing list should be provided.")

    if words and label:
        if len(words) != len(label):
            raise ValueError("Lengths of words and labels should be equal")

    if words is None and label is None and data:
        sentence = data
    else:
        sentence = []
        for index in xrange(len(words)):
            sentence.append((words[index], label[index]))

    if grammar is None:
        parser = RegexpParser('''
                        ''')
    else:
        parser = RegexpParser(grammar)

    return parser.parse(sentence)


def __create_inner_json_subtree(inner_json_value):
    LOG.info('Inside __create_inner_json_subtree')
    inner_json = "["
    for index in xrange(len(inner_json_value)):
        if index == len(inner_json_value) - 1:
            inner_json += "{\"" + inner_json_value[index][1] + "\":\"" + inner_json_value[index][0] + "\"}"
        else:
            inner_json += "{\"" + inner_json_value[index][1] + "\":\"" + inner_json_value[index][0] + "\"},"
    inner_json += "]"
    return inner_json


def __create_inner_json(tree, index, inner_json_value):
    LOG.info('Inside __create_inner_json')
    if index == len(tree) + 1:
        inner_json = "{\"" + inner_json_value[1] + "\":\"" + inner_json_value[0] + "\"}"
    else:
        inner_json = "{\"" + inner_json_value[1] + "\":\"" + inner_json_value[0] + "\"},"
    return inner_json


def __create_outer_json(tree, subtree, index, inner_json):
    LOG.info('Inside __create_outer_json')
    if index == len(tree) + 1:
        outer_json = "{\"" + subtree.label() + "\":" + inner_json + "}"
    else:
        outer_json = "{\"" + subtree.label() + "\":" + inner_json + "},"
    return outer_json


def __traverse_tree(tree):
    LOG.info('Inside __traverse_tree')
    json_value = ""
    index = 1
    for subtree in tree:
        index += 1
        if type(subtree) == nltk.tree.Tree:
            if subtree.height() > 2:
                if index == len(tree) + 1:
                    outer_json = "{\"" + subtree.label() + "\": [" + __traverse_tree(subtree) + "]}"
                else:
                    outer_json = "{\"" + subtree.label() + "\": [" + __traverse_tree(subtree) + "]},"
            else:
                inner_json_value = json.loads(json.dumps(subtree, ensure_ascii=False))
                inner_json = __create_inner_json_subtree(inner_json_value)
                outer_json = __create_outer_json(tree, subtree, index, inner_json)
        else:
            inner_json_value = json.loads(json.dumps(subtree, ensure_ascii=False))
            outer_json = __create_inner_json(tree, index, inner_json_value)
        json_value += outer_json
    return json_value


def get_json(data=None, words=None, label=None, grammar=None):
    """Provides a JSON output for a given list
    Arguments:
    - data contains a list which should look like,
        [('I', 'NN'), ('am', 'NN'), ('a', 'NN'), ('good', 'VB'), ('boy', 'NN')]
    - grammar is optional, it accepts NLTK regexp grammar.
    """
    LOG.info('Inside get_json()')

    tree = __depict_tree(data=data, words=words, label=label, grammar=grammar)
    json_value = __traverse_tree(tree)
    return "{\"SENTENCE\":[" + json_value + "]}"
