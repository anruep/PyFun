class Identity:

    # a -> Identity a
    @staticmethod
    def of(value):
        return Identity(value)

    # Identity a: (a -> b) -> b
    def map(self, f):
        return Identity(f(self.value))

    # Identity a: (a -> Identity b) -> Identity b
    def chain(self, f):
        return f(self.value)

    # Identity (a -> b): Identity a -> Identity b
    def apply(self, identityValue):
        return Identity(self.value(identityValue.value)

    # Identity a: a -> a
    def get(self):
        return self.value