from malleus.api.domain.protos.timings_pb2 import Timings
import time
import numpy


class Timer:
    def __init__(self, timings=None):
        if timings is None:
            self.timings = Timings()
        else:
            self.timings = timings

    def start(self, description):
        # TODO: Blegh
        timing = self.timings.timings.add()
        # TODO: replace with timeit?
        timing.start = time.time()
        timing.description = description
        return timing

    def _arr(self):
        return [(t.end - t.start) for t in self.timings.timings]

    def end(self, timing):
        timing.end = time.time()

    def get_duration(self):
        return self.timings.timings[-1].end - self.timings.timings[0].start

    def get_avg(self):
        return numpy.mean(self._arr())

    def get_95p(self):
        return numpy.percentile(self._arr(), 95)

    def get_99p(self):
        return numpy.percentile(self._arr(), 99)

