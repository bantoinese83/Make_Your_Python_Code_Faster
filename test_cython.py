import cython_example
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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


if __name__ == "__main__":
    try:
        logging.info("Running cython_function...")
        execution_time, result = measure_time(cython_example.cython_function, 1000000)
        logging.info(f"Result: {result}")
        logging.info(f"Execution took {execution_time:.6f} seconds.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
