import random as rand
import src.GCD as gcd


def generateKeys():
    # p,q = prime.generatePrimeNumbers()
    p, q = 5, 11
    n = p * q
    print("n = ", n)
    phi = findPHI()
    print("phi = ", phi)
    public_key = generatePublicKey(phi, p, q)
    print("public key = ", public_key)
    private_key = findPrivateKey(phi, public_key)
    print("private key = ", private_key)
    print("Keys were generated")
    return private_key, public_key, n


def findPHI(p=5, q=11):
    phi = (p - 1) * (q - 1)
    return phi


def generatePublicKey(phi=60, p=5, q=11):
    e = rand.randint(2, phi)
    while gcd.gcd(e, phi) != 1:
        e = rand.randint(2, phi)
    return e


def findPrivateKey(phi, publicKey):
    x = gcd.extendedGCD(publicKey, phi)
    key = x[0] % phi
    return key


# TODO
def encryptMessage(message, public_key, n):
    print(" n = ", n)
    cipher = []
    for char in message:
        print(char)
        char_code = ((char)**public_key) % n
        cipher.append(char_code)
    return cipher


# TODO
def decryptMessage(message, private_key, n):
    print(" n = ", n)
    plain_text = []
    for char in message:
        char_code = (char**private_key) % n
        print(char_code)
        plain_text.append((char_code))
    return plain_text
