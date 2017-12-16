import json
import falcon

from malleus.api.service.bench_service import BenchService

import datetime

class BenchController(object):

    def on_get(self, req, resp):
        bench_service = BenchService()
        resp.body = json.dumps(bench_service.bench_datastore_direct(int(req.params["num"])).toJSON())

