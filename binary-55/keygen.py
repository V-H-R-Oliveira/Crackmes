import sys

username = input("Enter your username: ")
charset = [0x53, 0x65, 0x52, 0x69, 0x41, 0x6C, 0x41, 0x62, 0x43, 0x64,
           0x45, 0x66, 0x47, 0x68, 0x49, 0x6A, 0x4B, 0x6C, 0x4D, 0x6E,
           0x4F, 0x70, 0x51, 0x72, 0x53, 0x74, 0x55, 0x76, 0x57, 0x78, 0x59, 0x7A]

if len(username) < 5:
    print("[-] Username length must be greater or equal than 5")
    sys.exit(1)

j = 0
serial = ""

for i in range(len(charset)-1, -1, -1):
    serial += chr(ord(username[j % len(username)]) ^ charset[i])
    j += 1

serial = serial[::-1]

with open("/var/tmp/thegame.serial", "w") as f:
    f.write(serial)
    
print("[+] Run the executable with the inputed username")
