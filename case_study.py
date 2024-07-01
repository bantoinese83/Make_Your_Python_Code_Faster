# case_study.py

import cProfile
import pstats
from numba import jit


@jit(nopython=True)
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


if __name__ == "__main__":
    cProfile.run('example_function()', 'profile_results')
    p = pstats.Stats('profile_results')
    p.sort_stats('cumulative').print_stats(10)
