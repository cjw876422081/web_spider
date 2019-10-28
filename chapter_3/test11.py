#-*-coding:utf-8-*-
from urllib.parse import urlencode, parse_qs, parse_qsl

#序列化
params = {
    'name':'germey',
    'age':22
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)

#反序列化
print(parse_qs(url)) #字典
print(parse_qsl(url))#元组