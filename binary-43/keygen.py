#!/usr/bin/python3

import string
import random
import sys

def validation(username: int):
    username_calc: int = 0
    serial_calc: int = 0

    for i in range(len(username) - 1 , -1, -1):
        username_calc += (( (i + 1) * (i + 1)) % (( (i + 1) - 2) + ord(username[i])))

    serial_length = int(input("Enter the serial length, that must be divisible by 10: "))

    if serial_length % 10 == 0:
        while True:
            serial = genSerial(serial_length)

            for j in range(len(serial) - 1, -1, -1):
                serial_calc += (ord(serial[j]) % ((j + 1) + 8))

            if serial_calc == username_calc:
                print("A serial was founded for \"{}\":".format(username),  serial)
                sys.exit(0)
            else:
                serial_calc = 0
    else:
        print("Invalid serial length!!!")
        sys.exit(1)

def genSerial(length: int) -> str:
    charset = string.digits + string.ascii_letters
    key = ""

    for i in range(length):
        key += random.choice(charset)
    return key

def menu():
    print("Welcome!!!")
    print("The longer is your username, the longer it will take to get a valid serial, so be careful!!!")
    print("Developed by Binary Newbie")
    print()

if __name__ == "__main__":
    menu()
    username = input("Enter an username: ")

    if username.isalpha():
        validation(username)
    else:
        print("The username must be only alpha characters...")
        sys.exit(1)
