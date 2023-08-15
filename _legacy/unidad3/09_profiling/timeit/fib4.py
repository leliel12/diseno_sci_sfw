import math

sqrt5 = math.sqrt(5)
phi = (1 + sqrt5) / 2

def fib(n):
    return int((phi**n - (-phi)**-n) / sqrt5)
