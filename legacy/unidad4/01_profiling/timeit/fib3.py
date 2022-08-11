def fib(n, m={0: 0, 1: 1}):
    if n not in m:
        m[n] = fib(n - 1) + fib(n - 2)
    return m[n]
