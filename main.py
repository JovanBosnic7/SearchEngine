from datastructures.trie import Trie

if __name__ == '__main__':
    trie = Trie()
    trie.insert('rec','putanja')
    trie.insert('rec2','putanja')
    trie.insert('rec2','putanja2')
    print(trie.find('rec2'))