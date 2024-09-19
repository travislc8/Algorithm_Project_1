import random as rand
import src.GCD as gcd


def generateKeys():
    # p,q = prime.generatePrimeNumbers()
    p, q = 7, 17
    n = p * q
    phi = findPHI(p, q)
    public_key = generatePublicKey(phi, p, q)
    private_key = findPrivateKey(phi, public_key)
    return private_key, public_key, n


def generateKeysFromPrime(p=7, q=11):
    n = p * q
    phi = findPHI(p, q)
    public_key = generatePublicKey(phi, p, q)
    private_key = findPrivateKey(phi, public_key)
    return private_key, public_key, n


def findPHI(p=7, q=17):
    phi = (p - 1) * (q - 1)
    return phi


def generatePublicKey(phi=96, p=7, q=17):
    e = rand.randint(2, phi)
    # print("test key = ", e)
    # e = 5
    # print("repeate if not 1: ", gcd.gcd(e, phi))
    while gcd.gcd(e, phi) != 1:
        e = rand.randint(2, phi)
    return e


def findPrivateKey(phi, publicKey):
    x = gcd.extendedGCD(publicKey, phi)
    key = x[0] % phi
    return key


# TODO
def encryptMessage(message, public_key, n):
    cipher = []
    for char in message:
        char_code = ord(char)
        char_code = gcd.fastExponetialMod(char_code, public_key, n)
        cipher.append(char_code)
    return cipher


# TODO
def decryptMessage(message, private_key, n):
    plain_text = ""
    for char in message:
        char_code = gcd.fastExponetialMod(char, private_key, n)
        char_code = chr(char_code)
        plain_text += ((char_code))
    return plain_text
