# CHECK FLAG

Here the flag is encoded in the executable by running gdb we can get the flag

```
gdb <filename>
disas main
```

In the main we can see a function checkflag

```
disas checkflag
```

![image](https://user-images.githubusercontent.com/73250884/120993939-a6fa0f80-c7a1-11eb-888f-9eee43791fe6.png)

We can see a compare which is highlighted. 

So here the value is being compared to 0x913 i.e 2323 in decimal.

![image](https://user-images.githubusercontent.com/73250884/120994751-6a7ae380-c7a2-11eb-9818-0f1f37ddbe2b.png)

Flag: ``SHELL{bas1c_r3v}``
