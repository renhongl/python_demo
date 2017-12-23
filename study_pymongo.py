import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

db = client.wangyi

collection = db.comments

result = collection.find({'comment': {'$regex': '\w*爱\w*'}})

for item in result:
    print(item)
