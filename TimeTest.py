import time


def time_test(func):
    """calculate the run time of a function."""

    def wrapper(*args, **kwargs):
        now_time = time.time()

        result = func(*args, **kwargs)

        exec_time = time.time() - now_time

        print(f"Execution time: {exec_time}s.")

        return result

    return wrapper
