.. toctree::
    :maxdepth: 2

Debugging
=========

A set of decorators that are related to debugging.



@inactive
---------

The :code:`@inactive`  is a decorator that allows you to deactivate (temporaily) a function without modifying its code. It replaces the behavior of a function with a logging statement and the return of a list of :func:`None` if values are being returned.

**usage**

.. code-block:: python

    from pyDeco.debug import inactive


    @inactive
    def func():
        ...
        
    func()

**output**

.. parsed-literal::

    2023-02-14 21:50:39,150 [DEBUG] Function func() decorated with @inactive. Skipping...


@redirect
---------

The :code:`@redirect`  is a decorator that allows you to 
collect all the printed statements of a function in the order in which were called.

**usage**

.. code-block:: python

    from pyDeco.debug import redirect

    @redirect
    def func():
        print("func running...")
        print("--------------------------------")
        print("EOF")

    func()

**output**


.. parsed-literal::
    2023-02-14 21:54:26,732 [DEBUG] 1: func running... /mnt/Personal/py_decorators/test.py 20 
    2023-02-14 21:54:26,732 [DEBUG] 2: -------------------------------- /mnt/Personal/py_decorators/test.py 20 
    2023-02-14 21:54:26,733 [DEBUG] 3: EOF /mnt/Personal/py_decorators/test.py 20 


@redirect(line_print=<list>)
`````````````````````````````


The :code:`@redirect` with an empty list is a decorator that allows you to store  all the printed output of a function in the *list variable*, in the order in which they were called.

**usage**

.. code-block:: python

    from pyDeco.debug import redirect


    std_lines = []

    @redirect(line_print=std_lines)
    def func():
        print("func running...")
        print("--------------------------------")
        print("EOF")

    func()

    print(std_lines)

**output**

.. parsed-literal::
    ['func running...', '--------------------------------', 'EOF']

@stacktrace
-----------

The :code:`@stacktrace`  is a decorator that logs all the functions and nested functions that are called in a function.


**usage**

.. code-block:: python

    from pyDeco.debug import stacktrace

    def nested_func():
        print("nested_func called")


    def inner_func():
        print("inner called")
        nested_func()


    @stacktrace
    def func():
        print("func running...")

        inner_func()

        print("EOF")


    func()


**output**

.. parsed-literal::
    2023-02-14 21:59:28,173 [DEBUG] @stacktrace set up for func()...
    2023-02-14 21:59:28,173 [DEBUG]         Executing func(), line 16, from /mnt/Personal/py_decorators/pyDeco/debug/debug/stacktrace.py
    func running...
    2023-02-14 21:59:28,173 [DEBUG]         Executing inner_func(), line 11, from /mnt/Personal/py_decorators/test.py
    inner called
    2023-02-14 21:59:28,173 [DEBUG]         Executing nested_func(), line 7, from /mnt/Personal/py_decorators/test.py
    nested_func called
    EOF