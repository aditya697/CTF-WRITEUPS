# LEVEL 6

The first thing I noticed about this level was that it seemed to take a while for it to generate the encrypted flag. Sometimes the waiting time would be short, but other times it would be longer. Additionally, the encrypted flag was a number. Encrypting 00, 01, 02 gave 0, 1, and 8 respectively. It seems like the scheme was just to cube the message after converting it to an int. So, we could just take the cube root of the flag using sage. Or so I thought. Attempting to do so resulted in sage telling me that the encrypted flag was not a perfect cube.

When considering the time that it took to generate the encrypted flag, and the fact that the encrypted flag is different on each connection, this actually makes sense. The most likely scenario here is that the encryption does cubing modulo some large prime, where the prime generation is what took time. And with a different prime, if the original message is large enough, the encryption result will be different. Then, it's just about finding what that prime is.

This is not difficult; we can just encrypt increasingly large messages until result != message^3. I increased the value of my messages by appending a 00 byte at the end(the same as multiplying the int value by 256). Find two messages that have result != message^3, take the differences of message1^3 - result1 and message2^3 - result2, find their GCD, and factor to get the prime(since the GCD is likely to be a small multiple of the prime). Then, just used sage's nth_root function(have the encrypted flag as an element of GF(p)) to get the flag. I was a bit lazy with this, so instead I only used 1 message, and, figuring that a cube is quite small, just directly factored the difference message^3 - result to get the prime. The reason this(and the previous GCD method) works is because the encryption scheme is E(x) = x^3 (mod p), so x^3 - E(x) = 0 (mod p), meaning that the difference is a multiple of p, the prime in question.

The flag is ``Cube modulo prime, any guesses what might be coming next?``