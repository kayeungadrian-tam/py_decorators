from py_deco.dev import redirect, stacktrace, inactive


lines = []


@redirect(line_print=lines)
def hoge():
    print("hoge")
    for i in range(10):
        print(f"Line #{i+1}")


@redirect
def hoge2():
    print("hoge")
    for i in range(10):
        print(f"Line #{i+1}")


def func_b():
    # print("func_b")
    return 1


# @inactive
# def func_c(n, m):
# return n, m


@stacktrace
def func_a(arg):
    # print("func_a")
    # print(arg)
    # func_b()

    foo = Foo()
    foo.run()
    res = func_b()

    # n, m = func_c(1, 2)

    res = func_b()
    aes2 = func_b()
    # print(res)
    return "EOF"


class Foo:
    def __init__(self):
        print("FOOL!")

    def run(self):
        print("Fool is running!")


def hoge3():
    func_a(1)


# hoge()
# print(lines)
# hoge2()
hoge3()
