import pymongo

# TODO : HIDE & MODULARIZE
PASSWORD = "makingausableapi"
uri = "mongodb+srv://admin:" + PASSWORD + "@poc-5vbvd.mongodb.net/test"

def get_client():
    return pymongo.MongoClient(uri)

def get_test_db():
    return get_client()['test']
