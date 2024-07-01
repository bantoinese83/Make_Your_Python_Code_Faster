# test_cython.py

import cython_example

if __name__ == "__main__":
    result = cython_example.cython_function(1000000)
    print(f"Result: {result}")
