# Imaginary

We are given a `.py` file.

So as we see its basic imaginary numbers calculation.

We have to solve 300 imaginary number calculations.

Manually its no possible, we can do using pwntools.

By running the following we can get the flag.

```py
from pwn import *
r = remote("chal.imaginaryctf.org", 42015)
r.recvuntil(" so watch out!)\n")
r.recvuntil("\n")

e=(((r.recvline()).decode("ASCII")).strip("\n"))
print(e)
e=e.replace("i","j")
x = eval(e)
x=(str(x).replace("j","i")).strip("()")
print(x)
r.sendline(str(x))
y=(((r.recvline()).decode("ASCII")).strip("\n"))
while(y=='> Correct!'):
    e=(((r.recvline()).decode("ASCII")).strip("\n"))
    print(e)
    if (e[0]=='_'):
        r.sendline(str("a"))
    elif(e[0:3]=='You'):
        print(r.recvline)
        r.interactive()
    else:
        e=e.replace("i","j")
        x = eval(e+"+0")
        if (x.real==0.0 and x.imag>0):
            x=str('0+')+x
        elif(x.real==0.0 and x.imag<0):
            x=str('0')+x
        x=(str(x).replace("j","i")).strip("()")
        print(x)
        r.sendline(str(x))
    y=(((r.recvline()).decode("ASCII")).strip("\n"))
    print(y)
r.interactive()
```

Flag:- ```ictf{n1c3_y0u_c4n_4dd_4nd_subtr4ct!_49fd21bc}```
