from pyDeco.debug import inactive


@inactive
def hoge():
    return True


hoge()
