#-*-coding:utf-8-*-
import json
import re
import time

import requests
#z抓取首页

def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',

    }
    response = requests.get(url , headers = headers)
    print(response.status_code)
    if response.status_code == 200 :
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
    , re.S)
    items = re.findall(pattern , html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
            # 'index': item[0],
            # 'image': item[1],
            # 'title': item[2].strip(),
            # 'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            # 'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            # 'score': item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open('result.txt', 'a' , encoding="utf-8") as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False,)+'\n')

def main(offset):
    url = 'http://maoyan.com/board/4' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i  in range(10):
        main(offset = 1 * 10)
        time.sleep(1)

