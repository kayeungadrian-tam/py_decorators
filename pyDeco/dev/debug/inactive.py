import sys

sys.path.insert(0, "../../")
from pyDeco.utils import init_logger

logger = init_logger(__name__)


def inactive(func: callable):
    def inner(*args, **kwargs):
        logger.info(f"Function {func.__name__}() decorated with @inactive. Skipping...")

        if len(args) > 0:
            return [None] * len(args)

    return inner
