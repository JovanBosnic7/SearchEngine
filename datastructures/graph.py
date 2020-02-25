class Graph(object):

    def __init__(self):
        self.odlazeci = {}
        self.dolazeci = {}

    def insert_vertex(self, e):
        self.odlazeci[e] = []
        self.dolazeci[e]= []

    def insert_edge(self, u, v):
        self.odlazeci[u].append(v)
        self.dolazeci[v].append(u)

    def __str__(self):
        string = ""
        for key in self.odlazeci.keys():
            list1 = self.odlazeci[key]
            list2 = self.dolazeci[key]

            string += ("\n*" + str(key) + " out links = " + str(len(list1)) + " in links = " + str(len(list2)))
            string += "\n"

            for d in list1:
                string += str("{} -----> {}\n".format(" " * 20, d))

            for d in list2:
                string += str("{} <---- {}\n".format(" " * 20, d))

        return str(string)
