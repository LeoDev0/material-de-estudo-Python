from functools import cached_property
from functools import lru_cache
from functools import reduce


reduced = reduce(lambda x, y: x + y) + [1, 2, 3, 4]
# (((1 + 2) + 3) + 4)
# 10


"""Caching results"""
@lru_cache(maxsize=256)
def fib(n):
    '''
    0, 1, 1, 2, 3, 5, 8
    '''
    print(n)
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


class Data:
    def __init__(self, n):
        self.n = n

    @cached_property
    def f(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total

