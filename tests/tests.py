# coding=UTF-8

import unittest
import treetojson


class TreeToJsonTests(unittest.TestCase):
    def test_list(self):
        result = {u'SENTENCE': [{u'NN': u'Everyone'}, {u'VBZ': u'knows'}, {u'DT': u'an'}, {u'NN': u'Elephant'}, {u'VBZ': u'is'}, {u'JJR': u'larger'}, {u'IN': u'than'}, {u'DT': u'a'}, {u'NN': u'Dog'}]}
        sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'),
                    ('larger', 'JJR'), ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
        output = treetojson.get_json(data=sentence)
        self.assertEqual(output, result)


    def test_listWithGrammar(self):
        result = {u'SENTENCE': [{u'NP': [{u'NN': u'Everyone'}]}, {u'VERB': [{u'VBZ': u'knows'}]}, {u'COMP': [{u'DT': u'an'}, {u'NP': [{u'NN': u'Elephant'}]}, {u'VERB': [{u'VBZ': u'is'}]}, {u'CP': [{u'JJR': u'larger'}]}, {u'THAN': [{u'IN': u'than'}]}, {u'DT': u'a'}, {u'NP': [{u'NN': u'Dog'}]}]}]}
        sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'),
                    ('larger', 'JJR'), ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
        grammar = """
            NP:   {<PRP>?<JJ.*>*<NN.*>+}
            CP:   {<JJR|JJS>}
            VERB: {<VB.*>}
            THAN: {<IN>}
            COMP: {<DT>?<NP><RB>?<VERB><DT>?<CP><THAN><DT>?<NP>}
            """
        output = treetojson.get_json(data=sentence, grammar=grammar)
        self.assertEqual(output, result)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
