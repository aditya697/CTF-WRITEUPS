import pwn

host = "hopscotch.hsc.tf"
port = 1337

s = pwn.remote(host, port)

s.recvuntil(b"==\n")
msg = s.recvline().decode().strip()
while msg:
    n = int(msg)
    F = [1, 2]
    for i in range(2, n):
        F.append(F[i - 1] + F[i - 2])
    
    s.recvuntil(": ")
    s.sendline(str(F[n -1] % 10000))
    msg = s.recvline().decode().strip()
    print(msg)
