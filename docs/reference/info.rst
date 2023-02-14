.. toctree::
    :maxdepth: 2

Info
====

A set of decorators that provide information about a function.


@timeit
-------


The :func:`timeit` function is a decorator that measures the runtime of a function and logs this information. It wraps the function with a new function that measures the runtime and logs the result.


**usage**

.. code-block:: python

    from pyDeco.info import timeit


    @timeit
    def func():
        # do something
        
    func()


**output**

.. parsed-literal::
    2023-02-14 22:07:40,978 [INFO ] Function func() took 0.5007 seconds.


@memoryit



The :func:`timeit` function is a decorator that measures the memory usage of a function and logs this information. It wraps the function with a new function that measures the memory and logs the result.

**usage**


.. code-block:: python

    import numpy as np
    from pyDeco.info import memoryit


    @memoryit
    def func():
        np.ones((100, 100, 100), dtype=np.float64)


    func()


**output**

.. parsed-literal::
    2023-02-14 22:59:44,307 [INFO ] Peak memory usage for function func() was 8.000 MB.