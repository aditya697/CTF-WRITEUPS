def get_waste(l, w, a):
    if (l, w) in result:
        return result[(l,w)]
    minimum = l*w
    for cake in a:
        x = cake[0]
        y = cake[1]
        if (x <= l and y <= w):
            minimum = min(minimum, (get_waste(l-x, w, a) + get_waste(x, w-y, a)))
            minimum = min(minimum, (get_waste(l, w-y, a) + get_waste(l-x, y, a)))
    result[(l,w)] = minimum
    return minimum

    
l, w, n = map(int, input().split())

lst = []

for i in range(n):
    dim = []
    x, y = map(int, input().split())
    dim.append(x)
    dim.append(y)
    lst.append(dim)

result = {}
print(get_waste(l,w,lst))

#AUTOMATED CODE FOR THE ABOVE CODE

from pwn import *

p = remote("lunch-with-the-cia.hsc.tf",1337)

result = {}

def get_waste(l, w, a):
    if (l, w) in result:
        return result[(l,w)]
    minimum = l*w
    for cake in a:
        x = cake[0]
        y = cake[1]
        if (x <= l and y <= w):
            minimum = min(minimum, (get_waste(l-x, w, a) + get_waste(x, w-y, a)))
            minimum = min(minimum, (get_waste(l, w-y, a) + get_waste(l-x, y, a)))
    result[(l,w)] = minimum
    return minimum

for i in range(10):
    p.recvuntil("Test case ")
    print(p.recvline())
    l, w, n = map(int, p.recvline().split())
    lst = []
    for _ in range(n):
        lst.append(tuple(map(int, p.recvline().split())))
    result = {}
    print(l, w, lst)
    res = get_waste(l, w, lst)
    print(res)
    p.sendline(str(res))
    print(p.recvline())
print(p.recvline())
