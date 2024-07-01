import cProfile
import pstats
import time
import logging
import argparse
from numba import jit

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@jit(nopython=True)
def example_function(n=10000):
    total = 0
    for i in range(n):
        total += i
    return total


def profile_function(func, iterations):
    logging.info(f"Profiling {func.__name__} with {iterations} iterations.")
    cProfile.run(f'{func.__name__}({iterations})', 'profile_results')
    p = pstats.Stats('profile_results')
    p.sort_stats('cumulative').print_stats(10)


def measure_time(func, iterations):
    logging.info(f"Measuring execution time for {func.__name__} with {iterations} iterations.")
    start_time = time.time()
    result = func(iterations)
    end_time = time.time()
    return result, end_time - start_time


def main(iterations):
    try:
        # Measure execution time
        result, exec_time = measure_time(example_function, iterations)
        logging.info(f"Execution result: {result} (Time taken: {exec_time:.6f} seconds)")

        # Profile function
        profile_function(example_function, iterations)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Profile and measure execution time of a function.")
    parser.add_argument("-i", "--iterations", type=int, default=1000000, help="Number of iterations for the function.")
    args = parser.parse_args()

    main(args.iterations)
