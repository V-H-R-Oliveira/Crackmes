from random import choice
from subprocess import run
from time import sleep

def pickKey(tam: int) -> str:
    key: str = "aatt"

    for x in range(tam):
        key += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    return key

def menu():
    print("================================================================")
    print("The first fgets is the only that's matter, and you must type aa")
    print("And hit enter for the rest of the program...")
    print("================================================================")

menu()

print("Key length constraint:  4 < tam <= 122")
keyLength = int(input("Enter the length of the key: "))
key: str = ""

if keyLength < 5 and key > 122:
    print("Invalid length")
else:
    key = pickKey(keyLength)

    print("Key:", key)

    op: int = int(input("Do you want to run your program with the key?, press 1 to confirm: "))

    if op == 1:
        print("Don't forget to enter aa")
        sleep(3)
        run(["./adventure3", key])
