import random as rand
import src.GCD as gcd


def generateKeys():
    print("Keys were generated")
    return 7, 11


def generatePublicKey(p=7, q=11):
    phi = (p - 1) * (q - 1)
    e = rand.randint(2, phi)
    while gcd.gcd(e, phi) != 1:
        e = rand.randint(2, phi)
    return e


def findPrivateKey(phi, publicKey):
    x = gcd.extendedGCD(publicKey, phi)
    key = x[0] % phi
    return key
