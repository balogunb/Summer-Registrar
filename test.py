#import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://Basitb:*******@collegecourses-ne1ze.mongodb.net/test?retryWrites=true&w=majority")
db = client.schools_db

schools_db = {
'name' : 'lafayette'

}

db.schools.insert_one(schools_db)
