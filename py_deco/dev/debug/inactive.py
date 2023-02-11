import sys

sys.path.insert(0, "../")
from py_deco.dev.utils import init_logger

logger = init_logger(__name__)


def inactive(func: callable):
    def inner(*args, **kwargs):
        logger.info(f"\nSkipping function {func.__name__}. Decorated with @inactive...")

        if len(args) > 0:
            return [None] * len(args)

    return inner
