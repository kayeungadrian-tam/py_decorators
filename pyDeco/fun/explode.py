import sys
import time
import inspect

EXPLOSION = """
                             ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
"""


def explode(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print(
                f"Something went wrong in {func.__name__}(), line {inspect.stack()[1][2]}, file {inspect.stack()[1][1]}...",
                flush=True,
            )
            print("3..", end="", flush=True)
            time.sleep(1)
            print("2..", end="", flush=True)
            time.sleep(1)
            print("1..", end="", flush=True)
            time.sleep(1)
            print(f"{EXPLOSION}", flush=True)
            sys.exit(1)
        return None

    return wrapper
