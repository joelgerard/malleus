import pytest
from malleus.api.repository.mongodb import MongoDB
from malleus.api.domain.user import User
from malleus.api.domain.user_generator import UserGenerator


@pytest.fixture
def mongodb():
    return MongoDB()


def test_update(mongodb):
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
    mongodb.update(user)

    retrieved_user = mongodb.get(1)
    assert retrieved_user.__dict__ == user.__dict__

def test_update_list(mongodb):
    user_gen = UserGenerator()
    users = user_gen.get_random_users(500)
    mongodb.update_list(users)