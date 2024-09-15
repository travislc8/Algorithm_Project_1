import src.GCD as GCD
import unittest
import random as rand


class TestGCDMethods(unittest.TestCase):
    def test_fastExponentialMod(self):
        for i in range(0, 20):
            with self.subTest(i=i):
                c = rand.randrange(0, 1000, 1)
                d = rand.randrange(0, 1000, 1)
                n = rand.randrange(0, 1000, 1)
                test = GCD.fastExponetialMod(c, d, n)
                python = pow(c, d, n)
                self.assertEqual(test, python)

    def test_gcd(self):
        for i in range(0, 20):
            with self.subTest(i=i):
                a = rand.randrange(1, 1000, 1)
                b = rand.randrange(1, 1000, 1)
                test = GCD.gcd(a, b)
                self.assertEqual(a % test, 0)
                self.assertEqual(b % test, 0)
                # self.assertTrue(isPrime(a))
                # self.assertTrue(isPrime(b))

    def test_extendedGCD(self):
        for i in range(0, 20):
            with self.subTest(i=i):
                a = 0
                b = 1
                while (a < b):
                    a = rand.randrange(1, 1000, 1)
                    b = rand.randrange(1, 1000, 1)
                x, y, d = GCD.extendedGCD(a, b)
                self.assertEquals(d, GCD.gcd(a, b))
                self.assertEquals(d, (a * x + b * y))


if __name__ == '__main__':
    unittest.main()
