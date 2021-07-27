from itertools import *
from gmpy2 import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
import random

def x_fixed(a, b):
    l = max(*map(len, [a, b]))
    output = b''
    for i in range(l):
        output += chr(a[i % len(a)] ^ b[i % len(b)]).encode()
    return output

def x(a,b):
    return bytes(islice((x^y for x,y in zip(cycle(a), cycle(b))), max(*map(len, [a, b]))))

def t(x):
    return sum((((x & 28) >> 4) & 1) << i for i, x in enumerate(x))

flag = 2535320453775772016257932121117911974157173123778528757795027065121941155726429313911545470529920091870489045401698656195217643
T = 136085

for _ in range(421337):
    if flag & 2**419 != 0:
        flag_prev = (flag & (2**419 - 1)) << 1
        # last bit can be 0 or 1
        # we need popcount(flag & T) & 1 to equal 1
        
        if popcount(flag_prev & T) & 1 == 0:
            # set last bit to 1 to get odd popcount
            flag = flag_prev | 1
        else:
            flag = flag_prev | 0
    else:
        flag_prev = flag << 1
        # we need popcount(flag & T) & 1 to equal 0
        if popcount(flag_prev & T) & 1 == 1:
            # set last bit to 1 to get even popcount
            flag = flag_prev | 1
        else:
            flag = flag_prev | 0
            
print(long_to_bytes(flag)[::-1])
#ictf{I_did_not_have_linear_relations_with_that_LFSR}
