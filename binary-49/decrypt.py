def method_1(enc_data, key):
    passwd = ""
    for bytee in enc_data:
        passwd += chr(bytee - key)
    return passwd

def method_2(enc_data, key):
    passwd = ""
    for bytee in enc_data:
        passwd += chr(bytee ^ key)
    return passwd

enc_data = [0xf7, 0xf8, 0xf1, 0xf4, 0xf1, 0xf8, 0xb3, 0xfc, 0xfc]
key = 0x90

print("Method 1:", method_1(enc_data, key))
print("Method 2:", method_2(enc_data, key))