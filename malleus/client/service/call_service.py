import config
from malleus.api.service.protos.bench_service_pb2 import BenchRequest
#from malleus.api.service.protos.bench_service_pb2 import BenchRequest.Datasource
from malleus.api.domain.timer import Timer
import grpc

import malleus.api.service.protos.bench_service_pb2_grpc as bench_service_pb2_grpc

class CallService:

    def __init__(self, region):
        channel = grpc.insecure_channel(config.host[region])
        self.stub = bench_service_pb2_grpc.BenchServiceStub(channel)

    def write(self, num):
        bench_request = BenchRequest()
        bench_request.num = num

        return self.stub.write(bench_request)

    def read(self, num):
        bench_request = BenchRequest()
        bench_request.num = num
        timings = self.stub.read(bench_request)
        timer = Timer(timings)
        print("Duration: " + str(timer.get_duration()))
        print("Average: " + str(timer.get_avg()))
        print("95pct:" + str(timer.get_95p()))
        print("99pct:" + str(timer.get_99p()))

        return timings
