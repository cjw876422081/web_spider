#-*-coding:utf-8-*-
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='123456')

#s是否存在
print(bool(redis.exists('name')))
#删除
print(redis.delete('name'))
redis.set('name','Bob')
print(redis.type('name'))

print(redis.keys('n*'))
print(redis.randomkey())

