# Hidden Inside 2

We were provided a jpeg image 

It says .jpeg but running `file` on it tells us it's a PNG. 

So I upload it to https://stegonline.georgeom.net/upload to test different thing on it.

While browsing the bit planes I've noticed a thin line on the green layer 0:

![green_0](https://user-images.githubusercontent.com/73250884/120990994-ccd1e500-c79e-11eb-91c8-99deaeb59aa0.png)

So I switched to extract data and selected that layer:

![extract_data](https://user-images.githubusercontent.com/73250884/120991145-f723a280-c79e-11eb-863a-f11c1023c887.png)

The result had a PNG magic number so I downloaded it:

![extracted_data](https://user-images.githubusercontent.com/73250884/120991193-04409180-c79f-11eb-93ae-73c1d09825ed.png)

Flag : ``SHELL{RayMONd_redDINTON_is_nOt_iLLYA}``
