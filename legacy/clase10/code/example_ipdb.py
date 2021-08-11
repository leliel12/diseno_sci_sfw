# code/example_ipdb.py

def fact(num):
    import ipdb; ipdb.set_trace()
    if num <= 1:
        return 1
    return num * fact(num - 1)

fact(5)
