import src.RSA as RSA
import unittest
import random as rand


class TestGCDMethods(unittest.TestCase):
    def test_keysAreValid(self):
        p = 7
        q = 11
        phi = (p - 1) * (q - 1)
        publicKey = RSA.generatePublicKey(p, q)
        privateKey = RSA.findPrivateKey(phi, publicKey)
        temp = (publicKey * privateKey) % phi
        self.assertEqual(temp, 1)


if __name__ == '__main__':
    unittest.main()
