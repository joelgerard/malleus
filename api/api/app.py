import falcon
from .request import Request
from .fill import Fill

api = application = falcon.API()

request = Request()
api.add_route('/request', request)

fill = Fill()
api.add_route('/fill', fill)