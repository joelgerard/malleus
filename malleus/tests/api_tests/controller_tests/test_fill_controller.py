import falcon
from falcon import testing
import pytest

from malleus.api.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_fill(client):
    response = client.simulate_get('/fill',query_string='size=500')
    assert response.status == falcon.HTTP_OK