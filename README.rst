treetojson
==========

.. image:: https://travis-ci.org/saadsahibjan/treetojson.svg?branch=master
    :target: https://travis-ci.org/saadsahibjan/treetojson
    
-  Simple Library to map a tree structure to a valid JSON object.
-  This treetojson module is `published on the Python Package
   Index <https://pypi.python.org/pypi/treetojson>`__

Summary
=======

treetojson is a helpful in converting a given tree structure into a
valid JSON. Using this a tree strcuture can be easily interpreted to a
valid JSON. Further explaination on how the input should be given and
the output are explained under Basic Usage. This is pure Python code
with a single dependency of `NLTK <http://www.nltk.org/>`__. This can
also be used along with `NLTK
RegexpParser <http://www.nltk.org/_modules/nltk/chunk/regexp.html>`__.

This was a mainly developed due to a problem faced during a project on
Part-of-Speech (POS) tagger which is a part of Natural Language
Processing. When a tree structure is created with specific tags of it
using the NLTK module, the tree structure was not able to map
accordingly to a JSON object using the existing libraries. The problem
occurred due to the existence of repetitive 'key' since tags are fixed
for languages. Because of such a problem this was initially developed to
come out of this problem and was later decided to publish as an open
source Python module.

Further treetojson maintains the order provided. It does'nt mix up the
order. The output given will be a readable sentence as its given in to
treetojson. The output given by treetojson can be a respond to a HTTP
request, and can be used, manipulated and display appropriately in the
front-end.

Installation
============

The treetojson module is `published on the Python Package
Index <https://pypi.python.org/pypi/treetojson>`__, so you can install
it using ``pip`` or ``easy_install``.

::

    pip install treetojson

or

::

    easy_install treetojson

That should be all you need to go.

Basic Usage
===========

Example1
--------

When a list containing words and it's appropriate tags are provided as
follow:

::

    >>> import treetojson
    >>> sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'), ('larger', 'JJR'),
     ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
    >>> print treetojson.get_json(data=sentence)
    {u'SENTENCE': [{u'NN': u'Everyone'}, {u'VBZ': u'knows'}, {u'DT': u'an'}, {u'NN': u'Elephant'}, {u'VBZ': u'is'}, 
    {u'JJR': u'larger'}, {u'IN': u'than'}, {u'DT': u'a'}, {u'NN': u'Dog'}]}

Example2
--------

When a list containing words with appropriate tags along with a grammar
is provided:

::

    >>> import treetojson
    >>> sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'), ('larger', 'JJR'), 
    ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
    >>> grammar = """
          NP:   {<PRP>?<JJ.*>*<NN.*>+}
          CP:   {<JJR|JJS>}
          VERB: {<VB.*>}
          THAN: {<IN>}
          COMP: {<DT>?<NP><RB>?<VERB><DT>?<CP><THAN><DT>?<NP>}
        """
    >>> print treetojson.get_json(data=sentence, grammar=grammar)
    {u'SENTENCE': [{u'NP': [{u'NN': u'Everyone'}]}, {u'VERB': [{u'VBZ': u'knows'}]}, {u'COMP': [{u'DT': u'an'}, 
    {u'NP': [{u'NN': u'Elephant'}]}, {u'VERB': [{u'VBZ': u'is'}]}, {u'CP': [{u'JJR': u'larger'}]}, 
    {u'THAN': [{u'IN': u'than'}]}, {u'DT': u'a'}, {u'NP': [{u'NN': u'Dog'}]}]}]}

Example3
--------

When words and labels or tags are seperately provided:

::

    >>> import treetojson
    >>> words = ['Everyone', 'knows', 'an', 'Elephant', 'is', 'larger', 'than', 'a', 'Dog']
    >>> labels = ['NN', 'VBZ', 'DT', 'NN', 'VBZ', 'JJR', 'IN', 'DT', 'NN']
    >>> print treetojson.get_json(words=words, label=labels)
    {u'SENTENCE': [{u'NN': u'Everyone'}, {u'VBZ': u'knows'}, {u'DT': u'an'}, {u'NN': u'Elephant'}, {u'VBZ': u'is'}, 
    {u'JJR': u'larger'}, {u'IN': u'than'}, {u'DT': u'a'}, {u'NN': u'Dog'}]}

Example4
--------

When words and labels or tags seperately along with a grammar is
provided:

::

    >>> import treetojson
    >>> words = ['Everyone', 'knows', 'an', 'Elephant', 'is', 'larger', 'than', 'a', 'Dog']
    >>> labels = ['NN', 'VBZ', 'DT', 'NN', 'VBZ', 'JJR', 'IN', 'DT', 'NN']
    >>> grammar = """
          NP:   {<PRP>?<JJ.*>*<NN.*>+}
          CP:   {<JJR|JJS>}
          VERB: {<VB.*>}
          THAN: {<IN>}
          COMP: {<DT>?<NP><RB>?<VERB><DT>?<CP><THAN><DT>?<NP>}
        """
    >>> print treetojson.get_json(words=words, label=labels, grammar=grammar)
    {u'SENTENCE': [{u'NP': [{u'NN': u'Everyone'}]}, {u'VERB': [{u'VBZ': u'knows'}]}, {u'COMP': [{u'DT': u'an'}, 
    {u'NP': [{u'NN': u'Elephant'}]}, {u'VERB': [{u'VBZ': u'is'}]}, {u'CP': [{u'JJR': u'larger'}]}, 
    {u'THAN': [{u'IN': u'than'}]}, {u'DT': u'a'}, {u'NP': [{u'NN': u'Dog'}]}]}]}

Debugging
=========

You can enable debugging information.

::

    >>> import treetojson
    >>> treetojson.set_debug()
    Debug mode is on. Events are logged at: treetojson.log

To turn debug mode off, call ``set_debug`` with an argument of
``False``:

::

    >>> treetojson.set_debug(False)
    Debug mode is off.

If you encounter any errors in the code, please file an issue on github:
https://github.com/saadsahibjan/treetojson/issues

Contributing guide
==================

Use guidelines provided in
`CONTRIBUTING.md <https://github.com/saadsahibjan/treetojson/blob/master/CONTRIBUTING.md>`__

License
=======

`MIT <https://github.com/saadsahibjan/treetojson/blob/master/LICENSE>`__

Author
======

-  Author: Saad Sahibjan
-  Email: saadsahibjan@gmail.com
-  Repository: https://github.com/saadsahibjan/treetojson
