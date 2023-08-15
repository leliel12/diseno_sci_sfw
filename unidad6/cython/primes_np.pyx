# primes_np.pyx
import numpy as np

def primes(int nb_primes):
    
    # Memoryview on a NumPy array
    narr = np.empty(nb_primes, dtype=np.dtype(int))
    cdef long [:] narr_view = narr
    
    len_p = 0  # The current number of elements in p.
    n = 2
    
    while len_p < nb_primes:
        # Is n prime?
        for i in narr_view[:len_p]:
            if n % i == 0:
                break
        # If no break occurred in the loop, we have a prime.
        else:
            narr_view[len_p] = n
            len_p += 1
        n += 1
    return narr