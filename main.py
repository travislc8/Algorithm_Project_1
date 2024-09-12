import RSA as RSA
import InputOutput as IO


def publicLoop():
    print("in publicLoop")
    list = ["one", "two", "three"]
    while (1):
        choice = IO.publicUserPrompt()
        if (choice == "1"):
            IO.sendMessagePrompt()
        elif (choice == "2"):
            IO.authenticatePrompt(list)
        elif (choice == "3"):
            break
        else:
            print("Invalid Choice")


def privateLoop():
    print("in privateLoop")
    list = ["one", "two", "three"]
    while (1):
        choice = IO.privateUserPrompt()

        if (choice == "1"):
            IO.decryptPrompt(list)
        elif (choice == "2"):
            IO.signMessagePrompt()
        elif (choice == "3"):
            IO.showKeysPrompt()
        elif (choice == "4"):
            IO.generatePrompt()
        elif (choice == "5"):
            break
        else:
            print("Invalid Choice")


public, private = RSA.generateKeys()
print("RSA keys have been generated.")

while (1):
    user_type = IO.getUserType()

    if (user_type == "1"):
        publicLoop()
    elif (user_type == "2"):
        privateLoop()
    elif (user_type == "3"):
        print("Bye for now")
        exit(0)
    else:
        print("Invalid Choice")
