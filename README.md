# Summary
treetojson is a helpful in converting a given tree structure into a valid JSON. Using this a tree strcuture can be easily interpreted to a valid JSON. Further explaination on how the input should be given and the output are explained under Basic Usage. This is pure Python code with a single dependency of [NLTK](http://www.nltk.org/). This can also be used along with [NLTK RegexpParser](http://www.nltk.org/_modules/nltk/chunk/regexp.html).

This was a mainly developed due to a problem faced during a project on Part-of-Speech (POS) tagger which is a part of Natural Language Processing. When a tree structure is created with specfic tags of it using the NLTK module, the tree strcuture was not able to map accordingly to a JSON object using the existing libraries. The problem occured due to the existence of repetitive 'key' since tags are fixed for languages. Because of such a problem this was initially developed to come out of this problem and was later decided to publish as an open source Python module.

Further treetojson maintains the order provided. It does'nt mix up the order. The output given will be a readable sentence as its given in to treetojson. The output given by treetojson can be a respond to a HTTP request, and can be used, manipulated and display appropriately in the front-end.

# Installation

The treetojson module is [published on the Python Package Index](https://pypi.python.org/pypi/treetojson), so you can install it using `pip` or `easy_install`.

```
pip install treetojson
```
or
```
easy_install treetojson
```

That should be all you need to go.

# Basic Usage

##Example1

When a list containing words and it's appropriate tags are provided as follow:
```
>>> import treetojson
>>> sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'), ('larger', 'JJR'), ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
>>> print treetojson.get_json(data=sentence)
{"SENTENCE":[{"NN":"Everyone"},{"VBZ":"knows"},{"DT":"an"},{"NN":"Elephant"},{"VBZ":"is"}, {"JJR":"larger"},{"IN":"than"},{"DT":"a"},{"NN":"Dog"}]}
```

##Example2

When a list containing words with appropriate tags along with a grammar is provided:
```
>>> import treetojson
>>> sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'), ('larger', 'JJR'), ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
>>> grammar = """
	  NP:   {<PRP>?<JJ.*>*<NN.*>+}
	  CP:   {<JJR|JJS>}
	  VERB: {<VB.*>}
	  THAN: {<IN>}
	  COMP: {<DT>?<NP><RB>?<VERB><DT>?<CP><THAN><DT>?<NP>}
	"""
>>> print treetojson.get_json(data=sentence, grammar=grammar)
{"SENTENCE":[{"NP":[{"NN":"Everyone"}]},{"VERB":[{"VBZ":"knows"}]},{"COMP": [{"DT":"an"},{"NP":[{"NN":"Elephant"}]},{"VERB":[{"VBZ":"is"}]},{"CP":[{"JJR":"larger"}]},{"THAN":[{"IN":"than"}]},{"DT":"a"},{"NP":[{"NN":"Dog"}]}]}]}
```

##Example3

When words and labels or tags are seperately provided:
```
>>> import treetojson
>>> words = ['Everyone', 'knows', 'an', 'Elephant', 'is', 'larger', 'than', 'a', 'Dog']
>>> labels = ['NN', 'VBZ', 'DT', 'NN', 'VBZ', 'JJR', 'IN', 'DT', 'NN']
>>> print treetojson.get_json(words=words, label=labels)
{"SENTENCE":[{"NN":"Everyone"},{"VBZ":"knows"},{"DT":"an"},{"NN":"Elephant"},{"VBZ":"is"},{"JJR":"larger"},{"IN":"than"},{"DT":"a"},{"NN":"Dog"}]}
```

##Example4

When words and labels or tags seperately along with a grammar is provided:
```
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
{"SENTENCE":[{"NP":[{"NN":"Everyone"}]},{"VERB":[{"VBZ":"knows"}]},{"COMP": [{"DT":"an"},{"NP":[{"NN":"Elephant"}]},{"VERB":[{"VBZ":"is"}]},{"CP":[{"JJR":"larger"}]},{"THAN":[{"IN":"than"}]},{"DT":"a"},{"NP":[{"NN":"Dog"}]}]}]}
```

#Debugging

You can enable debugging information.

```
>>> import treetojson
>>> treetojson.set_debug()
Debug mode is on. Events are logged at: treetojson.log
```

To turn debug mode off, call `set_debug` with an argument of `False`:

```
>>> treetojson.set_debug(False)
Debug mode is off.
```

If you encounter any errors in the code, please file an issue on github: 
[https://github.com/saadsahibjan/treetojson/issues](https://github.com/saadsahibjan/treetojson/issues)

#Author

* Author: Saad Sahibjan
* Email: saadsahibjan@gmail.com
* Repository: [https://github.com/saadsahibjan/treetojson](https://github.com/saadsahibjan/treetojson)
