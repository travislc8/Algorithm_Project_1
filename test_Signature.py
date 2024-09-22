import unittest
import src.RSA as rsa
import src.Signature as sig


# function that signs the message and then verifies the signature
def signatureTest(signature):
    private, public, n = rsa.generateKeys()
    encripted_signature, signature = sig.signMessage(signature, private, n)
    check = sig.verifySignature(encripted_signature, signature, public, n)
    return check


# tests that the verification returns false if the wrong key is used
def signatureFailTest(signature):
    private1, public1, n1 = rsa.generateKeys()
    private2, public2, n2 = rsa.generateKeys()
    # signs with private key 1 and checks with public key 2
    encripted_signature, signature = sig.signMessage(signature, private1, n1)
    check = sig.verifySignature(encripted_signature, signature, public2, n2)
    # should return false
    return check


class TestSignatureMethods(unittest.TestCase):
    # tests that the signature returns true for a valid signature
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

    # tests that the signature returns false for invalid signature
    def test_failSignature(self):
        try:
            check = signatureFailTest("test signature")
        except Exception:
            check = False
        self.assertFalse(check)
        try:
            check = signatureFailTest("some long string asdfasdfasdfasdfasdf")
        except Exception:
            check = False
        self.assertFalse(check)
        try:
            check = signatureFailTest("#$()@{#$~#@{)$()] #$()")
        except Exception:
            check = False
        self.assertFalse(check)
        try:
            check = signatureFailTest("126345968574845")
        except Exception:
            check = False
        self.assertFalse(check)


if __name__ == '__main__':
    unittest.main()
