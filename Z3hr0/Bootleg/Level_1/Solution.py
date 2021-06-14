def level1(passed):
	print("Level 1")
	if not passed:
		r.recvuntil("Level: 1, encrypted flag: ")
		ef1 = r.recvline().decode()[:-1]
		r.recvuntil(">>> ")
		f1 = hex(int(ef1))[2:]
		print(f1)
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f1)
