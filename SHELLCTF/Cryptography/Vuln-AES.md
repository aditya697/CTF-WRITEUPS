# Vuln_AES

we are given a port and a program.

The from the program we can know that it is ``AES no padding`` and the key ``b'sixteen byte key``.

When we run the and just click enter we get a value that is the encoded string.

![image](https://user-images.githubusercontent.com/73250884/120999093-5a650300-c7a6-11eb-9afe-ddd6c68442b8.png)

```
import base64 as b
from Crypto.Cipher import AES

def decrypt(key,plain):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(plain)

key = b'sixteen byte key'
encoded = "xX+NDjg0X9tmJLobdQv9kzzf4zva3CporIGB5RbbOOg="
decrypted = decrypt(key,b.b64decode(encoded))
print (decrypted.decode())
```

Now using this program we can get the flag.

Flag: ``shell{kinda_sus}``
