import time
import sys

sys.path.insert(0, "../../")

import pyDeco.utils as util


logger = util.init_logger(__name__)


def timeit(func: callable):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logger.info(f"Function {func.__name__}() took {total_time:.4f} seconds.")

        return result

    return inner
