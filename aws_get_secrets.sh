#!/bin/bash

aws --endpoint-url="http://127.0.0.1:4566" secretsmanager list-secrets | grep "arn:aws" | grep -oP '".*?"' | grep -v "ARN" | tr -d '"' | while read secret_id; do
	echo -e "\n[+] Enumerando secret_id: $secret_id:\n"
	aws --endpoint-url="http://127.0.0.1:4566" secretsmanager get-secret-value --secret-id "$secret_id"
done
