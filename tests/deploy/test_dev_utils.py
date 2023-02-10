from py_deco.deploy import inactive


@inactive
def hoge():
    return True


hoge()
