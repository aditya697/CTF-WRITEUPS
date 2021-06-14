def level7(passed):
	print("Level 7")
	if not passed:
		r.recvuntil("Level: 7, encrypted flag: ")
		ef7 = int(r.recvline().decode()[:-1])
		print(ef7)
		r.recvuntil(">>> ")
		r.sendline("1")
		r.recvuntil("message in hex:")
		r.sendline("02")
		power = int(log(int(r.recvline()[:-1].decode()), 2))
		print(power)
		pay = 256
		r.recvuntil(">>> ")
		r.sendline("1")
		r.recvuntil("message in hex:")
		r.sendline("0" + hex(pay)[2:])
		res = r.recvline()[:-1].decode()
		while pay**power == int(res):
			pay = int(1.1 * pay)
			r.recvuntil(">>> ")
			r.sendline("1")
			r.recvuntil("message in hex:")
			payload = hex(pay)[2:]
			if len(payload) % 2:
				r.sendline("0" + payload)
			else:
				r.sendline(payload)
			res = r.recvline()[:-1].decode()
		mod = pay**power - int(res)
		print(mod)
		# factor mod to get the prime(assume it was a prime modulo), then use sage nth_root to calculate root
		f7 = input("gimme the flag in hex> ")
		r.recvuntil(">>> ")
		r.sendline("2")
		r.recvuntil("flag in hex:")
		r.sendline(f7)
