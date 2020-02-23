from datastructures.trie import Trie
from datastructures.graph import Graph
from loading.parser import Parser


import os
import time

class Loader:

    def __init__(self, path):
        self.path = path
        self.trie = Trie()
        self.parser = Parser()
        self.graph = Graph()

    def get_trie(self):
        return self.trie

    def get_graph(self):
        return self.graph

    def load_data(self):
        print("\nUcitavanje u graph i trie ... \n")
        edge_list = list()
        graph = self.graph
        trie = self.trie
        parser = self.parser
        start_time = time.time()
        filesystem_walk(self.path, parser, edge_list, trie)
        print("\n\nParsiranje za: %s sekundi." % (time.time() - start_time))
        all_vertex = set()
        for e in edge_list:
            all_vertex.add(e[0])
            all_vertex.add(e[1])

        for v in all_vertex:
            graph.insert_vertex(v)

        for e in edge_list:
            src = e[0]
            dest = e[1]

            graph.insert_edge(src, dest)

        print("\n\nUcitavanje u graph za: %s sekundi" % (time.time() - start_time))

        return graph, trie


def filesystem_walk(path, parser, edge_list, trie):
    for dic in os.listdir(path):
        dic = os.path.join(path, dic)
        if os.path.isdir(dic):
            filesystem_walk(dic, parser, edge_list, trie)
        elif os.path.isfile(dic):
            if dic.endswith(".html"):
                links, words = parser.parse(dic)

                for word in words:
                    trie.insert(word.lower(), dic)

                for link in links:
                    edge_list.append((dic, link))