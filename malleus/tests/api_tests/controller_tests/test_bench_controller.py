import falcon
from falcon import testing
import pytest
import msgpack

from malleus.api.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_bench(client):
    response = client.simulate_get('/bench',query_string='num=500')
    result_doc = msgpack.unpackb(response.content, encoding='utf-8')
    

    # TODO: Weak assertion here
    assert response.status == falcon.HTTP_OK