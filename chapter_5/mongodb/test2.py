#-*-coding:utf-8-*-
import pymongo
client = pymongo.MongoClient()
db = client.test
collection = db.students

result = collection.find_one({'name':'Mike'})
print(type(result))
print(result)

from bson.objectid import ObjectId
result = collection.find_one({'_id':ObjectId('5ce34ce429bd8b1f24232f57')})
print(result)


results = collection.find({'age':20})
print(results)
for result in results:
    print(result)

results = collection.find({'name': {'$regex': '^M.*'}})