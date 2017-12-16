from malleus.api.repository.datastore import Datastore
from malleus.api.domain.user_generator import UserGenerator

class FillService(object):

    def fill_datastore(self, size):
        datastore = Datastore()
        user_gen = UserGenerator()
        users = user_gen.get_random_users(size)
        datastore.update_list(users)
