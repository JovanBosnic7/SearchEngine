class TrieNode:

    def __init__(self, letter=None):
        self.word = None  # Rec, samo kod cvorova koji predstavljaju kraj reci nije None
        self.letter = letter  # Slovo koje cvor predstavlja
        self.children = {}  # Recnik dece cvora, kljuc je slovo, vrednost je cvor uz to slovo
        self.counters = {}  # Recnik koji cuva podatke o pojavljivanju reci u dokumentu, kljuc je putanja do stranice, vrednost je broj pojava date reci u stranici

    def add_child(self, letter):
        self.children[letter] = TrieNode(letter)

    def __getitem__(self, key):
        return self.children[key]
