## **BELL**

```py
def triangle(a, b):
    lVar1 = lVar2 = 0

    if a < b:
        lVar1 = 0
    else:
        if (a == 1) and (b == 1):
            lVar1 = 1
        else:
            if b == 1:
                lVar1 = triangle(a - 1, a - 1)
            else:
                lVar2 = triangle(a, b - 1)
                lVar1 = triangle(a - 1, b - 1)
                lVar1 = lVar1 + lVar2
    return lVar1


n = int(input("Enter the first number that was printed: "))
for k in range(1, n + 1):
    print(triangle(n, k))
```
By running the ```nc dctf-chall-bell.westeurope.azurecontainer.io 5311```

By giving the number that came in when we enter the port in the above program we get some values if we enter those values in the port we get the flag.

Flag : ***```dctf{f1rst_step_t0wards_b3ll_l4bs}```***

