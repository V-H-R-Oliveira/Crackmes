#!/usr/bin/python

import os

def xor(char, key):
    return ord(char) ^ key

string = "SvenJoergenIkeaBirdWaterSheepBoatCowPeePeePooPoo"
final_hex, final_plaintext = "", ""
new_key = 0xb
lista = bytearray([])

for x in xrange(len(string)):
    if x == 0:
        new_key = xor(string[x], new_key)
        final_plaintext += chr(new_key)
        final_hex += "\\x" + format(new_key, '02x')
        lista.append(new_key)
    else:
        aux = xor(string[x], new_key)
        final_plaintext += chr(aux)
        final_hex += "\\x" + format(aux, '02x')
        lista.append(aux)
        new_key = aux

file = open(os.getcwd() + '/solution', 'wb')
file.write(lista)
file.close()

print "Developed by Binary Newbie"
print "This program creates a binary file called \"solution\" in your current folder"
print "Execute the crackme program and feed the input with \"solution\""
print "The content of the \"solution\" file:"
print "Escaped hex string:", final_hex
print "Plaintext string:", final_plaintext
