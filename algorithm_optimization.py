import logging
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def inefficient_fibonacci(n):
    """
    Calculate Fibonacci number inefficiently using recursion.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to calculate.

    Returns
    -------
    int
        The Fibonacci number at index n.
    """
    if n <= 1:
        return n
    else:
        return inefficient_fibonacci(n - 1) + inefficient_fibonacci(n - 2)


@lru_cache(maxsize=None)
def efficient_fibonacci(n):
    """
    Calculate Fibonacci number efficiently using recursion and memoization.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to calculate.

    Returns
    -------
    int
        The Fibonacci number at index n.
    """
    if n <= 1:
        return n
    return efficient_fibonacci(n - 1) + efficient_fibonacci(n - 2)


def iterative_fibonacci(n):
    """
    Calculate Fibonacci number iteratively.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to calculate.

    Returns
    -------
    int
        The Fibonacci number at index n.

    Raises
    ------
    ValueError
        If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    logging.info(f"Calculating iterative Fibonacci({n})...")

    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    try:
        # Calculate Fibonacci numbers
        n = 30
        logging.info(f"Efficient Fibonacci with Recursion and Memoization ({n}): {efficient_fibonacci(n)}")
        logging.info(f"Iterative Fibonacci ({n}): {iterative_fibonacci(n)}")

        # Testing large numbers
        n_large = 1000
        logging.info(f"Iterative Fibonacci ({n_large}): {iterative_fibonacci(n_large)}")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
