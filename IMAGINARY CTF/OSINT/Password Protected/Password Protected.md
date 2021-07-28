# Password Protected

We are given a `.txt` file and `.zip` file.

In the text file we can addresses looking that we can know that we should use `libc.so.6` library file.

Using `bkcrack` or `pkcrack` we can solve the challenge.

For this we need `the zip file given to us` , `libc.so.6` , `a zip file creaste by us with libc.so.6 file`.

First we need to run this command ``./bkcrack -C encrypted.zip -c "libc.so.6" -P "leaked.zip" -p "libc.so.6"``

![image](https://user-images.githubusercontent.com/73250884/127378173-20370790-f00f-4519-91f0-8fee302e8c2c.png)

``169ab86d 8faccdaf 4f259cb4``

We got three values using these values we should give a `zip` file of our with our own password and run the command.

When we run it, it will create zip file that name and when open it with the password we gave we can access the files inside.

``./bkcrack -C encrypted.zip -k <1st value> <2nd value> <3rd value> -U <new zip file name> <own password>``

![image](https://user-images.githubusercontent.com/73250884/127378629-582187d7-13de-4851-afde-10bacfc5750f.png)

It has created a new file `unlocked.zip` open it with the password given.

![image](https://user-images.githubusercontent.com/73250884/127378750-a1e35a53-7f79-485c-9210-82a48451954e.png)

Flag:- ``ictf{dont_use_zipcrypto_5e2b32f3}``
