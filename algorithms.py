import math

def is_prime(a,primes = [2]):
    # tests whether a is a multiple of any integer between 2 and sqrt(a).
    for p in primes:
        if a % p == 0:
            return False
        if p > math.sqrt(a):
            break
    return True

def primesToIndex(n):
    primes = [2]
    i=3
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
        i+=2
    return primes

def primesToInteger(n):
    primes = [2]
    i=3
    while i < n:
        if is_prime(i, primes):
            primes.append(i)
        i+=2
    return primes