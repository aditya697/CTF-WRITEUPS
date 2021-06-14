def level5(passed):
	print("Level 5")
	if not passed:
		r.recvuntil("Level: 5, encrypted flag: ")
		ef5 = r.recvline().decode()[:-1]
		f5 = ""
		base = ef5[-10:]
		for i in range(0, len(ef5) - 10, 10):
			block = ef5[i:i + 10]
			for j in range(0, len(block), 2):
				diff = int(base[j:j + 2], 16) ^ int(block[j:j + 2], 16)
				if diff in range(32, 128):
					f5 += hex(diff)[2:].zfill(2)
				else:
					break
		r.recvuntil(">>> ")
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f5)
