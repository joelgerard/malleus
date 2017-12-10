import pytest
from api.repository.datastore import Datastore
from api.domain.user import User


@pytest.fixture
def datastore():
    return Datastore()


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_request(datastore):
    user = User()
    user.first_name = "Joel"
    datastore.update(user)