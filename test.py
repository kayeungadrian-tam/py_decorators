from pyDeco.time import timeit
from pyDeco.debug import stacktrace, inactive, redirect

from time import sleep


def nested_func():
    print("nested_func called")


def inner_func():
    print("inner called")
    nested_func()


@timeit
def func():
    print("func running...")

    inner_func()

    print("EOF")


func()
