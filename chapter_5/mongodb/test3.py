#-*-coding:utf-8-*-
import pymongo
client = pymongo.MongoClient()
db = client.test
collection = db.students

count = collection.find().count()
print(count)

results = collection.find().sort('name' ,pymongo.ASCENDING)
print([result['name']for result in results])



#偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])


results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])


from bson.objectid import ObjectId
collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})