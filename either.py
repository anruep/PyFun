class Either:
    
    # a -> Either<None, a>
    @staticmethod
    def of(value):
        return Right(value)
    
    # Either a b: Boolean
    def isRight(self):
        return self.left is None

    # Either a b: Boolean
    def isLeft(self):
        return self.right is None

    # Either a b: (b -> c) -> Either a c
    def map(self, f):
        if (self.isLeft()):
            return self
        value = f(self.right)
        return Right(value)

    # Either a b: (b -> Either a c) -> Either a c
    def chain(self, f):
        if (self.isLeft()):
            return self
        return f(self.right)

    # Either a b: (a -> c) -> Either c b
    def mapLeft(self, f):
        if (self.isRight()):
            return self
        value = f(self.left)
        return Left(value)

    # Either a b: (a -> Either c b) -> Either c b
    def chainLeft(self, f):
        if (self.isRight()):
            return self
        return f(self.left)

    # Either a (b -> c) -> Either a b -> Either a c
    def apply(self, eitherVal):
        if (self.isLeft() or eitherVal.isLeft()):
            return self
        return tryCatch(eitherVal.either(lambda x: x, self.value))

    # Either a None: (a -> c) -> (b -> d) -> c
    # Either None b: (a -> c) -> (b -> d) -> d
    def either(self, leftFn, rightFn):
        if (self.isLeft()):
            return leftFn(self.left)
        return rightFn(self.right)

class Right(Either):
    def __init__(self, value):
        self.right = value
        self.left = None

class Left(Either):
    def __init__(self, value):
        self.right = None
        self.left = value