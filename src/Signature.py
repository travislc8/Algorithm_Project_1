import src.RSA as rsa


# function to send a signature
# returns: encrypted signature and plain text signature
def signMessage(name, d, n):
    signature = rsa.encryptMessage(name, d, n)
    return signature, name


# function to verify a signature
# returns: true if the signature if valid
def verifySignature(signature, name, e, n):
    verification = rsa.decryptMessage(signature, e, n)
    # Returns whether or not verification and nameInt are equal
    return verification == name
