#-*-coding:utf-8-*-
import http.cookiejar
import urllib

filename = "cookies.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard = True  , ignore_expires = True )