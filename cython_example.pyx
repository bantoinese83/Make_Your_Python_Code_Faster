# cython_example.pyx
# cython: language_level=3

def cython_function(int n):
    cdef int i, total = 0
    for i in range(n):
        total += i
    return total
