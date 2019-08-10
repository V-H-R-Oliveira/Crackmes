#!/usr/bin/python

user_input = ".-8.4.p"
decrypted = ""

for x in user_input:
    decrypted += chr(ord(x) ^ ord('B'))

print decrypted
