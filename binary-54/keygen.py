import sys
import ctypes

# https://www.aldeid.com/wiki/Category:Encryption/rol-ror
rol = lambda val, r_bits, max_bits=8: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

print "A keygen for \"thething\" crackme developed by Binary Newbie."
print "-----------------------------------------------------------"

username = raw_input("Enter your username: ")

if len(username) < 2:
    print "[-] You should enter an username"
    sys.exit(1)

if len(username) == 2:
    username += ((3 - len(username)) * '\x00' + '\xff')
else:
    username += ((4 - len(username)) * '\x00')
                 
parsed_username = chr(rol(int(username[0].encode("hex"), 16), 0x20))
parsed_username += chr(rol(int(username[1].encode("hex"), 16), 0x10))
parsed_username += chr(rol(int(username[2].encode("hex"), 16), 0x8))
parsed_username += chr(rol(int(username[3].encode("hex"), 16), 0x4))
parsed_username = parsed_username[::-1]
parsed_username = parsed_username.encode("hex")

username = username.replace('\xff', '\x00')
print "[+] Username: %s\n[+] Serial: %d" % (username, ctypes.c_int32(int(parsed_username, 16)).value)
