cdef extern from "hello_c.c":
    void f()
    
cpdef myf():
    f()