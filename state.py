from commons import pipe

## apply still missing --> no applicative
class State:

    # function: s -> a -> (s, b)
    def __init__(self, function):
        self.func = function

    @staticmethod
    def of(function):
        return State(function)

    def map(self, function):
        newFunc = pipe(
            self.func,
            lambda x: (x[0], function(x[1]))
        )
        return State(newFunc)

    def chain(self, function):
        newFunc = pipe(
            self.func,
            lambda x: x[1],
            function
        )
        def inner(a):
            return newFunc(a).run(a)
     
        return State(inner)

    def eval(self, value):
        return self.func(value)[1]

    def next(self, value):
        return self.func(value)[0]

    def run(self, value):
        return self.func(value)