import numpy as np

def sieve(n):
    """
    Returns a list of all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    # Create a boolean array of size n+1 initialized to True.
    is_prime = np.ones(n+1, dtype=bool)

    # Mark 0 and 1 as composite.
    is_prime[0] = is_prime[1] = False

    # Loop through all numbers up to the square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        # If the current number is prime, mark all its multiples as composite.
        if is_prime[i]:
            is_prime[i*i:n+1:i] = False

    # Return a list of all prime numbers up to n.
    primes = np.nonzero(is_prime)[0][2:]
    return primes.tolist()

sieve(100_000_000)
