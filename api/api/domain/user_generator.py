from api.domain.user import User
import random
import string

class UserGenerator:

    def get_random_user(self, user_id):
        user = User()
        user.id = user_id
        user.first_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        user.last_name = ''.join(random.choices(string.ascii_uppercase, k=15))

        user.address1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        user.address2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        user.city = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        user.state = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        user.postal_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        user.country = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        user.description = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))

        return user

    def get_random_users(self, num):
        users = []
        for i in range(1,num):
            users.append(self.get_random_user(i))
        return users
