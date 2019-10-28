#-*-coding:utf-8-*-

import  requests
response = requests.get("https://www.12306.cn")
print(response.status_code)
response = requests.get("https://www.12306.cn" ,verify = False)
print(response.status_code)

import requests
import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn" , verify = False)
print(response.status_code)