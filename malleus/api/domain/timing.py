import time

class Timing:

    start = 0
    end = 0
    description = ''

    def start(self, description):
        self.start = time.time()
        self.description = description

    def end(self):
        self.end = time.time()

    def get_duration(self):
        return self.end - self.start

