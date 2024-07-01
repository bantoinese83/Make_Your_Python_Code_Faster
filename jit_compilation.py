# jit_compilation.py

from numba import jit


@jit(nopython=True)
def fast_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


if __name__ == "__main__":
    print(fast_function())
