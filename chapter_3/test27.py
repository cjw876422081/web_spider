#-*-coding:utf-8-*-

import  requests

requests.get("http://httpbin.org/cookies/set/number/123456789")
r  = requests.get("http://httpbin.org/cookies")
print(r.text)


#使用session
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)
