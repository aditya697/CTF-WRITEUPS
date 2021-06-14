def level0(passed):
	print("Level 0")
	if not passed:
		r.recvuntil("Level: 1, encrypted flag: ")
		ef1 = r.recvline().decode()[:-1]
		r.recvuntil(">>> ")
		f1 = ""
		for i in range(0, len(ef1), 2):
			byte = int(ef1[i:i + 2], 16)
			byte -= 1
			f1 += hex(byte)[2:]
		print(f1)
		assert len(f1) == len(ef1)
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f1)
