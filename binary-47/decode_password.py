i, aux, tmp = 0, 0, ""

def magic(cipher_text):
    global i
    global aux
    global tmp

    if len(cipher_text) != 0:
        aux = 0x7b1
        tmp = cipher_text

    if tmp[i] == 0x0:
        magic = 0
    else:
        offset = (aux * 7 >> 0x1f) >> 0x10
        aux = (aux * 7 + offset & 0xffff) - offset
        magic = ord(tmp[i]) + ((aux // 10) * 10 - aux)
        i += 1

    return magic

cipher_password = "fhz4yhx|~g=5"
password = chr(magic(cipher_password))

while i < len(tmp):
    password += (chr(magic('')))

print("Password:", password)
