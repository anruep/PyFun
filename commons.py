import functools
from maybe import Nothing, Just
from either import Left, Right

def flatmap(f, l):
    return reduce(lambda x, y: x + y, (map(f, l)))

def compose(*fns):
    return reduce(lambda f1, f2: lambda x: f1(f2(x)), fns, lambda x: x)

def pipe(*fns):
    return reduce(lambda f1, f2: lambda x: f2(f1(x)), fns, lambda x: x)

product = functools.partial(reduce, lambda x,y : x * y)

def saveMax(l):
    return Just(max(l)) if len(l) > 0 else Nothing()

partial = functools.partial

def tryCatch(func, *args):
    try:
        return Right(func(*args))
    except Exception, e:
        return Left(e)