.. toctree::
    :maxdepth: 2

Debugging
=========

A set of decorators that are related to debugging.



@inactive
---------

The :func:`@inactive`  is a decorator that allows you to deactivate (temporaily) a function without modifying its code. It replaces the behavior of a function with a logging statement and the return of a list of :func:`None` if values are being returned.

usage
`````
.. code-block:: python

    from time import sleep
    from pyDeco.time import timeit


    @timeit
    def func():
        sleep(1)
        
    func()

output
```````

.. parsed-literal::
    pyDeco  | INFO | Function hoge3() took 0.5007 seconds.



@redirect
---------


usage
`````
.. code-block:: python

    from time import sleep
    from pyDeco.time import timeit


    @timeit
    def func():
        sleep(1)
        
    func()

output
```````

.. parsed-literal::
    pyDeco  | INFO | Function hoge3() took 0.5007 seconds.



@stacktrace
-----------


usage
`````
.. code-block:: python

    from time import sleep
    from pyDeco.time import timeit


    @timeit
    def func():
        sleep(1)
        
    func()

output
```````

.. parsed-literal::
    pyDeco  | INFO | Function hoge3() took 0.5007 seconds.

