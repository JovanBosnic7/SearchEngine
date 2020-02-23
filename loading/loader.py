from datastructures.trie import Trie
from loading.parser import Parser

import os


class Loader:

    def __init__(self, path):
        self.path = path
        self.trie = Trie()
        self.parser = Parser()

    def get_trie(self):
        return self.trie

    def load_data(self):
        filesystem_walk(self.path, self.parser, self.trie)


def filesystem_walk(path, parser, trie):
    for dic in os.listdir(path):
        dic = os.path.join(path, dic)
        if os.path.isdir(dic):
            filesystem_walk(dic, parser, trie)
        elif os.path.isfile(dic):
            if dic.endswith(".html"):
                links, words = parser.parse(dic)

                for word in words:
                    trie.insert(word.lower(), dic)
