# crypto/aptenodytes-forsteri

## Description
Here's a warmup cryptography challenge. Reverse the script, decrypt the output, submit the flag.
### Attachments
```python
flag = open('flag.txt','r').read() #open the flag
assert flag[0:5]=="flag{" and flag[-1]=="}" #flag follows standard flag format
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = ""
for character in flag[5:-1]:
    encoded+=letters[(letters.index(character)+18)%26] #encode each character
print(encoded)
```
output: `IOWJLQMAGH`

## Solution

18 is being added and mod with 26. So after 26 it again starts from 1. 

So since they adding 18 for encrypting, for decrypting just do -18 i.e 18%26 = 8

So by doing ROT8 we get the flag.

Flag:- ``flag{QWERTYUIOP}``
