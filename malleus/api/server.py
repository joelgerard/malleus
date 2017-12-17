from concurrent import futures
import time
import grpc
import service.protos.bench_service_pb2_grpc as bench_service_pb2_grpc
from malleus.api.service.bench_service import BenchService

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


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
