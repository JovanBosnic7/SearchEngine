from datastructures.trie_node import TrieNode
from datastructures.set import Set
import os


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, path):
        curr_node = self.root
        len1 = len(word)
        flag = 1

        for i in range(len1):
            if word[i] in curr_node.children:
                curr_node = curr_node.children[word[i]]
            else:
                flag = 0
                break

        if flag == 0:
            while i < len1:
                curr_node.add_child(word[i])
                curr_node = curr_node.children[word[i]]
                i = i + 1

        curr_node.word = word
        ext_path = os.path.abspath(path)

        try:
            curr_node.counters[ext_path] += 1
        except KeyError:
            curr_node.counters[ext_path] = 1

    def find(self, word):
        curr_node = self.root
        for key in word:
            if key in curr_node.children:
                curr_node = curr_node.children[key]
            else:
                return Set()
        return Set(curr_node.counters.keys())
