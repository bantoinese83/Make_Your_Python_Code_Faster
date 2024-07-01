# built_in_functions.py

def original_sum(nums):
    total = 0
    for number in nums:
        total += number
    return total


def built_in_sum(nums):
    return sum(nums)


if __name__ == "__main__":
    numbers = list(range(1000000))
    print(original_sum(numbers))
    print(built_in_sum(numbers))
