def sieve(n):
    """
    Returns a list of all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    # Create a list of boolean values, indicating whether each number is prime or not.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Loop through all numbers up to the square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        # If the current number is prime, mark all its multiples as composite.
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False

    # Return a list of all prime numbers up to n.
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

sieve(100_000_000)
