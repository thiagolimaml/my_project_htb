#!/usr/bin/python3
# coding:utf-8

from pwn import *
import requests,re,pdb

def def_handler(sig, frame):
	print("\n[!]Saindo...\n")
	sys.exit(1)

# CTRL + C
signal.signal(signal.SIGINT, def_handler)

# Variable_Global
main_url = "http://10.10.10.93/transfer.aspx"
burp = {'http': 'http://127.0.0.1:8080'}

def makeRequest(file):

	s = requests.session()

	r = s.get(main_url)

	viewstate = re.findall(r'id="__VIEWSTATE" value="(.*?)"',r.text)[0]

	event = re.findall(r'id="__EVENTVALIDATION" value="(.*?)"',r.text)[0]

	data_post = {
		'__VIEWSTATE': viewstate,
		'__EVENTVALIDATION': event,
		'btnUpload': 'Upload'
	}

	fileUpload = {'FileUpload1':(f'test{file}','testing')}

	r = s.post(main_url, data=data_post, files=fileUpload, proxies=burp)

	if "Invalid File. Please try again" not in r.text:
		log.info(f"Valid: {file}")

if __name__ == '__main__':

	f = open('/tmp/wordlist','rb')

	p1 = log.progress("Brute Force Extension")
	p1.status("Starting")

	sleep(2)

	for file in f.readlines():

		file = file.decode().strip()
		p1.status(f"Testing Extension: {file}")
		makeRequest(file)
