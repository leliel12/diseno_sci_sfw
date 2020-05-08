import numba
from numba.pycc import CC

cc = CC('mult')


@cc.export('mult', 'f8(f8, f8)')
@cc.export('mult', 'i4(i4, i4)')
def mult(a, b):
    return a * b