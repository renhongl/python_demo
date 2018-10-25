

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

student = {
    'id': '20180101',
    'name': 'renhong',
    'age': 18,
    'gender': 'male'
}
result = collection.insert_one(student)

print(result)


res = collection.find()

print(res)
