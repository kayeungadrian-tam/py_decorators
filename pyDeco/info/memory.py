import sys

sys.path.insert(0, "../../")

import tracemalloc
import pyDeco.utils as util


logger = util.init_logger(__name__)


def memoryit(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        logger.info(
            f"Peak memory usage for function {util.bcolors.BOLD}{func.__name__}(){util.bcolors.ENDC} was {util.bcolors.BOLD}{peak / 10**6:.3f} MB{util.bcolors.ENDC}."
        )
        return result

    return wrapper
