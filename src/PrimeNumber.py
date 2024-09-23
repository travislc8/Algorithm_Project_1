import random as rand
import src.GCD as gcd
import math


def is_prime(p):
    if p <= 1:
        return False
    if p == 2:
        return True
    elif p < 20:
        for b in range(2, p):
            if gcd.gcd(p, b) > 1:
                return False
            else:
                continue
        return True
    else:
        for b in range(2, math.floor(math.sqrt(p))):
            if gcd.gcd(p, b) > 1:
                return False
            else:
                continue
        return True


def smallPrimeCheck(prime):
    check = (prime % 2) * (prime % 3) * (prime % 5) * (prime % 7)
    check *= (prime % 11) * (prime % 13) * (prime % 17) * (prime % 19)


def generatePrime(n1=10000, n2=20000, k=100):
    prime = rand.randint(n1, n2)
    pseudo_prime = False

    # loops until a prime is found
    while not pseudo_prime:
        for i in range(k):
            if not smallPrimeCheck(prime):
                prime = rand.randint(n1, n2)
            j = rand.randint(2, prime)
            if pow(j, prime-1, prime) > 1:
                prime = rand.randint(n1, n2)
                break
            else:
                pseudo_prime = True
        if not is_prime(prime):
            prime = rand.randint(n1, n2)
            pseudo_prime = False

    return prime


def generatePrimes():
    p = generatePrime(10000, 20000, 100)
    q = generatePrime(10000, 20000, 100)
    return p, q
