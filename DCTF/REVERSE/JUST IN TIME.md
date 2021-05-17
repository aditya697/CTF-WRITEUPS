## ***JUST IN TIME***

This will give the flag.

***```ltrace -s 90 ./justintime```***
```
malloc(8)                                        = 0x5631a2b6e2a0
malloc(8)                                        = 0x5631a2b6e2c0
fopen(&quot;./justintime&quot;, &quot;rb&quot;)                      = 0x5631a2b6e2e0
fread(0x5631a2b6e2c0, 8, 1, 0x5631a2b6e2e0)      = 1
fclose(0x5631a2b6e2e0)                           = 0
strncpy(0x5631a2b6e2a0, &quot;\177ELF\002\001\001&quot;, 8) = 0x5631a2b6e2a0
malloc(39)                                       = 0x5631a2b6e4c0
strncpy(0x5631a2b6e4c0, &quot;\033&amp;8 yegHr($g1bKu{&quot;f5`N}t#331Nv/%`11F#1&quot;, 39) = 0x5631a2b6e4c0
strlen(&quot;\033&amp;8 yegHr($g1bKu{&quot;f5`N}t#331Nv/%`11F#1&quot;) = 38
puts(&quot;Decryption finished.&quot;Decryption finished.
)                     = 21
malloc(39)                                       = 0x5631a2b6e900
malloc(40)                                       = 0x5631a2b6e930
strncpy(0x5631a2b6e900, &quot;dctf{df77dbe0c407dd4a188e12013ccb009f}&quot;, 39) = 0x5631a2b6e900
malloc(40)                                       = 0x5631a2b6e960
strlen(&quot;\033&amp;8 yegHr($g1bKu{&quot;f5`N}t#331Nv/%`11F#1&quot;) = 38
free(0x5631a2b6e4c0)                             = &lt;void&gt;
free(0x5631a2b6e960)                             = &lt;void&gt;
free(0x5631a2b6e2a0)                             = &lt;void&gt;
+++ exited (status 0) +++
```

Flag : ***``dctf{df77dbe0c407dd4a188e12013ccb009f}``***
