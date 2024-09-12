
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


def sendMessagePrompt():
    print("sendMessagePrompt")
    message = input("Enter a message: ")
    return message


def authenticatePrompt(message_list):
    print("authenticatePrompt")
    displayMessages(message_list)
    choice = input("Enter your choice: ")
    return choice


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


def decryptPrompt(message_list):
    print("in decryptPrompt")
    displayMessages(message_list)
    choice = input("Enter your choice: ")
    return choice


def signMessagePrompt():
    print("signMessagePrompt")
    message = input("Enter a message:  ")
    print("Message signed and sent.")
    return message


def showKeysPrompt():
    print("showKeysPrompt")


def generatePrompt():
    print("New Keys Generated\n")


def availableMessagePrompt():
    print("availableMessagePrompt")
    choice = input("Enter your choice: ")
    return choice


def displayMessages(message_list):
    i = 1
    for item in message_list:
        print("\t", i, ". (length = ", len(item), ")")
        i += 1
