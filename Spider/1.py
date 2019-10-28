#-*-coding:utf-8-*-
from  urllib import  request

if __name__ == '__main__':
    url = "http://www.baidu.com"
    req  = request.urlopen(url)
    html = req.read()
    print(html.decode("utf-8"))