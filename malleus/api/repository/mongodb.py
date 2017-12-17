from pymongo import MongoClient
import os
from malleus.api.domain.user import User


class MongoDB:

    def __init__(self):
        self.client = MongoClient(os.environ["MONGODB_HOST"])
        self.db = self.client.bench

    def update(self, user):
        self.db.users.insert_one(user.__dict__.copy())

    def update_list(self, users):
        ents = []
        for user in users:
            ents.append(user.__dict__)
        self.db.users.insert(ents)

    def get(self, user_id):
        user_str = self.db.users.find_one({"id": user_id})
        user = User()
        keys = ['first_name', 'last_name', 'address1', 'address2', 'city', 'postal_code', 'state', 'country', 'id']
        for key in keys:
            user.__dict__[key] = user_str[key]
        return user
