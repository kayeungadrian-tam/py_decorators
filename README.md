<div align="center">

<h1> <strong>py</strong>thon <strong>Deco</strong>ractor<br>
<img src="https://img.shields.io/badge/made%20with-LOVE-red">
<img src="https://img.shields.io/badge/license-MIT-blue">
<a href='https://py-decorators.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/py-decorators/badge/?version=latest' alt='Documentation Status' />
</a>
</h1>
</div>

An OSS that has something to do with decorators in python

# :sparkles: Features

- Time related decorators
- Debugging decorators
- Custom cli input decorators

# :hammer: Install

To install, run the following command.

```bash
$ pip install python-deco
```

# :package: Modules

- **Info**: Decorators that provide information about the function.

- **Debug**: Decorators that help debug the function.

- **CLI**: Decorators that uses variables defined in a [yaml/json] file as function arugments.

- **Fun**: Decorators just for FUN!

# :books: Usage

A quick usage example.

@timeit

```python
from pyDeco.dev import inactive
from pyDeco.time import timeit

@timeit
def func():
    # do something
    return 1
```

```bash
2023-02-17 00:05:09,721 [INFO ] Function func() took 2.0120s.
```

# :construction: TODO

## credits

https://bytepawn.com/python-decorators-for-data-scientists.html
