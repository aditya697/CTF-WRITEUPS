# EASY RSA

We are given 

```
n = 1763350599372172240188600248087473321738860115540927328389207609428163138985769311

e = 65537

c = 33475248111421194902497742876885935310304862428980875522333303840565113662943528
```

First we have find p,q using n. ``n = pq``

We can use factordb http://factordb.com/ or https://www.alpertron.com.ar/ECM.HTM to find factors for n.

Then using this we get the flag.

```py
from Crypto.Util.number import inverse

n = 1763350599372172240188600248087473321738860115540927328389207609428163138985769311
e = 65537
c = 33475248111421194902497742876885935310304862428980875522333303840565113662943528
p = 31415926535897932384626433832795028841
q = 56129192858827520816193436882886842322337671

ph = (p-1)* (q-1)
d = inverse(e,ph)
flag_hex = hex(pow( c, d, n))[2:]
print(bytes.fromhex(flag_hex))
#b'shell{switchin_to_asymmetric}'
```

Flag: ``shell{switchin_to_asymmetric}``