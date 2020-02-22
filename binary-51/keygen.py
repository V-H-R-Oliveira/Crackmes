username = input("Enter your username: ")
s = sum(map(ord, username))
calc = (s + 0x3a2f49 << (ord(username[0]) & 0x1f) ^ 0x1337) & 0xffffffff
serial = "~{}#{}#~".format("1337", calc) 
print("Your serial is:", serial) 