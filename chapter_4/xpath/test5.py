#-*-coding:utf-8-*-
from lxml import  etree

html = etree.parse("./text.html" , etree.HTMLParser())

result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)


result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

