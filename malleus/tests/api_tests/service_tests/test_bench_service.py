import pytest
from malleus.api.service.bench_service import BenchService
from malleus.api.service.protos.bench_service_pb2 import  BenchRequest



@pytest.fixture
def bench_service():
    return BenchService()

def test_bench_datastore_direct(bench_service):
    bench_request = BenchRequest()
    bench_request.num = 5


    bench_service.write(bench_request)
    timings = bench_service.read(bench_request)

    assert timings.get_duration() > 0
