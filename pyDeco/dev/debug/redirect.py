import sys

sys.path.insert(0, "../../")
from contextlib import redirect_stdout
from io import StringIO
import inspect
from math import floor, log

from pyDeco.utils import init_logger

logger = init_logger(__name__)


def redirect(func=None, line_print: list = None):
    def decorator(func: callable):
        def inner(*args, **kwargs):
            with StringIO() as buf, redirect_stdout(buf):
                func(*args, **kwargs)
                output = buf.getvalue()
            lines = output.splitlines()
            if line_print is not None:
                for line in lines:
                    line_print.append(line)
            else:
                width = floor(log(len(lines), 10)) + 1
                for i, line in enumerate(lines):
                    i += 1
                    logger.info(
                        f"{i:0{width}}: {line} {inspect.stack()[1][1]} {inspect.stack()[1][2]} "
                    )

        return inner

    if func is None:
        return decorator
    else:
        return decorator(func)
