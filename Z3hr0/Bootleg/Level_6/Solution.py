def level6(passed):
	print("Level 6")
	if not passed:
		r.recvuntil("Level: 6, encrypted flag: ")
		ef6= int(r.recvline().decode()[:-1])
		print(ef6)
		pay = "10"
		payint = int(pay, 16)
		r.recvuntil(">>> ")
		r.sendline("1")
		r.recvuntil("message in hex:")
		r.sendline(pay)
		res = r.recvline()[:-1].decode()
		while payint**3 == int(res):
			pay += "00"
			r.recvuntil(">>> ")
			r.sendline("1")
			r.recvuntil("message in hex:")
			r.sendline(pay)
			res = r.recvline()[:-1].decode()
			payint = int(pay, 16)
		mod = payint**3 - int(res)
		print(mod)
		# factor mod to get the prime(assume it was a prime modulo), then use sage nth_root to calculate root
		f6 = input("gimme the flag in hex> ")
		r.recvuntil(">>> ")
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f6)
