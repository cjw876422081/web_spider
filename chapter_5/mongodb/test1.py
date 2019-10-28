#-*-coding:utf-8-*-
import pymongo
client = pymongo.MongoClient(host = 'localhost' , port=27017)
#client = MongoClient('mongodb://localhost:27017/')
db = client.test
#db = client['test']
collection = db.students
#collection = db['stdudents']
#插入一条数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert_one(student)
print(result)
print(result.inserted_id)

#插入多条数据
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = collection.insert_many([student1 , student2])
print(result)
print(result.inserted_ids)





