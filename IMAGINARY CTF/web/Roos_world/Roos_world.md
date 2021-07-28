# Roos World

We are given a link.

If we open that link we can see that ROO is looking for flag.

So firstly check the source, we can a javascript.

Looking at it we will know it is `brainfuck` or `jsfuck`

So in this case it is jsfuck so to decode it we can use https://enkhee-osiris.github.io/Decoder-JSFuck/

So we get the following

![image](https://user-images.githubusercontent.com/73250884/127367820-a3739e6c-60cd-4ef7-a0ec-946528221b4b.png)

``console.log(atob("aWN0ZnsxbnNwM2N0MHJfcjAwX2cwZXNfdGgwbmt9"));``

The string inside it is decode in ``base64``.

Using cyberchef we can decode it.

![image](https://user-images.githubusercontent.com/73250884/127368028-028cab1f-5bc3-4004-aa62-cb076835d87d.png)

Flag:- ``ictf{1nsp3ct0r_r00_g0es_th0nk}``
