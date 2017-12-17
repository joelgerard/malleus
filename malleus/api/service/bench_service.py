from malleus.api.repository.datastore import Datastore
from malleus.api.domain.timer import Timer

class BenchService:

    def bench_datastore_direct(self, num):
        datastore = Datastore()
        timer = Timer()

        for i in range(1, num):
            timing = timer.start('DS Call')
            user = datastore.get(i)
            timer.end(timing)

        return timer
