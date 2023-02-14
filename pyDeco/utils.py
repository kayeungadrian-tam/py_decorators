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


def init_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create separate handlers and formatters for each log level
    debug_handler = logging.StreamHandler()
    debug_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter(
        f"%(asctime)s{bcolors.BOLD}\t{bcolors.OKBLUE}[%(levelname)-5s]{bcolors.ENDC} %(message)s"
    )
    debug_handler.setFormatter(debug_formatter)

    logger.addHandler(debug_handler)

    return logger
