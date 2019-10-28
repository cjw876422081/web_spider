#-*-coding:utf-8-*-

import  json
data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
#unicode 字符
with open('data.json' , 'w') as file :
    file.write(json.dumps(data , indent=2))


with open('data.json' , 'w' , encoding='utf-8') as file :
    file.write(json.dumps(data , indent=2 , ensure_ascii=False))