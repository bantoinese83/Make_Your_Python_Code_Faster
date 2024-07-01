# parallelization.py

import multiprocessing


def square(n):
    return n * n


if __name__ == "__main__":
    numbers = range(1000000)
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(square, numbers)
    print(result[:10])
