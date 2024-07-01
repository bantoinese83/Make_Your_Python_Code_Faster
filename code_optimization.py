# code_optimization.py

def original_function():
    result = []
    for i in range(1000000):
        result.append(i * 2)
    return result


def optimized_function():
    return [i * 2 for i in range(1000000)]


if __name__ == "__main__":
    print(original_function()[:10])
    print(optimized_function()[:10])
