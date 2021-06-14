Once again, I started off by sending 00. Just like before, the encryption was a new hex string of the same length. Sending 01 and 02 also gave the same pattern as with level 2. Sending them again gave the same result, so it seemed like a mapping just like before was happening.

However, sending 0000 showed a difference from before; the second byte returned was different from the first. It seemed to be more troublesome than level 2. At this point, I suspected 2 possibilities: the whole message is mapped to some other message of the same length, or each byte position(for example, the 1st vs the 2nd 00 in 0000) has a different mapping table.

The first option would be very difficult to brute-force to decrypt the encrypted flag, so I tried testing for the second scenario by sending 0100. The second returned byte was the same as in 0000, showing me that the likelihood of the second scenario was high. Testing a few more messages in a similar manner confirmed this theory.

Then the question becomes, how could I figure out the flag in a timely manner? One option is to simply create a table like with level 2, except for each byte position. However, this is something of a waste, because each table would only be used to decrypt a single byte of the encrypted flag.

So instead, I just encrypted 00, 01, until I got the corresponding byte in the flag for each byte position. The byte that, when encrypted, matched the one in the encrypted flag, would be the original byte in the decrypted flag. To test the encryptions for byte position x + 1, I first put x 00s and then the byte I wanted to encrypt(For example, 000001, 000002, etc.).

Notably, in the worst case this still would take (# of bytes in the encrypted flag)*256 requests, and it's possible for the connection to close itself in this time. However, this isn't much of an issue because the flag itself never changes, even if the encryption does. So we can just keep track of which byte position we are on and start from there until we recover the entire flag. The following code simply assumes that this issue doesn't occur.
