from pwn import *
fib = [0,1]
for i in range(1001):
    fib.append((fib[-1]+fib[-2]))
sec = [0]
for i in range(1,len(fib)):
    sec.append(int((str(sec[i-1])+str(fib[i]))[-11:]))

p = remote("extended-fibonacci-sequence.hsc.tf", 1337)
p.recvline()

while True:
    x = p.recvline()
    x = x.strip(b'\n')
    print(x)
    print(p.recvuntil(": "))
    n = 0
    for i in x:
        # print(n)
        n = n * 10
        n = n + (i-48)
    sum = 0
    for i in range(n+1):
        sum += sec[i]
    print(n)    
    print(str(sum)[-11:])
    p.sendline(str(int(str(sum)[-11:])))
