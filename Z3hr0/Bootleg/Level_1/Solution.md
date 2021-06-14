# LEVEL 1

The encrypted flag for this level is just a number, rather than a hex string like the previous. 

So, it's likely that the message passed in is converted to a number and then something else is done to it. 

Sending 00 returns 0, so I suspected that it simply converts the hex to a number. 

Testing with a few more messages confirms this, so we just convert the given encrypted flag into hex and send it over.

The flag is ``Nothing fancy, just standard bytes_to_int``
