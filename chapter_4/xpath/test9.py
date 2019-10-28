#-*-coding:utf-8-*-

from lxml import  etree
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)

result = html.xpath('//li[contains(@class , "li")]/a/text()')
#contains() 方法，第一个参数传入属性名称，第二个参数传入属性值，
print(result)