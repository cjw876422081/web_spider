#-*-coding:utf-8-*-
from urllib import request
import bs4

response = request.urlopen("http://www.xuexila.com/fwn/xindetihui/gongzuo/4510798.html")
html = response.read().decode('gbk')