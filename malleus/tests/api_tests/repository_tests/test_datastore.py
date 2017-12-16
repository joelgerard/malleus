import pytest
# TODO: Pathing sucks here.
from malleus.api.repository.datastore import Datastore
from malleus.api.domain.user import User
from malleus.api.domain.user_generator import UserGenerator


@pytest.fixture
def datastore():
    return Datastore()


def test_update(datastore):
    user = User()
    user.first_name = "Joel"
    user.last_name = "Gerard"
    user.address1 = "87234 B St"
    user.address2 = "Apt 2A"
    user.city = "San Francisco"
    user.postal_code = 94105
    user.state = "CA"
    user.country = "USA"

    user.id = 1
    datastore.update(user)

    retrieved_user = datastore.get(1)
    assert retrieved_user.__dict__ == user.__dict__

def test_update_list(datastore):
    user_gen = UserGenerator()
    users = user_gen.get_random_users(500)
    datastore.update_list(users)
