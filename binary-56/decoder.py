passwd = "+HCU"
const, const2 = 0x811c9dc5, 0x1000193

for char in passwd:
    const *= const2
    const ^= ord(char)

print(hex(const & 0xffffffff))
