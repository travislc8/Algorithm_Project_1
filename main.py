import src.RSA as RSA
import src.InputOutput as IO


# generates keys
public_key, private_key, n = RSA.generateKeys()
print("RSA keys have been generated.")

# variable initialization
message_list = []
signature_list = []

# main loop: runs until the user wants to exit the program
while (1):
    user_type = IO.getUserType()

    # if user specifies they are a public user
    if (user_type == "1"):
        IO.publicLoop(public_key, n, message_list, signature_list)
    # if the user specifies they are the owner of the keys
    elif (user_type == "2"):
        private_key, public_key, n, message_list, signature_list = IO.privateLoop(
            private_key, public_key, n,
            message_list, signature_list)
    # if the use specifies to exit the program
    elif (user_type == "3"):
        print("Bye for now")
        break
    # if the user does not enter 1-3
    else:
        print("Invalid Choice")
