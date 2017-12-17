import config
import urllib.request

class CallService:

    def call_filler(self, region, size):
        print(config.host[region])

        print(urllib.request.urlopen(config.host[region]+"/fill?size="+ str(size)).read())

    def call_bench_datastore(self, region, num):
        print(urllib.request.urlopen(config.host[region] + "/bench?num=" + str(num)).read())
