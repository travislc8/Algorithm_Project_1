import random as rand
import src.GCD as gcd


def generateKeys():
    public_key, phi = generatePublicKey()
    private_key = findPrivateKey(phi, public_key)
    print("Keys were generated")
    return private_key, public_key


def generatePublicKey(p=7, q=11):
    phi = (p - 1) * (q - 1)
    e = rand.randint(2, phi)
    while gcd.gcd(e, phi) != 1:
        e = rand.randint(2, phi)
    return e, phi


def findPrivateKey(phi, publicKey):
    x = gcd.extendedGCD(publicKey, phi)
    key = x[0] % phi
    return key


# TODO
def encryptMessage(message, private_key):
    return message


# TODO
def decryptMessage(message, public_key):
    return message
