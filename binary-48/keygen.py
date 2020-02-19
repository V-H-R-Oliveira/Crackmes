import sys
import string
import random

def convert_to_hex(serial, const):
    rep = "0x"
    tmp = 0
    
    for char in serial:
        if ord(char) < 0x41:
            tmp = ord(char) - 0x30
        else:
            tmp = (ord(char) - 0x57) & 0xff
            const = const - 0xf - 1
            tmp = tmp + (const & 0xff) & 0xff
        tmp &= 0xf
        rep += format(tmp, 'x')
    return int(rep, 16)
        
def extract_checksum(ebx, esi, ecx):
    edi, eax = 1, 1
    while ecx > 0:
        if (ecx & 1) != 0:
            eax = edi
            eax *= ebx
            edi = eax % esi
        ecx >>= 1
        ebx **= 2
        ebx %= esi
    return edi 

def float_op(checksum, const, const1):
    checksum = float(checksum)
    const = float(const)
    checksum *= const
    const1 = float(const1)
    const1, checksum = checksum, const1
    return int(int(const1) % int(checksum))

def pick_str():
    candidate = ""
    charset = string.hexdigits
    
    for i in range(9):
        if i == 4:
            candidate += '-'
        else:
            candidate += random.choice(charset)
    return candidate

def keygen():
    username = input("Enter an username, with a length >= 5: ")
   
    if len(username) < 5:
        print("[-] Username length must be great or equal than 5")
        sys.exit(1)
        
    while True:
        const = 0x7e4c9e32
        const1 = 0xf2a7
        const2 = 0xf2a5
        const3 = 0x3ca9d
        const4 = 0x15346
        const5 = 0x307c7
        
        serial = pick_str()    
        
        for char in username:
            const *= ord(char)

        const &= 0xffffffff 
        first_half_hex = convert_to_hex(serial[:4], const) 
        second_half_hex = convert_to_hex(serial[5:], const) 
        
        checksum2 = extract_checksum(second_half_hex, const1, const2)
        val = float_op(checksum2, const, const1)
        val2 = float_op(first_half_hex, checksum2, const1)
        checksum3 = extract_checksum(const4, const3, val)
        checksum4 = extract_checksum(const5, const3, val2)
        val3 = float_op(checksum4, checksum3, const3)
        
        if (val3 % const1) == first_half_hex:
            print("success", username, serial)
            sys.exit(0)

if __name__ == "__main__":
    keygen()