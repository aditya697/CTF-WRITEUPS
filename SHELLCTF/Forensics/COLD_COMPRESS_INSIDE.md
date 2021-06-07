# Cold Compress Inside

We are given a jpeg file.
Running `file` on it quickly tells us it's a PNG even though it has .jpeg extension.

As the name suggests already we assume that there is another file hidden inside of it. So we run foremost on it:

```foremost <filename>```

We extracted a o.exe let's just run `string o.exe` on it:

We can see a meaningfull line which is the flag 

Flag: ``SHELL{CRazy_MosQUIto_nEEDS_odoMOS}``
