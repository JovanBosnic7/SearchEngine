from loading.loader import Loader

if __name__ == '__main__':
    loader = Loader('python-2.7.7-docs-html')
    graph, trie = loader.load_data()
    print(trie.find('recursion'))