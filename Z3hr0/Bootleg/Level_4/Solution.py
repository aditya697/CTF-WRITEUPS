def level4(passed):
	print("Level 4")
	if not passed:
		r.recvuntil("Level: 4, encrypted flag: ")
		ef4 = r.recvline().decode()[:-1]
		f4 = ""
		table = {}
		for n in range(256):
			for i in range(3):
				r.recvuntil(">>> ")
				r.sendline("1")
				r.recvuntil("message in hex:")
				r.sendline(hex(n)[2:].zfill(2) * 512)
				res = r.recvline().decode()[:-1]
				for j in range(0, len(res), 4):
					block = res[j:j + 4]
					if block not in table:
						table[block] = hex(n)[2:].zfill(2)
		for i in range(0, len(ef4), 4):
			block = ef4[i:i + 4]
			f4 += table[block]
		print(f4)
		assert len(f4) == len(ef4) // 2
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f4)
