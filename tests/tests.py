# coding=UTF-8

import unittest
import treetojson


class TreeToJsonTests(unittest.TestCase):
    def test_list(self):
        result = "{\"SENTENCE\":[{\"NN\":\"Everyone\"},{\"VBZ\":\"knows\"},{\"DT\":\"an\"},{\"NN\":\"Elephant\"}," \
                 "{\"VBZ\":\"is\"},{\"JJR\":\"larger\"},{\"IN\":\"than\"},{\"DT\":\"a\"},{\"NN\":\"Dog\"}]}"
        sentence = [('Everyone', 'NN'), ('knows', 'VBZ'), ('an', 'DT'), ('Elephant', 'NN'), ('is', 'VBZ'),
                    ('larger', 'JJR'), ('than', 'IN'), ('a', 'DT'), ('Dog', 'NN')]
        output = treetojson.get_json(data=sentence)
        self.assertEqual(output, result)


def test_listWithGrammar(self):
    result = "{\"SENTENCE\":[{\"NP\":[{\"NN\":\"Everyone\"}]},{\"VERB\":[{\"VBZ\":\"knows\"}]},{\"COMP\": " \
             "[{\"DT\":\"an\"},{\"NP\":[{\"NN\":\"Elephant\"}]},{\"VERB\":[{\"VBZ\":\"is\"}]},{\"CP\":" \
             "[{\"JJR\":\"larger\"}]},{\"THAN\":[{\"IN\":\"than\"}]},{\"DT\":\"a\"},{\"NP\":" \
             "[{\"NN\":\"Dog\"}]}]}]}"
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
