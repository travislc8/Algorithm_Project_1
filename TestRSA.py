import src.RSA as RSA
import unittest
import random as rand


def keyTest(q, p):
    phi = (p - 1) * (q - 1)
    publicKey = RSA.generatePublicKey(p, q)
    privateKey = RSA.findPrivateKey(phi, publicKey)
    temp = (publicKey * privateKey) % phi
    return temp


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


if __name__ == '__main__':
    unittest.main()
