import src.RSA as rsa


def publicLoop(public_key, n, list):
    print("in publicLoop")

    while (1):
        choice = publicUserPrompt()
        if (choice == "1"):
            decryptPrompt(list, public_key)
        elif (choice == "2"):
            authenticatePrompt(list, public_key)
        elif (choice == "3"):
            break
        else:
            print("Invalid Choice")
    return public_key, list


def privateLoop(private_key, public_key, n, list):
    print("in privateLoop")
    list = ["one", "two", "three"]
    while (1):
        choice = privateUserPrompt()

        if (choice == "1"):
            decryptPrompt(list, public_key, n)
        elif (choice == "2"):
            encrypted_message = sendMessagePrompt(private_key, n)
            list.add(encrypted_message)
        elif (choice == "3"):
            showKeysPrompt(private_key, public_key)
        elif (choice == "4"):
            generatePrompt()
        elif (choice == "5"):
            break
        else:
            print("Invalid Choice")


def getUserType():
    print("Please select your user type:")
    print("\t1. A Public user")
    print("\t2. The owner of the keys")
    print("\t3. Exit program")
    choice = input("Enter your choice: ")
    return choice


def publicUserPrompt():
    print("As a public user, what would you like to do?")
    print("\t1. Send an encrypted message")
    print("\t2. Authenticate a digital signature")
    print("\t3. Exit")
    print()
    choice = input("Enter your choice: ")
    return choice


def sendMessagePrompt(private_key, n):
    print("sendMessagePrompt")
    message = input("Enter a message: ")
    # encrypted_message = rsa.encrypt(private_key, message, n)
    encrypted_message = message
    return encrypted_message


def authenticatePrompt(message_list):
    print("The following messages are available: ")

    # if there are no messages
    if (len(message_list) <= 0):
        print("No messages to authenticate")
        return

    displayMessages(message_list)
    while (1):
        choice = int(input("Enter your choice: "))
        if (len(message_list) > choice or choice < 1):
            print("Invalid choice")
            continue

        # check = signature.authenticate(message_list[choice])
        # if (check):
            # print("Signature is valid")
        # else:
            # print("Signature is not valid")
        break


def privateUserPrompt():
    print("As a private user, what would you like to do?")
    print("\t1. Decrypt a received message")
    print("\t2. Digitally sign a message")
    print("\t3. Show the keys")
    print("\t4. Generate a new set of keys")
    print("\t5. Exit")
    print()
    choice = input("Enter your choice: ")
    return choice


def decryptPrompt(message_list, public_key):
    print("The following messages are available to decrypt: ")

    # if there are no messages
    if (len(message_list) <= 0):
        print("No messages to authenticate")
        return

    displayMessages(message_list)
    while (1):
        choice = int(input("Enter your choice: "))
        if (len(message_list) > choice or choice < 1):
            print("Invalid choice")
            continue

        # message = rsa.decryptMessage(message_list[choice], public_key)
        # print(message)
        break
    return


def signMessagePrompt():
    print("signMessagePrompt")
    message = input("Enter a message:  ")
    print("Message signed and sent.")
    return message


def showKeysPrompt(private_key, public_key):
    print("The private key is: ", private_key,
          " The public key is: ", public_key)


def generatePrompt():
    private_key, public_key = rsa.generateKeys()


def availableMessagePrompt():
    print("availableMessagePrompt")
    choice = input("Enter your choice: ")
    return choice


def displayMessages(message_list):
    i = 1
    for item in message_list:
        print("\t", i, ". (length = ", len(item), ")")
        i += 1
