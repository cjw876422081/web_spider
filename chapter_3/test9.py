#-*-coding:utf-8-*-

from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])