import json
import falcon

from malleus.api.service.fill_service import FillService

import datetime

class FillController(object):

    def on_get(self, req, resp):
        fill_service = FillService()
        resp.body = json.dumps(fill_service.fill_datastore(int(req.params["size"])))

