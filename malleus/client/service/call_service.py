import config
import urllib.request
from malleus.api.service.protos.bench_service_pb2 import BenchRequest
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
        return self.stub.read(bench_request)
