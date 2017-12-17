from malleus.api.domain.protos.timings_pb2 import Timings
import time


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

    def end(self, timing):
        timing.end = time.time()

    def get_duration(self):
        return self.timings.timings[-1].end - self.timings.timings[0].start
