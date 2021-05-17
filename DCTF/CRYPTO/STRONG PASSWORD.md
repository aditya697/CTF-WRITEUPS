## ***STRONG PASSWORD***

WE can crack the password using *`JOHN THE RIPPER`*

***```zip2john strong_password.zip > zip.hash```***

***```john --wordlist=rockyou.txt zip.hash```***

We get the password as **``Bo38AkRcE600X8DbK3600``**

In the lorem.txt we find the flag by ``cat lorem.txt | grep dctf``

Flag: ***```dctf{r0cKyoU_f0r_tHe_w1n}```***
