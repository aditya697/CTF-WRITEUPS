# Poly-Alpha

We are given a flag like this:
```
UYCAE{J0_P0A_CFE_XF335}
```
The challenge name tells us that it is something about a poly-alphabetic cypher so we try to solve it online automatically.

I like using this tool: https://www.dcode.fr/vigenere-cipher.
We can use what we already know - the beginning of the flag in plaintext "SHELL":

![decode](https://user-images.githubusercontent.com/73250884/120997756-19b8ba00-c7a5-11eb-8a3c-04414ce4a061.png)

But that's not the whole answere, as the flag is still not readable. So I guessed around in CyberChef:

![cyberchef](https://user-images.githubusercontent.com/73250884/120997826-2806d600-c7a5-11eb-8d38-b8fa1dd226f6.png)

I had some ideas with different keys. One of it was "cryptochallenge":

![cryptochallenge](https://user-images.githubusercontent.com/73250884/120997911-381eb580-c7a5-11eb-9034-2498de508b98.png)

This look right in some parts with that "NOT CUT"... I guessed there is something like "DO NOT CUT" and the word at the end could be "knees" or "trees". In terms of "do not cut", "trees" could be fine. Figuering around I got the flag, but this was really try 'n error as the keyword became "crptgchalleoge":

![cryptgchalleoge](https://user-images.githubusercontent.com/73250884/120997986-466cd180-c7a5-11eb-8042-c8efda7b5d3b.png)
