def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2


from hypothesis import given, settings, Verbosity, example
from hypothesis import strategies as st

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_sum(num1, num2):
    assert sum(num1, 0) == num1
    assert sum(num1, num2) == sum(num2, num1)
    assert float(num1) % 2 == 0
