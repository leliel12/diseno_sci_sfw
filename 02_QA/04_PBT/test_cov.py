
def division(a, b):
    return a / b

def sum(a, b):
    return a + b

def test_division():
    assert division(1, 2) == .5

def test_sum():
    assert sum(1, 2) == 3
    
if __name__ == "__main__":
    test_division()
    test_sum()