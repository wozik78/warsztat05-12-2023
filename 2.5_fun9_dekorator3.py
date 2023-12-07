import time
import numpy as np


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"czas wykonania funkcji {func.__name__}: {execution_time} sekundy")
        return result

    return wrapper


@measure_time
def my_function():
    # pass
    total = sum(range(150000000))


@measure_time
def my_function_np():
    total = np.sum(np.arange(1500000), dtype=np.int64)
    print("sum is:", total)


my_function()

my_function_np()
