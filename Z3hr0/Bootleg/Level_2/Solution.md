# LEVEL 2

This is where the levels start requiring more work and consideration. 
Once again, I sent 00 first(in general, this is a good practice), and got a hex string of the same length back. 
Sending 01 and 02 got two more different hex strings of length 2, and the three do not differ from each other by a constant amount(mod 256, since these are 1 byte each), meaning that there isn't just simple addition happening.

Next, I tried sending varied lengths of 00, such as 0000, etc.., and noticed that it got me the same hex string from before, but multiple times. 
It seemed like the encryption maps each individual byte to another byte, regardless of where each byte is in the message. 
So, we can simply construct a table for all possible 256 bytes to see what bytes map to what bytes. 
We can do this by encrypting each of 00, 01, 02, ..., ff. 
We can then decrypt the encrypted flag by reversing the mapping.

The flag is ``mono substitutions arent that creative``
