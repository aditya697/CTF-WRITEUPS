# digits-of-pi-2

We are given a Google EXEL doc link.

Tapping on the Show Formula shortcut, we notice that on cell A2, it imports a sheet with the ID `1MD4O3pFoQY59_YoW_ZzxRUg-rBgHFlAaYxnNABmqc3A.` 

Unfortunately we have no access to it and the challenge is unsolvable, or is it?

Checking the network traffic and filtering for `1MD4O3pFoQY59_YoW_ZzxRUg-rBgHFlAaYxnNABmqc3A` in the request body. 

And reading the responses, we found the flag without the usual wrapped brackets!

Flag:- ``flag{m4k3_sur3_t0_r3str1ct_y0ur_imp0rtr4ng3s}``
