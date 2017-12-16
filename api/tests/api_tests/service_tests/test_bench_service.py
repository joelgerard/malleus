import pytest
from api.service.bench_service import BenchService
from api.service.fill_service import FillService
import time


@pytest.fixture
def bench_service():
    return BenchService()

def test_bench_datastore_direct(bench_service):
    limit = 5
    fill_service = FillService()
    fill_service.fill_datastore(limit)
    start = time.time()
    timings = bench_service.bench_datastore_direct(limit)
    end = time.time()

    assert (end - start) >= timings.get_duration()