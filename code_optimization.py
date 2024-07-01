import time
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def original_function(n):
    result = []
    for i in range(n):
        result.append(i * 2)
    return result


def optimized_function(n=1000000):
    return [i * 2 for i in range(n)]


def measure_time(func, n):
    logging.info(f"Measuring execution time for {func.__name__} with range {n}.")
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time


def main(n):
    try:
        # Measure execution time of the original function
        original_result, original_time = measure_time(original_function, n)
        logging.info(
            f"Original function result (first 10 elements): {original_result[:10]} (Time taken: {original_time:.6f} seconds)")

        # Measure execution time of the optimized function
        optimized_result, optimized_time = measure_time(optimized_function, n)
        logging.info(
            f"Optimized function result (first 10 elements): {optimized_result[:10]} (Time taken: {optimized_time:.6f} seconds)")

    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize and measure execution time of a function.")
    parser.add_argument("-n", "--number", type=int, default=1000000, help="Range limit for the function.")
    args = parser.parse_args()

    if args.number <= 0:
        logging.error("The range limit must be a positive integer.")
    else:
        main(args.number)
