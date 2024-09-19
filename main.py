import src.RSA as RSA
import src.InputOutput as IO


public_key, private_key, n = RSA.generateKeys()
list = []
init_message = RSA.encryptMessage("test pre message", public_key, n)
list.append(init_message)
print(list)
print("RSA keys have been generated.")

while (1):
    user_type = IO.getUserType()

    if (user_type == "1"):
        IO.publicLoop(public_key, n, list)
    elif (user_type == "2"):
        IO.privateLoop(private_key, public_key, n, list)
    elif (user_type == "3"):
        print("Bye for now")
        break
    else:
        print("Invalid Choice")
