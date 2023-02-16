from pyDeco.debug import inactive, stacktrace, redirect


@inactive
def create_inactive():
    ...


@stacktrace
def create_stack():
    ...


lines = []


@redirect(line_print=lines)
def create_redirect():
    print("A")
    print("B")
    print("C")


def test_redirect():
    create_redirect()
    assert len(lines) == 3


def test_stacktrace(capfd):
    create_stack()
    out_string = capfd.readouterr()
    assert out_string.err[46:70] == "Executing create_stack()"


def test_inactive(capfd):
    create_inactive()
    out_string = capfd.readouterr()
    assert out_string.err[-23:-4] == "@inactive. Skipping"
