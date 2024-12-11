from src.databases.mongo.mongo_worker import MongoWorker
from typing import List


class ForumsCollection:

    def __init__(self):
        self.collection = MongoWorker.db_mongo.get_collection("forums")

    async def get_all_forums(self):
        return self.collection.find().to_list()

    async def get_closed_forums(self):
        return self.collection.find({"is_closed": True}).to_list()

    async def create_forum(self, id_user: int, title: str, tags: List[str], text_question: str):
        self.collection.insert_one(
            {
                "id_user": id_user,
                "title": title,
                "tags": tags,
                "text_question": text_question,
                "comments": []
            }
        )

        return True

    async def update_forum(self, id_forum, comment: dict):
        return self.collection.update_one({"_id": id_forum}, {"$push": {"comments": comment}})
