## ***A SIMPLE SP BOX***

```py
from pwn import *
from string import ascii_letters, digits
from math import ceil, log

ALPHABET = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"
s_box = {}
flag_length = 42
rounds = int(2 * ceil(log(flag_length, 2)))
p = remote('dctf1-chall-sp-box.westeurope.azurecontainer.io', 8888)
p.recvline()
ct = p.recvline().strip().decode()
info(ct)

for i in range(len(ALPHABET)):
    p.sendlineafter('> ', ALPHABET[i] * flag_length)
    p.recvline()
    s_box[p.recvline().decode()[0]] = ALPHABET[i]
print(s_box)
flag = ''
for c in ct:
    flag += s_box[c]
info(flag)
def un_shuffle(message):
    global flag_length
    result = [''] * flag_length
    first = message[:flag_length//2]
    second = message[flag_length//2:]
    i = 0
    f = 0
    s = 0
    while i < flag_length:
        if i % 2 == 1:
            result[i] = first[f]
            f += 1
        else:
            result[i] = second[s]
            s += 1
        i += 1
    return ''.join(result)

for _ in range(rounds - 1):
    flag = un_shuffle(flag)

success(flag)
p.sendline(flag)
p.interactive()
```
Flag : ***```dctf{S0_y0u_f0und_th3_cycl3s_in_th3_s_b0x}```***
