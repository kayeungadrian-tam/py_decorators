from pyDeco.dev import inactive


@inactive
def hoge():
    return True


hoge()
