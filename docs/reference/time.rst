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

    from pyDeco.time import timeit


    @timeit
    def func():
        # do something
        
    func()


**output**

.. parsed-literal::
    2023-02-14 22:07:40,978 [INFO ] Function func() took 0.5007 seconds.

