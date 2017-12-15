from api.api.repository.datastore import Datastore
from api.api.domain.timings import Timings
from api.api.domain.timing import Timing

class BenchService:

    def bench_datastore_direct(self, num):
        datastore = Datastore()
        timings = Timings()

        for i in range(1, num):
            timing = Timing()
            timing.start('DS Call')
            user = datastore.get(i)
            timing.end()
            timings.add(timing)

        return timings
