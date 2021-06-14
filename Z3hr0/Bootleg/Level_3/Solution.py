def level3(passed):
	print("Level 3")
	if not passed:
		r.recvuntil("Level: 3, encrypted flag: ")
		ef3 = r.recvline().decode()[:-1]
		f3 = ""
		for i in range(0, len(ef3), 2):
			byte = ef3[i:i + 2]
			buff = "00" * (i // 2)
			for j in range(256):
				r.recvuntil(">>> ")
				r.sendline("1")
				r.recvuntil("message in hex:")
				r.sendline(buff + hex(j)[2:].zfill(2))
				target = r.recvline().decode()[:-1][-2:]
				if target == byte:
					f3 += hex(j)[2:].zfill(2)
					break
			print(i)
			print("flag so far: ", f3)
		assert len(f3) == len(ef3)
		print(f3)
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f3)
