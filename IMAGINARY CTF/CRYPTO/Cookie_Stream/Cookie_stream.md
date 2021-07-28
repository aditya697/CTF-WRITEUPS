# Cookie Stream

We are given a login page which says we have to enter username and password.

We are given its source as a `.py` file.

Soo lokking at source i could figure out the username and password for the website.

```
Username :- firepwny
Password :- pwned
```

After we login we will have rick rolled vedio.

As we look into the source there is some AES CTR encryption happening to the cookie.

Because of that some bits are being flipped in the cookie.

This is the reason why the website shows ``Only the admin user can view the flag.`` even if we login.

![image](https://user-images.githubusercontent.com/73250884/127356950-cc08d396-83d5-4455-95f5-bf1f86a72a3e.png)

`f89173d7dea12f54a777acb58b3bc3a90d791407c64d1f1e`

With this code we can flip the bits of the cookie correctly and get access.

```py
from pwn import *
from Crypto.Util.Padding import pad, unpad

ct = unhex(input("enter the cookie:"))
iv, ct = ct[:8], ct[8:]

pt = pad(b'firepwny', 16)
need = pad(b'admin', 16)
new = xor(pt, need, ct)

print(enhex(iv + new))
```

If we give the cookie to this program it will give us an output.

![image](https://user-images.githubusercontent.com/73250884/127358142-940cfbdd-e558-42b3-baf9-fd1bb466559d.png)

`f89173d7dea12f54a07ab3b99547a6db0e7a1704c54e1c1d`

Now change this to the cookie on the web page and reload.

![image](https://user-images.githubusercontent.com/73250884/127358687-6339a23c-b547-4e85-bb34-0006356bd18f.png)

Flag:- ``ictf{d0nt_r3us3_k3ystr34ms_b72bfd21}``
