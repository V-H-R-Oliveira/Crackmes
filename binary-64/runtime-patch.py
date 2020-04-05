import os
import r2pipe
import sys

# Install it by typing: pip3 install r2pipe

def keygen(username: str) -> int:
    return sum(list(map(ord, username)))

def auto_step():
    r2.cmd("ds")
    r2.cmd("sr eip")

def modify_input_file(username: str, serial: int):
    path: str = os.getcwd() + "/input.txt"
    content: str = username + '\n' + str(serial) + '\n'

    with open(path, "w") as f:
        f.write(content)

    print("[LOG] Input.txt was modified...")

def preparements() -> tuple:
    print ("===================================")
    print ("Runtime Patch by Binary Newbie !!!!")
    print ("===================================")

    username: str = input("Enter your username: ")

    if len(username) < 1:
        print ("Username length is invalid...", file=sys.stderr)
        sys.exit(1)

    try:
        serial: int = int(input("Enter a serial number: "))

        if len(str(serial)) < 1:
            print ("Serial length is invalid...", file=sys.stderr)
            sys.exit(1)

        modify_input_file(username, serial)
        return username, serial
    except ValueError:
        print ("Serial must be a number...", file=sys.stderr)
        sys.exit(1)

username, serial = preparements()
path: str = os.getcwd() + "/drscm1"

r2 = r2pipe.open(path)
r2.cmd("e dbg.profile=drscm1.rr2")
r2.cmd("doo")
r2.cmd("db 0x80486d5")
r2.cmd("dc")

patch: str = input("Do you want to patch? (s/n): ").lower()

if patch == 's':
    new_serial: int = keygen(username)
    print ("[LOG] Your serial ({}) was patched in runtime by the correct one ({})".format(serial, new_serial))
    print ("[LOG - Before patching] Current eax value:", r2.cmdj("drj")["eax"])
    r2.cmd("dr eax={}".format(new_serial))
    print ("[LOG - After patching] Current eax value:", r2.cmdj("drj")["eax"])

r2.cmd("db 0x08048788")
r2.cmd("dc")

auto_step()

strings: list = list(filter(lambda i: i != '', r2.cmdj("psj @0x80488e0")["string"].split('\x00')))

while True:
    current_eip: str = hex(r2.cmdj("drj")["eip"])
    offset: str = current_eip[len(current_eip)-2:]

    if offset == "c1":
        correct_serial: int = r2.cmdj("drj")["ecx"]
        print ("The correct key for the pair {}:{} is: {}".format(username, serial, correct_serial))
    elif offset == "ca":
        print (strings[0] % username)
        print (strings[1])
        r2.cmd("dc")
        break
    elif offset == "d3":
        print (strings[2][:len(strings[2]) - 1] % username)
        r2.cmd("dc")
        break
    auto_step()
r2.quit()
