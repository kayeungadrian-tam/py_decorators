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

# Features

- Time related decorators
- Debugging decorators
- Custom cli input decorators

# Example

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
 pyDeco  | INFO | Function func() took 2.0261 seconds.
```

@stacktrace

```python
from pyDeco.dev import stacktrace


def nested_func():
    print("nested")


def func_b():
    print("func_b")
    nested_func()


@stacktrace
def func_a():
    print("func_a")
    func_b()
    return 1


func_a()
```

```terminal
 pyDeco  | INFO | @stacktrace set up for func_a()...
func_a
 pyDeco  | INFO |       Executing func_b, line 9, from /mnt/Personal/test.py
func_b
 pyDeco  | INFO |       Executing nested_func, line 5, from /mnt/Personal/test.py
nested
```

##

# TODO

## credits

https://bytepawn.com/python-decorators-for-data-scientists.html
