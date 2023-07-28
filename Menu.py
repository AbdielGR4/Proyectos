import random

import Cesar
import OneTimePad
import SubstitutionCipher


def show_options():
    print("\nOption menu:")
    print("1. caesar encryption")
    print("2. Brute force attack on Cesar encryption")
    print("3. One Time Pad")
    print("4. substitution cipher")
    print("5. stream cipher")
    print("0. quit")

def generate_message():
    breaker = True
    while breaker == True:

        message = input("enter a message: \n")
        Choice = input("do you wish to continue? (y/n) ")
        if Choice.lower() == "y":
            breaker = False
        elif Choice.lower() == "n":
            pass
        else:
            print("you choose an incorrect answer:", Choice)

    return message

def generate_message_substitutionCipher():
    breaker = True
    while breaker == True:
        Correct_Message = False
        while Correct_Message == False:
            Submessage = input("enter a message: \n")
            Submessage.lower()
            if Submessage.isalpha():
                Correct_Message = True
            else:
                print("you can only write letters!!!")

        Choice = input("do you wish to continue? (y/n) ")
        if Choice.lower() == "y":
            breaker = False
        elif Choice.lower() == "n":
            pass
        else:
            print("you choose an incorrect answer:", Choice)

    return Submessage

def menu():
    while True:
        show_options()
        opcion = input("\nSelect an option (0-5): ")

        if opcion == '1':
            cntKey=random.randint(1,94)
            message = generate_message()
            Caesarkey = Cesar.generate_key(cntKey)
            CaesarCipher = Cesar.encrypt(Caesarkey, message)
            print("-------------CaesarCipher--------------")
            print(f"\n key: {Caesarkey}")
            print(f"\n message: {message}")
            print(f"\n cipher: {CaesarCipher}")
            print(f"\n jump between letters of: {cntKey}")
            print("---------------------------------------")

        elif opcion == '2':
            dkey = Cesar.get_decryption_key(Caesarkey)
            Cesar.bruteForce(dkey, CaesarCipher)

        elif opcion == '3':
            message = generate_message()
            messageEncoded = message.encode()
            keyOTP= OneTimePad.generate_key_stream(len(messageEncoded))
            CipherOTP= OneTimePad.xor_bytes(keyOTP, messageEncoded)
            print("-------------OneTimePad--------------")
            print(f"\n key: {keyOTP}")
            print(f"\n message: {message}")
            print(f"\n cipher: {CipherOTP}")
            print("-------------------------------------")

        elif opcion == '4':
            Subkey = SubstitutionCipher.generate_key()
            SubMessage = generate_message_substitutionCipher()
            SubtCipher = SubstitutionCipher.encrypt(Subkey, SubMessage)
            print("----------SubstitutionCipher-----------")
            print(f"\n key: {Subkey}")
            print(f"\n message: {SubMessage}")
            print(f"\n cipher: {SubtCipher}")
            print("--------------------------------------")

        elif opcion == '5':
            print()

        elif opcion == '0':
            print("Come back soon.")
            break
        else:
            print("Invalid option. Please select a valid option (0-5).")
menu()

