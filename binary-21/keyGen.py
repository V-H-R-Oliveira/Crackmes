#!/usr/bin/python3

def genKey(username: str) -> str:
    offset: int = 0x5
    key: str = ""

    for char in username:
        key += chr(ord(char) | offset)
        offset = int(hex(ord(char)), 16)

    return key

print("Welcome to my keygen")
print("Please enter an username length between 3 and 14")

key: str = ""
username = input("Enter an username: ")
user_length = len(username)

if user_length >= 3 and user_length <= 14:
    key:str = genKey(username)
    print("Username: {}\nKey: {}".format(username, key))
