from py_deco.time import timeit


def hoge():
    return 1


@timeit
def test_timeit():
    from time import sleep

    adrian = 20

    sleep(1)

    assert True


test_timeit()
