# Flip Flops

We are given a `.py` file.

By looking at the code we can see that we encrypt a flag and check by entering a hex it the entered hex is correct.

Soo using the following code we can do bitflipping.

```py
def solve():
    hexs = input("Give me output: ")
    target = int(b"gimmeflag".hex(), 16)
    part1, part2 = int(hexs[:32], 16), int(hexs[32:], 16)
    return hex(part1 ^ target ^ 0x10101010101010101010101010101010)[2:].zfill(32) + hex(part2)[2:].zfill(32)
print(solve())
```

this only uses 1 block

then the second block is originally 0x10101010101010101010101010101010 (just 16 bytes padding)

xor part1 with 0x10101010101010101010101010101010 to make part2 0x00000000000000000000000000000000

then xor target to change part2 to target (set to \0\0\0\0\0\0\0gimmeflag here)

So now when we run the port and encrypt by ``Sending "00000000000000000000000000000000"`` as our plaintext. We will get a string.

![image](https://user-images.githubusercontent.com/73250884/127111885-30b43a00-b1fb-4d3c-b00e-23160ea2c807.png)

Then give that string to the above code, we will get a output.

![image](https://user-images.githubusercontent.com/73250884/127111929-dedba162-b55a-49d4-8c1d-ef16500fe714.png)

If we send that output by checking we get the flag.

![image](https://user-images.githubusercontent.com/73250884/127111976-22f364b3-dbe1-483a-89ad-1981d15e468f.png)

FLAG:- ``ictf{fl1p_fl0p_b1ts_fl1pped_b6731f96}``
