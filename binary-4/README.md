# Solution for this challange

in gdb

b main
r
flag: could be anything

   0x0000000000400701 <+123>:	mov    rsi,rdx # probably rdx has our flag
   0x0000000000400704 <+126>:	mov    rdi,rax # probably move our entry to rdi
   0x0000000000400707 <+129>:	call   0x400560 <strcmp@plt> 
   0x000000000040070c <+134>:	test   eax,eax # strcmp probably compares rsi with rdi and put the value in eax ???
   0x000000000040070e <+136>:	jne    0x40071c <main+150> 
   0x0000000000400710 <+138>:	mov    edi,0x4007ff # 0x4007ff #copy G00d to edi ands calls puts after
   0x0000000000400715 <+143>:	call   0x400520 <puts@plt>




=> 0x0000000000400704 <+126>:	mov    rdi,rax

x/s $rsi - 0x7fffffffdec0:	"Flag{E4sy_ch4ll}"

./just\ see 
flag Flag{E4sy_ch4ll}
G00d

link for the problem: https://crackmes.one/crackme/5b81014933c5d41f5c6ba944
