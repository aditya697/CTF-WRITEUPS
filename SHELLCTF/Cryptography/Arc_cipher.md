# arc-cipher

In this challenge we were given an encrypted message:

```
a7 f9 de 54 29 92 7f 61 9a 7a 5f f3 f4 1a 88 a1 8f ca 97 47
```

and a python script:
```py
text = "<flag>"
key = "MANGEKYOU"

s = []

k = []

for i in key:
    k.append(((ord(i))))

for i in range(0,256):
    s.append(i) # i.e. s = [0 1 2 3 4 5 6 7 ..]
    if i >= len(key):
        k.append(k[i%len(key)])

def key_sche(s,k):
    j = 0
    for i in range(0,256):
        j = (j + s[i] + k[i])%256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        # print("s in the iteration:",i+1," is :",s)
    return s
def key_stream(text,s):
    ks = []
    i = 0
    j = 0
    status = 1
    while(status == 1):
        i = (i+1) % 256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        t = (s[i]+s[j])%256
        ks.append(s[t])
        if len(ks) == len(text):
            status = 0
    return ks

def encrypt(text,k):
    encrypted_txt = ''
    hex_enc_txt = ''
    for i in range(0,len(text)):
        xored = (ord(text[i])) ^ (k[i])
        encrypted_txt +=  chr(xored)
        hex_enc_txt += hex(xored)[2:] + ' '
    li = list(hex_enc_txt)
    li.pop()
    hex_enc_txt = ''.join(li)
    return encrypted_txt,hex_enc_txt

key_new = key_stream(text,key_sche(s,k))
ciphered_txt,ciphered_hex = encrypt(text,key_new)
print("ciphered hex : ",ciphered_hex)
print("ciphered text : ",ciphered_txt)
```

The given values are being xored with the new key that is generated in the program.

The numbers given to us are 20. So flag length is 20. Therefore in the first line give random a random 20 length string.

We can just put a print statement before key_new and print the key.

```py
text = "aaaaaaaaaaaaaaaaaaaa"
key = "MANGEKYOU"

s = []

k = []

for i in key:
    k.append(((ord(i))))

for i in range(0,256):
    s.append(i) # i.e. s = [0 1 2 3 4 5 6 7 ..]
    if i >= len(key):
        k.append(k[i%len(key)])

def key_sche(s,k):
    j = 0
    for i in range(0,256):
        j = (j + s[i] + k[i])%256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        # print("s in the iteration:",i+1," is :",s)
    return s
def key_stream(text,s):
    ks = []
    i = 0
    j = 0
    status = 1
    while(status == 1):
        i = (i+1) % 256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        t = (s[i]+s[j])%256
        ks.append(s[t])
        if len(ks) == len(text):
            status = 0
    return ks

def encrypt(text,k):
    encrypted_txt = ''
    hex_enc_txt = ''
    for i in range(0,len(text)):
        xored = (ord(text[i])) ^ (k[i])
        encrypted_txt +=  chr(xored)
        hex_enc_txt += hex(xored)[2:] + ' '
    li = list(hex_enc_txt)
    li.pop()
    hex_enc_txt = ''.join(li)
    return encrypted_txt,hex_enc_txt

key_new = key_stream(text,key_sche(s,k))
print(key_new)
```

The key_new is ``[244, 177, 155, 24, 101, 233, 44, 85, 201, 49, 10, 192, 171, 79, 203, 233, 190, 130, 163, 58]``

Convert the given hex values to decimal.

```py
content_list = ['a7','f9','de','54','29','92','7f','61','9a','7a','5f','f3','f4','1a','88','a1','8f','ca','97','47']
hex_list = [int(x,16) for x in content_list]
print(hex_list)
```

```
[167, 249, 222, 84, 41, 146, 127, 97, 154, 122, 95, 243, 244, 26, 136, 161, 143, 202, 151, 71]
```

```py
list1 = [167, 249, 222, 84, 41, 146, 127, 97, 154, 122, 95, 243, 244, 26, 136, 161, 143, 202, 151, 71]   
list2 = [244, 177, 155, 24, 101, 233, 44, 85, 201, 49, 10, 192, 171, 79, 203, 233, 190, 130, 163, 58] 
result = list(a^b for a,b in zip(list1,list2))
print('XOR =',result)
```

We get output as ``XOR = [83, 72, 69, 76, 76, 123, 83, 52, 83, 75, 85, 51, 95, 85, 67, 72, 49, 72, 52, 125]``

Now convert the decimal values to ascii

```py
list1 = [83, 72, 69, 76, 76, 123, 83, 52, 83, 75, 85, 51, 95, 85, 67, 72, 49, 72, 52, 125]
flag = [chr(x) for x in list1]
print(flag)
```

We get output as ``['S', 'H', 'E', 'L', 'L', '{', 'S', '4', 'S', 'K', 'U', '3', '_', 'U', 'C', 'H', '1', 'H', '4', '}']``

Flag: ``SHELL{S4SKU3_UCH1H4}``
