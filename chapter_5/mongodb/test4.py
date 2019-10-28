#-*-coding:utf-8-*-
import pymongo
client = pymongo.MongoClient()
db = client.test
collection = db.students
condition = {'name':'Jordan'}
student = collection.find_one(condition)
student['age'] = 25
result =collection.update(condition,student)
print(result)



