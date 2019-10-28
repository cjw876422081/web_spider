#-*-coding:utf-8-*-
from urllib.parse import quote, unquote

#编码
keyword = " 壁纸"
url = "https://www.baidu.com/s?wd=" + quote(keyword)

print(url)

#解码
print(unquote("https://www.baidu.com/s?wd=%20%E5%A3%81%E7%BA%B8"))

