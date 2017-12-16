from api.domain.timing import Timing

class Timings:
    timings = []

    def add(self, timing):
        self.timings.append(timing)

    def get_duration(self):
        return self.timings[-1].end - self.timings[0].start