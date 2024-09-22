import unittest
import src.PrimeNumber as prime


class TestPrimeNumber(unittest.TestCase):
    def test_PrimeNumber(self):
        for i in range(0, 20):
            with self.subTest(i=i):
                p, q = prime.generatePrimes()
                self.assertTrue(p > 10000)
                self.assertTrue(q > 10000)
                self.assertTrue(prime.is_prime(p))
                self.assertTrue(prime.is_prime(q))

    def test_isPrimeTest(self):
        self.assertTrue(prime.is_prime(3))
        self.assertTrue(prime.is_prime(11))
        self.assertTrue(prime.is_prime(467))
        self.assertTrue(prime.is_prime(907))
        self.assertTrue(prime.is_prime(1049))
        self.assertTrue(prime.is_prime(139))
        self.assertTrue(prime.is_prime(1601))
        self.assertTrue(prime.is_prime(4507))

        self.assertFalse(prime.is_prime(3))
        self.assertFalse(prime.is_prime(11))
        self.assertFalse(prime.is_prime(467))
        self.assertFalse(prime.is_prime(907))
        self.assertFalse(prime.is_prime(1049))
        self.assertFalse(prime.is_prime(139))
        self.assertFalse(prime.is_prime(1601))
        self.assertFalse(prime.is_prime(4507))
