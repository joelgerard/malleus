from malleus.api.domain.timing import Timing
import json

class Timings:
    timings = []

    def add(self, timing):
        self.timings.append(timing)

    def get_duration(self):
        return self.timings[-1].end - self.timings[0].start

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
