#-*-coding:utf-8-*-
from urllib.parse import urlparse

result = urlparse("http://www.baidu.com/index.html:user?id=5#comment")
print(type(result) , result)

res = urlparse("www.baidu.com/index.html:user?id=5#comment" ,scheme="https")
print(res)
#scheme，是默认的协议（比如http、https等），假如这个链接没有带协议信息，会将这个作为默认的协议。
res = urlparse("http://www.baidu.com/index.html:user?id=5#comment" ,scheme="https")
print(res)

# allow_fragments，即是否忽略 fragment，如果它被设置为 False，fragment 部分就会被忽略，它会被解析为 path、parameters 或者 query 的一部分，fragment 部分为空。
res = urlparse("http://www.baidu.com/index.html:user?id=5#comment" ,allow_fragments=False)
print(res)

res = urlparse("http://www.baidu.com/index.html#comment" ,allow_fragments=False)
print(res)
print(res.scheme, res[0], res.netloc, res[1], sep='\n')