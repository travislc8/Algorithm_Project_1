import src.RSA as rsa
import src.Signature as sig


# function for public user loop
def publicLoop(public_key, n, message_list, signature_list):
    # loops until the user specifies to exit
    while (1):
        # calls function to prompt the user for input and returns the input
        choice = publicUserPrompt()

        # if user specifies to send a message
        if (choice == "1"):
            encrypted_message = sendMessagePrompt(public_key, n)
            message_list.append(encrypted_message)
        # if the user specifies to authenticate a signature
        elif (choice == "2"):
            authenticatePrompt(signature_list, public_key, n)
        # if the user specifies to exit the public loop
        elif (choice == "3"):
            print("\n\n")
            break
        # if the user does not enter a valid choice
        else:
            print("Invalid Choice\n\n")
    return public_key, list


# function for the private user/owner of the keys
def privateLoop(private_key, public_key, n, message_list, signature_list):
    # loops until the user specifies to exit
    while (1):
        # calls the function to prompt the user for input and returns the input
        choice = privateUserPrompt()

        # if the user specifies to decrypt a message
        if (choice == "1"):
            decryptPrompt(message_list, private_key, n)
        # if the user specifies to send a signature
        elif (choice == "2"):
            encrypted_message, signature = sendSignaturePrompt(private_key, n)
            signature_list.append(encrypted_message)
            signature_list.append(signature)
        # if the user specifies to show the keys
        elif (choice == "3"):
            showKeysPrompt(private_key, public_key)
        # if the user specifies to generate new keys
        elif (choice == "4"):
            # generates new keys
            private_key, public_key, n = generatePrompt()

        # if the user specifies to end the private loop
        elif (choice == "5"):
            print("\n\n")
            return private_key, public_key, n

        # if the user enters an invalid choice
        else:
            print("\n\n")
            print("Invalid Choice")


# prompts for input for user type
# returns: choice
def getUserType():
    print("Please select your user type:")
    print("\t1. A Public user")
    print("\t2. The owner of the keys")
    print("\t3. Exit program")
    choice = input("Enter your choice: ")
    return choice


# prompt for public user to choose what the user wants to do
def publicUserPrompt():
    print("\nAs a public user, what would you like to do?")
    print("\t1. Send an encrypted message")
    print("\t2. Authenticate a digital signature")
    print("\t3. Exit")
    print()
    choice = input("Enter your choice: ")
    return choice


# gets user input for a signature, then encrypts
# returns: encrypted signature and plain text signature
def sendSignaturePrompt(key, n):
    message = input("\tEnter a message: ")
    # calls the function that encrypts the signature
    encrypted_message, signature = sig.signMessage(message, key, n)
    print("\n\n")
    return encrypted_message, signature


# gets user input for a message
# returns: encrypted message
def sendMessagePrompt(key, n):
    message = input("\tEnter a message: ")
    encrypted_message = rsa.encryptMessage(message, key, n)
    print("\n\n")
    return encrypted_message


# gets the user input for which signature to authenticate
# then displays whether the signature is authentice
def authenticatePrompt(signature_list, public_key, n):
    print("\n\n")
    print("The following messages are available: ")

    # if there are no messages
    if (len(signature_list) <= 0):
        print("No messages to authenticate")
        print("\n\n")
        return

    # loops through the available signatures and displays the plain text
    i = 0
    count = 1
    while i < len(signature_list):
        # displays only the odd items in the list, those are the plain text
        if i % 2 == 1:
            print("\t", count, " = ", signature_list[i])
            count += 1
        i += 1

    # gets user input for which signature to authenticate
    # loops until the input is valid
    while (1):
        choice = int(input("Enter your choice: "))
        if (choice > (len(signature_list)/2) or choice < 1):
            print("Invalid choice")
            continue

        # adjust the choice to be zero indexed
        # multiplied by 2 because the list contains both the plain text and encripted text
        choice = (choice - 1) * 2

        # calls function to verify the signature
        check = sig.verifySignature(
            signature_list[choice], signature_list[choice + 1], public_key, n)

        # displays if the signature is valid
        if (check):
            print("Signature is valid")
        else:
            print("Signature is not valid")
        break


# prompt for private user to choose what they want to do
# returns the choice
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


# prompts the user for which message they want to decrypt
# then displays the decrypted message
def decryptPrompt(message_list, private_key, n):
    print("The following messages are available to decrypt: ")

    # if there are no messages
    if (len(message_list) <= 0):
        print("No messages to authenticate")
        return

    # calls function to display the messages in the list
    displayMessages(message_list)

    # loops until the user enters a valid choice
    while (1):
        choice = int(input("Enter your choice: "))
        if (len(message_list) < choice or choice < 1):
            print("Invalid choice")
            continue
        break

    # decriments the choice for 0 indexing
    choice -= 1
    # calls the function to decrypt the message
    message = rsa.decryptMessage(message_list[choice], private_key, n)
    print("Decrypted Message: ", message)
    return


# function to display the private and public keys
def showKeysPrompt(private_key, public_key):
    print("\n\nThe private key is: ", private_key,
          " The public key is: ", public_key)
    print("\n\n")


# function to generate new keys
# returns the new keys
def generatePrompt():
    print("\n\n")
    # calls function to generate new keys
    private_key, public_key, n = rsa.generateKeys()
    print("new keys generated")
    return private_key, public_key, n


# displays the messages in a list
def displayMessages(message_list):
    i = 1
    for item in message_list:
        print("\t", i, ". (length = ", len(item), ")")
        i += 1
