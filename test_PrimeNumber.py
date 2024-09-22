import unittest
import src.PrimeNumber as prime


class TestPrimeNumber(unittest.TestCase):
    def test_PrimeNumber(self):
        for i in range(0, 100):
            with self.subTest(i=i):
                p, q = prime.generatePrimes()
                self.assertTrue(p > 10000)
                self.assertTrue(q > 10000)
                self.assertTrue(prime.is_prime(p))
                self.assertTrue(prime.is_prime(q))

    def test_isPrimeTest(self):
        self.assertTrue(prime.is_prime(7))
        self.assertTrue(prime.is_prime(11))
        self.assertTrue(prime.is_prime(13))
        self.assertTrue(prime.is_prime(17))
        self.assertTrue(prime.is_prime(19))
        self.assertTrue(prime.is_prime(11))
        self.assertTrue(prime.is_prime(467))
        self.assertTrue(prime.is_prime(907))
        self.assertTrue(prime.is_prime(1049))
        self.assertTrue(prime.is_prime(139))
        self.assertTrue(prime.is_prime(1601))
        self.assertTrue(prime.is_prime(4507))

        self.assertFalse(prime.is_prime(8))
        self.assertFalse(prime.is_prime(9))
        self.assertFalse(prime.is_prime(10))
        self.assertFalse(prime.is_prime(12))
        self.assertFalse(prime.is_prime(14))
        self.assertFalse(prime.is_prime(15))
        self.assertFalse(prime.is_prime(16))
        self.assertFalse(prime.is_prime(18))
        self.assertFalse(prime.is_prime(20))
        self.assertFalse(prime.is_prime(12))
        self.assertFalse(prime.is_prime(468))
        self.assertFalse(prime.is_prime(908))
        self.assertFalse(prime.is_prime(1050))
        self.assertFalse(prime.is_prime(140))
        self.assertFalse(prime.is_prime(1602))
        self.assertFalse(prime.is_prime(4509))


if __name__ == '__main__':
    unittest.main()
