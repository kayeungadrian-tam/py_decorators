import logging


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def init_logger(name: str) -> logging:
    logging.basicConfig(
        level=logging.INFO,
        format="\033[1m\033[94m pyDeco \033[0m | %(levelname)s | %(message)s",
    )
    logging.getLogger(name)
    return logging
