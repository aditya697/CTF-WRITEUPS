# opisthocomus-hoazin

We are given an switch has some values.

And look at that code we can see that every character of flag is being iterated through the and xored with e i.e 65537.

So if we xor the values given to us and convert we will get the flag.

Since xor has property if `a ^ b = c` then `b ^ c = a` and also `c ^ a = b`

Using this property we can write a code. ![code_here](Solution.py)

Flag:- ``flag{tH1s_ic3_cr34m_i5_So_FroZ3n_i"M_pr3tTy_Sure_iT's_4ctua1ly_b3nDinG_mY_5p0On}``
