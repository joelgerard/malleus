import pytest
from malleus.api.service.bench_service import BenchService
from malleus.api.service.fill_service import FillService



@pytest.fixture
def bench_service():
    return BenchService()

def test_bench_datastore_direct(bench_service):
    limit = 5
    fill_service = FillService()
    fill_service.fill_datastore(limit)
    timings = bench_service.bench_datastore_direct(limit)

    assert timings.get_duration() > 0