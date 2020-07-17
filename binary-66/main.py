import string

freq = "01234567890123456789012345"
charset = string.ascii_lowercase # could be upper case as well
final = ""

for i, ch in enumerate(freq):
    final += int(ch) * charset[i]

with open("keyfile", "w") as f:
    f.write(final)

print("[+] Keyfile created")
