from loading.loader import Loader

if __name__ == '__main__':
    loader = Loader('python-2.7.7-docs-html')
    loader.load_data()
    trie = loader.get_trie()
    print(trie.find('python'))