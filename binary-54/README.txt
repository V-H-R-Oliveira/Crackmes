This crackme has the ELF headers corrupted.

To fix it, me and my friend (AnotherN1ck) made a C program that parses the ELF headers and patches the values of 
    - e_shoff to 0x1734,
    - e_shnum to 34, 
    - shdr[31].sh_offset to 0x160a, (first 0 before symtab) 
    - shdr[31].sh_size to 0x126; (0x1730 - 0x160a) (0x1730 is the first 0 after "debug str")

Note: the values was retrieved from hexedit.

After the correction, we get a clean readelf output.

The algoritm:
- It reads the username and the serial from stdin. (Note: the author didn't verify the upper bound limit, so there is a buffer overflow, which can redirect us to any address of the crackme. With that in mind, we made an exploit to redirect us to the good message)
- It will check the serial length, which must be greater or equal than 4.
- After, it will rotate left (rol instruction) the first username byte to 0x20, the second username byte to 0x10, the third to 0x8 and the fourth byte to 0x4.
- Then, it will convert the output value to an int32 value, and it will check if the value matches with the serial.
- If it matches, then it will display the correct message, otherwise it will display the wrong message.

Thanks for the crackme.
Binary Newbie