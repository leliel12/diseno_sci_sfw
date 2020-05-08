def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2


from hypothesis import given
from hypothesis import strategies as st


@given(st.integers(), st.integers())
def test_sum(num1, num2):
    assert sum(num1, num2) == num1 + num2
