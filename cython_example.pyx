# cython_example.pyx
# cython: language_level=3

def cython_function(int n) -> int:
    """
    Calculate the sum of integers from 0 to n-1 using a Cython-optimized loop.

    Parameters
    ----------
    n : int
        The upper limit of the range to a sum (exclusive).

    Returns
    -------
    int
        The sum of integers from 0 to n-1.

    Raises
    ------
    ValueError
        If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    cdef int i, total = 0

    # Use an efficient approach to calculate the sum of integers
    for i in range(n):
        total += i

    return total
