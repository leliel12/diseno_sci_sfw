# code/example_ipdb_exeption.py

from ipdb import launch_ipdb_on_exception


def div(a, b):
    return a / b


with launch_ipdb_on_exception():
    div(1, 2)

with launch_ipdb_on_exception():
    div(1, 0)
