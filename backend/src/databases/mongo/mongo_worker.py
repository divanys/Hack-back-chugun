from pymongo import MongoClient
from configs.database_config import db


class MongoWorker:
    mongo_engine = MongoClient(db.MONGO_URI)
    db_mongo = mongo_engine.get_database("edu_connect")
