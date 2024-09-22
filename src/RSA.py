import random as rand
import src.GCD as gcd
import src.PrimeNumber as prime


# function that generates the public and private keys
# returns: public and private key and n
def generateKeys():
    # TODO
    p, q = prime.generatePrimes()
    n = p * q
    phi = (p - 1) * (q - 1)
    # calls funciton to generate the public key based on given input
    public_key = generatePublicKey(phi, p, q)
    # calls function to generate the private key based on the input
    private_key = findPrivateKey(phi, public_key)
    return private_key, public_key, n


# function that generates public and private keys given
# keys based on given prime numbers
# returns: public and private key and n
def generateKeysFromPrime(p=7, q=11):
    n = p * q
    phi = (p - 1) * (q - 1)
    # calls funciton to generate the public key based on given input
    public_key = generatePublicKey(phi, p, q)
    # calls function to generate the private key based on the input
    private_key = findPrivateKey(phi, public_key)
    return private_key, public_key, n


# function to generate public key
# returns: public key
# TODO comments
def generatePublicKey(phi=96, p=7, q=17):
    e = rand.randint(2, phi)
    while gcd.gcd(e, phi) != 1:
        e = rand.randint(2, phi)
    return e


# function to generate private key
# returns: private key
# TODO comments
def findPrivateKey(phi, publicKey):
    x = gcd.extendedGCD(publicKey, phi)
    key = x[0] % phi
    return key


# function to encrypt a given character string
# returns: encrypted message
def encryptMessage(message, public_key, n):
    cipher = []
    # loops through the message and decrypts each character individualy
    for char in message:
        # converts the character to the ascii interger representation
        char_code = ord(char)
        # encrypts the character
        char_code = gcd.fastExponetialMod(char_code, public_key, n)
        # appends the encrypted character to the encrypted message list
        cipher.append(char_code)
    return cipher


# function to decrypt a given message
# returns: decrypted message
def decryptMessage(message, private_key, n):
    plain_text = ""
    for char in message:
        # decrypts the item in the list
        char_code = gcd.fastExponetialMod(char, private_key, n)
        # converts the item to a character
        char_code = chr(char_code)
        # appends the devrypted character to the plain text
        plain_text += ((char_code))
    return plain_text
