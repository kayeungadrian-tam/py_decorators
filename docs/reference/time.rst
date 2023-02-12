.. toctree::
    :maxdepth: 2

Time
====

A set of decorators that are related to runtime.


@timeit
-------


The :func:`timeit` function is a decorator that measures the runtime of a function and logs this information. It wraps the function with a new function that measures the runtime and logs the result.


**usage**

.. code-block:: python

    from time import sleep
    from pyDeco.time import timeit


    @timeit
    def func():
        sleep(1)
        
    func()


**output**

.. parsed-literal::
    pyDeco  | INFO | Function hoge3() took 0.5007 seconds.

