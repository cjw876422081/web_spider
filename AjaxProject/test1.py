#-*-coding:utf-8-*-
from pyquery import PyQuery as pq
from urllib.parse import urlencode
import requests
import pymongo

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers ={
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2145291155' ,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36' ,
    'X-Requested-With':'XMLHttpRequest',

}



def get_page(page):
    params ={
        'type':'uid',
        'value':'2145291155',
        'containerid':'1076032145291155',
        'page':page,
    }
    url = base_url + urlencode(params)
    try:
        respone = requests.get(url , headers = headers)
        if respone.status_code == 200 :
            return respone.json()
    except requests.ConnectionError as e :
        print('Error' , e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield  weibo

if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.test2
    collection = db.weibo
    for page in range(1 , 15):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            a = collection.insert_one(result)
            print(a)
            print(result)

