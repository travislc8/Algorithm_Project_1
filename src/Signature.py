import src.RSA as rsa


def signMessage(name, d, n):
    signature = rsa.encryptMessage(name, d, n)
    print("Signature = ", signature)
    return signature


def verifySignature(signature, name, e, n):
    verification = rsa.decryptMessage(signature, e, n)
    # Returns whether or not verification and nameInt are equal
    return verification == name


