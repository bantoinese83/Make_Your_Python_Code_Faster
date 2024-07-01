# algorithm_optimization.py

def inefficient_fibonacci(n):
    if n <= 1:
        return n
    else:
        return inefficient_fibonacci(n - 1) + inefficient_fibonacci(n - 2)


def efficient_fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = efficient_fibonacci(n - 1, memo) + efficient_fibonacci(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(efficient_fibonacci(30))
