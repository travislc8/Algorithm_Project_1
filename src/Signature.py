import src.RSA as rsa


def signMessage(name, d, n):
    signature = rsa.encryptMessage(name, d, n)
    print("Signature = ", signature)
    return signature


def verifySignature(signature, name, e, n):
    verification = rsa.decryptMessage(signature, e, n)
    # Returns whether or not verification and nameInt are equal
    return verification == name


'''def main():

    d, e, n = rsa.generateKeys()
    print(d,e,n)
    
    name = "Alice"

    signature = signMessage(name, d, n)
    #print(f"Signature: {signature}")

    verification = verifySignature(signature, name, e, n)
    print(f"Verification successful: {verification}")

if __name__ == "__main__":
    main()'''
