class List:

    def __init__(self, *args):
        self.values = args

    @staticmethod
    def of(*args):
        return List(args)

    def add(self, list):
        return List(self.values + list.values)

    def map(self, f):
        newValues = []
        for x in self.values:
            newValues.append(f(x))
        return List(newValues)

    def apply(self, listValues):
        newValues = []
        for f in self.values:
            for x in listValues:
                newValues.append(f(x))
        return List(newValues)

    def chain(self, f):
        newList = List([])
        for x in self.values:
            newList = newList.add(f(x))
        return newList