#-*-coding:utf-8-*-
from pyquery import PyQuery as pq

doc = pq(filename="demo.html")
print(doc('li'))