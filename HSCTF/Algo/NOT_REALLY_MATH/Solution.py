from pwn import *

p = remote("not-really-math.hsc.tf",1337)

def solve(k):
    add = k.replace('a','+')
    result = add.replace('m',')*(')
    final = eval('(' + result + ')') % ((2**32)-1)
    return final

p.recvline()

for i in range(20):
    x = p.recvline().decode()
    print(x)
    print(p.recvuntil(': ' ))
    answer = solve(x)
    print(answer)
    p.sendline(str(answer))
