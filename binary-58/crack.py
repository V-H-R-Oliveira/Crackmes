import sys
import string
import random

def multiply_chars(key):
    mul = 1
    calc = 0
    for char in key:
        calc += ord(char) * mul
        mul = ord(char)
    return calc

def pick_str(calc1, username):
    charset = string.ascii_uppercase
    const_calc1 = 0x255a8 - ord(username[0]) * calc1

    while True:
        key = ""
        for i in range(25):
            key += random.choice(charset)

        calc2 = multiply_chars(key)

        if calc2 == const_calc1:
            print("Bypassed with", key)
            pow1 = pow(ord(key[19]), ord(key[1]))
            pow2 = pow(ord(key[0]), ord(key[2]))

            if ((pow1 - pow2 < 0) and (0 < ord(key[0]) - ord(key[19])) and (ord(key[12]) + ord(key[7]) < 0x8c)) and ((ord(key[10]) * ord(key[8]) <= ord(key[16]) * ord(key[4]))):
                print("Username: {}\nkey: {}".format(username, key))
                break

username = input("Enter your username: ")
username_length = len(username)

if len(username) < 4:
    print("Invalid length, must be >= 4", file=sys.stderr)
    sys.exit(1)

c = ord(username[2])
c2 = ord(username[len(username)-1])
c3 = ord(username[1])
calc = 0

if c > c2:
    calc = c3 + ((c // username_length) - c2)
else:
    if c2 > c:
        calc = c3 + ((c2 // username_length) - c)
    else:
        calc = c3 + username_length

pick_str(calc, username)
