import src.RSA as RSA
import unittest


def keyTest(q, p):
    phi = (p - 1) * (q - 1)
    publicKey = RSA.generatePublicKey(phi, p, q)
    privateKey = RSA.findPrivateKey(phi, publicKey)
    temp = (publicKey * privateKey) % phi
    return temp


def encryptDecrypt(message, p, q):
    private_key, public_key, n = RSA.generateKeysFromPrime(p, q)

    encripted_message = RSA.encryptMessage(message, public_key, n)
    decripted_message = RSA.decryptMessage(
        encripted_message, private_key, n)
    return decripted_message


class TestGCDMethods(unittest.TestCase):
    def test_keysAreValid(self):
        temp = keyTest(7, 11)
        self.assertEqual(temp, 1)
        temp = keyTest(13, 17)
        self.assertEqual(temp, 1)
        temp = keyTest(29, 53)
        self.assertEqual(temp, 1)
        temp = keyTest(97, 347)
        self.assertEqual(temp, 1)
        temp = keyTest(569, 547)
        self.assertEqual(temp, 1)

    def test_encriptionDecryptionOld(self):
        private_key, public_key, n = RSA.generateKeys()

        message = "test message"
        encripted_message = RSA.encryptMessage(message, public_key, n)
        decripted_message = RSA.decryptMessage(
            encripted_message, private_key, n)

        self.assertEqual(message, decripted_message)

    def test_encriptionDecryption(self):
        message = "test message"
        return_message = encryptDecrypt(message, 757, 733)
        self.assertEqual(message, return_message)
        return_message = encryptDecrypt(message, 569, 547)
        self.assertEqual(message, return_message)
        return_message = encryptDecrypt(message, 877, 907)
        self.assertEqual(message, return_message)
        return_message = encryptDecrypt(message, 787, 797)
        self.assertEqual(message, return_message)


if __name__ == '__main__':
    unittest.main()
