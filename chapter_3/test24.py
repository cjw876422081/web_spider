#-*-coding:utf-8-*-
import requests
r = requests.get("https://www.baidu.com")
print(r.cookies)
for k , v  in  r.cookies.items():
    print(k , v )