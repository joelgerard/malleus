# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

#import helloworld_pb2
#import helloworld_pb2_grpc

import service.protos.bench_service_pb2_grpc as bench_service_pb2_grpc

from malleus.api.domain.protos.timings_pb2 import Timings

#from malleus.api.service.protos.bench_service_pb2 import

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class BenchService(bench_service_pb2_grpc.BenchServiceServicer):

    def BenchDataStore(self, request, context):
        return Timings()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    bench_service_pb2_grpc.add_BenchServiceServicer_to_server(BenchService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()