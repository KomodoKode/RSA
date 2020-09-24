"""
Generates the prime numbers necessary for
RSA. This can only do numbers of up to 1024 Bits
in a reasonable amount of time. Hoping to improve
this using the Python Threads module
"""

import secrets
from math import gcd

rng = secrets.SystemRandom()
"""Gets the Random Number Generator
to generate probabilistic test numbers"""

base_primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
]

# Test to see if p1 & p2 are prime using Fermat's Theorem
def Fermat_prime(integer: int) -> bool:
    numTrials = 1001
    testnums = set()
    valid = 0
    while valid < numTrials:
        rand_testnum = rng.randint(2, integer - 1)
        if rand_testnum not in testnums:
            if gcd(integer, rand_testnum) != 1:
                return False
            testnums.add(rand_testnum)
            valid = valid + 1
            if pow(rand_testnum, integer - 1, integer) != 1:
                return False
    return True


# Test to see if p1 & p2 are prime using Rabin-Miller Prime Test
def RabinMiller_prime(n: int) -> bool:
    if n & 1 == 0:
        return False
    s = n - 1
    t = 0
    while s & 1 == 0:
        s >>= 1
        t += 1
    testnums = set()
    for _ in range(40):
        while True:
            testnum = rng.randrange(1, n)
            if testnum not in testnums:
                break
        testnums.add(testnum)
        x = pow(testnum, s, n)
        if x == 1 or x == n - 1:
            for i in range(t):
                x = (x * x) % n
                if x == n - 1:
                    return False
        else:
            return False
    return True


def get_basic_test(num: int) -> bool:
    for i in base_primes :
        if num % i == 0:
            return False
    return True
            

def GetRandPrime(numbits: int) -> int:
    """Not 100% guaranteed to work,
    but highly likely to give true prime"""
    trialset = set()
    while True:
        trialnum = secrets.getrandbits(numbits)
        if trialnum not in trialset:
            # Prime tests number using Fermat's Primality Test
            if RabinMiller_prime(trialnum) == True:
                return trialnum
            else:
                trialset.add(trialnum)
        
