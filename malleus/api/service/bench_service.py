from malleus.api.domain.user_generator import UserGenerator
from malleus.api.repository.datastore import Datastore
from malleus.api.repository.mongodb import MongoDB
from malleus.api.domain.timer import Timer
from malleus.api.service.protos.bench_service_pb2 import  BenchRequest
import malleus.api.service.protos.bench_service_pb2_grpc as bench_service_pb2_grpc

class BenchService(bench_service_pb2_grpc.BenchServiceServicer):

    datasources = {BenchRequest.GDATASTORE: Datastore,
                   BenchRequest.MONGODB: MongoDB}

    def read(self, request: BenchRequest, context = None):
        num = request.num
        datastore = Datastore()
        timer = Timer()

        for i in range(1, num):
            timing = timer.start('DS read 1')
            user = datastore.get(i)
            timer.end(timing)

        return timer.timings

    def write(self, request: BenchRequest, context = None):
        size = request.num
        datastore = self.datasources[request.datasource]()

        timer = Timer()
        user_gen = UserGenerator()
        users = user_gen.get_random_users(int(size))
        timing = timer.start('DS write batch')
        datastore.update_list(users)
        timer.end(timing)

        return timer.timings
