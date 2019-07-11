from random import choice
from subprocess import run
from time import sleep

def pickKey() -> str:
    key: str = "3"

    for c in range(3):
        key += choice("ABCDEFGHIJKLMNOPQRSTUVXYWZabcdefghijklmnopqrstuvxywz0123456789")
    return key

def menu():
    print("===========================================================================================================")
    print("Usage: ./adventure2 key")
    print("The sequence for solving the first puzzle are the letters:")
    print("Hit enter")
    print("H\ne\nl\nl\no")
    print("Hit enter until it goes to the step2")
    print("The argument is opcional, just press enter")
    print("The result of the math problem is 66, so your input must be 66, after just hit enter until the problem ends")
    print("===========================================================================================================")

menu()

payload: str = ""
key: str = pickKey()
print("Key:", key)

op: int = int(input("Hit 1, if you want to execute de program, with the key: "))

if op == 1:
    payload += key
    print('Remember the steps and have fun ...')
    sleep(3)
    run(["./adventure2", payload])
else:
    print("Your key:", key)
