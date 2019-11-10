def decode(cipher_buffer):
    decoded = ""
    offset = 0x7b1
    
    if type(cipher_buffer) == bytearray:
        for c in cipher_buffer:
            offset = offset * 7 & 0xffff
            decoded += chr(c + (offset // 10) * 0xa - offset) 
    else:
        for c in cipher_buffer:
            offset = offset * 7 & 0xffff
            decoded += chr(ord(c) + (offset // 10) * 0xa - offset) 
    return decoded

cipher_text = "Gtu.}\'uj{fq!p{$"
cipher_text2 = bytearray([0x4c, 0x73, 0x7a, 0x6c, 0x7b, 0x7b, 
0x25, 0x82, 0x76, 0x78, 0x7b, 0x21, 0x77, 0x68, 0x76, 0x74, 0x7c, 0x74, 0x77, 0x67, 0x3f, 0x25])
cipher_text3 = "Ftyynjy*" 
cipher_text4 = "Zwvup("
cipher_text5 = "fhz4yhx|~g=5"

print(decode(cipher_text), decode(cipher_text2), decode(cipher_text3), decode(cipher_text4), decode(cipher_text5), sep="\n")