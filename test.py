from pyDeco.time import timeit
from pyDeco.debug import stacktrace, inactive

from time import sleep


@inactive
def func():
    sleep(0.5)
    print("EOF")


func()
