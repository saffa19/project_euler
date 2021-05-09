import math

# number of factors for integer n
def factors(n):
    f = 0
    r = int(math.sqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            if i == n:
                f += 1
            elif i != n:
                f += 2

    return f

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