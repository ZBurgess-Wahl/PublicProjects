import sympy as sym
import numpy as np

# returns True if number in an integer
def is_integer(num):
    num = 2 * num
    if num % 2 == 0:
        return True
    else:
        return False


# finds all unique prime factors of a number
def prime_factors(x):
    p_factors = []
    for i in range(1, (x//2) + 1):
        if sym.isprime(i) and x % i == 0:
            p_factors.append(i)
    return p_factors


# expresses a number as its prime factors
def p_factn(x):
    factorisation = []
    p_factors = prime_factors(x)
    for i in p_factors:
        stop = False
        while not stop:
            if is_integer(x/i):
                factorisation.append(int(i))
                x = x/i
            else:
                stop = True
    return factorisation

# calculates the lowest common multiple of any number of given integers
def LCM(*args):
    primes = []
    non_primes = []

    # splits input sequence into primes and non-primes
    for i in args:
        if sym.isprime(i):
            primes.append(i)
        elif not sym.isprime(i) and i != 1:
            non_primes.append(i)

    # expresses non-primes as a product of prime factors
    factorised_non_primes = []
    for i in non_primes:
        x = p_factn(i)
        factorised_non_primes.append(x)

    # Removes unique primes from factorised_non_primes output from original primes list
    unique_primes = set()
    for i in factorised_non_primes:
        for j in i:
            unique_primes.add(j)
    unique_primes = list(unique_primes)
    for i in unique_primes:
        primes.remove(i)

    # creates dictionary with unique prime keys and values equal to its largest exponent from the factorised_non_primes output
    exponents = []
    for i in unique_primes:
        x = 0
        for j in factorised_non_primes:
            y = j.count(i)
            if y > x:
                x = y
        exponents.append(x)
    exponents = dict(zip(unique_primes,exponents))

    # calculates lowest common multiple
    lcm = 1
    for i in unique_primes:
        lcm = lcm * i ** (int(exponents[i]))
    lcm = lcm * np.prod(primes)
    return lcm

seq = list(range(1,21))
print(LCM(*seq))
