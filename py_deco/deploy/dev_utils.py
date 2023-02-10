def inactive(func: callable):
    def inner(*args, **kwargs):
        print(f"\nSkipping function {func.__name__}. Decorated with @inactive...")

    return inner
