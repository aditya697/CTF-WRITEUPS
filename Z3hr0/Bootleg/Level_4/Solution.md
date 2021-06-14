# LEVEL 4

Once again, I sent 00 first. Different from before, I got a hex string of twice the original length. Sending 0000 gave me a hex string of length 8, so it seems that the encryption does something to double the length of the original message.

Then, I sent 01 and 02 again, with similar results. It seemed like it was a similar system to level 3, since the 2-byte blocks from 0000 were different from each other. So I thought that it was just an mapping from single bytes to 2-byte blocks instead of byte to byte like before.

However, sending 00 again revealed something troublesome; it gave me a result different from before, meaning that this encryption was non-deterministic. Even so, we are supposed to be able to decrypt the encrypted flag. Combining these two facts, I realized that the encrypted flag must be one of many possible encryptions of the original flag, using the same encryption system.

Based on this, the general approach would to be find which message the encrypted flag could be a possible encryption of. In order for this to be feasibly bruteable, I figured the encryption probably didn't map entire messages to encrypted messages, but rather encrypted byte-by-byte like previous stages.

Additionally, after more various testing and thinking, I realized that it was likely that the system was not like in level 3 where the encryption was different per byte position, and instead a single mapping table was being used for all byte positions like in level 2. The main reasons I considered this where 1) with 256*256 possible 2-bytes, I would have to send up to 256*256*(# of 2-bytes in the encrypted flag) requests, which would take a long time considering it's a remote connection (likely not feasible, especially with 3 levels remaining after) and 2) When encrypting longer messages like 00000000000000000000, I noticed that occasionally the 00 bytes in different positions encrypted to the same 2-byte blocks.

With this in mind, I figured the encryption scheme was likely: Encrypt each byte to 1 of x 2-bytes, for each byte in the message. This scheme also requires for no two bytes to encrypt to any same 2-bytes(for example, 00 and 01 cannot both encrypt to 0e5f), or else we would not be able to uniquely decrypt some messages. To test this, I sent long strings of 00s and 01s, and checked if they shared any 2-byte blocks. They didn't, confirming that my idea was likely correct.

Then, the approach would be pretty much the same as level 2: Build a table finding out which 2-byte blocks each byte encrypts to. The main problem with this is doing it the same way as in level 2 naively would be rather infeasible. For one, we don't know how many 2-byte blocks each byte individually maps to; it could be the same for all, or it could be different for all, so sending only one byte at a time doesn't seem like a good idea, since we wouldn't know when to move on to the next byte.

Instead, I opted to send long strings of the same byte repeated, like I had done in my previous testing. Assuming my idea was correct, I could just use each individual message to collect a bunch of the mappings at a time, rather than wait in between requests. I did this a few times, and found that bytes seemed to map to 256 2-byte blocks each, which makes a lot of sense, since 256 * 256 / 256 = 256.

So my approach became: For each byte, send a few long messages of the byte repeated, and use it collect the possible blocks that byte maps to. Build the table this way, and then look at each 2-byte block in the encrypted flag, reverse the mapping, and get the original flag. I opted to use messages of 512 bytes, with 3 messages per byte, since that seemed to consistently find 254-256 mappings per byte, which was generally enough.

The flag is ``Glad that you figured out the invariant``
