# Brute Force

from values.json

```
e = 65537
n = 105340920728399121621249827556031721254229602066119262228636988097856120194803
enc_msg = 36189757403806675821644824080265645760864433613971142663156046962681317223254
```

use [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

`python3 RsaCtfTool.py -n 105340920728399121621249827556031721254229602066119262228636988097856120194803 -e 65537 --uncipher 36189757403806675821644824080265645760864433613971142663156046962681317223254`

output :

![image](https://user-images.githubusercontent.com/73250884/121068529-03811d00-c7ea-11eb-93d3-dee2ac79b195.png)

Flag: ``shellctf{k3y_s1ze_m@tter$}``