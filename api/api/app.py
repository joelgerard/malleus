import falcon
from api.controllers.bench_controller import BenchController
from api.controllers.fill_controller import FillController

api = application = falcon.API()

fill_controller = FillController()
api.add_route('/fill', fill_controller)

bench_controller = BenchController()
api.add_route('/bench', bench_controller)