from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    def fibonacci(n: int):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

#fibonacci function variable
fib = caching_fibonacci()

#usage
print(fib(10))  # 55
print(fib(15))  # 610
