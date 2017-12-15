from google.cloud import datastore
from google.auth import credentials
# TODO: Should this be here?
from api.api.domain.user import User
import datetime
import json


class DoNothingCreds(credentials.Credentials):
    def refresh(self, request):
        pass

class Datastore(object):

    def __init__(self, project_id=None, credentials=None):
        if credentials is None:
            self.credentials = DoNothingCreds()
        if project_id is None:
            self.project_id = 'malleus-local'

    def get_client(self):
        return datastore.Client(self.project_id, credentials=self.credentials)

    def update(self, user):
        client = self.get_client()
        key = client.key('User', user.id)

        ent = datastore.Entity(
            key, exclude_from_indexes=['description'])

        ent.update(user.__dict__)

        client.put(ent)

        return ent.key

    def update_list(self, users):
        client = self.get_client()
        ents = []
        for user in users:
            ents.append(datastore.Entity(client.key('User', user.id)))
        client.put_multi(ents)


    def get(self, id):
        client = self.get_client()
        key = client.key('User', id)
        ent = client.get(key)
        user = User()
        for key in ent.keys():
            user.__dict__[key] = ent[key]
        return user
