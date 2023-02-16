Cli arguments
=============

A set of decorators that are related to command line interface (CLI) arguments.



@cli_yaml
---------

The :code:`@cli_yaml` (and :code:`@cli_json` alike) provides a convenient way to read the contents of a YAML file and pass them as arguments to a function directly.

**usage**

`demo.yaml`

.. code-block:: yaml

    name: "adrian"
    age: 28

`demo.py`

.. code-block:: python

    from pyDeco.cli import cli_yaml

    @cli_yaml
    def func(name: str, age: int):
        print(f"{name} is {age} years old.")

    func()

run command

.. code-block:: bash

    $ python demo.py --yaml ./demo.yaml

**output**

.. parsed-literal::
    adrian is 28 years old.



@cli_json
---------

Same as above
