from __future__ import print_function

import grpc

import service.protos.bench_service_pb2_grpc as bench_service_pb2_grpc

from malleus.api.domain.protos.timings_pb2 import Timings

# from malleus.api.service.protos.bench_request_pb2 import BenchRequest
from malleus.api.service.protos.bench_service_pb2 import BenchRequest


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = bench_service_pb2_grpc.BenchServiceStub(channel)
    #stub = helloworld_pb2_grpc.GreeterStub(channel)

    response = stub.BenchDataStore(BenchRequest(num=22))


    print("Greeter client received ok " + str(response is not None))


if __name__ == '__main__':
    run()