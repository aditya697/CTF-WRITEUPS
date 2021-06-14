# Level 0

There were two level 1s, so we'll call this first one level 0. 

After a bit of testing by sending multiple hex strings of 0s, I figured out that it just adds 1 to the value of each byte in the message. 

So, we just take the encrypted flag and subtract 1 from each byte to get the original flag. Here is the code to do this:

![Solution](Solution.py)
