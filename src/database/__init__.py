import pymongo, os

class SingletonDB:
    _instance = None
    client = pymongo.MongoClient(os.getenv('MONGO_URL'))

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class DB:
    def __init__(self, db_name, collection_name):
        self.db = SingletonDB().client[db_name]
        self.collection = self.db[collection_name]
