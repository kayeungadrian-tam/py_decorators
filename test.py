import time
from pyDeco.info import memoryit
from pyDeco.fun import epic_intro, explode


def throttle(max_calls, interval):
    def decorate(func):
        last_called = 0
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called, calls
            print(last_called, calls)
            elapsed = time.monotonic() - last_called
            if elapsed < interval:
                # Throttle the call
                time.sleep(interval - elapsed)
            last_called = time.monotonic()
            calls += 1
            if calls <= max_calls:
                # Call the function
                return func(*args, **kwargs)
            else:
                # Exceeded the maximum number of calls
                raise Exception(
                    f"Function {func.__name__} exceeded maximum call limit of {max_calls}"
                )

        return wrapper

    return decorate


def interval(interval_time):
    def decorate(func):
        last_called = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.monotonic() - last_called
            if elapsed >= interval_time:
                last_called = time.monotonic()
                return func(*args, **kwargs)
            else:
                return None

        return wrapper

    return decorate


@interval(interval_time=1.0)
def func():
    print("starting...", end=" ", flush=True)
    # time.sleep(1)
    print("DONE!")


# for cnt in range(10):
#     # print(cnt, flush=True)

#     func()
#     time.sleep(0.5)


import numpy as np
import pyfiglet
import emoji


@explode
@epic_intro
def random_func(name):

    int(name)

    # np.ones((100, 100, 100), dtype=np.float64)
    return name


nae = random_func("shit")
print(nae)
