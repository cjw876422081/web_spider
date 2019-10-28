#-*-coding:utf-8-*-
import urllib
from pip._vendor import chardet

if __name__ == '__main__':
    url = "http://www.baidu.com"
    req = urllib.request.urlopen(url)

    print(type(req))
    print(req.info())
    html = req.read()
    cs = chardet.detect(html)
    print(type(cs))
    html = html.decode(cs.get("encoding" , "utf-8"))
    # print(html)
