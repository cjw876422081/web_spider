#-*-coding:utf-8-*-

from lxml import etree

html = etree.parse("./text.html" , etree.HTMLParser())
result = html.xpath("//li/a")
print(result)
