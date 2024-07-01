# main.py
import multiprocessing
import sys

# Import functions from other modules
from cython_example import cython_function
from profiling_example import example_function as profile_example_function
from algorithm_optimization import efficient_fibonacci
from memory_management import create_large_list, create_generator
from code_optimization import optimized_function
from built_in_functions import built_in_sum
from parallelization import square as parallel_square
from jit_compilation import fast_function
from case_study import example_function as case_study_example_function


# Main function to call all examples
def main():
    # Profiling and Benchmarking
    print("Profiling and Benchmarking:")
    print(f"Example function result: {profile_example_function()}")

    # Algorithmic Optimization
    print("\nAlgorithmic Optimization:")
    print(f"Efficient Fibonacci(30): {efficient_fibonacci(30)}")

    # Memory Management
    print("\nMemory Management:")
    large_list = create_large_list()
    generator = create_generator()
    print(f"Size of list: {sys.getsizeof(large_list)} bytes")
    print(f"Size of generator: {sys.getsizeof(generator)} bytes")

    # Code Optimization Techniques
    print("\nCode Optimization Techniques:")
    print(f"Optimized function (first 10 elements): {optimized_function()[:10]}")

    # Leveraging Built-in Functions and Libraries
    print("\nLeveraging Built-in Functions and Libraries:")
    numbers = list(range(1000000))
    print(f"Built-in sum: {built_in_sum(numbers)}")

    # Parallelization and Concurrency
    print("\nParallelization and Concurrency:")
    numbers = range(1000000)
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(parallel_square, numbers)
    print(f"Parallelization result (first 10 elements): {result[:10]}")

    # Just-in-Time (JIT) Compilation
    print("\nJust-in-Time (JIT) Compilation:")
    print(f"JIT function result: {fast_function()}")

    # External Tools and Techniques (Cython)
    print("\nExternal Tools and Techniques (Cython):")
    print(f"Cython function result: {cython_function(1000000)}")

    # Case Study: Profiling and Optimization
    print("\nCase Study: Profiling and Optimization:")
    print(f"Example function result: {case_study_example_function()}")


if __name__ == "__main__":
    main()
