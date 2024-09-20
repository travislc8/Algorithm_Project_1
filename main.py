import src.RSA as RSA
import src.InputOutput as IO


public_key, private_key, n = RSA.generateKeys()
print("RSA keys have been generated.")
message_list = []
signature_list = []

while (1):
    user_type = IO.getUserType()

    if (user_type == "1"):
        IO.publicLoop(public_key, n, message_list, signature_list)
    elif (user_type == "2"):
        IO.privateLoop(private_key, public_key, n,
                       message_list, signature_list)
    elif (user_type == "3"):
        print("Bye for now")
        break
    else:
        print("Invalid Choice")
