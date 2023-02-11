import inspect
import sys
from sys import settrace

sys.path.insert(0, "../")
from py_deco.dev.utils import init_logger

logger = init_logger(__name__)


def stacktrace(func=None, exclude_files=["logging", ".pyenv", r".*venv"]):
    def tracer_func(frame, event, arg):

        co = frame.f_code
        line_no = co.co_firstlineno
        func_name = co.co_name
        caller_filename = frame.f_back.f_code.co_filename

        if func_name == "write":
            return  # ignore write() calls from print statements
        for file in exclude_files:
            if file in caller_filename:
                return  # ignore in ipython notebooks
        if event == "call":
            logger.info(
                f"\tExecuting {func_name}, line {line_no}, from {caller_filename}"
            )
            return tracer_func

        return

    def decorator(func: callable):
        logger.info(f"\033[93mstacktrace starting for {func.__name__}()\033[0m")

        def inner(*args, **kwargs):
            settrace(tracer_func)
            func(*args, **kwargs)
            settrace(None)

        return inner

    if func is None:
        # decorator was used like @stacktrace(...)
        return decorator
    else:
        # decorator was used like @stacktrace, without parens
        return decorator(func)
