#-*-coding:utf-8-*-

import  requests
from pyquery import  PyQuery as pq

url = 'https://www.zhihu.com/explore'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',

}
response = requests.get(url ,headers = headers)
print(response.status_code)
html = response.text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
print(html)
for item in items :
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer =pq(item.find('.content').html()).text()
    # file = open('explore.text' , 'a' , encoding='utf-8')
    # file.write('\n'.join([question , author , answer]))
    # file.write('\n'+'='*50 +'\n')
    # file.close()
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')

