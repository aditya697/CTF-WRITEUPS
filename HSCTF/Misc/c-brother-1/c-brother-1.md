# c-brother-1

**Description:-** AC01010 and JC01010's long lost twin has joined the HSCTF discord and started a Youtube channel! Although they haven't uploaded any videos, they've made some customizations to some of their video watermarks.

Soo searching on their discord we get an Discord ID

![image](https://user-images.githubusercontent.com/73250884/122713146-d8cfa380-d282-11eb-856f-4c3a793392cb.png)

That discord account has a youtube link in its description.

![image](https://user-images.githubusercontent.com/73250884/122713202-f56bdb80-d282-11eb-9061-cb0691201209.png)

There are no vedios with watermark in the channel.

We can get a vedio which has watermark and get the URL through which watermark is being loaded.

``
https://i.ytimg.com/an/B6PV0cvJpzlcXRG7nz6PpQ/featured_channel.jpg
``

If you noticed, in the watermark URL the ID is missing two characters from the start i.e. UC

``
Channel   : https://www.youtube.com/channel/UCqZq81jZcdjAHQJ3UtAbdaA
Watermark : https://i.ytimg.com/an/B6PV0cvJpzlcXRG7nz6PpQ/featured_channel.jpg
``

Using the channel link of `BC01010` I changed the link of the watermark.

``
https://i.ytimg.com/an/qZq81jZcdjAHQJ3UtAbdaA/featured_channel.jpg
``

This image is our flag.

![image](https://user-images.githubusercontent.com/73250884/122714004-3adcd880-d284-11eb-98fe-bbf8aeb8ccfc.png)

Flag:- flag{h1dd3n_wat3rm@rk}
