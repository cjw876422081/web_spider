#-*-coding:utf-8-*-
from urllib.parse import urlunparse ,urlunsplit

data = [
    'http' , 'www.baidu.com' , 'index.html' ,
    'user' , 'a=6','comment'

]
print(urlunparse(data))
data = [
    'http' , 'www.baidu.com' , 'index.html' ,
     'a=6','comment'

]
print(urlunsplit(data))