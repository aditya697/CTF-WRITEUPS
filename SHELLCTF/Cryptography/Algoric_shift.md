# Algoric-Shift

In this challenge we were given an encrypted flag:
```
HESL{LRAT5PN51010T_CNPH1R}3
```

And a python script that includes the encryption algorithm:
```py
text = 'HESL{LRAT5PN51010T_CNPH1R}3'

key = [3,1,2]

li0 = []
li1 = []
li2 = []
for i in range(0,len(text)):
    if i % 3 == 0:
        li0.append(text[i])
    elif (i - 1) % 3 == 0:
        li1.append(text[i])
    elif (i - 2) % 3 == 0:
        li2.append(text[i])
li = []
for i in range(len(li1)): 
    li.append(li1[i]) 
    li.append(li2[i])
    li.append(li0[i])

# print(li)
print("The ciphered text is :")
ciphered_txt = (''.join(li))
print(ciphered_txt)
```
If we run the program we get ``ESH{LLATRPN51050T1CN_H1P}3R``

With that output if we run the program again we get the flag.
```py
text = 'ESH{LLATRPN51050T1CN_H1P}3R'

key = [3,1,2]

li0 = []
li1 = []
li2 = []
for i in range(0,len(text)):
    if i % 3 == 0:
        li0.append(text[i])
    elif (i - 1) % 3 == 0:
        li1.append(text[i])
    elif (i - 2) % 3 == 0:
        li2.append(text[i])
li = []
for i in range(len(li1)): 
    li.append(li1[i]) 
    li.append(li2[i])
    li.append(li0[i])

# print(li)
print("The ciphered text is :")
ciphered_txt = (''.join(li))
print(ciphered_txt)
```

We get the by running this.

Flag: ``SHELL{TRAN5P051T10N_C1PH3R}``
