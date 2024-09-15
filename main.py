import src.RSA as RSA
import src.InputOutput as IO


public, private = RSA.generateKeys()
print("RSA keys have been generated.")

while (1):
    user_type = IO.getUserType()

    if (user_type == "1"):
        IO.publicLoop()
    elif (user_type == "2"):
        IO.privateLoop()
    elif (user_type == "3"):
        print("Bye for now")
        break
    else:
        print("Invalid Choice")
