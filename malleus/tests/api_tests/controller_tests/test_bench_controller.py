import falcon
from falcon import testing
import pytest

from malleus.api.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_bench(client):
    response = client.simulate_get('/bench',query_string='num=500')
    # TODO: Weak assertion here
    assert response.status == falcon.HTTP_OK