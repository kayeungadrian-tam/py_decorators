from py_deco.dev import inactive


@inactive
def hoge():
    return True


hoge()
