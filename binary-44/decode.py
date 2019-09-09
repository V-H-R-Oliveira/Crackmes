#!/usr/bin/python

def menu():
    print "[+] My flag decrypt script!!!"
    print "[+] Developed by Binary Newbie"

menu()

encrypted_flag = bytearray([0x16, 0x1, 0x33, 0x47,0x69, 0x7,
0x7a ,0x6d ,0x6e ,0x23, 0x60, 0x63, 0x75, 0x74, 0x42
,0x63 ,0x31 ,0x41 ,0x72, 0x60, 0x3, 0x25, 0x31, 0x4, 0x72])

flag_length = 0x19
decrypted_flag = ""

for i in xrange(flag_length):
    op = encrypted_flag[i] - 1
    op2 = encrypted_flag[i % 3] - 1
    decrypted_flag += chr(op ^ op2)

print "[+] The decrypted_flag is: %s" % decrypted_flag
