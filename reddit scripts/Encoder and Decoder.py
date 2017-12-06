"""
Encoder/decoder reddit
"""


def encode():
    message = raw_input("Enter message that will be encoded: ")
    shift = raw_input("Shift by a number between 1 and 10: ")
    if int(shift) > 10 or int(shift) < 1:
        print "!WARNING: shift number must be between 1 and 10"
        shift = raw_input("Shift by a number between 1 and 10: ")
    i = 0
    encoded = [None] * len(message)
    str1 = list(message)
    while i < len(str1):
        encoded[i] = chr(ord(str1[i]) + int(shift))
        i += 1
    print "".join(encoded)


def decode():
    encoded_message = raw_input("Enter message that will be encoded: ")
    shifter = raw_input("Enter shifter to decode the message ")
    i = 0
    decoded = [None] * len(encoded_message)
    str1 = list(encoded_message)
    while i < len(str1):
        decoded[i] = chr(ord(str1[i]) - int(shifter))
        i += 1
    print "".join(decoded)


def menu():
    meniu = 1
    while meniu:
        print "### MENU ###"
        print "1. Encode message"
        print "2. Decode message"
        print "3. Exit"
        choose = raw_input("Enter a number corresponding: ")
        if choose == "1":
            encode()
            print "\n"
        elif choose == "2":
            decode()
            print "\n"
        elif choose == "3":
            return
        else:
            print "Invalid option"
            print "\n"


menu()
