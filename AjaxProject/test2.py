#-*-coding:utf-8-*-
import os
import time
from _md5 import md5
from multiprocessing.pool import Pool

import  requests
from urllib.parse import urlencode

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    'referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
'cookie':'tt_webid=6693713510311134734; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16addf9b29a85c-0b0e75cd2e70a9-57b143a-144000-16addf9b29b17e; CNZZDATA1259612802=755004767-1558499329-%7C1558499329; tt_webid=6693713510311134734; __tasessionId=ewz8ezjbo1558502290173; csrftoken=e6b9963e20be7af8752532f607aff2c2; s_v_web_id=378612f952323a115d8653aaf227ecc7',
    'X-Requested-With':'XMLHttpRequest',
}

def get_page(offset):
    params ={
        'aid':'24',
        'app_name':'web_search',
        'offset':'30',
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':int(time.time()* 1000)
}
    url = 'http://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response = requests.get(url ,headers=headers )
        if response.status_code == 200 :
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    data = json.get('data')
    if data :
        for item in data:
            title = item.get('title')
            images = item .get('image_list')
            if images :
                for image in images :
                    yield {
                        'image':image.get('url'),
                        'title':title,
                    }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try :
        url = 'http:'+item.get('image')
        response = requests.get(url)
        if response.status_code == 200 :
            file_path = '{0}/{1}.{2}'.format(item.get('title') , md5(response.content).hexdigest() ,'jpg')
            if not os.path.exists(file_path):
                with open(file_path , 'wb' ) as file :
                    file.write(response.content)
            else:
                print('Already Downloaded' , file_path )
    except requests.ConnectionError :
        print("Failed to Svae Image")




def main(offset):
    json = get_page(offset)
    for item  in get_images(json):
        print(item)
        save_image(item)

#
GROUP_START = 1
GROUP_END = 20
if __name__ == '__main__':
    main(20)
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START , GROUP_END + 1)])
    pool.map(main , groups)
    pool.close()
    pool.join()






