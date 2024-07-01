import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def original_sum(nums):
    if not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("All elements in the input list must be numbers.")

    total = 0
    for number in nums:
        total += number
    return total


def built_in_sum(nums):
    if not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("All elements in the input list must be numbers.")

    return sum(nums)


def measure_time(func, nums):
    start_time = time.time()
    result = func(nums)
    end_time = time.time()
    return result, end_time - start_time


if __name__ == "__main__":
    numbers = list(range(1000000))

    try:
        logging.info("Starting original_sum calculation.")
        original_result, original_time = measure_time(original_sum, numbers)
        logging.info(f"Original sum result: {original_result} (Time taken: {original_time:.6f} seconds)")

        logging.info("Starting built_in_sum calculation.")
        built_in_result, built_in_time = measure_time(built_in_sum, numbers)
        logging.info(f"Built-in sum result: {built_in_result} (Time taken: {built_in_time:.6f} seconds)")

    except ValueError as e:
        logging.error(f"Error: {e}")
