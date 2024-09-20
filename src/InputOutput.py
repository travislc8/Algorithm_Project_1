import src.RSA as rsa
import src.Signature as sig


def publicLoop(public_key, n, message_list, signature_list):
    while (1):
        choice = publicUserPrompt()
        if (choice == "1"):
            encrypted_message = sendMessagePrompt(public_key, n)
            message_list.append(encrypted_message)
        elif (choice == "2"):
            authenticatePrompt(signature_list, public_key, n)
        elif (choice == "3"):
            print("\n\n")
            break
        else:
            print("Invalid Choice\n\n")
    return public_key, list


def privateLoop(private_key, public_key, n, message_list, signature_list):
    while (1):
        choice = privateUserPrompt()

        if (choice == "1"):
            decryptPrompt(message_list, private_key, n)
        elif (choice == "2"):
            encrypted_message, signature = sendSignaturePrompt(private_key, n)
            signature_list.append(encrypted_message)
            signature_list.append(signature)
        elif (choice == "3"):
            showKeysPrompt(private_key, public_key)
        elif (choice == "4"):
            generatePrompt()
        elif (choice == "5"):
            print("\n\n")
            break
        else:
            print("\n\n")
            print("Invalid Choice")


def getUserType():
    print("Please select your user type:")
    print("\t1. A Public user")
    print("\t2. The owner of the keys")
    print("\t3. Exit program")
    choice = input("Enter your choice: ")
    return choice


def publicUserPrompt():
    print("\nAs a public user, what would you like to do?")
    print("\t1. Send an encrypted message")
    print("\t2. Authenticate a digital signature")
    print("\t3. Exit")
    print()
    choice = input("Enter your choice: ")
    return choice


def sendSignaturePrompt(key, n):
    message = input("\tEnter a message: ")
    encrypted_message, signature = sig.signMessage(message, key, n)
    print("\n\n")
    return encrypted_message, signature


def sendMessagePrompt(key, n):
    message = input("\tEnter a message: ")
    encrypted_message = rsa.encryptMessage(message, key, n)
    print("\n\n")
    return encrypted_message


def authenticatePrompt(signature_list, public_key, n):
    print("\n\n")
    print("The following messages are available: ")

    # if there are no messages
    if (len(signature_list) <= 0):
        print("No messages to authenticate")
        print("\n\n")
        return

    i = 0
    count = 1
    while i < len(signature_list):
        if i % 2 == 1:
            print("\t", count, " = ", signature_list[i])
            count += 1
        i += 1

    while (1):
        choice = int(input("Enter your choice: "))
        if (choice > (len(signature_list)/2) or choice < 1):
            print("Invalid choice")
            continue

        choice = (choice - 1) * 2

        check = sig.verifySignature(
            signature_list[choice], signature_list[choice + 1], public_key, n)
        if (check):
            print("Signature is valid")
        else:
            print("Signature is not valid")
        break


def privateUserPrompt():
    print("\nAs a private user, what would you like to do?")
    print("\t1. Decrypt a received message")
    print("\t2. Digitally sign a message")
    print("\t3. Show the keys")
    print("\t4. Generate a new set of keys")
    print("\t5. Exit")
    print()
    choice = input("Enter your choice: ")
    return choice


def decryptPrompt(message_list, private_key, n):
    print("The following messages are available to decrypt: ")

    # if there are no messages
    if (len(message_list) <= 0):
        print("No messages to authenticate")
        return

    displayMessages(message_list)
    while (1):
        choice = int(input("Enter your choice: "))
        if (len(message_list) < choice or choice < 1):
            print("Invalid choice")
            continue
        choice -= 1

        message = rsa.decryptMessage(message_list[choice], private_key, n)
        print("Decrypted Message: ", message)
        break
    return


# TODO
def signMessagePrompt():
    message = input("\tEnter a message:  ")
    print("Message signed and sent.")
    print("NOT IMPLEMENTED")
    return message


def showKeysPrompt(private_key, public_key):
    print("\n\nThe private key is: ", private_key,
          " The public key is: ", public_key)
    print("\n\n")


def generatePrompt():
    print("\n\n")
    private_key, public_key, n = rsa.generateKeys()
    print("\n\n")


def availableMessagePrompt():
    print("availableMessagePrompt")
    choice = input("Enter your choice: ")
    return choice


def displayMessages(message_list):
    i = 1
    for item in message_list:
        print("\t", i, ". (length = ", len(item), ")")
        i += 1
