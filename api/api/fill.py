import json
import falcon
from google.cloud import datastore
from google.auth import credentials

import datetime

class DoNothingCreds(credentials.Credentials):
    def refresh(self, request):
        pass

class Fill(object):

    def create_client(self, project_id):
        return datastore.Client(project_id, credentials=DoNothingCreds())

    def on_get(self, req, resp):
        client = self.create_client('malleus-local')
        if (client is None):
            resp.status = falcon.HTTP_500
        else:
            key = client.key('Task')

            task = datastore.Entity(
                key, exclude_from_indexes=['description'])

            task.update({
                'created': datetime.datetime.utcnow(),
                'description': 'Desc',
                'done': False
            })

            client.put(task)

            #return task.key

            doc = {
                'timeline': [
                    {
                        't0': 1
                    }
                ]
            }

            # task.key above in place of 1

            # Create a JSON representation of the resource
            resp.body = json.dumps(doc, ensure_ascii=False)

            # The following line can be omitted because 200 is the default
            # status returned by the framework, but it is included here to
            # illustrate how this may be overridden as needed.
            # resp.status = falcon.HTTP_200

