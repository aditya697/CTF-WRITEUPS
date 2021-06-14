def level2(passed):
	print("Level 2")
	if not passed:
		r.recvuntil("Level: 2, encrypted flag: ")
		ef2 = r.recvline().decode()[:-1]
		table = [""]*256
		for i in range(256):
			r.recvuntil(">>> ")
			r.sendline("1")
			r.recvuntil("message in hex:")
			r.sendline(hex(i)[2:].zfill(2))
			key = int(r.recvline().decode()[:-1], 16)
			table[key] = hex(i)[2:].zfill(2)
			print(i)
		f2 = ""
		for i in range(0, len(ef2), 2):
			f2 += table[int(ef2[i:i + 2], 16)]
		assert len(f2) == len(ef2)
		print(f2)
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f2)
