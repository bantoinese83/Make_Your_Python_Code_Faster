import logging
import time
from numba import jit

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@jit(nopython=True)
def fast_function(n=1000000):
    """
    Calculate the sum of integers from 0 to n-1 using a JIT-compiled loop.

    Parameters
    ----------
    n : int
        The upper limit of the range to a sum (exclusive).

    Returns
    -------
    int
        The sum of integers from 0 to n-1.
    """
    total = 0
    for i in range(n):
        total += i
    return total


def regular_function(n):
    """
    Calculate the sum of integers from 0 to n-1 using a regular Python loop.

    Parameters
    ----------
    n : int
        The upper limit of the range to sum (exclusive).

    Returns
    -------
    int
        The sum of integers from 0 to n-1.
    """
    total = 0
    for i in range(n):
        total += i
    return total


def measure_time(func, n):
    """
    Measure the execution time of a function.

    Parameters
    ----------
    func : function
        The function to measure.
    n : int
        The argument to pass to the function.

    Returns
    -------
    float
        The time taken to execute the function.
    """
    logging.info(f"Measuring execution time for {func.__name__} with range {n}.")
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    logging.info(f"Result: {result} (Time taken: {end_time - start_time:.6f} seconds)")
    return end_time - start_time


def main(n):
    try:
        if n <= 0:
            raise ValueError("The input must be a positive integer.")

        logging.info("Running fast_function with JIT compilation.")
        jit_time = measure_time(fast_function, n)

        logging.info("Running regular_function without JIT compilation.")
        regular_time = measure_time(regular_function, n)

        logging.info(f"Performance improvement: {regular_time / jit_time:.2f}x faster with JIT compilation")

    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compare JIT-compiled function performance with regular function.")
    parser.add_argument("-n", "--number", type=int, default=1000000, help="Range limit for the function.")
    args = parser.parse_args()

    main(args.number)
