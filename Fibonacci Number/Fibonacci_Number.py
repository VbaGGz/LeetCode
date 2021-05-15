from functools import lru_cache
@lru_cache(maxsize = 1000)
def fib(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N > 1:
        return fib(N-1) + fib(N-2)

print(fib(101))