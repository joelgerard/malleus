import pytest
from malleus.api.domain.protos.timings_pb2 import Timings
from malleus.api.domain.timer import Timer



@pytest.fixture
def timer():
    ts = Timings()
    t = ts.timings.add()
    t.start = 1
    t.end = 2
    t = ts.timings.add()
    t.start = 3
    t.end = 5
    return Timer(ts)


def test__arr(timer):
    arr = timer._arr()
    assert 1 == arr[0]
    assert 2 == arr[1]

def test_avg(timer):
    avg = timer.get_avg()
    assert 1.5 == avg

