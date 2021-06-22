# regulus-regulus

find p and q using rsatool.

i got p,q now after deep analysis i came to know that d in AP with a common difference of ``phi/2(there phi=(p-1)*(q-1))``.

I tried it initially for small numbers understood the common difference in phi/2).

```py
p = num1
q = num2
phi = (p-1) * (q-1)
d = inverse(65537,phi)
print(d+(phi//2))
```
from here i put that printed character as `d_`

Flag:- ``flag: flag{r3gulus_regu1us_regUlus_regulu5_regUlus_Regulus_reguLus_regulns_reGulus_r3gulus_regu|us}(edited)``
