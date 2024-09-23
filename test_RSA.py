import src.RSA as RSA
import src.PrimeNumber as prime
import unittest


def keyTest():
    p, q = prime.generatePrimes()
    phi = (p - 1) * (q - 1)
    publicKey = RSA.generatePublicKey(phi, p, q)
    privateKey = RSA.findPrivateKey(phi, publicKey)
    temp = (publicKey * privateKey) % phi
    return temp


def encryptDecrypt(message):
    private_key, public_key, n = RSA.generateKeys()
    # print(private_key, " _____ ",  public_key, n)
    # private_key = 4895507
    # public_key = 73559003
    # n = 240202517
    encripted_message = RSA.encryptMessage(message, public_key, n)
    decripted_message = RSA.decryptMessage(
        encripted_message, private_key, n)
    return decripted_message


class TestRSAMethods(unittest.TestCase):
    def test_keysAreValid(self):
        for i in range(0, 100):
            with self.subTest(i=i):
                temp = keyTest()
                self.assertEqual(temp, 1)

    def test_encriptionDecryption(self):
        message = "test message"
        return_message = encryptDecrypt("test message")
        self.assertEqual(message, return_message)


if __name__ == '__main__':
    unittest.main()
