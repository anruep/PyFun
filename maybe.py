class Maybe:

    # a -> Maybe a
    @staticmethod
    def of(value):
        if (value is None):
            return Nothing()
        return Just(value)
    
    # Maybe a: -> Boolean
    def isJust(self):
        return self.value is not None

    # Maybe a: -> Boolean
    def isNothing(self):
        return self.value is None

    # Maybe a: (a -> b) -> Maybe b
    def map(self, f):
        if (self.isNothing()):
            return self
        value = f(self.value)
        return Just(value)

    # Maybe a: (a -> Maybe b) -> Maybe b
    def chain(self, f):
        if (self.isNothing()):
            return self
        return f(self.value)

    # Maybe (a -> b): Maybe a -> Maybe b
    def apply(self, maybeVal):
        if (self.isNothing() or maybeVal.isNothing()):
            return Nothing()
        return Just(self.value(maybeVal.value))

    # Maybe a: (a -> b) -> b -> b
    def maybe(self, func, default):
        if (self.isNothing()):
            return default
        return func(self.value)

    # Maybe a: a -> a
    def getOrElse(self, default):
        if (self.isNothing()):
            return default
        return self.value

class Just(Maybe):
    def __init__(self, value):
        self.value = value

    def printMe(self):
        print "Just "
        print self.value

class Nothing(Maybe):
    def __init__(self):
        self.value = None

    def printMe(self):
        print "Nothing"