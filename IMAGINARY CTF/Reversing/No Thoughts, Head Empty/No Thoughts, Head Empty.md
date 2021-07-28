# No Thoughts, Head Empty

We are given a `.bf` file which has brainfuck language.

If we try to decode using normal decoders we cannot do it.

The reason is it has many loops running.

So i found 2 solutions for it.

First convert that `.bf` file to a `.c` file using the code in this repository.

https://github.com/paulkaefer/bftoc/blob/master/bftoc.py

After converting if we see the code we can see ``tape[ptr] += 2;``

Because of that the words will be printed `2**n` times.

The solution for doubling is changing ``tape[ptr] += 2; to tape[ptr] += 1;`` in that C code.

then either adding `setbuf(stdout, NULL);` at the start of main or running it as stdbuf -o0 `./prog`

Then run the c program you can get the flag.

Either way is you can compile the c code using gcc and run the `ELF`.

We can see the terminal goes brrrrrr....😂 So output it into file.

Each word will be printed in the orser of ``2**n`` 

like 1st letter 1 time , 2nd letter 2 times , 3rd letter 4 times , 4th letter 8 times.....Soo on.

If we note down all the letters being printed it will form the flag.

Didn't much reversing but got the flag 😅

Flag:- ``ictf{th3_l3s5_th0ugh+_+he_b3teR}``
