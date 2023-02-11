import logging


def init_logger(name: str) -> logging:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | \033[1m\033[94m py_deco \033[0m | %(message)s",
    )
    logging.getLogger(name)
    return logging
