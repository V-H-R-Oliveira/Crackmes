#!/usr/bin/python3

import string
import random
import subprocess

def pickKey():
    array = []
    charset = string.ascii_uppercase + string.digits
    n1, n2 = 0, 0

    while True:
        for item in range(10):
            array.append(ord(random.choice(charset)))

        n = array[0]
        n2 = array[9]

        print("Original array:", array)

        if n != (n2 - 3):
            while n != (n2 - 3):
                n = ord(random.choice(charset))
                n2 = ord(random.choice(charset))
            array.insert(0, n)
            array.insert(9, n2)
            del array[10]
            del array[10]

        n = array[1]
        n2 = array[8]

        if n != (n2 + 14):
            while n != (n2 + 14):
                n = ord(random.choice(charset))
                n2 = ord(random.choice(charset))
            array.insert(1, n)
            del array[2]
            array.insert(8, n2)
            del array[9]

        n = array[2]
        n2 = array[7]

        if n != (n2 - 0x14):
            while n != (n2 - 0x14):
                n = ord(random.choice(charset))
                n2 = ord(random.choice(charset))
            array.insert(2, n)
            del array[3]
            array.insert(7, n2)
            del array[8]

        n = array[3]
        n2 = array[6]

        if n != (n2 + 6):
            while n != (n2 + 6):
                n = ord(random.choice(charset))
                n2 = ord(random.choice(charset))
            array.insert(3, n)
            del array[4]
            array.insert(6, n2)
            del array[7]

        n = array[4]
        n2 = array[5]

        if (n + n2 >> 0x1f) == 0:
            if (n + n2 >> 1) != array[0]:
                while (n + n2 >> 1) != array[0]:
                     n = ord(random.choice(charset))
                     n2 = ord(random.choice(charset))
                array.insert(4, n)
                del array[5]
                array.insert(5, n2)
                del array[6]
        elif ((n + n2 >> 0x1f) >> 0x1f) == 0:
            if (n + n2 >> 1) != array[0]:
                while (n + n2 >> 1) != array[0]:
                    n = ord(random.choice(charset))
                    n2 = ord(random.choice(charset))
                array.insert(4, n)
                del array[5]
                array.insert(5, n2)
                del array[6]
        else:
            soma = (n + n2 >> 0x1f) >> 0x1f
            if (soma + n + n2 >> 1) != array[0]:
                while (n + n2 >> 1) != array[0]:
                    n = ord(random.choice(charset))
                    n2 = ord(random.choice(charset))
                array.insert(4, n)
                del array[5]
                array.insert(5, n2)
                del array[6]

        print("Final array", array)
        return array


print("Welcome to my self-keygen")
print("The code sucks, but the only thing that matter is the fact that it solves the problem :)")
print("Made by Binary Newbie")
print()

bytes_array = pickKey()
key_string = ""

for i in bytes_array:
    key_string += chr(i)

print("Your key:", key_string)
print("Running ....")
subprocess.run(["./crkme1-linux32", key_string])
