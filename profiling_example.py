import cProfile
import pstats
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def example_function(iterations=10000):
    """
    Example function to sum numbers up to a specified iteration limit.

    Parameters
    ----------
    iterations : int, optional
        Number of iterations to sum up to, by default 10000.

    Returns
    -------
    int
        Total sum of numbers up to the specified iteration limit.
    """
    total = 0
    for i in range(iterations):
        total += i
    return total


def run_profiling(iterations=10000):
    """
    Run cProfile profiling on example_function.

    Parameters
    ----------
    iterations : int, optional
        Number of iterations for example_function, by default 10000.
    """
    try:
        cProfile.run(f'example_function({iterations})', 'profile_results')
        p = pstats.Stats('profile_results')
        p.strip_dirs().sort_stats('cumulative').print_stats(10)
    except Exception as e:
        logging.error(f"An error occurred during profiling: {e}")


if __name__ == "__main__":
    iterations = 1000000  # Change the number of iterations here
    logging.info(f"Running profiling for {iterations} iterations...")
    run_profiling(iterations)
