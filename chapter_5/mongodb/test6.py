#-*-coding:utf-8-*-
import pymongo
client = pymongo.MongoClient()
db = client.test
collection = db.students


result = collection.remove({'name':'Jordan'})
print(result)



result = collection.delete_one({'name': 'Jordan'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)