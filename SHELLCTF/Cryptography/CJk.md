# CJK

We are given an png with symbols to find a PIN:

![pin](https://user-images.githubusercontent.com/73250884/120980337-254fb500-c794-11eb-91d9-3c14837b61b6.png)

The title CJK gives us a hint to find the symbols in unicode: https://en.wikipedia.org/wiki/CJK_characters

Now we can search for a specific cutout for CJK-Symbols in unicode and search around that area: https://www.unicode.org/charts/PDF/U3000.pdf

![symbols](https://user-images.githubusercontent.com/73250884/120980423-3ac4df00-c794-11eb-8029-669668587850.png)

Now we can sum the values:

``3036 + 3004 + 3013 ``

This number is the PIN we can use for the flag: SHELL{9053}
