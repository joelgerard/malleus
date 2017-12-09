import falcon
from .request import Request

api = application = falcon.API()

request = Request()
api.add_route('/request', request)