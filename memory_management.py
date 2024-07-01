# memory_management.py

import sys


def create_large_list():
    return [i for i in range(1000000)]


def create_generator():
    return (i for i in range(1000000))


if __name__ == "__main__":
    large_list = create_large_list()
    generator = create_generator()

    print(f"Size of list: {sys.getsizeof(large_list)} bytes")
    print(f"Size of generator: {sys.getsizeof(generator)} bytes")
