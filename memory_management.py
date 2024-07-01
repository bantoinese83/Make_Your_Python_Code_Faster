import sys
import time
import logging
import tracemalloc

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_large_list():
    return [i for i in range(1000000)]


def create_generator():
    return (i for i in range(1000000))


def measure_memory_and_time(func):
    """
    Measure memory usage and execution time of a function.

    Parameters
    ----------
    func : function
        The function to measure.

    Returns
    -------
    tuple
        Memory usage in bytes and execution time in seconds.
    """
    tracemalloc.start()
    start_time = time.time()
    result = func()
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    logging.info(f"Memory usage: Current={current / 1024:.2f} KB; Peak={peak / 1024:.2f} KB")
    logging.info(f"Execution time: {end_time - start_time:.6f} seconds")
    return result, current, end_time - start_time


def main():
    try:
        logging.info("Creating large list...")
        large_list, list_memory, list_time = measure_memory_and_time(create_large_list)
        logging.info(f"Size of list object: {sys.getsizeof(large_list)} bytes")

        logging.info("Creating generator...")
        generator, generator_memory, generator_time = measure_memory_and_time(create_generator)
        logging.info(f"Size of generator object: {sys.getsizeof(generator)} bytes")

        # Measure time to iterate over the list
        logging.info("Iterating over large list...")
        start_time = time.time()
        sum_large_list = sum(large_list)
        end_time = time.time()
        logging.info(f"Time to iterate over list: {end_time - start_time:.6f} seconds")

        # Measure time to iterate over the generator
        logging.info("Iterating over generator...")
        start_time = time.time()
        sum_generator = sum(generator)
        end_time = time.time()
        logging.info(f"Time to iterate over generator: {end_time - start_time:.6f} seconds")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
