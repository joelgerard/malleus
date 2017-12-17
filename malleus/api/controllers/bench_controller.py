import json
import falcon
import msgpack

from malleus.api.service.bench_service import BenchService

import datetime

class BenchController(object):

    def on_get(self, req, resp):
        bench_service = BenchService()
        timings = bench_service.bench_datastore_direct(int(req.params["num"]))

        #json = timings.toJSON()
        #resp.body = json

        resp.data = msgpack.packb(timings.__dict__, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK

