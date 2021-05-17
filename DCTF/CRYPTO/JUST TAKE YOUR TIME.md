## ***JUST TAKE YOUR TIME***

```py
import socket
from time import time
from Crypto.Cipher import DES3
from binascii import unhexlify

remotehost = "dctf-chall-just-take-your-time.westeurope.azurecontainer.io"
remoteport = 9999

# Connect to the remote side and capture the output
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((remotehost, remoteport))
output1 = str(s.recv(1024).decode("utf-8"))
print("debug remote output:\n" + output1 + "\n")

# Parse and process the output to calculate result 1
remotelines = output1.splitlines();
num1 = remotelines[1].split()[0];
num2 = remotelines[1].split()[2];
print("debug number extract: 1=" + num1 + " 2=" + num2)
result1 = str(int(num1) * int(num2))
print("debug multiplication: " + result1)

# Send result to remote side, and check response
s.send(bytearray(result1 + "\n", 'utf-8'))
output2 = str(s.recv(1024).decode("utf-8"))
print("debug remote output:\n" + output2 + "\n")

# Parse and process the output to calculate result 2
remotelines = output2.splitlines();
enc = remotelines[1];
print("debug cipher extract: enc=" + enc)

# Generate the decryption key based on the timestamp
key = str(int(time())).zfill(16).encode("utf-8")
print("debug decryption key: key=" + str(key.decode("utf-8")))

# Decrypt the ciphertext
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
cleartext = str(cipher.decrypt(unhexlify(enc)).decode("utf-8"))
print("debug show cleartext: clr=" + cleartext)

# Sent decryption result to remote, and check for flag
s.send(bytearray(cleartext + "\n", 'utf-8'))
output3 = str(s.recv(1024).decode("utf-8"))
print("debug remote output:\n" + output3 + "\n")
```
Flag : ***```dctf{1t_0n1y_t0Ok_2_d4y5...}```***
