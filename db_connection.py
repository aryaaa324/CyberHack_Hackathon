import pymongo

def get_database():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client["digital_dna"]

db = get_database()
