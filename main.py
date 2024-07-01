# main.py

import logging
import sys
import time

from algorithm_optimization import efficient_fibonacci
from built_in_functions import built_in_sum
from case_study import example_function as case_study_example_function
from code_optimization import optimized_function
# Import functions from other modules
from cython_example import cython_function
from jit_compilation import fast_function
from memory_management import create_large_list, create_generator
from parallelization import parallel_square
from profiling_example import example_function as profile_example_function

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to measure execution time
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    try:
        result = func(*args, **kwargs)
    except Exception as e:
        logging.error(f"Error occurred in {func.__name__}: {e}")
        result = None
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Execution time for {func.__name__}: {execution_time:.6f} seconds")
    return execution_time, result


# Main function to call all examples
def main():
    try:
        # Profiling and Benchmarking
        logging.info("Profiling and Benchmarking:")
        profile_time, profile_result = measure_time(profile_example_function, 1000000)
        if profile_result is not None:
            print(f"Example function result: {profile_result}")
        else:
            print("Error occurred during profiling.")

        # Algorithmic Optimization
        logging.info("\nAlgorithmic Optimization:")
        fibonacci_result = efficient_fibonacci(30)
        print(f"Efficient Fibonacci(30): {fibonacci_result}")

        # Memory Management
        logging.info("\nMemory Management:")
        large_list = create_large_list()
        generator = create_generator()
        print(f"Size of list: {sys.getsizeof(large_list)} bytes")

        # Code Optimization Techniques
        logging.info("\nCode Optimization Techniques:")
        optimized_time, optimized_result = measure_time(optimized_function)
        if optimized_result is not None:
            print(f"Optimized function (first 10 elements): {optimized_result[:10]}")
        else:
            print("Error occurred during code optimization.")

        # Leveraging Built-in Functions and Libraries
        logging.info("\nLeveraging Built-in Functions and Libraries:")
        numbers = list(range(1000000))
        built_in_sum_result = built_in_sum(numbers)
        print(f"Built-in sum: {built_in_sum_result}")

        # Parallelization and Concurrency
        logging.info("\nParallelization and Concurrency:")
        parallel_time, parallel_result = measure_time(parallel_square, numbers)
        if parallel_result:
            print(f"Parallelization result (first 10 elements): {parallel_result[:10]}")
        else:
            print("Error occurred during parallelization.")

        # Just-in-Time (JIT) Compilation
        logging.info("\nJust-in-Time (JIT) Compilation:")
        jit_time, jit_result = measure_time(fast_function)
        if jit_result is not None:
            print(f"JIT function result: {jit_result}")
        else:
            print("Error occurred during JIT compilation.")

        # External Tools and Techniques (Cython)
        logging.info("\nExternal Tools and Techniques (Cython):")
        cython_time, cython_result = measure_time(cython_function, 1000000)
        if cython_result is not None:
            print(f"Cython function result: {cython_result}")
        else:
            print("Error occurred during Cython execution.")

        # Case Study: Profiling and Optimization
        logging.info("\nCase Study: Profiling and Optimization:")
        case_study_time, case_study_result = measure_time(case_study_example_function)
        if case_study_result is not None:
            print(f"Case study example function result: {case_study_result}")
        else:
            print("Error occurred during case study execution.")

    except Exception as e:
        logging.error(f"Main function encountered an error: {e}")


if __name__ == "__main__":
    main()
