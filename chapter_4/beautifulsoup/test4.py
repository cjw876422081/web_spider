#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
'''
soup = BeautifulSoup(html , 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)