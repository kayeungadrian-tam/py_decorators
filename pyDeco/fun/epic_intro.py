import sys

try:
    import pyfiglet
except ModuleNotFoundError as exception:
    sys.exit(
        f"pyfiglet is required to run the `fun decorators`.\nYou can install it by running:\n\tpip install pyfiglet"
    )


def epic_intro(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        ascii_text = pyfiglet.figlet_format(f"{func.__name__}", font="cosmic")
        print(f"{ascii_text}")
        return func(*args, **kwargs)

    return wrapper
