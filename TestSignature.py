import unittest
import src.RSA as rsa
import src.Signature as sig


def signatureTest(signature):
    private, public, n = rsa.generateKeys()
    encripted_signature, signature = sig.signMessage(signature, private, n)
    check = sig.verifySignature(encripted_signature, signature, public, n)
    return check


class TestSignatureMethods(unittest.TestCase):
    def test_signature(self):
        check = signatureTest("test signature")
        self.assertTrue(check)
        check = signatureTest("asdf asdf asd")
        self.assertTrue(check)
        check = signatureTest("some string")
        self.assertTrue(check)
        check = signatureTest("15687 5671")
        self.assertTrue(check)
        check = signatureTest("test $()@")
        self.assertTrue(check)
        check = signatureTest("")
        self.assertTrue(check)
        check = signatureTest("long signature test asasdfasdfasdfasdfasdfs")
        self.assertTrue(check)
