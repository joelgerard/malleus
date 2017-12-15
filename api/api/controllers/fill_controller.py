import json
import falcon

from api.service.fill_service import FillService

import datetime

class FillController(object):

    def on_get(self, req, resp):
        fill_service = FillService()
        fill_service.fill_datastore(int(req.params["size"]))
