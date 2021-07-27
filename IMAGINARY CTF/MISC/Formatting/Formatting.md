# Formatting

We are given `.py` file.

If we see the script we can see that flag is not being modified anywhere in the code.

The flag is declared globaly and the challenge desc says formatting strings.

So i checked for formatting string in python https://lucumr.pocoo.org/2016/12/29/careful-with-str-format/

By reading through that in the end there is safe method like ``{0.__class__}'.format(42)`` instead of ``.format()``

So by using this command we are calling the flag that is declared globally ``{a.__init__.__globals__[flag]}``

if we enter this on the port then it will be a safe input and since we calling flag it will be printed.

![image](https://user-images.githubusercontent.com/73250884/127201652-3482d48c-3533-451c-9d3d-e0a0a13f6b88.png)

FLAG:- ``ictf{c4r3rul_w1th_f0rmat_str1ngs_4a2bd219}``
