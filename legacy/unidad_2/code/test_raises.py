# content of test_sysexit.py
import pytest

def f():
    raise ZeroDivisionError()

def test_mytest():
    with pytest.raises(SystemExit):
        f()
