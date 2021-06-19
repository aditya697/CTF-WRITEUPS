import pwn
host = "extended-fibonacci-sequence-2.hsc.tf"
port = 1337
s = pwn.remote(host, port)
s.recvuntil(b"== proof-of-work: disabled ==\n")
s.recvuntil(b"!\n")
num = s.recvline().decode().strip()
while num:
    n = int(num)
    F = [4,5]
    S = [4]
    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])
    
    for i in range(1, n + 1):
        S.append(S[i - 1] + F[i])
    
    sum = 0
    for i in range(n+1):
        sum += S[i]

    res = str(int(str(sum)[-1:-11:-1][::-1]))    
    s.sendline(res)
    print(s.recvline())
    print(s.recvline())
    print(s.recvline())
    num = s.recvline().decode().strip()
    print(num)
