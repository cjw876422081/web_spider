#-*-coding:utf-8-*-


import requests

r = requests.get("https://www.taobao.com" , timeout = 1 )
print(r.status_code)