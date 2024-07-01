# parallelization.py

import logging
import multiprocessing
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def square(n):
    return n * n


def parallel_square(numbers, processes=4):
    """
    Calculate the square of each number in the list using parallel processing.

    Parameters
    ----------
    numbers : list[int]
        List of numbers to square.
    processes : int, optional
        Number of parallel processes to use. Default is 4.

    Returns
    -------
    list[int]
        List of squared numbers.
    """
    try:
        with multiprocessing.Pool(processes=processes) as pool:
            result = pool.map(square, numbers)
        return result
    except Exception as e:
        logging.error(f"Error during parallel execution: {e}")
        return []


def sequential_square(numbers):
    """
    Calculate the square of each number in the list using sequential processing.

    Parameters
    ----------
    numbers : list[int]
        List of numbers to square.

    Returns
    -------
    list[int]
        List of squared numbers.
    """
    return [square(n) for n in numbers]


def measure_time(func, *args):
    """
    Measure the execution time of a function.

    Parameters
    ----------
    func : function
        The function to measure.
    args : tuple
        Arguments to pass to the function.

    Returns
    -------
    float
        The time taken to execute the function.
    result
        The result of the function execution.
    """
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    logging.info(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
    return end_time - start_time, result
