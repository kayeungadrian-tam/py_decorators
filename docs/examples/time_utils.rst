Time Utils
==========


Time the function.

.. code-block:: python

    from time import sleep
    from py_deco.time import timeit

    @timeit
    def func():
        sleep(1)
    
    func()

.. parsed-literal::
    Function func took 1.0012 seconds

