class Set(object):

    def __init__(self, data=[]):
        self.data = {}
        for element in data:
            self.data[element] = None

    def add(self, other):
        if other not in self.data:
            self.data[other] = None

    def discard(self, other):
        if other in self.data:
            self.data.pop(other)

    def __contains__(self, item):
        if item in self.data:
            return True
        else:
            return False

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return self.data.__iter__()

    def __and__(self, other):
        result = Set()
        for e in self:
            if e in other:
                result.add(e)
        return result

    def __or__(self, other):
        result = Set()
        for e in self:
            result.add(e)
        for e in other:
            result.add(e)
        return result

    def __not__(self, other):
        result = Set()
        for e in self:
            if e not in other:
                result.add(e)
        return result
