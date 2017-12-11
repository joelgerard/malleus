import datetime

class Timings:
    timings = []

    def add_timing(self, description):
        self.timings.append({'time': datetime.datetime.timestamp(), 'description': description})

