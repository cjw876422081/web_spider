#-*-coding:utf-8-*-

import requests
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('https://www.taobao.com', proxies=proxies)



import requests

proxies = {
    'https': 'http://user:password@10.10.1.10:3128/',
}
requests.get('https://www.taobao.com', proxies=proxies)



#socks
import requests

proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get('https://www.taobao.com', proxies=proxies)