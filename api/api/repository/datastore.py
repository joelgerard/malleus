from google.cloud import datastore
from google.auth import credentials
import datetime



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
        key = client.key('User')

        ent = datastore.Entity(
            key, exclude_from_indexes=['description'])

        ent.update({
            'created': datetime.datetime.utcnow(),
            'description': 'asdfadsfasdfasdf',
            'done': False
        })

        client.put(ent)

        return ent.key
