from time import sleep
from pyDeco.info import timeit, memoryit


@timeit
def create_sleep():

    sleep(1)


@memoryit
def create_stress():
    data = [[[1] * 1024] * 1024] * 1024


def test_timeit(capfd):
    create_sleep()

    out_string = capfd.readouterr()

    assert out_string.err[-13:-9] == "1.00"


def test_memoryit(capfd):

    create_stress()

    out_string = capfd.readouterr()

    assert out_string.err[-14:-9] == "0.025"
