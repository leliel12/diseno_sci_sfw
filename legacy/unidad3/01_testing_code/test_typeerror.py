import pytest
 

def sum(a, b):
    if not isinstance(a, (float, int)):
        raise TypeError('Error de tipo')
        
    return a + b

def test_mytest():
    with pytest.raises(TypeError):
        sum('1', 2)