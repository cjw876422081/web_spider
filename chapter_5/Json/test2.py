#-*-coding:utf-8-*-
import json

#无法载入
str = '''
[{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
'''
data = json.loads(str)